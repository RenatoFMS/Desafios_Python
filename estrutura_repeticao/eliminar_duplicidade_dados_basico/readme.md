# Desafio
O Banco ByteSafe é conhecido por sua eficiência digital, mas recentemente um bug no sistema causou a duplicação de algumas transações em seu extrato online. Como analista de dados do banco, você foi encarregado de criar uma ferramenta que ajude a identificar e remover essas inconsistências. Cada linha do extrato é uma sequência de identificadores de transações, separados por espaço, e pode conter transações repetidas. Sua missão é garantir que cada transação apareça apenas uma vez, mantendo a ordem da primeira ocorrência. Assim, o extrato ficará limpo e sem duplicatas, facilitando a conferência dos clientes e a auditoria do banco.

Implemente uma função que receba uma string com identificadores de transações separados por espaço e retorne uma nova string, também separada por espaço, contendo apenas a primeira ocorrência de cada transação, na ordem em que aparecem originalmente. Não utilize bibliotecas externas para manipulação de listas ou conjuntos.

Entrada
Uma única linha contendo identificadores de transações separados por espaço. Cada identificador é uma sequência de caracteres alfanuméricos sem espaços.

Saída
Uma única linha contendo os identificadores de transações, separados por espaço, sem repetições e na ordem da primeira ocorrência.
## Exemplos: Ferramentas Bancárias

| Entrada | Saída |
| :--- | :--- |
| Planilha Excel de simulacao de parcelas de emprestimo | Calcula valor das parcelas com juros sobre o emprestimo |
| Consulta SQL com total de compras no cartao | Soma compras registradas no cartao em uma tabela |
| Planilha Excel de pagamento | Tecnica desconhecida |
| Consulta SQL listando emprestimos em aberto | Retorna emprestimos ativos para analise de risco |
