from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm
from accounts.views import logout_view, register

app_name = 'accounts'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name = 'accounts/connexion.html', redirect_authenticated_user = True, authentication_form = LoginForm), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    # Page de demande de réinitialisation de mot de passe
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/reset_password.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt'
         ),
         name='password_reset'),

    # Confirmation d'envoi de l'e-mail
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_sent.html'
         ),
         name='password_reset_done'),

    # Lien pour la réinitialisation de mot de passe (inclus dans l'email)
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_form.html'
         ),
         name='password_reset_confirm'),

    # Confirmation de la réinitialisation réussie
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_complete'),

    # path('reset_password_send', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset_confirm'),
    # path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete')

]