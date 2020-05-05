#Comentario de una sola linea
'''
Comentario de 
varias 
lineas
'''
#Variables no se declaran
#Puedes cambiar el tipo de las variables el tipo e ve con type 

print("Hola mundo")
x=10
print(type(x))
print(x)
x=y=z=2.3
print(x,y,z)
print(type(x))
x="Cadena"
print(type(x))
c1="hola"
c2="Eduardo"
saludo=c1+" "+c2
print(saludo)
#concatenar colocar una cadena al final de la otra
saludo2="{} {} {}".format(c1, c2, 3)
print(saludo2)
saludo3="Cambio de orden {2} {0} {1}".format(c1, c2, 3)
print(saludo3)
