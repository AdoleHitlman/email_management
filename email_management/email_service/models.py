
from django.db import models
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    def get_absolute_url(self):
        return reverse('email_list')


class Message(models.Model):
    subject = models.CharField(max_length=200,verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    email = models.ForeignKey('MarketingEmail', related_name='emails', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('email_detail', args=[str(self.pk)])


class MarketingEmail(models.Model):
    email_time = models.DateTimeField(verbose_name='Дата')
    frequency = models.CharField(max_length=200, verbose_name="частота отправки")
    status = models.CharField(max_length=200, verbose_name="состояние")
    message = models.ManyToManyField('Message', related_name='newsletters', verbose_name='Сообщение')
    clients = models.ManyToManyField('Clients', related_name='newsletters', verbose_name='Кому')

    CREATED = 'Создана'
    RUNNING = 'Запущена'
    FINISHED = 'Завершена'
    STATUS_CHOICES = (
        (CREATED, 'Создана'),
        (RUNNING, 'Запущена'),
        (FINISHED, 'Завершена'),
    )

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'Маркетинговые рассылки'

    def __str__(self):
        return f"Рассылка число {self.email_time.date()} Статус {self.status}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = self.CREATED
        elif self.status != self.RUNNING:
            self.status = self.RUNNING
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.status = self.FINISHED
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('email_detail', args=[str(self.pk)])
class EmailLog(models.Model):
    last_attempt = models.DateTimeField(auto_now=True)
    attempt_status = models.BooleanField(default=False)
    server_response = models.TextField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы электронной почты'
    def __str__(self):
        return f"Log for {self.message.subject} at {self.last_attempt}"
    def get_absolute_url(self):
        return reverse('email_detail', args=[str(self.pk)])