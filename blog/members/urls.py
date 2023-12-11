from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views





urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('<int:id_password>/password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view()),
    path('password_success', views.password_success, name="password_success"),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile_page'),
    path('edit_profile_page/<int:pk>', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile', CreateProfilePageView.as_view(), name='create_profile'),

    






]