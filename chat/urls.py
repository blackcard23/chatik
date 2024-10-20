from django.urls import path

from chat.views import CreateChat

urlpatterns = [
    path('create/',CreateChat.as_view())
]