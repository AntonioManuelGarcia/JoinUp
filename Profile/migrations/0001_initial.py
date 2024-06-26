# Generated by Django 5.0.4 on 2024-05-04 22:36

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128, verbose_name='first name')),
                ('last_name', models.CharField(max_length=128, verbose_name='last name')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('email_validated', models.BooleanField(default=False, verbose_name='email address validated')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='ES', verbose_name='phone number')),
                ('phone_number_validated', models.BooleanField(default=False, verbose_name='phone number validated')),
                ('hobbies', models.CharField(blank=True, max_length=1024, null=True, verbose_name='hobbies')),
            ],
            options={
                'ordering': ['-id'],
                'indexes': [models.Index(fields=['id'], name='Profile_pro_id_2b22c0_idx'), models.Index(fields=['last_name', 'first_name'], name='Profile_pro_last_na_b45980_idx'), models.Index(fields=['email'], name='Profile_pro_email_5dfd8b_idx'), models.Index(fields=['phone_number'], name='Profile_pro_phone_n_549276_idx')],
            },
        ),
    ]
