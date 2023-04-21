from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True,blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/No_avatar.png')
    info = models.TextField(verbose_name='Личная информация', blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=False)
    birth_date = models.DateField(verbose_name='День рождения',blank=True, null=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=100, blank=True)
    subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Account', related_name='subscribers')
    subscriptions_count = models.PositiveIntegerField(default=0)
    subscribers_count = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.email}'