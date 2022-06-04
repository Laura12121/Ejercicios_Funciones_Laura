class Cuenta:
    pass
    def _init_(self,numero,fecha,saldo):
        self.numero=numero
        self.fecha=fecha
        self.saldo=saldo

    def retirar(self):
        while True:
            self.retiro=int(input('Digite el valor a retirar:  '))
            if self.retiro>0 and self.retiro<=self.saldo:
                self.saldo-=self.retiro
                return f'El retiro fue exitoso {self.saldo}'
            else:
                return 'fondos insuficientes'
    
    def consigna(self):
        self.consigna=int(input('digite el valor a consignar : '))
        self.saldo+=self.consigna
        return 'consina exitosa'
    
        
    def getNumero(self):
        return self.numero

    def getFecha(self):
        return self.fecha
    
    def getSaldo(self):
        return self.saldo
    
    def informacion(self):
        return f'numero de cuenta: {self.numero}\nfecha de apertura: {self.fecha}\nsaldo de cuenta: {self.consigna}'

class cuentaCorriente(Cuenta):
    def _init_(self, numero, fecha, saldo, numeroCheque):
        super()._init_(numero, fecha, saldo)
        self.numeroCheque=numeroCheque
        
    def Chequera(self):
        return f'Chequera: {self.numeroCheque}'