# Declaramos una variable
calificacion = input("Introduce tu calificacion de la AZ-900")

calificacion = int(calificacion)

# Pregunta si la calificacion es menor a 700
if calificacion < 700 :
    print("No pasaste") # Si es menor a 700, muestra el mensaje
elif calificacion == 700 :
    print("Pasaste justo")
elif calificacion > 1000 :
    print("La calificacion final no es mas de 1000")
else : # Si no se cumple e; if anterior, pasa a esta linea
    print("Felicidades, pasa por tu calificacion") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad = input("Introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al ... ")
elif edad > 100 :
    print("Si vienes acompañado, puedes ...")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# En Python no hay SWITCH CASE