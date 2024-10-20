from django.contrib import admin

from chat.models import Chat, Message
from users.models import User

# Register your models here.
admin.site.register(Chat)

admin.site.register(Message)
admin.site.register(User)
