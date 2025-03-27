# variabili
# devono iniziare per a-z o A-Z o _
A2459 = 34
# non e' possibile fare 2A459 = 34 
art321= "Prova"
_var="prova"
# non e' possibile usare parole chiave com if, else, for ,print etc..
# quindi if="Ciao" non fiziona!
# convenzione variabili:
# le varibili dovrebbero essere sempre minuscole con undescore a separare le parole
varibileUno = 1 # si puo' usare
varibile_uno = 1 # meglio per seguire la convenzione
# mentre le classi per convenzione sono espresse in lettere miniscole con iniziali maiscole
# LaMiaClasse
# Tipi di variabili
x = 10      # intero > int()
y = 3.24    # float  > float()
n = "Alice" # stringa > str()
att = True  # boleano > bool()
lista = [1,2,3,"Ciao"] # lista > list()
lista[3] = "Quattro" # modifica il singolo elemento gli elenti erano 0,1,2,3
print(lista)
lista.append("Cinque") # aggiunge un elmento alla fine
lista.insert(1,"Franco") # insert inserisce prima dell'elemento
print(lista)
coordinate = (10, 20) # tupla
coordinate = (30, 10) # nella tupla non si puo' modificare gli elementi
print(coordinate[0])
utente = {"nome": "Alice", "eta": 35, "altezza": "175cm"} # dizionario
print(utente)
print(utente["nome"])
utente["nome"] = "Piera"  # modifica
print(utente)
del utente["eta"] # cancella
print(utente)
utente["eta"] = 24 # aggiunge 
print(utente)
utente.pop("eta") # cancella
print(utente) 
print(utente.keys()) # mostra le keys
print(utente.values()) # mostra valoro
print(utente.items()) # invia le combinanazioni in un array di tuple