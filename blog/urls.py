from .views import home, posts, post_detail
from django.urls import path

urlpatterns = [
    path('', home),
    path('posts/', posts, name='index'),
    path('<int:id>/', post_detail, name='detail'),
]
