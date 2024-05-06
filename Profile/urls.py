from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('signup/', views.CreateProfileView.as_view(), name='create_profile'),
    path('profile/<pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
]
