entrada = input()
abertura_str, fechamento_str = entrada.split()

abertura = int(abertura_str)
fechamento = int(fechamento_str)



if abertura > fechamento:
  print("BAIXA")
elif abertura < fechamento:
  print("ALTA")
elif abertura == fechamento:
  print("ESTAVEL")
else:
  print("Insira valores validos.")