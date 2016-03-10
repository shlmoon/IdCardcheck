
from unittest import TestCase
from myIdcard import IdCardCheck

class IdCardTestCase(TestCase):
    def setUp(self):
        self.ic = IdCardCheck()

    def test_valid_id_card(self):
        self.ic.IdCard = ''
        self.assertTrue(self.ic.IdCard_isvalid())

    def test_invalid_idCard_checkcode(self):
        self.ic.IdCard = '121212121245454587'
        self.assertFalse(self.ic.IdCard_isvalid())

    def test_invalid_idCard(self):
        self.assertRaises(ValueError, lambda: self.ic.IdCard_isvalid())

    def tearDown(self):
        self.ic = None
