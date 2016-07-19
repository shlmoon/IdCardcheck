# coding: utf-8

from unittest import TestCase
from myIdcard import IdCardCheck


class IdCardTestCase(TestCase):
    def setUp(self):
        self.ic = IdCardCheck()

    def test_null_valid_idCard(self):
        with self.assertRaises(ValueError):
            self.ic.IdCard = ''

    def test_invalid_idCard_checkcode(self):
        self.ic.IdCard = '330726196507040011'
        self.assertFalse(self.ic.IdCard_isvalid())

    def test_invalid_idCard(self):
        with self.assertRaises(ValueError):
            self.ic.IdCard = '45612323'

    def test_valid_idCard(self):
        self.ic.IdCard = '330726196507040016'
        self.assertTrue(self.ic.IdCard_isvalid())

    def tearDown(self):
        self.ic = None
