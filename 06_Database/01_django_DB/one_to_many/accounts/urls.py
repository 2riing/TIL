from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow', views.follow, name='follow'),

    # 회원정보 변경/삭제
    # accounts/update/
    path('update/', views.update, name='update'),
    # accounts/delete/
    path('delete/', views.delete, name='delete'),
    # accounts/password/
    path('password/', views.password, name='password'),


]
