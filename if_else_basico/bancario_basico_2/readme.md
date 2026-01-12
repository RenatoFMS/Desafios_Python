# Desafio
Desafio de codigo basico sobre uso de Excel e SQL em contexto de banco e mercado financeiro. Uma equipe de analistas utiliza planilhas e consultas para simular emprestimos, acompanhar gastos e analisar operacoes de cartao dos clientes. Sua missao e criar um programa que receba o nome de um desses usos e retorne uma breve descricao correspondente.

Caso o nome informado nao exista na lista de opcoes, o sistema deve retornar: Tecnica desconhecida.

Entrada
O programa deve ler uma string com o nome de um dos usos a seguir:

"Planilha Excel de simulacao de parcelas de emprestimo"
"Relatorio em Excel com resumo de gastos do cliente"
"Consulta SQL com total de compras no cartao"
"Consulta SQL listando emprestimos em aberto"
Saida
O programa deve imprimir uma string com a descricao correspondente:

Calcula valor das parcelas com juros sobre o emprestimo
Mostra resumo mensal dos gastos do cliente no banco
Soma compras registradas no cartao em uma tabela
Retorna emprestimos ativos para analise de risco
Se a entrada nao corresponder a nenhuma das opcoes validas, o programa deve imprimir:

Tecnica desconhecida

### Exemplos de Uso

| Entrada | Saída |
| :--- | :--- |
| Planilha Excel de simulacao de parcelas de emprestimo | Calcula valor das parcelas com juros sobre o emprestimo |
| Consulta SQL com total de compras no cartao | Soma compras registradas no cartao em uma tabela |
| Planilha Excel de pagamento | Tecnica desconhecida |
| Consulta SQL listando emprestimos em aberto | Retorna emprestimos ativos para analise de risco |
