import json

with open("matricole.json", "r") as file:
    mat_list = json.load(file)

print("Questo programma permette di farsi liberamente i cazzi degli altri, associando al nome il numero di matricola e viceversa.\nI numeri di matricola noti sono salvati nel file 'matricole.json'\n\n\Digita 'traduci [nome/numero di matricola]' per associare un nome ad una matricola o viceversa.\n Digita 'aggiungi [nome e cognome] [numero di matricola]' per aggiungere un valore al database.\n Digita 'esci' per uscire")

while True:
    t = input("Cosa vuoi fare?  ")
    t = t.split(" ")
    if (t[0] == "traduci"):
        if (len(t) > 2):
            [print(i) for i in mat_list if (t[1]+" "+t[2]).lower() in i]
        else:
            [print(i) for i in mat_list if (t[1]).lower() in i]
    
    elif (t[0] == "aggiungi"):
        if (len(t) < 4):
            pass
        else:
            with open("matricole.json", "w") as file:
                mat_list += [[t[1] + " " + t[2], t[3]]]
                json.dump(mat_list, file)
    
    elif (t[0] == "esci"):
        break

    else:
        print("Comando non riconosciuto, riprova")

