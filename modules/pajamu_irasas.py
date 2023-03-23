from .irasas import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas}, info: {self.info}"
