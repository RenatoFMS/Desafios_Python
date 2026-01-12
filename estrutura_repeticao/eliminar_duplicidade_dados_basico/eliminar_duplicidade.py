entrada = input()
transacoes = entrada.split()

verificador = set()

lista = []


for item in transacoes:
  if item not in verificador:
    verificador.add(item)
    lista.append(item)
    
   
print(" ".join(lista))