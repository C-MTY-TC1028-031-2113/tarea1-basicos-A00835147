def main():
    s=float(input("Dame el saldo del mes anterior: "))
    i=float(input("Dame los ingresos: "))
    e=float(input("Dame los egresos: "))
    c=float(input("Dame el numero de cheques: "))
    n=c*13
    saldo_final=float((s+i-e-n)-(s+i-e-n)*.075)
    print("El saldo final de la cuenta es: "+str(saldo_final))



if __name__ == '__main__':
    main()
