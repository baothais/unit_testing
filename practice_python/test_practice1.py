from . import practice1

p = practice1.Practice1()


def test_split():
    assert p.split("abcde") == "aebcd"
    assert p.split("Hello!") == "eoHll!"
    assert p.split("What's the time?") == "aeieWht's th tm?"


def test_calc_diff():
    assert p.calc_diff({"baseball bat": 20}, 5) == 15

    assert p.calc_diff({"skate": 10, "painting": 20}, 19) == 11

    assert p.calc_diff({"skate": 200, "painting": 200, "shoes": 1}, 400) == 1

def test_get_distance():
    assert (p.get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}) == 6.325, "Example #1")
    assert (p.get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}) == 1.414, "Example #2")
    assert (p.get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16})== 21.095, "Example #3")
    assert (p.get_distance({"x": 4, "y": 3}, {"x": 3, "y": -2})== 5.099)
    assert (p.get_distance({"x": -1, "y": -1}, {"x": 10, "y": 10})== 15.556)
    assert (p.get_distance({"x": 100, "y": 100}, {"x": 100, "y": 100})== 0)
    assert (p.get_distance({"x": 14239, "y": -11222}, {"x": -12301, "y": 12888})== 35856.153)

def test_sum_of_evens():
    assert (p.sum_of_evens([
        [1, 5, 1, 3],
        [4, 1, 2, 0],
        [6, 9, 7, 4],
        [5, 1, 2, 6]
    ]) == 24)

    assert (p.sum_of_evens([
        [1, 0, 1],
        [33, 1, 2],
        [15, 9, 1],
        [5, 1, 979]
    ]) == 2)

    assert (p.sum_of_evens([
        [2, 19, 5, 43],
        [67, 2, 0, 12]
    ]) == 16)

    assert (p.sum_of_evens([
        [1, 3, 7, 9],
        [11, 13, 15, 17],
        [19, 21, 23, 25]
    ]) == 0)

    assert (p.sum_of_evens([
        [],
        [],
        []
    ]) == 0)

def test_count_all():
    assert (p.count_all("Hello") == {"LETTERS": 5, "DIGITS": 0})
    assert (p.count_all("137") == {"LETTERS": 0, "DIGITS": 3})
    assert (p.count_all("H3LL0") == {"LETTERS": 3, "DIGITS": 2})
    assert (p.count_all("149990") == {"LETTERS": 0, "DIGITS": 6})
    assert (p.count_all("edabit 2018") == {"LETTERS": 6, "DIGITS": 4}, "Spaces are not letters.")
    assert (p.count_all("    ") == {"LETTERS": 0, "DIGITS": 0})

def test_to_list_number():
    assert (p.to_list(235) == [2, 3, 5])
    assert (p.to_list(19) == [1, 9])
    assert (p.to_list(0) == [0])
    assert (p.to_number([2, 3, 5]) == 235)
    assert (p.to_number([1, 9]) == 19)
    assert (p.to_number([0]) == 0)

def test_first_last_arg():
    assert (p.first_arg(1, 2, 3) == 1)
    assert (p.first_arg('a', 'b', 'c') == 'a')
    assert (p.first_arg(8) == 8)
    assert (p.first_arg() == None)
    assert (p.last_arg(1, 2, 3) == 3)
    assert (p.last_arg('a', 'b', 'c') == 'c')
    assert (p.last_arg(8) == 8)
    assert (p.last_arg() == None)

