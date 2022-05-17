from rest_framework import viewsets

from .serializers import CountryGDPSerializer, GDPSerializer
from .models import countryGDP,GDP
import pandas as pd


class CountryGDPViewSet(viewsets.ModelViewSet):
    queryset = countryGDP.objects.filter(countryname='India').order_by('countryname')
    list1 = []
    for x in queryset:
        list1.append(f'year:{x.year}, {x.countryname}:{x.gdp}')

    print(list1)
    serializer_class = CountryGDPSerializer

class GDPViewSet(viewsets.ModelViewSet):
    queryset = GDP.objects.all()
    serializer_class = GDPSerializer