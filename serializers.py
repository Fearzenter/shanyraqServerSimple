from rest_framework import serializers

from shServ.models import Slave, GuardianCompany, Guardian


class GuardianCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianCompany
        fields = ('name', 'phone_number', 'mail', 'company_type', 'inn', 'kpp', 'ogrn',
                  'country', 'city', 'address_ur', 'address_real',
                  'payment_number', 'volume', 'time_create', 'time_update')


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ('name', 'phone_number', 'mail', 'age', 'sex',
                  'country', 'city', 'address', 'volume', 'time_create', 'time_update')


class SlaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slave
        fields = ('name', 'phone_number', 'mail', 'age', 'sex',
                  'country', 'city', 'address', 'summary', 'volume_need', 'volume_get',
                  'card_number', 'time_create', 'time_update')
