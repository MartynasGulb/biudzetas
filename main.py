from modules.biudzetas import Biudzetas
import os

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - pridėti pajamas\n2 - pridėti išlaidas\n3 - balansas\n4 - ataskaita\n0 - išeiti\n"))
    match pasirinkimas:
        case 1:
            suma = float(input("Suma: "))
            siuntejas = input("Siuntėjas: ")
            info = input("Papildoma informacija: ")
            biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
        case 2:
            suma = float(input("Suma: "))
            budas = input("Mokėjimo būdas: ")
            isigyta = input("Įsigyta prekė/paslauga: ")
            biudzetas.prideti_islaidu_irasa(suma, budas, isigyta)
        case 3:
            print(biudzetas.gauti_balansa())
        case 4:
            biudzetas.parodyti_ataskaita()
        case 9:
            try:
                biudzetas.zurnalas.clear()
                os.remove('zurnalas.pkl')
            except FileNotFoundError:
                print('faila nera')

        case 0:
            print("Viso gero")
            break
