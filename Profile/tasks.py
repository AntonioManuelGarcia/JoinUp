from celery import shared_task
from twilio.base.exceptions import TwilioRestException
from query_counter.decorators import queries_counter
from djangoProject.settings import base
from .models import Profile
from twilio.rest import Client

sms_client = Client(base.MY_ACCOUNT_SID, base.TWILIO_AUTH_TOKEN)


@shared_task
def profile_created(profile_id):
    """
    Task to send an e-mail and sms notification when a profile is
    successfully created.
    """
    profile = Profile.objects.get(id=profile_id)

    if profile.send_email("check email address", "message", [profile.email]):
        profile.email_validated = True
    try:
        if sms_client.messages.create(to=profile.phone_number.national_number,
                                      from_=base.MY_TWILIO_NUMBER,
                                      body="message_to_broadcast"):
            profile.phone_number_validated = True
    except TwilioRestException:
        profile.phone_number_validated = True

    if profile.email_validated or profile.phone_number_validated:
        profile.save()

    return profile.id
