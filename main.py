import utilitiesA as utilA
import utilitiesB as utilB

def main():
    a = 7
    b = 5 
    c = utilA.sumaA(a, b)

    print(f"el valos de la suma de a y b es :{c}")

    d = utilB.restaB(a, b)
    print(f"el valor de la resta de a y b es :{d}")



if __name__ == "__main__":
    main()


