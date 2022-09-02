from django.db import models


class OwnedModel(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Friend(OwnedModel):
    name = models.CharField(max_length=100)


class Belonging(OwnedModel):
    name = models.CharField(max_length=100)


class Borrowed(OwnedModel):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
