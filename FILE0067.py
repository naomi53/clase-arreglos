class Calculadora:
    
    def __init__(self):
        self.opetrador1 = ''
        self.opetrador2 = ''
        print("Se creo la calculadora")
    
    def Suma(self):
        return self.opetrador1 + self.opetrador2
    
    def Resta(self):
        return self.opetrador1 - self.opetrador2
        
    def Multiplicar(self):
        return self.opetrador1 / self.opetrador2
        
    def Dividir(self):
        return self.opetrador1 * self.opetrador2

    
laCalculadora = Calculadora(3, 4)
print(laCalculadora.Suma())
print(laCalculadora.Resta())
print(laCalculadora.Multiplicar())
print(laCalculadora.Dividir())
