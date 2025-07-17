from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# Example model import
# from .models import YourModel


def updateUser(sender, instance, **kwargs):
    user = instance
    if not user.email:
        user.email = user.username


pre_save.connect(updateUser, sender=User)  # Connect the signal to the User model
