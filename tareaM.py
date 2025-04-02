class Aprendiz:
    LosAprendicez = []
    def  __init__(self, doc, nom, apell):
        self._documentoA = doc
        self.nombres = nom
        self.apellidos = apell
        print('Se creo un aprendiz')
    
    @property
    def documento(self):
        return self._documentoA
    
    @documento.setter
    def documento(self, doc):
        if doc != '':
            self._documentoA = doc
        else:
            print("el documento no puede ser vacio, porfavor ingrese el documento")

    def AñadirAprendiz(self):
        if self._documentoA and self.nombres and self.apellidos:
            aprendiz = {
                self._documentoA,
                self.nombres,
                self.apellidos
            }
            Aprendiz.LosAprendicez.append(aprendiz)
            print("El aprendiz fue añadido de manera correcta")
        else:
            print("No se pudo añadir aprendiz los campos pueden estar vacios")

    def ArregloAprendices(self):
        return self.LosAprendicez
    
documento = str(input("Ingrese su numero de documento"))
nombre = str(input("Ingrese su nombre"))
apellido = str(input("Ingrese su apellido"))

Aprendiz_1 = Aprendiz(documento,nombre,apellido)
Aprendiz_1.AñadirAprendiz()
Arreglo = Aprendiz_1.ArregloAprendices()
print(Arreglo)

#Instructores
class Instructor:
    LosIntructores = []
    def __init__(self, doc, nomCo, correo):
        self._documntoI = doc
        self.nombreCompleto = nomCo
        self.correo = correo
        print('Se creo un Instructor')

    @property
    def documento(self):
        return self._documntoI
    
    @documento.setter
    def documento(self,doc):
        if doc != '':
            self._documntoI = doc
        else:
            print("El documento no puede ser vacio, porfavor ingrese el documento")

    def AñadirInstructor(self):
        if self._documntoI and self.nombreCompleto and self.correo:
            instructor = {
                self._documntoI,
                self.nombreCompleto,
                self.correo
            }
            Instructor.LosIntructores.append(instructor)
            print("El instructor fue añadido de manera correcta")
        else:
            print("No se pudo añadir instructor los campos pueden estar vacios")

    def ArregloIntructores(self):
        return self.LosIntructores
    
documentoINS = str(input("Ingrese su numero de documento"))
nombreINS = str(input("Ingrese su nomre completo"))
correoINS = str(input("Ingrese su correo"))

Instructor_1 = Instructor(documentoINS,nombreINS,correoINS)
Instructor_1.AñadirInstructor()
Arreglo = Instructor_1.ArregloIntructores()
print(Arreglo)

# Usuarios
class Usuario:
    UsuariosA = []
    def __init__(self, nomU, contra):
        self.nombre = nomU
        self._contraseña = contra
    print("se creo un usuario")

    @property
    def Contraseña(self):
        return self._contraseña
    
    @documento.setter
    def documento(self,contra):
        if contra != '':
            self._contraseña = contra
        else:
            print("la contraseña no puede estar vacia, porfavor ingrese una contraseña")