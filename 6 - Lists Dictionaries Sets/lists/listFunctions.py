fruits = ["Apple", "Grape", "Pineapple", "Orange", "Watermelon"]

fruits.insert(3, "Melon")
print(fruits)

fruits.append("Peach")
print(fruits)

# Pega os valores da lista e adiciona a lista fruits
fruits.extend(["Banana", "Blueberry"])
print(fruits)

fruits.remove("Orange")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

print(fruits.index("Banana"))


scores = [1, 3, 7, 10, 84, 24, 65, 33]
# Encontra o maior valor
print(max(scores))

print(min(scores))

print(sum(scores))

print(scores.count(10))

# Cria uma lista reversa
print(list(reversed(scores)))
print(list(reversed(fruits)))

# Reverte a lista original
print(scores.reverse())
print(scores)

print(fruits.reverse())
print(fruits)

print("\nSorted lists")

print(list(sorted(fruits)))

fruits.sort()
print(fruits)


print(list(sorted(scores)))

scores.sort()
print(scores)