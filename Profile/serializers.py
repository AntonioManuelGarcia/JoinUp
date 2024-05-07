from rest_framework import serializers
from .models import Profile
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import UniqueValidator
from .tasks import profile_created


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'email_validated', 'phone_number', 'phone_number_validated',
                  'hobbies']


class CreateProfileSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(
        region="ES",
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())])
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number',
                  'hobbies']

    def create(self, validated_data):
        profile = Profile.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            hobbies=validated_data['hobbies'],
        )
        profile_created.delay(profile.id)
        return profile
