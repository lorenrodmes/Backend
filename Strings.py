name = "Lorenira"
last_name = 'Rodriguez Mesa'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)


# Si usaramos la comilla sencilla para marcar el texto tendriamos un problema con la sintaxys de Python, podemos jugar con las comillas para ingluir en el texto 

quote = "I'm Lorenita "
print(quote)


quote2 = ' She said "Holiitas Chip"  '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)

