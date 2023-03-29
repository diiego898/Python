#1
x = [ [5,2,3], [10,8,9] ] 
x [1][0]=15
print(x)

#----------------------------------------------------------

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes [0] ['last_name']='bryant'
print(estudiantes)

#-----------------------------------------------------------

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes ["fútbol"][0]='Andres'
print(directorio_deportes)

#-----------------------------------------------------------

z = [ {'x': 10, 'y': 20} ]
z [0]['y']=30
print(z)

#-----------------------------------------------------------

#2

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'eloycito'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(lista):
    for i in range(0, len(lista)):
        output = ""
        for key,val in lista[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_dictionary(estudiantes)
#-------------------------------------------------------------

#3

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',estudiantes)
iterate_dictionary2('last_name',estudiantes)

#----------------------------------------------------------------

#4
dojo = {
    'Ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(diccionario):
    for key,val in diccionario.items():
        print("--------------")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])
printinfo(dojo)
