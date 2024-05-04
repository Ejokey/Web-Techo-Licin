from . import views 
from django.urls import path 
from .import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

urlpatterns = [ 

    path('', views.PostList.as_view(), name='home'), 
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), 

] 

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('api/v1/', include(router.urls))
]
