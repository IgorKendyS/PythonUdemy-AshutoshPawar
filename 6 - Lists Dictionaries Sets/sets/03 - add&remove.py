seta = {1,2,3,4,5}

seta.add(80)

#dá erro se não tiver o valor
seta.remove(5)

print(seta)

#não dá erro caso não tenha
seta.discard(71)
print(seta)

print(f"Elemento retirado: {seta.pop()}")
print(seta)

seta.clear()
print(seta)