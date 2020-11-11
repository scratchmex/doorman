from django.db import models
from django.contrib.auth.models import AbstractUser


from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    pass


# Create your models here
class Profile(models.Model):
    # - relational
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", primary_key=True,
    )
    # - own
    phone_number = PhoneNumberField()
    mobile_number = PhoneNumberField()
