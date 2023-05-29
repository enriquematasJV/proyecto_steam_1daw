from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]

        self.humedades=[]

        
        self.presiones = []

       
   
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas

     
    # Metodos get_humedad y get_humedades: Joaquin, Fran, PabloV 
    def get_humedad(self):
        if self.sense.humidity is None:
            return None
        h=round(self.sense.humidity, 2)
        self.humedades.append(h)
        return h

         
    def get_presion(self):
        p = round(self.sense.pressure, 2)
        self.presiones.append(p)
        return p

    def get_presiones(self):
        return self.presiones
  
    def get_valor_medio(self, lista):
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)

    
    def get_humedades(self):
        return self.humedades
     
    def get_valor_medio(self,lista):
       pass
    
    def get_valor_max(self,lista):
       return max(lista)
    
    def get_valor_min(self,lista):
       return min(lista)  
                                            
