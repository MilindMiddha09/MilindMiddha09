# *(star) --> unpacks a tuple/list
# --------------------------------------
#numbers=(1, 2, 3, 4, 5, 6, 7)
#print(*numbers, sep="; ")
#print(numbers)
#---------------------------------------

def test_star(*arg):
    print(arg)
    for i in arg:
        print(i)


test_star(1,2,3,4,5,6,7)
