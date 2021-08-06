from . import practice2

p = practice2.Practice2()

def test_two_digit_sum():
    assert (p.two_digit_sum(45) == 9)
    assert (p.two_digit_sum(65) == 11)
    assert (p.two_digit_sum(85) == 13)
    assert (p.two_digit_sum(52) == 7)

    assert (p.two_digit_sum(15) == 6)
    assert (p.two_digit_sum(48) == 12)
    assert (p.two_digit_sum(33) == 6)
    assert (p.two_digit_sum(29) == 11)

    assert (p.two_digit_sum(81) == 9)
    assert (p.two_digit_sum(10) == 1)
    assert (p.two_digit_sum(40) == 4)
    assert (p.two_digit_sum(66) == 12)

    assert (p.two_digit_sum(19) == 10)
    assert (p.two_digit_sum(38) == 11)
    assert (p.two_digit_sum(67) == 13)
    assert (p.two_digit_sum(96) == 15)

def test_get_frequencies():
    assert (p.get_frequencies(['A', 'A']) == {'A': 2})
    assert (p.get_frequencies(['A', 'B', 'A', 'A', 'A']) == {'A': 4, 'B': 1})
    assert (p.get_frequencies(['A', 'B', 'C', 'A', 'A']) == {'A': 3, 'B': 1, 'C': 1})
    assert (p.get_frequencies([1, 2, 3, 3, 2]) == {1: 1, 2: 2, 3: 2})
    assert (p.get_frequencies([True, False, True, False, False]) == {True: 2, False: 3})
    assert (p.get_frequencies([]) == {})

def test_alphanumeric_restriction():
    assert (p.alphanumeric_restriction("Bold") == True)
    assert (p.alphanumeric_restriction("123454321") == True)
    assert (p.alphanumeric_restriction("H3LL0") == False)
    assert (p.alphanumeric_restriction("hhefuhiwfgn") == True)
    assert (p.alphanumeric_restriction("0") == True)
    assert (p.alphanumeric_restriction("hhefuhiwfgn") == True)
    assert (p.alphanumeric_restriction("ed@bit") == False)
    assert (p.alphanumeric_restriction("only letters right") == False)
    assert (p.alphanumeric_restriction("132 143 234") == False)
    assert (p.alphanumeric_restriction("()") == False)
    assert (p.alphanumeric_restriction("Hello") == True)
    assert (p.alphanumeric_restriction("10,000") == False)
    assert (p.alphanumeric_restriction("1a2b3c") == False)
    assert (p.alphanumeric_restriction("") == False)

def test_factor_chain():
    assert (p.factor_chain([1, 2, 4, 8, 16, 32]) == True)
    assert (p.factor_chain([1, 1, 1, 1, 1, 1]) == True)
    assert (p.factor_chain([2, 4, 6, 7, 12]) == False)
    assert (p.factor_chain([10, 1]) == False)
    assert (p.factor_chain([10, 20, 30, 40]) == False)
    assert (p.factor_chain([10, 20, 40]) == True)
    assert (p.factor_chain([1, 1, 1, 1, 7, 49]) == True)

def test_abcmath():
    assert (p.abcmath(1, 2, 3) == False)
    assert (p.abcmath(69, 15, 9) == False)
    assert (p.abcmath(9, 2, 52) == False)
    assert (p.abcmath(5, 2, 3) == False)
    assert (p.abcmath(5, 2, 1) == True)
    assert (p.abcmath(261, 2, 1) == True)
    assert (p.abcmath(22, 2, 22) == True)
    assert (p.abcmath(69, 12, 3) == True)

def test_convert_binary():
    assert (p.convert_binary("house") == "01110")
    assert (p.convert_binary("excLAIM") == "0100000")
    assert (p.convert_binary("moon") == "0111")
    assert (p.convert_binary("MOOn") == "0111")
    assert (p.convert_binary("topsyTurvy") == "1111111111")

def test_vow_replace():
    assert (p.vow_replace("apples and bananas", "u") == "upplus und bununus")
    assert (p.vow_replace("cheese casserole", "o") == "chooso cossorolo")
    assert (p.vow_replace("stuffed jalapeno poppers", "e") == "steffed jelepene peppers")
    assert (p.vow_replace("shrimp tempura", "a") == "shramp tampara")
    assert (p.vow_replace("tuna sashimi", "i") == "tini sishimi")
    assert (p.vow_replace("chocolate cake", "a") == "chacalata caka")

