# coding: utf-8

from functools import reduce


class IdCardCheck(object):

    def __init__(self):
        super(IdCardCheck, self).__init__()
        self._IdCard = ''

    @property
    def IdCard(self):
        return self._IdCard

    @IdCard.setter
    def IdCard(self, id_card):
        if isinstance(id_card, str) or isinstance(id_card, unicode):
            if len(id_card) == 18:
                self._IdCard = id_card
                return

        raise ValueError('IdCard is invalid.')

    def set_valus_datatype(self, valus):
        if isinstance(self.IdCard, str):
            return str(valus)
        else:
            return unicode(valus)

        # elif isinstance(self.IdCard, unicode):
        #     return unicode(valus)

    def get_checkCode(self):
        CountValue = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        get_checkcode_key = reduce(
            lambda x, y: x + y,
            map(
                lambda x, y: x * y,
                [int(x) for x in self.IdCard[:-1]],
                CountValue))

        checkcode_key = get_checkcode_key % 11
        CountRule = {
            '0': '1',
            '1': '0',
            '2': 'X',
            '3': '9',
            '4': '8',
            '5': '7',
            '6': '6',
            '7': '5',
            '8': '4',
            '9': '3',
            '10': '2'}
        get_checkcode_value = CountRule.get(str(checkcode_key), None)
        return self.set_valus_datatype(get_checkcode_value)

    def get_validIdCard(self):
        return '%s%s' % (self.IdCard[:-1], self.get_checkCode())

    def IdCard_isvalid(self):
        if self.IdCard[-1] == self.get_checkCode():
            return True

        return False
