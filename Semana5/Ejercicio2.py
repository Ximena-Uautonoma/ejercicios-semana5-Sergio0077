'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
temperatura = int(input("escriba la temperatura en grados celsius : "))
if temperatura <=10: 
          print ("La temperatura es Fria")

elif temperatura <=25:
         print ("la temperatura es templada")

elif temperatura > 25:
        print ("la temperatura es Calurosa")





