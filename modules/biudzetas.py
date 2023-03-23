import pickle
from .islaidu_irasas import IslaiduIrasas
from .pajamu_irasas import PajamuIrasas
print('laba diena')

class Biudzetas:
    def __init__(self):
        self.zurnalas = self._gauti_zurnala()

    def _gauti_zurnala(self):
        try:
            with open('zurnalas.pkl', 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def _irasyti(self):
        with open('zurnalas.pkl', 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self._irasyti()

    def prideti_islaidu_irasa(self, suma, budas, isigyta):
        irasas = IslaiduIrasas(suma, budas, isigyta)
        self.zurnalas.append(irasas)
        self._irasyti()

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                suma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                suma -= irasas.suma
        return suma

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)
