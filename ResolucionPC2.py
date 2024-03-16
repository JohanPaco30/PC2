#Resolucion de la Practica 2

"""
Estructuras Iterativas:
Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).
"""
div_prim = []

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        div_prim.append(i)
print(div_prim)

"""
Problema 2:
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
x = 5
for i in range(x):
    print("* " *(i+1))

for i in range(x -1,0,-1):
    print("* " *(i))

"""
Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
"""
def contar_par_impar(num):
    pares = 0
    impares = 0
    for i in num:
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

lista = []

while True:
    opcion = input("¿Desea ingresa un numero?: SI o NO")
    op_MAY= opcion.upper()
    if op_MAY == 'SI':
        n = int(input("Ingrese el número: "))
        lista.append(n)
    if op_MAY == 'NO':
        break
    pares, impares = contar_par_impar(lista)
    
print(f"Números ingresados: {lista}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

"""
Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
"""
alumnos_notas = []
notas = []

def ingreso_datos(n):
    for a in range(n):
        nombre = input(f"Ingrese el nombre del alumno {a+1}: ")
        for b in range(3):
            nota = float(input(f"Ingrese la calificacion {b+1} del alumno {nombre}: "))
            notas.append(nota)
        alumno_nota = {"Alumno": nombre, "Notas": notas}
        alumnos_notas.append(alumno_nota)
    return alumnos_notas

n = int(input("Ingrese la cantidad de almunos: ")) 
alumnos_notas = ingreso_datos(n)

print(alumnos_notas)

"""
Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
"""
def verficar(num, digito):
    numeros = str(num)
    conteo = numeros.count(digito)
    return conteo


numero = input("Ingrese el número: ")
digito = input("Ingrese el digito: ")
conteo = verficar(numero, digito)

print(f"El digito '{digito}' en el numero se repite: {conteo} veces.")

"""
Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.
"""
lista = [0,1]

while lista[-2] + lista[-1] <= 50:
        suma = lista[-2] + lista[-1]
        lista.append(suma)
else:
    print(f"La serie de Fibonacci hasta el numero 50 es:\n{lista}")

"""
Problema 7:
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.
"""
def primo(n):
    es_primo = True
    for i in range(2,n):
        if n % i == 0:
            es_primo = False
            break
    return es_primo

num = int(input("Ingrese un número: "))
es_primo = primo(num)

if es_primo:
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")

"""
Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
"""
def fact(num):
    facto = 1
    for i in range(1,num + 1):
        facto *= i
    return facto

facto = fact(n)
n = int(input("ngrese un numero: "))
print(facto)

"""
Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
"""
vocales = 'aeiouAEIOU'
sin_vocales = ''

msg = input("Escriba algo: ")
for i in msg:
    if i not in vocales:
        sin_vocales += i
        
print(sin_vocales)

"""
Problema 10:
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
"""
MESES = [
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]

mes = input("Ingrese el mes (MM): ")
dia = input("Ingrese el dia (DD): ")
año = input("Ingrese el año (AAAA): ")

for mes in range(*MESES):
    if mes == MESES:
        mes_1 = MESES.index(mes+1)


print(f"La fecha es: {año}-{mes + 1}-{dia}")


