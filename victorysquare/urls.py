from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from dynamic_rest.routers import DynamicRouter
from vsquare import viewsets

router = DynamicRouter()
router.register(r'organizations', viewsets.OrganizationViewSet)
router.register(r'games', viewsets.GameViewSet)
router.register(r'items', viewsets.ItemViewSet)
router.register(r'difficulties', viewsets.DifficultyViewSet)
router.register(r'categories', viewsets.CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
