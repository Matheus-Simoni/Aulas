import os
import requests
from dotenv import load_dotenv
from folium import Map, Marker, Popup

load_dotenv(".env")

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={os.getenv('SPTRANS_TOKEN')}"
)
print(res.text)

linhas_lapa = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Lapa"
)
linhas_lapa = linhas_lapa.json()
print(linhas_lapa[:3])

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506"
)
paradas = res.json()
print(paradas[:3])


m = Map(location=[-22.8773542,-47.2280647], zoom_start=14)
Marker(location=[-22.8773542,-47.2280647], popup=Popup("Estudo aqui!", max_width="100", show=True)).add_to(m)
m.save("unasp.html") 