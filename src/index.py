from varasto import Varasto

def luo_varastot():
    return Varasto(100.0), Varasto(100.0, 20.2)

def alku_demo(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def hakujen_demo(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def setterit_demo(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def negatiivinen_luvut_alustuksessa_demo():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7);")
    huono = Varasto(100.0, -50.7)
    print(huono)

def tilavuuden_ylitys_demo(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def lisaa_varastoon_negatiivinen_demo(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def ota_varastosta_yli_tilavuuden_demo(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def ota_varastosta_negatiivinen_demo(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.ota_varastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")




def main():
    mehua, olutta = luo_varastot()
    alku_demo(mehua, olutta)
    hakujen_demo(olutta)
    setterit_demo(mehua)
    negatiivinen_luvut_alustuksessa_demo()
    tilavuuden_ylitys_demo(olutta)
    lisaa_varastoon_negatiivinen_demo(mehua)
    ota_varastosta_yli_tilavuuden_demo(olutta)
    ota_varastosta_negatiivinen_demo(mehua)

if __name__ == "__main__":
    main()
