lista_numerica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_numeri_pari = []
lista_numeri_dispari = []
for numero in lista_numerica:
    if numero % 2 == 0: # % è operatore di modulo
        lista_numeri_pari.append(numero)
    else: lista_numeri_dispari.append(numero)
print(lista_numeri_pari)
print(lista_numeri_dispari)

lista_unita = []
lista_unita.extend(lista_numeri_pari)
lista_unita.extend(lista_numeri_dispari)
print(lista_unita)
