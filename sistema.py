import datetime

class Persona:
    def __init__(self):
        self._documento = ''
        self.nombre = ''
        self.apellido = ''
        self._fecha_nacimiento = ''
        print("presona creada")
    
    @property
    def documento(self):
        return self._documento
    
    @documento.setter
    def documento(self, valor):
        if valor != '':
            self._documento = valor
        else:
            print("el documento no puede ser vacio")
            
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha):
        dia, mes, anho = fecha
        if dia >0 and mes > 0 and anho > 0:
            self._fecha_nacimiento = datetime.date(anho, mes, dia)
        else:
            print("la fecha de nacimiento no puede ser vacio")
            
    def nombre_Completo(self):
        return self.nombre + " " + self.apellido

la_persona = Persona()
la_persona.nombre = 'Naomi'
la_persona.apellido = 'gamboa'
print(la_persona.nombre_Completo())
la_persona.documento = '5281456'
la_persona.fecha_nacimiento = (30, 8, 1982)
print(type(la_persona.fecha_nacimiento))
