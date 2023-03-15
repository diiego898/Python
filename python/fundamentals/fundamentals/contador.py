# Básico
for i in range(151):
   print(i) 
#-------------------------------------------------------#

# Múltiplos de cinco
for i in range(5,1005,5):
   print(i)
#-------------------------------------------------------#

# Contar, a la manera del Dojo
for i in range(1,101):
    if i % 10 == 0:
      print("codingdojo")
    elif i % 5 == 0:
      print("coding")
    else:
      print(i) 
#-------------------------------------------------------#

# Whoa. Es un gran idiota
sum =0
for i in range(1,500001,2):
   sum += i      
print(sum)

#-------------------------------------------------------#

# Cuenta regresiva de a 4
y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break
#-------------------------------------------------------#

# Contador flexible

lownum=2
highnum=500
mult=10
for i in range(lownum,highnum + 1):
 if i % mult ==0:
  print(i)



