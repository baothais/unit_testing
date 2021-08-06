from . import practice4

p = practice4.Practice4()

class TestPratice4:

    def test_get_discounts(self):
        assert (p.get_discounts([2, 4, 6, 11], "50%") == [1, 2, 3, 5.5])
        assert (p.get_discounts([10, 20, 40, 80], "75%") == [7.5, 15, 30, 60])
        assert (p.get_discounts([100], "45%") == [45])
        assert (p.get_discounts([20], "1%") == [0.2])
        assert (p.get_discounts([100, 1000, 10000], "5%") == [5, 50, 500])

    def test_retrieve(self):
        assert (p.retrieve("A simple life is a happy life for me.") == ["a", "is", "a"])
        assert (p.retrieve("Exercising is a healthy way to burn off energy.") ==
                           ["exercising", "is", "a", "off", "energy"])
        assert (p.retrieve("The poor ostrich was ostracized.") == ["ostrich", "ostracized"])
        assert (p.retrieve("") == [])

    def test_DECIMATOR(self):
        assert (p.DECIMATOR("1234567890") == "123456789")
        assert (p.DECIMATOR("1234567890AB") == "1234567890")
        assert (p.DECIMATOR("123") == "12")
        assert (p.DECIMATOR("123456789012345678901") == "123456789012345678")
        assert (p.DECIMATOR("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ABCDEFGHIJKLMNOPQRSTUVW")
        assert (p.DECIMATOR("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") ==
                           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst")
        assert (p.DECIMATOR("A") == "")
        assert (p.DECIMATOR("") == "")

    def test_jazzify(self):
        assert (p.jazzify(['G', 'F', 'C']) == ['G7', 'F7', 'C7'])
        assert (p.jazzify(['Dm', 'G', 'E', 'A']) == ['Dm7', 'G7', 'E7', 'A7'])
        assert (p.jazzify(['F7', 'E7', 'A7', 'Ab7', 'Gm7', 'C7']) == ['F7', 'E7', 'A7', 'Ab7', 'Gm7', 'C7'])
        assert (p.jazzify(['G', 'C7']) == ['G7', 'C7'])
        assert (p.jazzify([]) == [])

    def test_parity_analysis(self):
        assert (p.parity_analysis(243) == True)
        assert (p.parity_analysis(12) == False)
        assert (p.parity_analysis(3) == True)
        assert (p.parity_analysis(5) == True)
        assert (p.parity_analysis(4) == True)
        assert (p.parity_analysis(3453) == True)
        assert (p.parity_analysis(0) == True)
        assert (p.parity_analysis(123456789) == True)
        assert (p.parity_analysis(987654321) == True)
        assert (p.parity_analysis(13) == False)
        assert (p.parity_analysis(37) == False)
        assert (p.parity_analysis(182) == False)
        assert (p.parity_analysis(133331) == False)

    def test_ascii_sort(self):
        assert (p.ascii_sort(["hey", "man"]) == "man")
        assert (p.ascii_sort(["majorly", "then"]) == "then")
        assert (p.ascii_sort(["magic", "kingdom"]) == "magic")
        assert (p.ascii_sort(["bored", "shampoo"]) == "bored")
        assert (p.ascii_sort(["victory", "careless"]) == "victory")

    def test_get_xp(self):
        assert (p.get_xp({
            'Very Easy': 89,
            'Easy': 77,
            'Medium': 30,
            'Hard': 4,
            'Very Hard': 1
        }) == '2055XP')

        assert (p.get_xp({
            'Very Easy': 254,
            'Easy': 32,
            'Medium': 65,
            'Hard': 51,
            'Very Hard': 34
        }) == '7650XP')

        assert (p.get_xp({
            'Very Easy': 11,
            'Easy': 0,
            'Medium': 2,
            'Hard': 0,
            'Very Hard': 27
        }) == '2255XP')

    def test_remove_vowels(self):
        assert (p.remove_vowels("ben") == "bn")
        assert (p.remove_vowels("many") == "mny")
        assert (p.remove_vowels("candy") == "cndy")
        assert (p.remove_vowels("hello") == "hll")
        assert (p.remove_vowels("apple") == "ppl")
        assert (p.remove_vowels("fever") == "fvr")

    def test_get_type(self):
        assert (p.get_type([]) == "list")
        assert (p.get_type("") == "str")
        assert (p.get_type(0) == "int")
        assert (p.get_type(None) == "NoneType")
        assert (p.get_type(False) == "bool")
        assert (p.get_type(0xFF) == "int")
        assert (p.get_type(set()) == "set")
        assert (p.get_type(tuple()) == "tuple")
        assert (p.get_type(dict()) == "dict")

    def test_sort_descending(self):
        assert (p.sort_descending(123) == 321)
        assert (p.sort_descending(670276097) == 977766200)
        assert (p.sort_descending(2619805) == 9865210)
        assert (p.sort_descending(81294) == 98421)
        assert (p.sort_descending(0000000) == 0000000)
        assert (p.sort_descending(321) == 321)
        assert (p.sort_descending(628904) == 986420)
        assert (p.sort_descending(289327560) == 987653220)
        assert (p.sort_descending(6456) == 6654)
        assert (p.sort_descending(444111888555333) == 888555444333111)
