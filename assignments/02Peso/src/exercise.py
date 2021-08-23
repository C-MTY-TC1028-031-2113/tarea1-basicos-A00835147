def main():
    peso_inicial= float(input("Dame el peso inicial: "))
    peso_final= float(input("Dame el peso final: "))
    meses= int(input("Dime la cantidad de meses: "))
    
    pesoXbajar=(((peso_inicial)-(peso_final))/meses)
    
    print("lo que debes bajar por mes es: "+str(pesoXbajar))
    


if __name__ == '__main__':
    main()
