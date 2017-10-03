import requests

from Model.LocationModel import LocationModel
from Model.ThingsModel import ThingsModel

url = "https://dg-2ts-server.herokuapp.com/"


def searchThingByNumber(token, thingNumber):
    try:

        response = requests.get (url + "search_things_by_num/token=" + token +"&num=" + thingNumber)
        print (url + "search_things_by_num/token=" + token + "&num=" + thingNumber)
        data = response.json ()
        print (data)

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Aqui")
                else:
                    print (data["response"])
            except Exception as e:
                things = [ThingsModel (**data)]
                # for dado in data:
                #     things.append (ThingsModel (**dado))

                return things
    except Exception as e:
        print ("Erro no Servidor !!")
        print(e)

def searchThingsInactives(token):
    try:
        response = requests.get(url + "search_all_things_inactived/token=" + token)
        data = response.json()

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Nothing found !!")
                else:
                    print("Things: " + data["response"])
            except Exception as e:
                things = []
                for dado in data:
                    things.append (ThingsModel (**dado))

                return things

    except Exception as e :
        print("Server Error")

def searchThingsActived(token):
    try:
        response = requests.get(url + "search_all_things_actived/token=" + token)
        data = response.json()

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Nothing found !!")
                else:
                    print("Things: " + data["response"])
            except Exception as e:
                things = []
                for dado in data:
                    things.append (ThingsModel (**dado))

                return things

    except Exception as e :
        print("Server Error")

def activeThingByNumber(token, thingNumber):
        try:
            response = requests.get (url + "active_thing_by_num/token=" + token + "&num=" + thingNumber)
            data = response.json()
            # print(data)

            if response.ok:
                try:
                    if data["response"] == None:
                        print ("Nothing found !!")
                    else:
                        if data["response"] == 'true':
                            print ("Tag actived with sucess !!")
                        else:
                            print ("Unable to activate tag !!")
                except Exception as e:
                    things = []
                    for dado in data:
                        things.append (ThingsModel (**dado))

                    return things

        except Exception as e:
            print ("Server Error !!")



def searchThingsByLocation(token, idLocation):

    try:
        response = requests.get(url + "search_things_by_location/token=" + token + "&locaid=" + idLocation)
        data = response.json()

        print(data)

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Nothing found !!")
                else:
                    print ("Things: " + data["response"])
            except Exception as e:
                things = []
                for dado in data:
                    things.append(ThingsModel(**dado))

                return things
    except Exception as e:
        print("Server Error !!")


def searchLocations(token):
    try:
        response = requests.get (url + "search_locations/token=" + token)
        data = response.json ()

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Aqui")
                else:
                    print (data["response"])
            except Exception as e:
                locations=[]
                for dados in data:
                    # print(dados)
                    locations.append(LocationModel(**dados))

                return locations
    except Exception as e:
        print ("Erro no Servidor")

def searchThingsInactivesByLocation(token, loca_id):
    try:
        response = requests.get (url + "search_things_inactived_by_location/token=" + token + "&locaid=" + loca_id)
        data = response.json ()

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Aqui")
                else:
                    print (data["response"])
            except Exception as e:
                things = []
                for dado in data:
                    things.append (ThingsModel (**dado))

                return things
    except Exception as e:
        print ("Erro no Servidor")

def searchThingsActivesByLocation(token, loca_id):
    try:
        response = requests.get (url + "search_things_actived_by_location/token=" + token + "&locaid=" + loca_id)
        data = response.json ()

        if response.ok:
            try:
                if data["response"] == None:
                    print ("Aqui")
                else:
                    print (data["response"])
            except Exception as e:
                things = []
                for dado in data:
                    things.append (ThingsModel (**dado))

                return things
    except Exception as e:
        print ("Erro no Servidor")

# a = ThingsModel
a = searchThingByNumber('asdfasdfasdfz', '88670')
b = []
b.append([a[0].code_things, a[0].tag_activated ])

print(b)

# searchThingsInactives('sdfsdf')
# activeThingByNumber('asdfasdfasdfz', '88670')
# dados = searchThingsByLocation('asdfasdfasdfz', '7')
# dados = searchLocations('asdfasdfasdfz')
# #
# for b in dados:
#     print(b)
