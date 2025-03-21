#trabajo 1,punto 1:
edad = int(input("decime tu edad: "))
print(f"te faltan {100-edad} años para llegar a los 100 años")

#trabajo 1,punto 2:
temp = float(input("decime la temperatura en grados celsius: "))
print(f"la temperatura en grados fahrenheit es: {temp*1.8+32}")

#trabajo 1,punto 3:
j=0
for i in range(1,101):
    j+=i
print(j)

#trabajo 1,punto 4:
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for i in numeros:
    if i%2==0:
        print(i)

#trabajo 1,punto 5:
lista = input("ingrese una lista de numeros separados por coma: ")
lista = lista.split(",")
for i in lista:
    if int(i)>0:
        print(i)
    else:
        break

#trabajo 1,punto 6:
numeros = [0,1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []
for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
print(pares)
print(impares)

#trabajo 1,punto 7:
lista = input("ingrese una lista de numeros separados por coma: ")
lista = lista.split(",")
lista_nueva = []
for i in lista:
    if int(i) % 3 != 0:
        lista_nueva.append("-"+str(i))
print(lista_nueva)



