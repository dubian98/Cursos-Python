NombreUsuario=input("indroduce tu nombre de usuario: ")
print("el nombre es: ",NombreUsuario.upper())
print("el nombre es: ",NombreUsuario.lower())
print("el nombre es: ",NombreUsuario.capitalize())



edad=input("introduce tu edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
    print("por favot introduce una edad correcta")
    edad=input("introduce tu edad: ")
if(int(edad)<18):
    print("no puede pasar")
else:
    print("puede pasar")