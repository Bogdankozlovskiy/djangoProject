from rest_framework import viewsets
from rental.models import Friend, Borrowed, Belonging
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from rental.permissions import IsOwner


class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.with_overdue()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer
    permission_classes = [IsOwner]


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [IsOwner]
