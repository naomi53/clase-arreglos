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
                "documento": self._documentoA,
                "nombres": self.nombres,
                "apellidos": self.apellidos
            }
            Aprendiz.LosAprendicez.append(aprendiz)
            print("El aprendiz fue añadido de manera correcta")
        else:
            print("No se pudo añadir aprendiz los campos pueden estar vacios")

    def ArregloAprendices(self):
        return self.LosAprendicez

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
                "documento": self._documntoI,
                "nombreCompleto": self.nombreCompleto,
                "correo": self.correo
            }
            Instructor.LosIntructores.append(instructor)
            print("El instructor fue añadido de manera correcta")
        else:
            print("No se pudo añadir instructor los campos pueden estar vacios")

    def ArregloIntructores(self):
        return self.LosIntructores

# Usuarios
class Usuario:
    UsuariosA = []
    def __init__(self, nomU, contra):
        self.nomUsuario = nomU
        self._contraseña = contra
    print("se creo un usuario")

    @property
    def Contraseña(self):
        return self._contraseña
    
    @Contraseña.setter
    def Contraseña(self,contra):
        if contra != '':
            self._contraseña = contra
        else:
            print("la contraseña no puede estar vacia, porfavor ingrese una contraseña")

    def AñadirUsuario(self):
        if self.nomUsuario and self._contraseña:
            usuarios = {
                "nomUsuario": self.nomUsuario,
                "contraseña": self._contraseña
            }
            Usuario.UsuariosA.append(usuarios)
            print("El usuario fue creado con exito")
        else:
            print("No se pued crear el usuario, Puede estar vacio")
    
    def ArregloUsuarios(self):
        return self.UsuariosA

# condicional para registro
TipoUsuario = input("Ingrese un tipo de usuario para registrarse (Aprendiz/Instructor): ")

if TipoUsuario == 'Instructor':
    documentoINS = input("Ingrese su número de documento: ")
    nombreINS = input("Ingrese su nombre completo: ")
    correoINS = input("Ingrese su correo: ")

    Instructor_1 = Instructor(documentoINS, nombreINS, correoINS)
    Instructor_1.AñadirInstructor()
    print("Lista de instructores:", Instructor_1.ArregloIntructores())

    # Crear el usuario del Instructor
    Usuario_1 = Usuario(correoINS, documentoINS)
    Usuario_1.AñadirUsuario()
    print("Lista de usuarios:", Usuario_1.ArregloUsuarios())

elif TipoUsuario == 'Aprendiz':
    documento = input("Ingrese su número de documento: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    Aprendiz_1 = Aprendiz(documento, nombre, apellido)
    Aprendiz_1.AñadirAprendiz()
    print("Lista de aprendices:", Aprendiz_1.ArregloAprendices())

    Usuario_2 = Usuario(documento, documento)
    Usuario_2.AñadirUsuario()
    print("Lista de usuarios:", Usuario_2.ArregloUsuarios())