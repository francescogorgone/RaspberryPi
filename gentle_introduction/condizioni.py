input_utente = int(input("Inserisci un numero: "))

if (input_utente) < 10:
    print(f"{input_utente} < 10")
elif(input_utente < 20):
    print("10 <" , input_utente , "< 20")
elif(input_utente < 30):
    print("20 <" , input_utente , "< 30")
else:
    print('Input utente >=30')
    print(f'Input utente = {input_utente}')
