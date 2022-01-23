import main
import unittest


class labTests(unittest.TestCase):

    def test_input1(self): # Проверка если вдруг IP4 не той версии
        with self.assertRaises(Exception):
            main.calc('ffe0::1:0:0:0')
    
    def test_input2(self): # Проверка если вдруг IP6 не той версии
        with self.assertRaises(Exception):
            main.calc6('255.255.3.0')

    def test_input3(self): # Проверка если файл с IPv4 пустой
        with self.assertRaises(Exception):
            main.calc('')
    
    def test_input4(self): # Проверка если файл с IPv6 пустой
        with self.assertRaises(Exception):
            main.calc6('')

    def test_input5(self): # Проверка если некорректный IPv4
        with self.assertRaises(Exception):
            main.calc('123 3213')

    def test_input6(self): # Проверка если некорректный IPv6
        with self.assertRaises(Exception):
            main.calc6('123 3213')

    def test_input7(self): # Проверка если граничное значение IPv4
        with self.assertRaises(Exception):
            main.calc('255.255.255.255', '255.255.255.255')

    def test_input8(self): # Проверка если граничное значение IPv6
        with self.assertRaises(Exception):
            main.calc6('FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF', 'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF') 
    
    def test_bin_to_dec(self):
        x = main.bin_to_dec(['1111111111111111', '1111111111111111','1111111111111111', '1111111111111111','1111111111111111', '1111111111111111','1111111111111111', '1111111111111111'])
        x1 = [65535, 65535, 65535, 65535, 65535, 65535, 65535, 65535]
        self.assertEqual(x, x1)


if __name__ == "__main__":
    unittest.main()