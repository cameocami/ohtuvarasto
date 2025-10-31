import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negative_capacity_and_negative_initial_balance(self):
        v = Varasto(-5, -10)
        self.assertEqual(v.tilavuus, 0)
        self.assertEqual(v.saldo, 0)

    def test_initial_balance_equals_capacity(self):
        v = Varasto(10, 10)
        self.assertEqual(v.saldo, 10)
        self.assertEqual(v.paljonko_mahtuu(), 0)

    def test_add_to_full_varasto(self):
        v = Varasto(5, 5)
        v.lisaa_varastoon(1)
        self.assertEqual(v.saldo, 5)

    def test_add_negative_amount(self):
        v = Varasto(10, 5)
        v.lisaa_varastoon(-2)
        self.assertEqual(v.saldo, 5)

    def test_take_negative_amount(self):
        v = Varasto(10, 5)
        result = v.ota_varastosta(-3)
        self.assertEqual(result, 0)
        self.assertEqual(v.saldo, 5)

    def test_take_more_than_balance(self):
        v = Varasto(10, 4)
        result = v.ota_varastosta(10)
        self.assertEqual(result, 4)
        self.assertEqual(v.saldo, 0)

    def test_take_exact_balance(self):
        v = Varasto(10, 6)
        result = v.ota_varastosta(6)
        self.assertEqual(result, 6)
        self.assertEqual(v.saldo, 0)

    def test_str_representation_empty(self):
        v = Varasto(10, 0)
        self.assertEqual(str(v), "saldo = 0, vielä tilaa 10")

    def test_str_representation_full(self):
        v = Varasto(10, 10)
        self.assertEqual(str(v), "saldo = 10, vielä tilaa 0")

    def test_str_representation_partial(self):
        v = Varasto(10, 3)
        self.assertEqual(str(v), "saldo = 3, vielä tilaa 7")