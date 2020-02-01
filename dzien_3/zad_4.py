# # import random
# #
# # def random_number():
# #     return random.randint(1, 101)
# #
# # def test_random_number():
# #     random.seed(0)
# #     assert random_number() == 50
# #     random.seed(10)
# #     assert random_number() == 74
#
# def only_ints(a,b):
#     return type(a) == int and type(b) == int
#
#
# only_ints(1, 2)
#
#
#
#
# def test_only_ints():
#     assert only_ints(1, 2) == True
#     assert only_ints("10", 1) == False
#     assert  only_ints(1, True) == False
#
# def double_leters(napis):
#
#     for i in range(len(napis) - 1 ):
#         if napis[i] == napis[i + 1]:
#             return True
#     return False
#
#
#
#
# def test_double_leters():
#     assert double_leters("ala") == False
#     assert double_leters("alla") == True
#     assert double_leters("nono") == False

def add_dots(napis):
    return ".".join(napis)



def remove_dots(napis):
    #return "".join(napis.split("."))
    return napis.replace(".", "")

def test_add_dots():
    assert add_dots("test") == "t.e.s.t"