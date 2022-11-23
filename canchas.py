class Factura:
    numeroFactura = 0

    def __init__(self):    
        self.numeroFactura = 0
        self.fecha = ""
        self.cliente = ""
        self.totalFactura = 0
        self.totalImpuesto = 0
        self.listaItem = []
        
    def crearFactura(self, fecha, cliente):
        if(fecha != "" and cliente != ""):
            Factura.numeroFactura += 1
            self.numeroFactura = Factura.numeroFactura
            self.fecha = fecha
            self.cliente = cliente
        else:
            return "Error: Fecha Y cliente no deben de ser vacios"

    def verNumeroFactura(self):
        return self.numeroFactura
    
    def agregarItem(self, nombreProducto, precioUnitario, cantidad):
        if(isinstance(precioUnitario,int) and isinstance(cantidad,int)):
            if(isinstance(nombreProducto,str)and (nombreProducto != "")):
                self.listaItem += [[nombreProducto,precioUnitario,cantidad]]
            else:
                return"Error: NO debe ser vacio nombreProducto"
        else:
            return "Error: precioUnitario y cantidad deben ser INt"
    def verTotal(self):
        total = 0
        impuesto = 0

        for item in self.listaItem:
            total += item[1] * item[2] #precioUnitario * cantidad
        impuesto = total * 0.13
        self.totalFactura = total
        self.totalImpuesto = impuesto
        return "Total acumulado es: " + str(total + impuesto) + " Colones"
    def cerrarFactura(self):
        
        return "Total a pagar es: " + str(self.totalFactura + self.totalImpuesto) + "Colones"

class reserva:
     def __init__(self,cedula,identificador_cancha,fecha, hora_inicio,hora_fin, identificador_reserva):
          self.cedula=cedula
          self.identificador_cancha=identificador_cancha
          self.fecha=fecha
          self.hora_inicio=hora_inicio
          self.hora_fin=hora_fin
          self.identificador_reserva = identificador_reserva
          
     def mostrar(self):
         return " Cedula: "+ self.cedula + " Identifacador: " + self.identificador_cancha + " Fecha: " + self.fecha +" HoraInicio: " + self.hora_inicio + " Horafinal: " + self.hora_fin + " Identifacador de reserva: " + self.identificador_reserva

class disponible:
     def __init__(self,identificador, HoraInicio ,Horafinal, reserva):
          self.identificador = identificador
          self.HoraIniio = HoraInicio
          self.Horafinal= Horafinal
          self.reserva= reserva
     def mostrar(self):
         return "Identificador: " + self.identificador + "Hora inicio: " + self.HoraInicio + " Hora final: " + self.Horafinal + " Codigo de reserva: " + self.reserva 
         


class cliente:
     def __init__(self,cedula,nombre,telefono,correo):
          self.cedula=cedula
          self.nombre=nombre
          self.telefono=telefono
          self.correo=correo
     def mostrar(self):
         return "Nombre: " + self.nombre + " Cedula: " + self.cedula + " Telefono: " + self.telefono + " Correo: " + self.correo
         

class cancha:
     def __init__(self,identificador,precio):
          self.identificador = identificador
          self.precio = precio
     def mostar(self):
         return " Identificador es : " + self.identificador + " Precio: " + self.precio    

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
                           if (valor.cedula == cedula):
                               return "la cedula ya existe"
                       lista = cliente(cedula,nombre,telefono,correo)
                       print("EL cliente ha sido creado exitosamente")
               else:
                  return "Error: En los parámetros ingrese de nuevo los valores correctamenete"
           else:
              return "Error: Parámetros no valdos intentelo de nuevo"
       else:
           return"Error: Parámetros no validos intenteo de nuevo"

    def modificar_cliente(self, cedula, nuevoTelefono, nuevoCorreo):
        contador=0
        if (cedula == "ALL"):
            for valor in canchas.clientes:
                valor.mostrar()
        else: 
            if (isinstance(cedula,int) and isinstance(nuevoTelefono,int) and isinstance(nuevoCorreo,str)):
                if (cedula!= "" and cedula < 1000000000 and cedula > 9999999):
                    if (nuevoTelefono!="" and nuevoTelefono < 100000000 and nuevoTelefono > 9999999 and nuevoCorreo!= ""):
                        for valor in canchas.clientes:
                            if (valor.cedula == cedula):
                                contador+=1
                                valor.telefono = nuevoTelefono
                                valor.correo = nuevoCorreo
                        if (contador == 0 ):
                             return "Error: No se encotró la cedula"
                        else:
                            return "Sus datos han sidos modificados correctamente"
                                   
                    else:
                        return "Error: En parámetros intentelo de nuevo "
                else:
                    return "Error: En parámetros intentelo de nuevo"
            else:
                return "Error: En las entradas intentelo de nuevo"

    def mostrarCliente(self,cedula):
          contador=0
          if (cedula!= "" and cedula < 1000000000 and cedula > 9999999):
               if (canchas.clientes == []):
                    return "Error: No cliente no encontado"
               else:
                    for valor in canchas.clientes:
                         if (valor.cedula == cedula):
                              contador+= 1
                              contador.mostrar()
                    if (contador == 0):
                         return "Error: Cedula no encontrada"
                         
          else:
               return "Error: intentelo de nuevo"



        
