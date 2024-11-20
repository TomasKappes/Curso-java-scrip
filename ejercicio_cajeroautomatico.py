class Cajero:
    def __init__(self):
        self.saldo = 0
        
    def mostrar_menu(self):
        print("\n--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        
    def depositar(self, monto):
        
        if monto > 0:
            self.saldo += monto
            print(f'\n depositando ${monto} , tu saldo es ${self.saldo}')
        else:
            print('\n debes ingresar un saldo mayor a $0')
            
    def retirar(self, monto):
        if monto > self.saldo:
            print(f'\n no tienen suficiente saldo, tu saldo es ${self.saldo}')
        else:
            self.saldo -= monto
            print(f'\n retirando ${monto} tu saldo ahora es ${self.saldo}')    
            
    def consultar_saldo (self):
        print(f'\n tu saldo es ${self.saldo}')
        
    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input('\n eliga la accion que quiera realizar:  ')
            
            if opcion =='1':
                self.consultar_saldo()
                
            elif opcion =='2':
                monto = float(input('\n inserte el monto que desea retirar $: '))
                self.retirar(monto)
            elif opcion =='3' :
                monto = float(input('\n inserte el monto que desea depositar $: '))
                self.depositar(monto)
            elif opcion == '4':
                print('\n saliendo...')
                break
            else:
                print('\n opcion incorrecta vuelva a intentarlo')


cajero = Cajero()

cajero.iniciar()