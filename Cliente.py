class Cliente:
    # El método __init__ es el constructor de la clase
    def __init__(self, estado, tiempo_inicio_espera):
        self.estado = estado
        self.tiempo_inicio_espera = tiempo_inicio_espera 
        self.tiempo_espera = None
        self.servidor_asignado = None
        self.tipo_servicio_demandado = -1
        self.tiempo_fin_atencion = 0
    
    def setEstadoSiendoAtendido(self, hora_actual, nro):
        if nro == 0:
            self.estado = 'siendoAtendido_caja'
        if nro == 1:
            self.estado = 'siendoAtendido_atencion_personalizada'
        if nro == 2:
            self.estado = 'siendoAtendido_tarjeta_credito'
        if nro == 3:
            self.estado = 'siendoAtendido_plazo_fijo'
        if nro == 4:
            self.estado = 'siendoAtendido_prestamos'

        self.tiempo_espera = hora_actual - self.tiempo_inicio_espera

    def setTiempoFin(self, hora_fin):
        self.tiempo_fin_atencion = hora_fin
    def setEstadoEnCola(self):
        self.estado = 'enCola'
    
    def asignar_servidor(self, servidor):
        self.servidor_asignado = servidor

    def get_tiempo_espera(self):
        return self.tiempo_espera

    def setEstadoNone(self):
        self.estado = None

    


