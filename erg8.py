import urllib.request
import json

def price(symbolism, symbolism_in_eur=["EUR"]):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbolism.upper(), ','.join(symbolism_in_eur).upper())
    f=urllib.request.urlopen(url)
    initial=f.read()
    initial=initial.decode()
    data=json.loads(initial)
    return data

fileName = input("Enter file name: ")
file = open(fileName,'r')
file = file.read()
file = json.loads(file)


keys = []
for key in file.keys():
    keys.append(key)

lst={}
for i in keys:
    n_lst = price(i)
    lst[i] = n_lst["EUR"]*float(file[i]),"€"
print("Το ποσό των", file, "αντιστοιχεί σε",lst)
