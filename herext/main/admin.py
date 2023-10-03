from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Text)
admin.site.register(DeletedChatRoom)
admin.site.register(DeletedText)