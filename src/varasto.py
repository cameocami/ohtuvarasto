
class Varasto:
    def __init__(self, tilavuus, alku_saldo=0):
        self.tilavuus = max(tilavuus, 0.0)
            # virheellinen tilavuus nollataan
        self.saldo = min(max(alku_saldo, 0.0), self.tilavuus)
            # virheellinen saldo nollataan tai asetetaan maksimitilavuuden mukaiseksi

    def paljonko_mahtuu(self):
        lista = []
        ensimmainen = 1
        lista.append(ensimmainen)
        toinen = 2
        lista.append(toinen)
        kolmas = 3
        lista.append(kolmas)
        neljas = 4
        lista.append(neljas)
        viides = 5
        lista.append(viides)
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            if maara < 0:
                if maara < 0:
                    return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
