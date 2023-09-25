from django.db import models
from django.urls import reverse
# Create your models here.
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
        return reverse('email_detail', args=[str(self.pk)])
class MarketingEmail(models.Model):
    email_time = models.DateTimeField()
    frequency = models.CharField(max_length=200) # день, неделя, месяц
    status = models.CharField(max_length=200) # создана, запущена, завершена
    clients = models.ManyToManyField(Client)
    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'Маркетинговые рассылки'

    def __str__(self):
        return f"Рассылка число {self.email_time.date()} Статус {self.status}"
    def get_absolute_url(self):
        return reverse('email_detail', args=[str(self.pk)])
class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    email = models.ForeignKey(MarketingEmail, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
    def __str__(self):
        return self.subject

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