class cliente:

    def __init__ (self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

       
        return monto

    def extraer(self,monto):
        self.monto=self.monto-monto
        return monto

    def retornar(self): 
        return self.monto 

    def imprimir(self):
        print("el cliente",self.nombre, "tiene la cantidad de ",self.monto)


        
class banco:

    def __init__ (self):
      self.cliente1= cliente("Juan")
      self.cliente2= cliente("Ana")
      self.cliente3= cliente("Diego")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(50)
          

    def depositost(self):
        total= self.cliente1.retornar() + self.cliente2.retornar()+ self.cliente3.retornar()
        print("el total del monto del banco es",total) 
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()


        
oso=banco()
oso.operar()
oso.depositost()
#hola como estas#
