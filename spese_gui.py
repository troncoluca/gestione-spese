import tkinter as tk

def carica_spese():
    spese = []
    try:
        with open("spese.txt", "r") as file:
            for riga in file:
                descrizione, importo = riga.strip().split(",")
                spese.append((descrizione, float(importo)))
    except FileNotFoundError:
        pass
    return spese

def salva_spesa_su_file(descrizione, importo):
    with open("spese.txt", "a") as file:
        file.write(f"{descrizione},{importo}\n")

def aggiorna_lista():
    lista_spese.delete(0, tk.END)
    spese = carica_spese()
    totale = 0
    for descrizione, importo in spese:
        lista_spese.insert(tk.END, f"{descrizione}: {importo:.2f}€")
        totale += importo
    etichetta_totale.config(text=f"Totale: {totale:.2f}€")

def aggiungi_spesa():
    descrizione = campo_descrizione.get()
    importo_testo = campo_importo.get()

    if descrizione == "" or importo_testo == "":
        etichetta_errore.config(text="Compila entrambi i campi!")
        return

    try:
        importo = float(importo_testo)
    except ValueError:
        etichetta_errore.config(text="L'importo deve essere un numero!")
        return

    salva_spesa_su_file(descrizione, importo)
    etichetta_errore.config(text="")
    campo_descrizione.delete(0, tk.END)
    campo_importo.delete(0, tk.END)
    aggiorna_lista()

# Finestra principale
finestra = tk.Tk()
finestra.title("Gestione Spese")
finestra.geometry("350x400")

tk.Label(finestra, text="Descrizione:").pack(pady=(15, 0))
campo_descrizione = tk.Entry(finestra, font=("Arial", 12))
campo_descrizione.pack()

tk.Label(finestra, text="Importo (€):").pack(pady=(10, 0))
campo_importo = tk.Entry(finestra, font=("Arial", 12))
campo_importo.pack()

tk.Button(finestra, text="Aggiungi spesa", command=aggiungi_spesa).pack(pady=10)

etichetta_errore = tk.Label(finestra, text="", fg="red")
etichetta_errore.pack()

lista_spese = tk.Listbox(finestra, width=40, height=10)
lista_spese.pack(pady=10)

etichetta_totale = tk.Label(finestra, text="Totale: 0.00€", font=("Arial", 12, "bold"))
etichetta_totale.pack(pady=5)

aggiorna_lista()
finestra.mainloop()
