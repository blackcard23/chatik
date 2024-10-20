from django.db import models


# Create your models here.


class Chat(models.Model):
    name = models.CharField(max_length=100, null=True)
    users = models.ManyToManyField('users.User', related_name='chats', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_group = models.BooleanField('Is Group', default=False)

    # user1 = models.ForeignKey('users.User',realated_name='chats1',null=True,on_delete=models.SET_NULL)
    # user2 = models.ForeignKey('users.User',realated_name='chats2', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.is_group:
            return self.name
        return f"PRIVATE-{self.id}"


class Message(models.Model):
    text = models.TextField('Text')
    created_at = models.DateTimeField('Created_at', auto_now_add=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    sender = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL)
    read_date = models.DateTimeField('Read date', null=True)

    def __str__(self):
        return f'{self.chat_id}'
