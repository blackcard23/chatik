from django.core.exceptions import BadRequest
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import get_object_or_404

from chat.models import Chat
from users.models import User


class ChatSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'user_id', 'name']

    def create(self, validate_data):

        user = get_object_or_404(User, id=validate_data['user_id'])
        if not user.is_active:
            raise PermissionDenied("Can't create chat with this user")
        request_user = self.context['request'].user
        if Chat.objects.filter(Q(users=user.id) & Q(users=request_user.id), is_group=False).exists():
            raise ValidationError('Chat already exists ')

        chat = Chat.objects.create()
        chat.users.add(request_user.id, user.id)
