from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(_('first name'), max_length=128, unique=False, null=False, blank=False)
    last_name = models.CharField(_('last name'), max_length=128, unique=False, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    email_validated = models.BooleanField(_('email address validated'), default=False)
    phone_number = PhoneNumberField(_('phone number'), blank=False, region="ES")
    phone_number_validated = models.BooleanField(_('phone number validated'), default=False)
    hobbies = models.CharField(_('hobbies'), max_length=1024, unique=False, null=True, blank=True)

    class Meta:
        ordering = ['-id']

        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
        ]

    def __str__(self):
        return self.first_name

    def send_email(self, subject, message, from_email=None):
        return send_mail(subject, message, from_email, [self.email])
