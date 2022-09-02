from rental.models import Friend, Borrowed, Belonging
from rest_framework.serializers import ModelSerializer, CurrentUserDefault, HiddenField


class FriendSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Friend
        fields = ('id', 'name', "owner")


class BelongingSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Belonging
        fields = ('id', 'name', "owner")


class BorrowedSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned', "owner")
