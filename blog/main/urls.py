from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>', show_post, name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]