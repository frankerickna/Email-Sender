
import tkinter as tk
from loginView import Login
from userView import UserView

class ComponentView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Component View")

        # Iniciar la interfaz de inicio de sesión
        self.login_interface = Login(self.root)

        self.current_view = None  # Variable para mantener la referencia a la vista actual
 

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    component_view = ComponentView()
    component_view.run()
