if __name__ == '__main__':
    N = input('Digite un numero entero: ').strip()

    if (N.isdigit()):
        N = int(N)

        if(N%2 != 0):
            print('Klk')
        elif(N%2 == 0 and N >= 2 and N <= 5):
            print('Palomaso')
        elif(N%2 == 0 and N >= 6 and N <= 20):
            print('Pariguayo')
        elif(N%2 == 0 and N > 20):
            print('Hugo Lombardi')
    else:
        print('digitaste un texto, favor digitar un numero entero.')

    '''
    Tarea: Dado un entero N, realiza las siguientes acciones condicionales:
        1. Si N es impar, imprime Weird
        2. Si N es par y está en el rango inclusivo de 2 a 5, imprime Not Weird
        3. Si N es par y está en el rango inclusivo de 6 a 20, imprime Weird
        4. Si N es par y es mayor que 20, imprime Not Weird
    '''
    
    