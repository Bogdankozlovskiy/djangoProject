from rest_framework import routers
from rental.api_views import FriendViewset, BelongingViewset, BorrowedViewSet


router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewSet)
