from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from rental.filters import BorrowedFilterSet
from rental.models import Friend, Borrowed, Belonging
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from rental.permissions import IsOwner


class FriendViewset(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Friend.objects.with_overdue()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewset(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer
    permission_classes = [IsOwner]


class BorrowedViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [IsOwner]
    filterset_class = BorrowedFilterSet
    # filterset_fields = {
    #     "returned": ["isnull", "gte", "lte", "exact"]
    # }

    @action(detail=True, url_path='remind', methods=['post'])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject=f"Please return my belonging: {obj.what.name}",
            message=f"You forgot to return my belonging: \"{obj.what.name}\" that you borrowed on {obj.when}.Please return it.",
            from_email="me@example.com",
            recipient_list=[obj.to_who.email]
        )
        return Response("email has been sent")

    @action(detail=False, url_path='remind', methods=['post'])
    def remind_many(self, request, *args, **kwargs):
        count = 0
        for obj in self.get_queryset():
            count += send_mail(
                subject=f"Please return my belonging: {obj.what.name}",
                message=f"You forgot to return my belonging: \"{obj.what.name}\" that you borrowed on {obj.when}.Please return it.",
                from_email="me@example.com",
                recipient_list=[obj.to_who.email]
            )
        return Response(f"{count=} emails has been sent")

