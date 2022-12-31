import random
from progressbar import ProgressBar
import time

# c = ["!","@","#","$","%","^","&","*","(",")"]
# t = [[],[],[],[],[]]
# a = 0
# while a < 5:
#     b = 0
#     while b < 5:
#         t[a].append(random.randint(0,9))
#         b += 1
#     a += 1
# print(t)
# print('******')
# a = 0
# while a < 5:
#     print(c[t[a][0]],c[t[a][1]],c[t[a][2]], c[t[a][3]], c[t[a][4]] )
#     a += 1

print('sedning report about failure')

a = 0
bar = ProgressBar(maxval=100)
bar.start()

while a < 100:
    time.sleep(0.1)
    bar.update(a)
    a += 10
bar.finish()
print("Done")