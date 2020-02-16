class CashMachine:


    def __init__(self):
        self._bills = []


    @property
    def is_available(self):
        if self._bills:
            return True
        return False


    def put_money(self,bills):
        self._bills.extend(bills)

    def withdraw_money(self, amount):
        to_withdraw = []
        for bill in sorted(self._bills, reverse=True):
            if sum(to_withdraw) + bill <= amount :
                to_withdraw.append(bill)
        if sum(to_withdraw) == amount:
            for bill in to_withdraw:
                 self._bills.remove(bill)
        else:
            return []
        return to_withdraw


class TestCaschMachine:
    def test_initialization(self):
       return CashMachine()

    def test_is_avaliable(self):
        cs = CashMachine()
        assert  not cs.is_available

    def test_cs_is_avaliable_after_put_money(self):
        cs = CashMachine()
        assert not cs.is_available
        cs.put_money([100,100])
        assert  cs.is_available

    def test_withdraw_money(self):
        cs = CashMachine()
        cs.put_money([100, 100])
        assert cs.withdraw_money(200) == [100,100]
        assert cs.is_available is False

        cs = CashMachine()
        cs.put_money([100, 100,100])
        assert cs.withdraw_money(200) == [100,100]
        assert cs.is_available is True

        cs = CashMachine()
        cs.put_money([50, 50, 50])
        assert cs.withdraw_money(200) == []
        assert cs.is_available is True