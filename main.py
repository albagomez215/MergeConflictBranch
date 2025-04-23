import utilitiesA as utilA
import utilitiesB as utilB

def main():
    a = 7
    b = 5 

    c = utilA.sumaA(a, b)


    print(f"el valor de la suma de a y b es :{c}")

 

    


    d = utilB.restaB(a, b)
    print(f"el valor de la resta de a y b es :{d}")

    #====== saludos
    print("hola mundo desde A")
    print("hola mundo somos del equipo AB")



if __name__ == "__main__":
    main()


