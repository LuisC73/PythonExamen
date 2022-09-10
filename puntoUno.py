
c=int(input("Cantidad de números: "))
contadorDos = 0
contadorTres = 0

for variable in range(c):
    
    numero=int(input("Número: "))

    if numero%2 == 0:
        contadorDos = contadorDos + 1

    if numero%3 == 0:
        contadorTres = contadorTres + 1

print(f'Usted ingreso {contadorDos} numeros multiplos de 2')
print(f'Usted ingreso {contadorTres} numeros multiplos de 3')
