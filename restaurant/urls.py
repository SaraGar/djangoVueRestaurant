from rest_framework import routers

from .viewsets import MenuViewSet, MenuItemViewSet, LocationViewSet

router = routers.SimpleRouter()
router.register('menus', MenuViewSet)
router.register('menuItems', MenuItemViewSet)
router.register('locations', LocationViewSet)

urlpatterns = router.urls