from django.urls import path
from .views import user_view,post_view,all_post,post_update,login_view,logout_view

urlpatterns = [
    path('user_reg/',user_view,name = 'user'),
    path('post/',post_view,name = 'post'),
    path('all_post/',all_post,name = 'all_post'),
    path('post_update/<int:uid>/',post_update,name = 'post_update'),
    path('login/',login_view,name = 'login'),
    path('logout/',logout_view,name = 'logout'),






]