# program.py    

from numpy import product
from datetime import date
# suma de dos numeros
sum = 1+2
print(sum)
# producto del resultado de la suma por dos
product=sum*2
print('')
# Impresión en pantalla print('Hola desde la consola')
print('hola desde la consola')
# Pintamos el resultado del producto en consola
print(product)
# funcion type
distancia_a_alfa_centauri=4.367
type(distancia_a_alfa_centauri)
# Mandamos a llamar el dia de hoy con la funcion today de date
# Para que la funcion "date.today()" pueda pintarse en la consola
# se requiere de encerrarlo en la funcion str, para que pueda pasar a ser un string ya que si no se
# hace esto, se presentara un error
print("Today´s date is "+str(date.today()))
print('')
print('bienvenido al programa de bienvenida')
name=input('Introduzca su nombre: ')
print('Saludos desde la consola ' + name)


