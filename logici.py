if(1 < 3): print("Vero")
if(1 > 3):
    print("non stampa")
else:
    print("non e' vero che 1 > 3")
if(1 <= 1): print("e' vero che 1 <= 1")
if(1 >= 1): print("1 >= 1 e' vero perche' 1=1")
if(2 != "Uno"): print("e' vero che 2 e' diverso da Uno")
if(1 == 1): print("e' vero che 1=1")
n=3 # ma magari potrebbe essere "3"
if(type(n) is int): print("e' un intero")
if(type("Ciao") is not int): print("e' vero che 'Ciao' non e' in intero")
lista = [1,2,3,"Franco"]
if ("Franco" in lista): print("Franco e' onnipresnte!")
if ("Paolo" not in lista): print("Paolo e' eterno assente")
if (not 1 > 1): print("negare l'evidenza!")
if ((1 > 1) or (2 == 2)): print("Una delle due doveva essere vera")
if ((1 == 1) and ("Franco" == "Franco")): print("E basta co sto Franco")
if ( 1 == "1"): print("Falso")