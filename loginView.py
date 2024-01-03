import tkinter as tk 
from userView import UserView
from adminView import AdminView
class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.resizable(0,0)
        #self.root.config(bg="sky blue")
        self.root.title("Inicio de Sesión")
        
        # Crear etiquetas y campos de entrada
        self.label_email = tk.Label(root, text="Correo electrónico:", font = ("Times New Roman", 12))
        self.entry_email = tk.Entry(root, width= 30, font = ("Times New Roman", 12) )
        
        self.label_password = tk.Label(root, text="Contraseña:", width= 30, font = ("Times New Roman", 12) )
        self.entry_password = tk.Entry(root, show="*", width= 30, font = ("Times New Roman", 12) )  # Para ocultar la contraseña
        
        # Botón de inicio de sesión
        self.button_login = tk.Button(root, text="Iniciar Sesión", command=self.open_user_view, fg="green", font = ("Times New Roman", 12))
        
        # Posicionar elementos en la ventana
        self.label_email.pack(pady=40)
        self.entry_email.pack(pady=10)
        self.label_password.pack(pady=10)
        self.entry_password.pack(pady=10)
        self.button_login.pack(pady=10)
    
    def open_user_view(self):
        # Verificar las credenciales (aquí se simula la verificación)
        # En una aplicación real, esta verificación se haría con una base de datos o algún sistema de autenticación
        # Aquí se está simulando una verificación de usuario
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if email == "hola" and password == "hola":
            print("Inicio de sesión exitoso")
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            # Abrir la vista del usuario para redactar un correo
            user_view = UserView()
        elif email == "admin" and password == "admin":
            print("Bienvenido crack!!")
            self.root.destroy()  # Cerrar la ventana de inicio de sesión
            # Abrir la vista del usuario para redactar un correo
            admin_view = AdminView()
        else:
            print("Credenciales incorrectas")
