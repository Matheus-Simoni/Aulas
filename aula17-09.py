import requests

def cotar(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='{data}'&%24format=json" 
    res = requests.get(url)
    res = res.json()
    return res['value'][0]['cotacaoCompra']

resultado = cotar('09-17-2026')
print(f'Cotação do dia é R${resultado:.2f}')