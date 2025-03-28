### STRINGS ###

#formas de definir una variable como un string
string = "Cadena de texto"
other_string= 'Otra cadena de texto'

# Como se colocan las comillas \' 
#print('Does\'t') #con comillas simples
#print("Does't") #si uso comillas dobles no necesito el \'

#print("\"YES\", he said") #Para doble comillas

#LO MAS COMODO SON LAS DOBLE COMILLAS, EN AMBAS OCASIONES



#print("String con\n salto de linea") #SALTA A LA SIGUEINTE LINEA CON ' \n '
#print("\tStringo con tabulacion") #TABULACION


#tambien funciona definiendo una variable
salto_linea = 'Hola.\nMi apellido es Zarate' 
#print(salto_linea)


'''si no queres que los caracteres 
especiales funcionen como tal se utiliza la ' r ' '''

#print(r"ASI SE DESABILITAN SUS FUNCIONES ESPECIALES*/[] \n\ {}")
'''
print("""\
    TODO LO QUE ESCRIBA EN EL BLOQUE ENTRE \" \" 
    VA      A SER         IMPRESO
    """

    )
'''


#Se puede concatenar cadena con ' + ' y repetir cadenas con ' * '.
#print(3*'hola'+ ' funci'+'ona')

primera_parte= 'Py'
#print(primera_parte +'thon')




#ejemplo anterios: salto_linea= 'Hola.\nMi apellido es Zarate'
#print(salto_linea[3]) #va a imprimir el 3er caracter empezando del 0
#print(salto_linea[-2]) #empieza al reves la cadena con el anteultimo caracter  

#'slicing' es tomar una porcion de una cadena
#print(salto_linea[0:5])


#FORMATEO

name, apellido, edad = "Lucas", "Zarate", 24
#print('Mi nombre es Lucas Zarate')

# se puede hacer con un .format() MANERA MAS ACONSEJABLE
#print("Mi nombre es {} {} y mi edad es {}".format(name, apellido, edad))
# %s significa que la primera cadena de texto frmateado lo va a meter ahi
#Si es un formateo con entero se usa %d

#La segunda forma es con % es util para que no pasen cualquier cosa
#ya que %d es para entero y %s para strings
#print("Mi nombre es %s %s y mi edad es %d" %(name, apellido, edad))

#print(F"Mi nombre es {name} {apellido} y mi edad es {edad}")



# DESEMPAQUETADO DE CARACTERES
lenguaje = "Python"
# a, b = lenguaje ---> esta linea da error porque en cada caracter se guarda un caracter y aca hay solo dos
a,b,c,d,e,f ="Python" # ---> Esta linea si esta bien
#print(a)
#print(b)

#FUNCIONES PARA STRINGS

print(lenguaje.capitalize()) # devuelve el string pero con el 1er caracter en mayuscula
print(lenguaje.upper()) # son todas mayusculas
print(lenguaje.lower()) # son todas minusculas
print(lenguaje.casefold()) 
print(lenguaje.isnumeric()) # es para saber si es un numero la varible
print("1".isnumeric())
print(lenguaje.count("h")) # cuenta cuantas h hay en Phyton
print(lenguaje.encode()) # se utiliza para 'codificar'
print(lenguaje.startswith("py")) #me va a devolver si Python empieza o no con 'py'

