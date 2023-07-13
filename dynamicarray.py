''' Dynamic array implementation'''

import ctypes
from sys import getsizeof

class DynamicArray(object):
    def __init__(self):
        self.n        = 0
        self.capacity = 1
        self.A        = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getItem__(self,k):
        
        if not 0 <= k < self.n:
            return IndexError("k is out of bounds!")
        return self.A[k]

    def append(self,element):
        if (self.n == self.capacity):
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1

    def _resize(self,new_capacity):
        
        B = self.make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        
        self.A = B
        self.capacity = new_capacity

    def make_array(self,capacity):
        return (capacity*ctypes.py_object)()

a = DynamicArray()
a.append(23)
a.append(12)

q = a.__getItem__(1)
print(q)

for i in range(50):
    q= (len(a))
    w = getsizeof(a)
    print("length:{0:3d}  ' size in bytes:{1:4d} ".format(q,w))
    a.append(i)