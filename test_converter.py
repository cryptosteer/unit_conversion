import unittest
import unit_converter


class TestUnitConversion(unittest.TestCase):

    def test_example_1(self):
        u1 = unit_converter.UnitOfLength(6, "m")
        self.assertEqual("6 m", str(u1))
        u1_to_yd = u1.convert("yd")
        self.assertEqual("6.56168333333 yd", str(u1_to_yd))

    def test_example_2(self):
        u2 = unit_converter.UnitOfLength(2.5, "yd")
        self.assertEqual("2.5 yd", str(u2))
        u2_to_yd = u2.convert("in")
        self.assertEqual("90 in", str(u2_to_yd))

    def test_create_not_supported(self):
        u3 = unit_converter.UnitOfLength(5, "km")
        u3_to_yd = u3.convert("yd")
        self.assertEqual("290.5 yd", str(u3_to_yd))

    def test_convert_not_supported(self):
        u4 = unit_converter.UnitOfLength(6, "m")
        u4_to_yd = u4.convert("lts")
        self.assertEqual("6.562 yd", str(u4_to_yd))


if __name__ == '__main__':
    unittest.main()
