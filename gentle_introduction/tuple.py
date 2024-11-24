tupla_lettere = ("a","b","c","d","e")
for lettera in tupla_lettere:
    print(f'Lettera: {lettera}')
print(len(tupla_lettere))
print(tupla_lettere.index("c"))#restituisce la posizione di quell'elemento

char = "c"
if char in tupla_lettere:
    print(tupla_lettere.index(char))
  
