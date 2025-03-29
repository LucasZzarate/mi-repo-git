## LISTAS ##

#my_list = [1,4,6,34,9]

#Las listas se pueden segmentar y idexar

#print(my_list[0]) # meustra el lugar cero (primer) de la lista
#print(my_list[-1]) # empieza a contar al reves mostraria el ultimo numero 
#print(my_list[-3:]) # recorta y crea una nueva lista contando de atras hacia delante las posiciones hasta la posicion -3

# Son mutables, es decir que se puede cambiar su contenido 
#my_list [0] = 100 #se reemplazo el entero en la posicion 0 por 100.
#print(my_list)

#print(len(my_list)) #Calcula la longitud de my_list (cuantos elementos tiene)

#Se puede agregar nuevo items al final de la lista con list.append()
#my_list.append(220)
#print(my_list)
#print(my_list.append(11)) Tener en cuenta que no se puede de esta maner

#funcion id(objeto) devuelve la identificacion unica de un pobjeto de tupla
my_list = [1,2,3]
my_list2 = my_list

print(id(my_list)) #identificador del objeto de lisat
print(id(my_list2)) #igual al identificador my_list, por que ambos apuntan al mismo objeto

my_list2.append(103) #modifico una de las listas
print(my_list)  #pero a la hora de mostrar se modifican ambas listas!!!
print(my_list2) #las listas SON MUTABLES, y ambas son referencias del mismo objeto en memoria, de ahi du id() coincida.
