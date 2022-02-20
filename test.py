import main
import unittest


class labTests(unittest.TestCase):

    def test_input1(self): # Проверка если вдруг IP не той версии
        with self.assertRaises(Exception):
            main.calc('ffe0::1:0:0:0')

    def test_input2(self): # Проверка если файл с IP пустой
        with self.assertRaises(Exception):
            main.calc('')

    def test_input3(self): # Проверка если некорректный IP
        with self.assertRaises(Exception):
            main.calc('123 3213')

    def test_input4(self): # Проверка если граничное значение IP
        with self.assertRaises(Exception):
            main.calc('999.999.999.999', '999.999.999.999')

    def test_input5(self): # Проверка если отрицательные значения IP
        with self.assertRaises(Exception):
            main.calc('-999.-999.-999.-999', '-999.-999.-999.-999')

    def test_input6(self):
        with self.assertRaises(Exception):
            main.calc('ghjsfdgfhs')
    
    def test_input7(self):
        with self.assertRaises(Exception):
            main.calc('1')

    def test_res1(self):
        x = main.calc('34.23.89.190', '34.23.101.190')
        x1 = main.calc('34.23.89.190', '34.23.101.190')
        self.assertEqual(x, x1)

    def test_res2(self):
        x = main.calc('34.23.89.190', '34.23.101.190')
        x1 = main.calc('34.23.101.190', '34.23.89.190')
        self.assertEqual(x, x1)

    def test_res3(self):
        x = main.calc('167.128.92.70', '167.128.92.17', '167.128.92.68', '152.139.27.80')
        self.assertTrue(x == '192.0.0.0   128.0.0.0')

    def test_alg1(self):
        x = main.calc('122.22.22.2', '122.22.22.2')
        self.assertTrue(x == '255.255.255.255   122.22.22.2')

    def test_alg2(self):
        x = main.calc('0.0.0.0', '0.0.0.0')
        self.assertTrue(x == '255.255.255.255   0.0.0.0')

    def test_alg3(self):
        x = main.calc('255.255.255.255', '255.255.255.255')
        self.assertTrue(x == '255.255.255.255   255.255.255.255')

    def test_alg4(self):
        x = main.calc('255.255.255.255', '0.0.0.0')
        self.assertTrue(x == '0.0.0.0   0.0.0.0')

    def test_alg5(self):
        x = main.calc('1.2.3.4', '128.5.7.8')
        self.assertTrue(x == '0.0.0.0   0.0.0.0')

    def test_alg6(self):
        x = main.calc('255.255.255.255', '255.255.255.255', '255.255.255.255', '255.255.255.255', '255.255.255.255', '0.0.0.0')
        self.assertTrue(x == '0.0.0.0   0.0.0.0')

    def test_alg7(self):
        x = main.calc('255.255.255.255', '255.255.255.0')
        self.assertTrue(x == '255.255.255.0   255.255.255.0')


if __name__ == "__main__":
    unittest.main()