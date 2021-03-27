correo = input("introduce tu dirección de correo: ")
acceso = False
while acceso == False:
    if correo.count("@")==1 and correo.find("@")>0 and (len(correo)-1 - correo.rfind("@"))>0:
        acceso = True

        print("eccediste")

    else:

        print("el correo es incorrecto")

        correo = input("introduce tu dirección de correo: ")
