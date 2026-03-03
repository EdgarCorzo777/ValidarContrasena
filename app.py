
# contra = input("Ingrese la contraseña: ")

# mayuscula = any(caracter.isupper() for caracter in contra)
# numero = any(caracter.isdigit() for caracter in contra)
# caracter = any(caracter in "@$-" for caracter in contra)

# if len(contra) < 8:
#     print("\nLa contraseña debe tener 8 o mas caracteres.")

# elif mayuscula == False:
#     print("\nLa contraseña debe tener al menos una mayuscula.")

# elif numero == False:
#     print("\nLa contraseña debe tener al menos un numero.")

# elif caracter == False:
#     print("\nLa contraseña debe tener al menos un caracter especial")

# else:
#     print("\n\nContraseña creada correctamente :)")


correo = input("Ingrese su correo electronico ej(correo123@gmail.com): ")

arroba = "@"
cantidadArroba = correo.count("@")
punto = "."

if arroba not in correo:
    print("Error: El correo debe tener un @ obligatorio.")

elif cantidadArroba > 1:
    print("Error: Un correo solo puede tener un @.")

else:
    posicion_arroba = correo.split("@") [1]
    
    # Buscar punto después del @
    if "." not in posicion_arroba:
        print("Error: Debe haber un punto después del @.")
    else:
        print("Correo creado correctamente :)")
