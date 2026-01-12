entrada = input().strip()

saldo = 0.0
d_total = 0
r_total = 0

lancamentos = entrada.split(',')


for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)

    if tipo == "R":
      r_total += valor
      
    if tipo == "D":
      d_total +=valor

saldo = r_total - d_total

print(f"{saldo:.2f}")