d1 = {"a":1,"b":2,"c":3}
d2 = {"w":4,"b":5,"c":6}
d1.update(d2)
print(d1)
print(d1.get("d" , "non esiste")) #se la chiave esiste, restituisce il valore corrispondente, altrimenti printa il valore inserito
