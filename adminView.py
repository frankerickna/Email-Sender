import tkinter as tk
from tkinter import filedialog
class AdminView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vista de administrador")
        
        # Crear campos para redactar el correo
        self.label_to = tk.Label(self.root, text="Destinatario:")
        self.entry_to = tk.Entry(self.root)
        
        self.label_subject = tk.Label(self.root, text="Asunto:")
        self.entry_subject = tk.Entry(self.root)
        
        # Botón para adjuntar un archivo HTML como cuerpo del correo
        self.button_attach_html = tk.Button(self.root, text="Adjuntar HTML", command=self.attach_html_file)
        self.button_attach_html.pack()
        
        # Botón para enviar el correo
        self.button_send = tk.Button(self.root, text="Enviar Correo", command=self.send_email)
        
        # Posicionar elementos en la ventana
        self.label_to.pack()
        self.entry_to.pack()
        self.label_subject.pack()
        self.entry_subject.pack()
        self.button_send.pack() 

    def attach_html_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
        if file_path:
            # Aquí podrías manejar el archivo HTML seleccionado, por ejemplo, enviarlo como cuerpo del correo
            print(f"Archivo HTML seleccionado: {file_path}")
    
    def send_email(self):
        # Obtener los datos del correo ingresados por el usuario
        receptor = self.entry_to.get()
        asunto = self.entry_subject.get()
        cuerpo = self.text_body.get("1.0", tk.END)  # Obtener el contenido del Text
        
        # Aquí podrías crear un objeto Email usando la clase Email que has definido y luego enviarlo
        # email = Email(receptor, sender, asunto, cuerpo, attachments)
        # email_sender = EmailSender()
        # email_sender.send_email(email)
        # Esto es un ejemplo simulado ya que necesitarías implementar la lógica real de envío de correo
        
        print(f"Correo enviado a: {receptor}\nAsunto: {asunto}\nCuerpo:\n{cuerpo}")
        # Puedes añadir la lógica de enviar el correo aquí
        
### falta manejar los datos y vistas de todo administrador
        