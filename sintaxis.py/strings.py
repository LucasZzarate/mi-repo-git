### STRINGS ###

#formas de definir una variable como un string
string = "Cadena de texto"
other_string= 'Otra cadena de texto'

# Como se colocan las comillas \' 
print('Does\'t') #con comillas simples
print("Does't") #si uso comillas dobles no necesito el \'

print("\"YES\", he said") #Para doble comillas

#LO MAS COMODO SON LAS DOBLE COMILLAS, EN AMBAS OCASIONES

print("String con\n salto de linea") #SALTA A LA SIGUEINTE LINEA CON ' \n '
print("\tStringo con tabulacion") #TABULACION

#tambien funciona definiendo una variable
salto_linea = 'Hola.\nMi apellido es Zarate' 
print(salto_linea)

'''si no queres que los caracteres 
especiales funcionen como tal se utiliza la ' r ' 
'''
print(r"ASI SE DESABILITAN SUS FUNCIONES ESPECIALES*/[] \n\ {}")
print("""\
    TODO LO QUE ESCRIBA EN EL BLOQUE ENTRE \" \" 
    VA      A SER 
                    IMPRESO
    """)


#Se puede concatenar cadena con ' + ' y repetir cadenas con ' * '.
print(3*'hola'+ ' funci'+'ona')

primera_parte= 'Py'
print(primera_parte +'thon')


#ejemplo anterios: salto_linea= 'Hola.\nMi apellido es Zarate'
print(salto_linea[3]) #va a imprimir el 3er caracter empezando del 0
print(salto_linea[-2]) #empieza al reves la cadena con el anteultimo caracter  

#'slicing' es tomar una porcion de una cadena
print(salto_linea[0:5])
