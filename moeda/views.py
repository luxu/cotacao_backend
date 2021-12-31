
from django.shortcuts import render

from .models import Moeda


def index(request):
    moeda = Moeda.objects.all()
    context = {
        'itens': moeda
    }
    return render(request, 'moeda/index.html', context)


def request_in_site(request):
    ...
    # last_four_days = datetime.now() - timedelta(days=4)
    # for day in range(1, 6):
    #     last_day = datetime.now() - timedelta(days=day)
    #     url = f'https://api.vatcomply.com/rates?base=USD&date={last_day.date()}'
    #     response = get(url)
    #     moeda = Moeda()
    #     moeda.continent = ''
    #     moeda.name_coin = ''
    #     moeda.data = ''
    #     moeda.value = ''
    #     moeda.save()
    # url = f'https://api.vatcomply.com/rates?base=USD&date={last_four_days.date()}'
    # response4 = get(url)
    # context = {
    #     'coins': response4.json()
    # }
    # return JsonResponse(response4.json())
    # return render(request, 'moeda/list-coins.html', context)
    # return HttpResponse('<h2>Lista de moedas atualizadas!!!</h2>')
