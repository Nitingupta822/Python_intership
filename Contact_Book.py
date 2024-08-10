import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Incomplete Data", "Please enter at least a name and phone number.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_query = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
    if search_query:
        found_contacts = [c for c in contacts if search_query.lower() in c['name'].lower() or search_query in c['phone']]
        if found_contacts:
            contact_listbox.delete(0, tk.END)
            for contact in found_contacts:
                contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        else:
            messagebox.showinfo("No Results", "No contacts found matching your search.")

def select_contact(event):
    try:
        selected_index = contact_listbox.curselection()[0]
        selected_contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        name_entry.insert(tk.END, selected_contact['name'])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, selected_contact['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(tk.END, selected_contact['email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(tk.END, selected_contact['address'])
    except IndexError:
        pass

def update_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        contacts[selected_index] = {
            "name": name_entry.get().strip(),
            "phone": phone_entry.get().strip(),
            "email": email_entry.get().strip(),
            "address": address_entry.get().strip()
        }
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to update.")
def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del contacts[selected_index]
        save_contacts(contacts)
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")

root = tk.Tk()
root.title("Contact Book")

contacts = load_contacts()
tk.Label(root, text="Name:").grid(row=0, column=0, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, pady=10)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=1, pady=10)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=2, pady=10)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=5, column=1, pady=10)

contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
contact_listbox.bind("<<ListboxSelect>>", select_contact)

update_contact_list()

root.mainloop()
