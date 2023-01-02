import matplotlib.pyplot as plt
import numpy as np
import random

def phi_zeros(n):
    phi_mods = [1, 3, 5, 10, 19, 35, 64, 117, 213, 387, 704, 1277, 2319, 4209, 7640, 13868, 25171, 45685, 82919, 150498, 273155, 495776, 899834, 1633198, 2964256, 5380124, 9764926, 17723342, 32167866, 58384676, 105968188]
    for i in range(len(phi_mods)):
        if n % phi_mods[i] != 0:
            return i
    return len(phi_mods)

def number_phi_dist():
    vals = []
    index = []
    counter = dict()
    for i in range(1, 10000):
        v = str(phi_zeros(random.randint(0,1<<32)))
        if v in counter:
            counter[v] += 1
        else:
            counter[v] = 1
    
    for k in counter:
        vals.append(counter[k])
        index.append(k)

    vals = [ x for _, x in sorted(zip(index, vals))]
    index.sort()
    plt.yscale('log')
    plt.bar(index, vals)
    plt.show()


def to_base(n, base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))
    return ''.join(reversed(nums))

def get_phi():
    vals=[]
    phi = 1.815
    for i in range(32):
        vals.append(int(phi ** i))
    print(vals)

number_phi_dist()
#get_phi()

# vals = np.arange(30)
# y1 = [int(x ** 1.815) for x in vals]
# y2 = [int(x ** 2) for x in vals]

# print(y1)
# print(y2)

# plt.plot(vals, y1, label='phi')
# plt.plot(vals, y2, label='square')
# plt.legend()
# plt.show()

