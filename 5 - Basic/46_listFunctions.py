fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grape']
print(len(fruits))

fruits.insert(1,'lemon')
print(fruits)

# nested list - adiciona uma lista dentro de outra
fruits.append(['pineapple', 'apricot'])
print(fruits)

# adiciona item na lista
fruits.extend(["strawberry", "blueberry"])
print(fruits)

fruits.remove(['pineapple', 'apricot'])
print(fruits)

# remove last item
fruits.pop()
print(fruits)

# search index item
print(fruits.index('orange'))

scores = [1, 2, 3, 4, 5, 6, 90, 30]
# print(max(scores))
print(min(scores))