from customtkinter import *


class Menu(CTkFrame):

    def __init__(self, parent, controller=None, ruta: str = None):
        super().__init__(parent)
        self.controller = controller
        self.configurationAplication()
        self.ruta_descarga = ruta
    
    def configurationAplication(self) -> None:
        label = CTkLabel(self, text="Configuraciones del sistema", font=("Arial", 20))
        label.pack(pady=20)

        descripcion = CTkLabel(self, text="En este apartado se gestionará donde se podrá configurar algunos campos de las descargas \n Ahora te dejamos las opciones:")
        descripcion.pack(pady=30)

        self.button_cambio = CTkButton(self, text="Ruta de descarga", command= self.cambiarRutaDescarga)
        self.button_cambio.pack(pady=10, padx=10)

    
    def getRutaFrame(self) -> str:
        return self.ruta_descarga
    
    def cambiarRutaDescarga(self) -> None:
        self.ruta_descarga = filedialog.askdirectory(initialdir="C:/", title="Explorar la carpeta")
        print(self.ruta_descarga)