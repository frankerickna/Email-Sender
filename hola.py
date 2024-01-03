import tkinter as tk

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Contactos")
        
        # Variables para almacenar datos de contacto
        self.contacts = []
        self.selected_contact_index = tk.StringVar()
        
        # Crear etiquetas y campos de entrada
        self.label_name = tk.Label(root, text="Nombre:")
        self.entry_name = tk.Entry(root)
        
        self.label_email = tk.Label(root, text="Correo electrónico:")
        self.entry_email = tk.Entry(root)
        
        # Botones para agregar y eliminar contactos
        self.button_add_contact = tk.Button(root, text="Agregar Contacto", command=self.add_contact)
        self.button_remove_contact = tk.Button(root, text="Eliminar Contacto", command=self.remove_contact)
        
        # Listbox para mostrar los contactos
        self.listbox_contacts = tk.Listbox(root, listvariable=self.selected_contact_index, selectmode=tk.SINGLE)
        self.listbox_contacts.bind('<<ListboxSelect>>', self.select_contact)
        
        # Posicionar elementos en la ventana
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        
        self.label_email.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)
        
        self.button_add_contact.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.button_remove_contact.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        
        self.listbox_contacts.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        
    def add_contact(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        if name and email:
            contact = f"{name} - {email}"
            self.contacts.append(contact)
            self.listbox_contacts.insert(tk.END, contact)
            self.clear_entries()
    
    def remove_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            index = selected_index[0]
            self.listbox_contacts.delete(index)
            del self.contacts[index]
            self.clear_entries()
    
    def select_contact(self, event):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            index = selected_index[0]
            self.selected_contact_index.set(index)
            contact = self.contacts[index]
            name, email = contact.split(" - ")
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, name)
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, email)
    
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()

# Iniciar el gestor de contactos
contact_manager = ContactManager(root)

# Mostrar la ventana
root.mainloop()
