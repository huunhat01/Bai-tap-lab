animal = {'cat','dog'}
print('cat' in animal)
print('fish' in animal)
animal.add('fish')
print('fish' in animal)
print(len(animal))
animal.add('cat')
print(len(animal))
animal.remove('cat')
print(len(animal))

print("")

#Loops
animal = {'cat','dog','fish'}
for idx, animal in enumerate(animal):
	print('#%d: %s' % (idx + 1, animal))

print("")

#Set comprehensions
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)