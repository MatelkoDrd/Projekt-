from datetime import date

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.



class UserManager(BaseUserManager):
        use_in_migrations = True

        def _create_user(self, email, password, **extra_fields):

            """Create and save a User with the given email and password."""
            if not email:
                raise ValueError('The given email must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, email, password=None, **extra_fields):

            """Create and save a regular User with the given email and password."""
            extra_fields.setdefault('is_staff', False)
            extra_fields.setdefault('is_superuser', False)
            return self._create_user(email, password, **extra_fields)

        def create_superuser(self, email, password, **extra_fields):

            """Create and save a SuperUser with the given email and password."""
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('date_of_birth', date.today())

            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')
            return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

        """
        User model.
        """
        username = None
        email = models.EmailField(verbose_name=('Email'), unique=True, null=False)
        phone_number = models.CharField(verbose_name=('Telefon'), max_length=17)
        date_of_birth = models.DateField(verbose_name=('Data urodzenia'))
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        objects = UserManager()

