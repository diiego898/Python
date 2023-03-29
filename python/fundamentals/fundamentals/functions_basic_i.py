#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#Respuesta: 5 porque es el numero que se retornara

#----------------------------------------------------------------------

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#Respuesta: Porque number_of_days_in_a_week_silicon_or_triangle_sides no esta definido en la funcion

#----------------------------------------------------------------------

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#Respuesta: 5 porque siempre se concidera el primer return 

#----------------------------------------------------------------------

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Respuesta: 5 porque el return le da el valor a number_of_fingers

#----------------------------------------------------------------------

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Respuesta: 5 porque se invoca number_of_great_lakes

#----------------------------------------------------------------------

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Respuesta: El print numero 1 dara 3 y el 2 5 ya que se suman b c

#----------------------------------------------------------------------

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Respuesta: 5 la respuesta de esta funcion es 25 

#-----------------------------------------------------------------------

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Respuesta: Se devuelve a 10 ya que al imprimir b es mayor que 10

#------------------------------------------------------------------------

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Respuesta:Dara multiplos de 7 hasta 21

#----------------------------------------------------------------------

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Respuesta: Esto dara 8 porque b + c se suman

#----------------------------------------------------------------------

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Respuesta: Esto dara 500,500 y se retornara a 300 para luego dar 500 nuevamente

#-----------------------------------------------------------------------

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Respuesta: Esto dara 500,500 y se retornara a 300 para luego dar 500 nuevamente

#------------------------------------------------------------------------

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Respuesta: Dara 500,500 y luego se va a la nueva funcion que dara 300,300

#-------------------------------------------------------------------------

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Respuesta: Declarara todos los print dando 1,3,2

#--------------------------------------------------------------------------

#15   x
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Respuesta: Dara todas las funciones 1,3,5 y se retornara a 10