from django.db import models


class Client(models.Model):

    ACCOUNT_STATUS_CHOICES = [
        ('active', 'В работе'),
        ('inactive', 'Не в работе'),
        ('declined', 'Отказ'),
        ('closed', 'Сделка закрыта'),
    ]

    account_number = models.CharField(max_length=20, unique=True, verbose_name="Номер счета")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    inn = models.CharField(max_length=12, unique=True, verbose_name="ИНН")
    responsible_person = models.CharField(max_length=150, verbose_name="ФИО ответственного")
    status = models.CharField(max_length=20, choices=ACCOUNT_STATUS_CHOICES, default='inactive', verbose_name="Статус")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.account_number})"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
