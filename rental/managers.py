from django.db import models
import pendulum


class FriendQuerySet(models.QuerySet):
    def with_overdue(self):
        return self.annotate(
            _ann_overdue=models.Case(
                models.When(
                    borrowed__when__lte=pendulum.now().subtract(months=2),
                    then=True
                ),
                default=models.Value(False),
                output_field=models.BooleanField()
            )
        )
