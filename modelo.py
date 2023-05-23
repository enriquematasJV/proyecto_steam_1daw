from sense_emu import SenseHat

class Mediciones:

    def __init__(self):
        self.sense=SenseHat()
    
        self.temperaturas=[]
        #Agregando un array de humedades
        self.humedades=[]
       
   
   
   
    def get_temperatura(self):
        t=round(self.sense.temp, 2)
        self.temperaturas.append(t)
        return t       
        
     
    def get_temperaturas(self):
         return self.temperaturas
     
    # Metodos get_humedad y get_humedades: Joaquin, Fran, PabloV 
    def get_humedad(self):
        h=round(self.sense.humidity, 2)
        self.humedades.append(h)
        return h
    
    def get_humedades(self):
        return self.humedades
     
    def get_valor_medio(self,lista):
       pass
    
    def get_valor_max(self,lista):
       pass
    
    def get_valor_min(self,lista):
       pass    
                                            
        
