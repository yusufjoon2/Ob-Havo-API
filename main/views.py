from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests



class WeatherAPIView(APIView):
    def get(self, request, city):
        url = f'https://api.weatherapi.com/v1/current.json?key=cb04c76678334a9a9ce133507251202&q={city}&aqi=no'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



