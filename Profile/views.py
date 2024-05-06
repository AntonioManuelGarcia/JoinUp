from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer, CreateProfileSerializer


class CreateProfileView(generics.CreateAPIView):
    """
        post:
            Create a new user profile.
    """
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer
    permission_classes = (permissions.AllowAny,)


class ProfileDetailView(generics.RetrieveAPIView):
    """
        get:
            Return a user profile instance.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
