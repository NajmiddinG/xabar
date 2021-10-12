from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'who', 'towhom', 'subject', 'message', 'time']
    list_filter =  ['who', 'towhom']