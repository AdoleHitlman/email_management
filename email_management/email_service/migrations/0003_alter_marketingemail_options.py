# Generated by Django 4.2.4 on 2023-09-25 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0002_alter_client_options_alter_emaillog_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketingemail',
            options={'verbose_name': 'рассылка', 'verbose_name_plural': 'Маркетинговые рассылки'},
        ),
    ]