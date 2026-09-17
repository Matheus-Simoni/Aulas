#importação de API + uso de datetime para manipular datas
import requests
import datetime

def cotar(data):
    url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"

    res = requests.get(url)
    res = res.json()

    if res['value']:
        return res['value'][0]['cotacaoCompra']

    else:
        dia_anterior = datetime.datetime.strptime(data, "%m-%d-%Y") - datetime.timedelta(1)

        dia_anterior = datetime.datetime.strftime(dia_anterior, "%m-%d-%Y")

        return cotar(dia_anterior)


resultado = [
    cotar(i) for i in [
        "09-02-2024",
        "09-01-2024",
        "08-31-2024",
        "08-30-2024",
        "08-29-2024"
    ]
]

print(resultado)