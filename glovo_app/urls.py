from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('users', views.UserProfileViewSet)
router.register('stores', views.StoreViewSet)
router.register('products', views.ProductViewSet)
router.register('categories', views.ProductCategoryViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('cart', views.CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]