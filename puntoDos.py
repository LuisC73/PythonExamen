frutas = []

for variable in range(2):
    fruta = {}

    nombre = input("ingrese el nombre de la fruta: ")
    color = input("ingrese el color de la fruta: ")
    precio = input("ingrese el precio de la fruta: ")

    fruta["nombres"]= nombre
    fruta["color"] = color
    fruta["precio"] = precio

    frutas.append(fruta)

print(frutas)

rev = list(reversed(frutas))
print(rev)
    

