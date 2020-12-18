xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop()
print(x,xs)
print("")
#Slicing
nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
print(nums[:-1])
nums[2:4] = [8,9]
print(nums)

print("")

#loops
animals = ['cat','dog','monkey']
for animal in animals:
	print(animal)

print("")

#list comprehensions
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
	squares.append(x ** 2)
print(squares)

print("")
#Dictionaries
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
	legs = d[animal]
	print('A %s has %d legs' % (animal, legs))

print("")
d = {'cat':'cute','dog':'furry'}
print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])
print(d.get('monkey','N/A'))
print(d.get('fish','N/A'))
del d['fish']
print(d.get('fish','N/A'))

print("")
#Dictionary comprehensions
nums = [0,1,2,3,4]
even_num_to_square = {x:x**2 for x in nums if x % 2 == 0}
print(even_num_to_square)




