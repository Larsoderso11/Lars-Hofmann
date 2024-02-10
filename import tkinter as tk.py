import tkinter as tk
from tkinter import messagebox
import os

def get_ios_documents_path():
    return os.path.expanduser('~/Documents')

def list_files_on_ios_device(directory_path, file_listbox):
    full_path = os.path.join(get_ios_documents_path(), directory_path)

    # Lösche alle vorhandenen Einträge in der Liste
    file_listbox.delete(0, tk.END)

    print(f"Inhalte von {full_path}:")
    
    for file_name in os.listdir(full_path):
        print(file_name)
        file_listbox.insert(tk.END, file_name)

def delete_file(directory_path, file_name, file_listbox):
    full_path = os.path.join(get_ios_documents_path(), directory_path, file_name)

    try:
        os.remove(full_path)
        messagebox.showinfo("Erfolg", f"Datei '{file_name}' wurde erfolgreich gelöscht.")
        list_files_on_ios_device(directory_path, file_listbox)  # Aktualisiere die Dateiliste nach dem Löschen
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Löschen der Datei '{file_name}': {str(e)}")

def create_window():
    def show_files():
        directory_path = entry.get()
        list_files_on_ios_device(directory_path, file_listbox)

    def delete_selected_file():
        directory_path = entry.get()
        selected_index = file_listbox.curselection()
        
        if selected_index:
            file_name = file_listbox.get(selected_index)
            confirmation = messagebox.askyesno("Bestätigung", f"Möchten Sie die Datei '{file_name}' wirklich löschen?")
            if confirmation:
                delete_file(directory_path, file_name, file_listbox)

    # Fenster erstellen
    fenster = tk.Tk()
    fenster.title("Mein Fenster")

    # Eingabefeld für das Verzeichnis
    label_path = tk.Label(fenster, text="Verzeichnis:")
    label_path.pack(pady=5)

    entry = tk.Entry(fenster, width=30)
    entry.pack(pady=5)

    # Button hinzufügen, um die Liste der Dateien anzuzeigen
    button_show_files = tk.Button(fenster, text="Dateien anzeigen", command=show_files)
    button_show_files.pack(pady=10)

    # Label für die Dateiliste
    label_files = tk.Label(fenster, text="Dateien:")
    label_files.pack()

    # Liste für die Dateien
    file_listbox = tk.Listbox(fenster, selectmode=tk.SINGLE)
    file_listbox.pack(pady=10)

    # Button hinzufügen, um ausgewählte Datei zu löschen
    button_delete_file = tk.Button(fenster, text="Datei löschen", command=delete_selected_file)
    button_delete_file.pack(pady=10)

    # Starten der Schleife für das Fenster
    fenster.mainloop()

if __name__ == "__main__":
    create_window()


