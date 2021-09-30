from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url1 = 'https://v6.exchangerate-api.com/v6/3bbf87391515a6481d631ec0/pair/{}/USD/{}'
    url2 = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=cb93c296ce22a6e93213e0942c2e1a17'


    curr = {}
    for name in request.POST:
        curr[name] = request.POST.get(name)

    a = curr['currency_input']
    b = curr['converter_input']
    h = curr['text_input']

    z = requests.get(url1.format(a, b)).json()

    r = requests.get(url2.format(h)).json()

    city_weather = {
        'city': h,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
    }

    reports = {
        'base': z["base_code"],
        'target': z["target_code"],
        'conversion': z["conversion_result"]
    }

    # st_tropez = 62,532
    # x = reports['conversion']

    context = {'reports': reports, 'city_weather': city_weather, 'curr': curr}

    return render(request, 'home.html', context)
