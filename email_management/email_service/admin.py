from django.contrib import admin

from email_service.models import Client, MarketingEmail, Message, EmailLog,User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    # другие опции админки

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    # list_filter =
    search_fields = ('full_name', 'message')


@admin.register(MarketingEmail)
class MarketingEmailAdmin(admin.ModelAdmin):
    list_display = ('email_time', "status")
    #list_filter = ("status")
    search_fields = ('frequency', "status")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', "body")
    #list_filter = ("subject")
    search_fields = ('subject', "body")


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ("last_attempt", "attempt_status")
    #list_filter =
    search_fields = ("last_attempt", "attempt_status")
