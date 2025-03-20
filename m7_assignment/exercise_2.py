#!/usr/bin/env python3

import operator

fruit = {'oranges':3, 'apples':5, 'bananas':7,'pears':2}
print(fruit)

sorted_fruit = sorted(fruit.items())
print(sorted_fruit)

# sort using the item's key
sorted_fruit_key = sorted(fruit.items(), key = operator.itemgetter(0))
print(sorted_fruit_key)

# sort using the item's value
sorted_fruit_key = sorted(fruit.items(), key = operator.itemgetter(1))
print(sorted_fruit_key)

# sort using revers parameter
sorted_fruit_key_rev=sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_fruit_key_rev)
