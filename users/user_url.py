from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, UserLogoutView, UserProfileUpdate

app_name='users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserProfileUpdate.as_view(), name='profile-edit')
]