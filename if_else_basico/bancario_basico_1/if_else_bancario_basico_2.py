entrada = input().strip()

def descrever_uso(nome):
    if nome == "Planilha Excel de simulacao de parcelas de emprestimo":
        return "Calcula valor das parcelas com juros sobre o emprestimo"

    elif nome == "Relatorio em Excel com resumo de gastos do cliente":
        return "Mostra resumo mensal dos gastos do cliente no banco"

    elif nome == "Consulta SQL com total de compras no cartao":
        return "Soma compras registradas no cartao em uma tabela"

    elif nome == "Consulta SQL listando emprestimos em aberto":
        return "Retorna emprestimos ativos para analise de risco"

    else:
        return "Tecnica desconhecida"

print(descrever_uso(entrada))