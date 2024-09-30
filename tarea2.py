
def preparar_te():
    print("1.	Comprar té y/o azúcar. Tener una taza y cuchara")
    print("2.	Poner a hervir agua")
    print("3.	Colocar la bolsa de té en la taza")
    print("4.	Verter el agua en la taza")
    print("5.	Esperar unos minutos a que disuelva el té")
    print("6.	Retirar la bolsa de té")
    while True:
        azucar = input("7.	¿Desea azúcar? ").lower()
        if azucar == "si":
            print(" Agregar azúcar al gusto y revolver. ")
            break
        elif azucar =="no":
            print("Un Te sin Azucar")
            break
        else:
            print("Respuesta invalida")

preparar_te()
