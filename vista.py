from sense_emu import SenseHat
import pandas as pd
import matplotlib.pyplot as plt

class Vista:
    
    def __init__(self):
        self.sense=SenseHat()
        
    def menu(self):
        print("0. Menú:")
        print("1. Medir temperatura")
        print("2. Medir presión")
        print("3. Medir humedad")
        print("4. Grafico de la temperatura")
        print("5. Grafico de la presion")
        print("6. Grafico de la humedad")
        print("7. Valor medio de la temperatura")
        print("8. Valor medio de la presión")
        print("9. Valor medio de la humedad")
        print("10. Valor maximo de la temperatura")
        print("11. Valor maximo de la presión")
        print("12. Valor maximo de la humedad")
        print("13. Valor minimo de la temperatura")
        print("14. Valor minimo de la presión")
        print("15. Valor minimo de la humedad")
        print("16. Medir temperatura continua")
        print("s. Salir")
        return input("Ingrese la opción deseada: ")
    
    def mostrar_temperatura(self,t):
        self.sense.show_message("{}C".format(t))
        print(t)


    def mostrar_presion(self,t):
        self.sense.show_message("{}C".format(t))
        print(t)

    def mostrar_humedad(self,t):
        self.sense.show_message("{}C".format(t))
        print(t)
          

 
    def mostrar_humedad(self,h):
        self.sense.show_message("{}HR".format(h))
        print(h)

    
    def mostrar_presion(self, p):
        self.sense.show_message("{} hPa".format(p))
        print(p)



    def mostrar_valor_medio(self, m, texto):
        print("El valor medio de {} es: {}".format(texto, m))
    
    
    
    def mostrar_grafico_temperatura (self, temperaturas):
        df_temperatura = pd.DataFrame({'Temperatura': temperaturas})

        # crear un gráfico de línea
        df_temperatura.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Temperatura')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Temperatura (°C)')

        # mostrar el gráfico
        plt.show()
        

   def medir_temperatura_continua(self,temperatura):
        print("Temperatura actual: {} °C".format(temperatura))
        time.sleep(1)  # Medir cada segundo     
   


   def mostrar_grafico_humedad (self, humedades):
        df_humedades = pd.DataFrame({'Humedad': humedades})

        # crear un gráfico de línea
        df_humedades.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Humedad')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Humedad (%)')

    def mostrar_grafico_presion (self, presiones):
        df_presiones = pd.DataFrame({'Presiones': presiones})

        # crear un gráfico de línea
        df_presiones.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Presion')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Hectopascales (hPa)/milibar(mbar)')


        # mostrar el gráfico
        plt.show()

            
