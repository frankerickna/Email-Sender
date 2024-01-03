import tkinter as tk
from tkinter import filedialog
import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class UserView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.resizable(0, 0)
        self.root.title("Vista principal")

        bg_color = "#F0F0F0"
        label_color = "#333333"
        entry_bg_color = "#FFFFFF"
        button_bg_color = "#4CAF50"
        button_fg_color = "#FFFFFF"

        self.root.configure(bg=bg_color)
        self.frame = tk.Frame(self.root, bg=bg_color)
        self.frame.pack(padx=20, pady=20)
        
        self.label_subject = tk.Label(self.frame, text="Asunto:", bg=bg_color, fg=label_color)
        self.entry_subject = tk.Entry(self.frame, bg=entry_bg_color)
        
        self.button_attach_html = tk.Button(self.frame, text="Adjuntar HTML", command=self.attach_html_file, bg=button_bg_color, fg=button_fg_color) 

        self.label_subject.grid(row=1, column=0, pady=5, sticky="w")
        self.entry_subject.grid(row=1, column=1, pady=5, padx=10, sticky="ew")
        self.button_attach_html.grid(row=2, columnspan=2, pady=10) 

        self.contact_list = []

        self.button_load_contacts = tk.Button(self.frame, text="Cargar Contactos desde Excel", command=self.load_contacts_from_excel, bg=button_bg_color, fg=button_fg_color)
        self.button_load_contacts.grid(row=4, columnspan=2, pady=10)

        self.button_send_emails = tk.Button(self.frame, text="Enviar Correos a Contactos", command=self.send_emails_to_contacts, bg=button_bg_color, fg=button_fg_color)
        self.button_send_emails.grid(row=5, columnspan=2, pady=10)

    def attach_html_file(self):
        try:
            self.file_path_html = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
            if self.file_path_html:
                print(f"Archivo HTML seleccionado: {self.file_path_html}")
        except Exception as e:
            print(f"Error al cargar el archivo HTML: {e}")

    def load_contacts_from_excel(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                workbook = openpyxl.load_workbook(file_path)
                sheet = workbook.active
                self.contact_list = []

                for row in sheet.iter_rows(min_row=2, values_only=True):
                    contact = {
                        "first_name": row[0],
                        "last_name": row[1],
                        "email": row[2]
                    }
                    self.contact_list.append(contact)
                
                print("Contactos cargados correctamente.")
                print(self.contact_list)
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo Excel: {e}")

    def send_emails_to_contacts(self):
        try:
            with open(self.file_path_html, 'r', encoding='utf-8') as archivo:
                html = archivo.read()

            for contact in self.contact_list:
                if all(contact.values()):  # Validar que los campos no estén vacíos ni None
                    first_name = contact["first_name"]
                    last_name = contact["last_name"]
                    email = contact["email"]
                    
                    sender = 'jefaturasecuretracking@gmail.com'
                    password = 'auen cmhu nmqq gzda'

                    topic = self.entry_subject.get()  # Obtener el asunto del correo desde la entrada
                    msg = MIMEMultipart()
                    msg['Subject'] = topic
                    msg['From'] = sender
                    msg['To'] = email

                    body = MIMEText(html, 'html')
                    msg.attach(body)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender, password)
                    server.sendmail(sender, email, msg.as_string())
                    server.quit()

                    print(f"Enviando correo a: {first_name} {last_name} ({email})")
                else:
                    print("Error: Los campos de contacto están incompletos.")
            print("Correos enviados a todos los contactos.")
        except FileNotFoundError:
            print("Error: Archivo HTML no encontrado.")
        except smtplib.SMTPException as e:
            print(f"Error al enviar correos: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    user_view = UserView()
    user_view.run()
##nomejodan xddd