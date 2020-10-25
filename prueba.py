import numpy as np
a=np.zeros(12,int)
b=np.zeros(12,int)
for num in a:
    a[num]=a
    b[num]=a

print(a)
print(b)
