from rest_framework import routers
from rental.api_views import FriendViewset, BelongingViewset, BorrowedViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


router = NestedDefaultRouter()
friends = router.register(r'friends', FriendViewset)
friends.register(r'borrowings', BorrowedViewSet, basename='friend-borrow', parents_query_lookups=['to_who'])
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewSet)
