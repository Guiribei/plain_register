from django.urls import path
from app_plain_register import views

urlpatterns = [
    #rota, view responsável, nome de referência;
	path('', views.home, name='home'),
	path('users/', views.users, name='users_list'),
	path('confirm_delete_all/', views.confirm_delete_all, name='confirm_delete_all'),
]
