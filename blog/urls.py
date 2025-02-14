from django.urls import path
from .views import user_update
from .views import password_change
from .views import signup, user_login, user_logout
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('login/', views.user_login, name='login'),  # 로그인 URL 추가
    path('logout/', user_logout, name='logout'),
    path('update/', user_update, name='user_update'),

    path('password_change/', password_change, name='password_change'),

    #path('', views.home, name='home'),

    path('prompt/', views.prompt, name='prompt'),

    path('export/', views.export, name='export'),

    path('export/', views.export, name='export'),
    path('profile/', views.profile, name='profile'),  # 프로필 URL 추가
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]

