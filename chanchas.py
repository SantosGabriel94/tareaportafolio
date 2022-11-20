class canchas:
    contadorFactura = 0
    facturas =[]
    validarcanchas = 20
    cancha = []
    clientes = []
    validar_Reserva = 0
    validacion = []
    reservas = []

    def __init__(self, nombre, telefono, direccion, correo):
        if(isinstance(nombre,str) and isinstance(telefono,int)and isinstance(direccion,str)and isinstance(correo,str)):
            if nombre != "" and telefono != "" and telefono <1000000000 and telefono >9999999 and direccion != "" and correo != "":
                self.nombre = nombre
                self.telefono = telefono
                self.direccion = direccion
                self. correo = correo
            else:
                return"Error: Parámetros no validos vuelva a intentarlo"
        else:
            return"Error: Datos ingresados no validos vuelva aintentarlo"
        
    def verInfo(self):
       return"Nombre: "+self.nombre+" Telefono: "+self.telefono+" Direccion: "+self.direccion+" Correo "+self.correo

    def crear_Cancha(self,precio):
       if(isinstance(precio,int) and precio > 1000 and precio != ""):
           canchas.validarcanchas += 1

           lista = cancha(canchas.validarcanchas,precio)
           canchas.cancha += [lista]
           print("identificador"+ canchas.validarcanchas)
       else:
           return "Error: el precio debe de ser mayor a 100 y no debe de ser vacio"
    def crear_Cliente(self, cedula, nombre,telefono,correo):
       if(isinstance(cedula,int) and isinstance(nombre,str)and isinstance(telefono,int) and isinstance(correo,str)):
           if(cedula != "" and cedula <100000000 and cedula > 9999999):
               if (nombre != "" and telefono != "" and telefono <1000000000 and telefono > 9999999 and correo != ""):
                   if (canchas.clientes == []):
                       lista = cliente(cedula, nombre,telefono,correo)
                       canchas.clientes += [lista]
                       print("EL cliente ha sido creado exitosamente")
                   else:
                       for valor in canchas.cliente:
                           if valor.cedula==cedula:
                               return "la cedula ya existe"
                       lista = cliente(cedula,nombre,telefono,correo)
                       print("EL cliente ha sido creado exitosamente")
               else:
                  return "Error: En los parámetros ingrese de nuevo los valores correctamenete"
           else:
              return "Error: Parámetros no valdos intentelo de nuevo"
       else:
           return"Error: Parámetros no validos intenteo de nuevo"
        
                       
                   
                   













           