def test_has_digit():
    assert (p.has_digit("c8") == True)
    assert (p.has_digit("23cc4") == True)
    assert (p.has_digit("abwekz") == False)
    assert (p.has_digit("sdfkxi") == False)
    assert (p.has_digit('rxizw') == False)
    assert (p.has_digit('jren3biy') == True)
    assert (p.has_digit('mxkbj3bg') == True)
    assert (p.has_digit('qageha') == False)
    assert (p.has_digit('qian5rtjzwgkjk') == True)
    assert (p.has_digit('kyehbjosrx') == False)
    assert (p.has_digit('cvlcg2ggggzowzas') == True)
    assert (p.has_digit('jjbbvb7kjmypz') == True)
    assert (p.has_digit('rfjgzn50djg') == True)
    assert (p.has_digit('mvepzvqgumaihtoudh') == False)
    assert (p.has_digit('kauhkwmd') == False)
    assert (p.has_digit('s8fonjkblhu') == True)
    assert (p.has_digit('krkccxwmmx3lcjbe') == True)
    assert (p.has_digit('dirg') == False)
    assert (p.has_digit('ntqdkskd6srln') == True)
    assert (p.has_digit('tkabcvzfabqz') == False)
    assert (p.has_digit('umqihuaikhzcaprtmrkf') == False)
    assert (p.has_digit('nvvwhxt') == False)
    assert (p.has_digit('r2clrks') == True)
    assert (p.has_digit('mlzuwfusierivfrbq') == False)
    assert (p.has_digit('mvggduqcr') == False)
    assert (p.has_digit('sbxfntq4ekwf') == True)
    assert (p.has_digit('ulylvolxuf5vofllvdjg') == True)
    assert (p.has_digit('usa3ouizefs') == True)
    assert (p.has_digit('hqmszb7somqcdnox') == True)
    assert (p.has_digit('ftnnqspmdifi') == False)
    assert (p.has_digit('fbgryiyzjirysz') == False)
    assert (p.has_digit('rhwikmwfzis') == False)
    assert (p.has_digit('ru4rlpyv') == True)
    assert (p.has_digit('kokzjam32zl7bnucb') == True)
    assert (p.has_digit('zpy6kasuouaq') == True)
    assert (p.has_digit('nctja8xktcipevfo') == True)
    assert (p.has_digit('anevx6cgqa') == True)
    assert (p.has_digit('fzxbb') == False)
    assert (p.has_digit('hryvztjuvjspcfjtezh') == False)
    assert (p.has_digit('qvwbeepylwsqnipb') == False)
    assert (p.has_digit('dsrgbgeqopjvqgjto') == False)
    assert (p.has_digit('o6fwynnypu') == True)
    assert (p.has_digit('oordrxk3j1lbo') == True)
    assert (p.has_digit('kgbfxnmjbh') == False)
    assert (p.has_digit('fklgfkiafmvxifqz') == False)
    assert (p.has_digit('xct') == False)
    assert (p.has_digit('kqf6tneg') == True)
    assert (p.has_digit('xu0w') == True)
    assert (p.has_digit('erqcrooj9tu') == True)
    assert (p.has_digit('niouwjzphmyllvmwf') == False)
    assert (p.has_digit('lmnuovrhlg') == False)
    assert (p.has_digit('xlnjr33gtj4gcmuw') == True)
    assert (p.has_digit('meijxmi0mfvsvajsqn') == True)
    assert (p.has_digit('gnd7rksfnx0vxz') == True)

def test_oddeven():
    assert (p.oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True)
    assert (p.oddeven([1]) == True)
    assert (p.oddeven([1, 2, 3, 4, 5, 6, 7, 9]) == True)
    assert (p.oddeven([2, 1, 3]) == True)
    assert (p.oddeven([42, 1, 66]) == False)
    assert (p.oddeven([2, 3, 4, 5, 6, 7, 8]) == False)
    assert (p.oddeven([43264573658142353463158]) == True)
    assert (p.oddeven([1, 2, 4]) == False)

def test_dict_to_list():
    d1 = {'D': 1, 'B': 2, 'C': 3}
    d2 = {'likes': 2, 'dislikes': 3, 'followers': 10}
    assert (p.dict_to_list(d1), [('B', 2), ('C', 3), ('D', 1)])
    assert (p.dict_to_list(d2), [('dislikes', 3), ('followers', 10), ('likes', 2)])