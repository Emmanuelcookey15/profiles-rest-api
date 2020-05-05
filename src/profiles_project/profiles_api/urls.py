from django.conf.urls import url
from django.conf.urls import include

from . import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]
