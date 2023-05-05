from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # post views
    # path('login', views.user_login, name='login'),
    path('login', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # path('logout-then-login', include('django.contrib.auth.views'), name='logout-then-login'),
    path('', views.dashboard, name='dashboard'),
    path('password-change', PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password-change'),
    path('password-change-done', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password-change/done/'),
    path('password-reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password-reset'),
    path('password-reset/done/', PasswordChangeDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password-reset-confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register', views.register, name='register'),
]
