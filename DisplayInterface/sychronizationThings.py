import requests

from Model.ThingsModel import ThingsModel


def synchronizationThings(Token, Location, nThings):
        try:
            url = "https://dg-2ts-server.herokuapp.com/"
            response = requests.get(url + "synchronize_location/token="+ Token +"&locaid="+Location+"&num=" + nThings)
            data = response.json()

            if response.ok:
                try:
                    if data["response"] == None:
                        print("Aqui")
                    else :
                        print(data["response"])
                except Exception as e:
                    u = ThingsModel (**data)
                    print (u.token)

        except Exception as e:
            print ("Erro no Servidor")

synchronizationThings("asdfasdfasdfz","8", "039583")