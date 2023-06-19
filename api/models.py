from django.db import models
# from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .manager import CustomUserManager

class UserProfile(AbstractBaseUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255, default='')
    lastName = models.CharField(max_length=255, default='')
    userName = models.CharField(max_length=255, default='', unique=True)
    organisation = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    active = models.BooleanField(max_length=255, default=0)
    createdOn = models.DateTimeField(default=datetime.now, blank=True)
    modifiedBy = models.DateTimeField(default=datetime.now, blank=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
   
    USERNAME_FIELD = "userName"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False