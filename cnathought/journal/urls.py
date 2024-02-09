
from django.urls import path

from . import views

from django.contrib.auth import views as auth_views




urlpatterns = [
    
    path('', views.homepage, name=''),
    
    path('register', views.register, name='register'),
    
    path('my-login', views.my_login, name='my-login'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('user-logout', views.user_logout, name='user-logout'),

    path('create-thought', views.create_thought, name='create-thought'),

    path('my-thoughts', views.my_thoughts, name='my-thoughts'),
    
    path('update-thought/<str:pk>', views.update_thought, name='update-thought'),

    path('delete-thought/<str:pk>', views.delete_thought, name='delete-thought'),
    
    path('profile-management', views.profile_management, name='profile-management'),

    path('delete-account', views.delete_account, name='delete-account'),

    
    # Password management

    # 1 - Allow us to enter our email in order to receive a password reset link

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='journal/password-reset.html'), name='reset_password'),


    # 2 - Show a success message stating that an email was sent to reset password
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='journal/password-reset-sent.html'), name='password_reset_done'),


    # 3 - send a link to our email, so that we can reset our password

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='journal/password-reset-form.html'), name='password_reset_confirm'
    ), 


    # $ - Show a success message that our password was changed

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='journal/password-reset-complete.html'), name='password_reset_complete'),
]



















