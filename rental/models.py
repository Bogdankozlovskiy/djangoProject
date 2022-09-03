from django.db import models
import pendulum

from rental.managers import FriendQuerySet


class OwnedModel(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Friend(OwnedModel):
    name = models.CharField(max_length=100)
    objects = FriendQuerySet.as_manager()

    @property
    def has_overdue(self):
        if hasattr(self, '_ann_overdue'):
            return self._ann_overdue
        return self.borrowed_set.filter(
            returned__isnull=True,
            when=pendulum.now().subtract(months=2)
        ).exists()

    def __str__(self):
        return self.name


class Belonging(OwnedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Borrowed(OwnedModel):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
