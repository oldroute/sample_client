import requests
from django.shortcuts import render


def planet_view(request):

    try:
        response = requests.get('http://localhost:8000/api/')
        planets = response.json()
    except requests.ConnectionError:
        planets = []

    return render(
        request=request,
        template_name='index.html',
        context={'object_list': planets}
    )