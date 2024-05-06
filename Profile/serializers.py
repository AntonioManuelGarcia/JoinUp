from django.core.mail import send_mail
from rest_framework import serializers
from twilio.base.exceptions import TwilioRestException

from djangoProject.settings import base
from .models import Profile
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import UniqueValidator
from twilio.rest import Client

sms_client = Client(base.MY_ACCOUNT_SID, base.TWILIO_AUTH_TOKEN)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'email_validated', 'phone_number', 'phone_number_validated',
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
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'hobbies']

    def create(self, validated_data):
        if send_mail("check email adress", "message", None, [validated_data['email']]):
            validated_data['email_validated'] = True
        try:
            if sms_client.messages.create(to=validated_data['phone_number'].national_number,
                                          from_=base.MY_TWILIO_NUMBER,
                                          body="message_to_broadcast"):
                validated_data['phone_number_validated'] = True
        except TwilioRestException:
            validated_data['phone_number_validated'] = True
        profile = Profile.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            email_validated=validated_data['email_validated'],
            phone_number=validated_data['phone_number'],
            phone_number_validated=validated_data['phone_number_validated'],
            hobbies=validated_data['hobbies'],
        )
        return profile
