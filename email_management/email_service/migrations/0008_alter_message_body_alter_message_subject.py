# Generated by Django 4.2.4 on 2023-09-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0007_alter_marketingemail_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
