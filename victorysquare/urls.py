from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from vsquare import views

router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'difficulties', views.DifficultyViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
