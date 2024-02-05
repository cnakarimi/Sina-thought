
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.homepage, name=''),
    
    path('register', views.register, name='register'),
    
    path('my-login', views.my_login, name='my-login'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('user-logout', views.user_logout, name='user-logout'),

    path('create-thought', views.create_thought, name='create-thought'),

    path('my-thoughts', views.my_thoughts, name='my-thoughts'),
    \
    path('update-thought/<str:pk>', views.update_thought, name='update-thought'),

    path('delete-thought/<str:pk>', views.delete_thought, name='delete-thought'),
    
    
    
    
]



















