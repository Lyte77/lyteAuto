from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    # path('logout/',views.logout_user, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:home'), name='logout')
    
]