from rental.models import Friend, Borrowed, Belonging
from rest_framework.serializers import ModelSerializer, CurrentUserDefault, HiddenField, BooleanField
from rest_flex_fields import FlexFieldsModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class FriendSerializer(FlexFieldsModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    ann_overdue = BooleanField(source="_ann_overdue", read_only=True)

    class Meta:
        model = Friend
        fields = ('id', 'name', "owner", "ann_overdue")


class BelongingSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Belonging
        fields = ('id', 'name', "owner")


class FriendPresentSerializer(FlexFieldsModelSerializer):
    expandable_fields = {
        "owner": UserSerializer
    }

    class Meta:
        model = Friend
        fields = ('id', 'name', "owner")


class BorrowedSerializer(FlexFieldsModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    expandable_fields = {
        "what": BelongingSerializer,
        "to_who": FriendPresentSerializer
    }

    class Meta:
        model = Borrowed
        fields = ('id', 'what', 'to_who', 'when', 'returned', "owner")
