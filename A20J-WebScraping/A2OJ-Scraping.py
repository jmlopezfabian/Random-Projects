import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://earthshakira.github.io/a2oj-clientside/server/"
response = requests.get(url + "Ladders.html")
if response.status_code == 200:
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    tabla_rating = soup.find_all('table')[0]
    tabla_div3_3 = soup.find_all('table')[1]

    elementos_div3_3 = tabla_div3_3.find_all('tr')
    elementos_rating = tabla_rating.find_all('tr')
    
    
    for elemento in elementos_rating:
        info = {
            "Nombre": [],
            "Enlace": []
        }

        tds = elemento.find_all('td')
        if len(tds) >= 3:
            link = url + tds[1].find('a').get('href')
            nombre = tds[1].find('a').text.replace(" ","") + ".csv"
            response_sub = requests.get(link)
            if response_sub.status_code == 200:
                print(response_sub.status_code)
                soup_sub = BeautifulSoup(response_sub.text,'html.parser')
                tabla_sub = soup_sub.find_all('table')[1]
                elementos_sub = tabla_sub.find_all('tr')
                for elemento_sub in elementos_sub:
                    tds_sub = elemento_sub.find_all('td')
                    if len(tds_sub) >= 3:
                        link_sub = tds_sub[1].find('a').get('href')
                        nombre_sub = tds_sub[1].find('a').text.replace(" ","")
                        print(link_sub, nombre_sub)
                        info["Nombre"].append(nombre_sub)
                        info["Enlace"].append(link_sub)
                        data = pd.DataFrame(info)
                        data.to_csv("data/" + nombre)

                        print(nombre_sub, link_sub)

    for elemento in elementos_div3_3:
        info = {
            "Nombre": [],
            "Enlace": []
        }

        tds = elemento.find_all('td')
        if len(tds) >= 3:
            link = url + tds[1].find('a').get('href')
            nombre = tds[1].find('a').text.replace(" ","") + ".csv"
            response_sub = requests.get(link)
            if response_sub.status_code == 200:
                print(response_sub.status_code)
                soup_sub = BeautifulSoup(response_sub.text,'html.parser')
                tabla_sub = soup_sub.find_all('table')[1]
                elementos_sub = tabla_sub.find_all('tr')
                for elemento_sub in elementos_sub:
                    tds_sub = elemento_sub.find_all('td')
                    if len(tds_sub) >= 3:
                        link_sub = tds_sub[1].find('a').get('href')
                        nombre_sub = tds_sub[1].find('a').text.replace(" ","")
                        print(link_sub, nombre_sub)
                        info["Nombre"].append(nombre_sub)
                        info["Enlace"].append(link_sub)
                        data = pd.DataFrame(info)
                        data.to_csv("data/" + nombre)

                        print(nombre_sub, link_sub)