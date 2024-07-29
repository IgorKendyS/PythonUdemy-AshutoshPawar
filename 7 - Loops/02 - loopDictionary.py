Pokemon = {"Pikachu":"Elétrico","Charizard":"Dragão, Fogo", "Squirtle":"Água"}
Naruto = dict(
    Naruto = 'Uzumaki', 
    Minato = 'Namikaze', 
    Kakashi = 'Hatake'
    )

print(f"Pokemon Type : {type(Pokemon)}\nNaruto Type : {type(Naruto)}")

for poke in Pokemon:
    print(poke)
    
for value in Pokemon.values():
    print(value)
    
for nome, tipo in Pokemon.items():
    print(f"{nome} - {tipo}")