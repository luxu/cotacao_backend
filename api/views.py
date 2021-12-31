from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import datetime, timedelta

from requests import get

from moeda.constantes import NAME
from .serializer import MoedaListSerializer, MoedaSerializer
from moeda.models import Moeda


@api_view(["GET"])
def coins_list(request):
    """Listar as moedas"""
    if request.method == "GET":
        moeda = Moeda.objects.all()
        serializer = MoedaListSerializer(moeda, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def request_site(request):
    """Pegar os dados do site"""
    if request.method == "GET":
        for day in range(5):
            cotation_day = datetime.now() - timedelta(days=day)
            url = f"https://api.vatcomply.com/rates?base=USD&date={cotation_day.date()}"
            response = get(url)
            list_initials_coins = ["BRL", "EUR", "JPY"]
            rates = response.json()["rates"]
            moeda = Moeda.objects.filter(data=cotation_day)
            if not moeda:
                for sigla in list_initials_coins:
                    value = rates[sigla]
                    if sigla == "BRL":
                        name_coin = NAME[0][0]
                    elif sigla == "JPY":
                        name_coin = NAME[1][0]
                    else:
                        name_coin = NAME[2][0]
                    dados = {
                        "initials": sigla,
                        "name_coin": name_coin,
                        "data": cotation_day.date(),
                        "value": value,
                    }
                    serializer = MoedaSerializer(data=dados)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
        return Response("Boa Timeeee!!!!")
