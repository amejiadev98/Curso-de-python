#Algoritmo para verificar si esta lloviendo 
while True:
    clima = input("¿Esta lloviendo(si/no)?")
    
    if clima == "si":
        print("Esta lloviendo, entonces  lleva un paraguas")
        break
    elif clima =="no":
        print("No esta lloviendo")
        break
    else:
        print("Respuesta no valida, intenlo de nuevo")
