from rest_framework import serializers

from .models import countryGDP,GDP

class CountryGDPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = countryGDP
        fields = ('countryname', 'year', 'gdp')

class GDPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GDP
        fields = ('year', 'USA', 'India', 'China', 'Europe')