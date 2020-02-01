# import time
#
# wynik = []
# N = 10000000
# start = time.time()
# for el in range(10):
#     wynik.append(el**3)
#     print(wynik)
#
# print([(el,el**3) for el in range(10) if el %2 ==0])
# print(time.time() - start)

print([(el/10) for el in range(0, 10, 1)])
print([(el - 10,(el-10)**2,(el-10)**3) for el in range(0,20,1)])
print([(el,el**2,el**3) for el in range(-10,10,1)])
x = set