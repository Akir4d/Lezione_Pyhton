def saluta(nome):
    saluto = f"Ciao, {nome}. Come stai? Tutto bene?"
    return saluto

def somma(numero, addendo):
    return numero + addendo

def sottrazione(numero=70, sottraendo=89):
    return numero - sottraendo

gl=30

def facciocose():
    gl=40
    print(f"gl={gl}")

def facciocose_globali():
    global gl
    gl=50
    print(f"gl={gl}")

def stampocose():
    print(f"gl={gl}")

def main():
    risposta=saluta("Paolo")
    print(risposta)
    print(saluta("Alice"))
    print(saluta("I gatti"))
    print(somma(1,2))
    print(sottrazione(sottraendo=3, numero=67))
    print(sottrazione(sottraendo=30))
    print(sottrazione(90))
    print(sottrazione(90,10))
    facciocose() # questa non ha il global e non sovrascive la varibile
    stampocose() # stampa 30
    facciocose_globali() # questa funzione con il global sovrascive la variabile
    stampocose() # stampa 50
main()
if __name__ == "__main__":
    main()

