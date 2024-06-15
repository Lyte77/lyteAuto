from . import views
from django.urls import path


app_name = 'shop'

urlpatterns = [

    path('', views.home_view, name='home'),
    path('car/add/', views.car_form_view, name='car_add'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('car/<int:id>/delete/', views.remove_car, name='remove_car'),
    path('car/<int:car_id>/update/', views.car_form_view, name='car_update'),
    

]