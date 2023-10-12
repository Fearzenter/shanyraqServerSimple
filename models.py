from django.db import models

# Create your models here.


class Guardian(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    mail = models.CharField(max_length=255, verbose_name='Адрес электронной почты')
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.FloatField(verbose_name='Пол')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    volume = models.FloatField(default=0, verbose_name='Сумма пожертвований')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.phone_number}"

    class Meta:
        verbose_name = 'Попечитель'
        verbose_name_plural = 'Попечители'
        ordering = ['time_create', 'volume', 'name', 'sex', 'age']


class GuardianCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    phone_number = models.CharField(max_length=255, verbose_name='Контактный номер')
    mail = models.CharField(max_length=255, verbose_name='Адрес электронной почты')
    company_type = models.CharField(max_length=255, verbose_name='Тип компании')
    inn = models.CharField(default=0, max_length=255, verbose_name='ИНН')
    kpp = models.CharField(default=0, max_length=255, verbose_name='КПП')
    ogrn = models.CharField(default=0, max_length=255, verbose_name='ОГРН')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    address_ur = models.CharField(default=0, max_length=255, verbose_name='Юридический адрес')
    address_real = models.CharField(default=0, max_length=255, verbose_name='Фактический адрес')
    payment_number = models.CharField(default=0, max_length=255, verbose_name='Расчетный счет')
    volume = models.FloatField(default=0, verbose_name='Сумма пожертвований')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_type} {self.name} {self.phone_number}"

    class Meta:
        verbose_name = 'Компания попечитель'
        verbose_name_plural = 'Компании попечители'
        ordering = ['time_create', 'volume', 'name', 'company_type']


class Slave(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    mail = models.CharField(max_length=255, verbose_name='Адрес электронной почты')
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.FloatField(verbose_name='Пол')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    summary = models.CharField(max_length=255, verbose_name='Описание проблемы')
    volume_need = models.FloatField(verbose_name='Необходимая сумма')
    volume_get = models.FloatField(default=0, verbose_name='Полученная сумма')
    card_number = models.CharField(max_length=255, verbose_name="Карта для пополнения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.phone_number}"

    class Meta:
        verbose_name = 'Подопечный'
        verbose_name_plural = 'Подопечные'
        ordering = ['time_create', 'volume_need', 'volume_get', 'sex', 'name', 'age']
