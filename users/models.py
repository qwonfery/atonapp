from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=50, verbose_name="ФИО", default="fullname")
    username = models.CharField(max_length=50, verbose_name="Логин", unique=True, default="username")
    password = models.TextField(max_length=50, verbose_name="Пароль", default="password")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