def test_special_reverse():
    assert (p.special_reverse('word searches are super fun', 's') == 'word sehcraes are repus fun')
    assert (p.special_reverse('first man to walk on the moon', 'm') == 'first nam to walk on the noom')
    assert (p.special_reverse('peter piper picked pickled peppers', 'p') == 'retep repip dekcip delkcip sreppep')
    assert (p.special_reverse('he went to climb mount everest', 'p') == 'he went to climb mount everest')

def test_flatten_the_curve():
    assert (p.flatten_the_curve([1, 2, 3, 4, 5]) == [3, 3, 3, 3, 3])
    assert (p.flatten_the_curve([0, 0, 0, 2, 7, 3]) == [2, 2, 2, 2, 2, 2])
    assert (p.flatten_the_curve([4]) == [4])
    assert (p.flatten_the_curve([]) == [])
    assert (p.flatten_the_curve([7, 4, 2, 1]) == [3.5, 3.5, 3.5, 3.5])
    assert (p.flatten_the_curve([-13, 0, -18]) == [-10.3, -10.3, -10.3])
    assert (p.flatten_the_curve([24, 9, 18, -26, -4]) == [4.2, 4.2, 4.2, 4.2, 4.2])
    assert (p.flatten_the_curve([-16, -4, -8, 28, 26]) == [5.2, 5.2, 5.2, 5.2, 5.2])
    assert (p.flatten_the_curve([21, 2, 10]) == [11.0, 11.0, 11.0])
    assert (p.flatten_the_curve([-19, 4, -21, -23, -25, 23, -4]) == [-9.3, -9.3, -9.3, -9.3, -9.3, -9.3, -9.3])
    assert (p.flatten_the_curve([-19, 20]) == [0.5, 0.5])
    assert (p.flatten_the_curve([1, -24, 19]) == [-1.3, -1.3, -1.3])
    assert (p.flatten_the_curve([6, -8, -12, 12, 22, 26, -9, 8, 27, 13]) ==
                       [8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5])
    assert (p.flatten_the_curve([-7, -4]) == [-5.5, -5.5])
    assert (p.flatten_the_curve([23, -13, -13, -15, 13]) == [-1.0, -1.0, -1.0, -1.0, -1.0])
    assert (p.flatten_the_curve([22, -12, 0, -19, 2, 17, -11, 6]) == [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6])
    assert (p.flatten_the_curve([-18, -1, 28, -29, -7, 12, -11]) == [-3.7, -3.7, -3.7, -3.7, -3.7, -3.7, -3.7])
    assert (p.flatten_the_curve([-7, 13, 18]) == [8.0, 8.0, 8.0])
    assert (p.flatten_the_curve([-19, 29, -15, 30, -17]) == [1.6, 1.6, 1.6, 1.6, 1.6])
    assert (p.flatten_the_curve([26, -15, 4, -7, 30, 25, -16, -10, -15]) ==
                       [2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4])
    assert (p.flatten_the_curve([-24, 19, -25, -2, 12, 22, -3, 8, 29]) ==
                       [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0])
    assert (p.flatten_the_curve([-10, 23, -4, -29, -3, -17, -17, 18]) ==
                       [-4.9, -4.9, -4.9, -4.9, -4.9, -4.9, -4.9, -4.9])
    assert (p.flatten_the_curve([2, -13, -20, -25, 24, -18, -30, -4, 14, -21]) ==
                       [-9.1, -9.1, -9.1, -9.1, -9.1, -9.1, -9.1, -9.1, -9.1, -9.1])
    assert (p.flatten_the_curve([-10, 26, 14, 1, 14, -8, 3, -19]) == [2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6])
    assert (p.flatten_the_curve([8, -16, 28, 8, 16, 30, -4]) == [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0])

def test_minutes_to_seconds():
    assert (p.minutes_to_seconds("01:00") == 60)
    assert (p.minutes_to_seconds("13:56") == 836)
    assert (p.minutes_to_seconds("10:60") == False, "60 is invalid")
    assert (p.minutes_to_seconds("132:21") == 7941)
    assert (p.minutes_to_seconds("132:271") == False)
    assert (p.minutes_to_seconds("01:30") == 90)
    assert (p.minutes_to_seconds("10:00") == 600)

