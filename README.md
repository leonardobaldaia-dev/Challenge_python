## Integrantes do Projeto
- **Maria Clara** - RM: 557478
- **Lorran do Santos** - RM: 558982
- **Gabriel Caetano** - RM: 557582
- **Leonardo Baldaia** - RM: 557416

# Simulador Básico de Corrida da Fórmula E

Este é um projeto simples em Python que simula uma corrida da Fórmula E, com foco no consumo de energia da bateria. O programa foi desenvolvido como um exercício de introdução à programação com a linguagem Python e ao uso de funções (`def`).

## Como funciona

### `obter_informacoes_piloto()`
- Solicita ao usuário o nome do piloto e a equipe.
- Retorna esses valores para serem usados na corrida.

### `simular_volta(energia_restante)`
- Simula uma volta da corrida.
- Subtrai 5 unidades da energia restante, simulando o consumo da bateria.
- Retorna a energia restante após a volta.

### `corrida()`
- Obtém as informações do piloto chamando `obter_informacoes_piloto()`.
- Inicializa a energia restante em 100% e define o número de voltas da corrida (10).
- Imprime a mensagem de largada com o nome do piloto e a equipe.
- Inicia um loop `for` para simular cada volta da corrida:
  - Chama `simular_volta()` para atualizar a energia restante.
  - Imprime a volta atual e a energia restante.
  - Verifica se a energia restante é menor ou igual a zero:
    - Se sim, imprime a mensagem de bateria esgotada e encerra a corrida.
    - Se o loop terminar sem interrupções, imprime a mensagem de conclusão da corrida.

### `corrida()` (chamada)
- Inicia a execução do programa chamando a função `corrida()`.


