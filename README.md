# grafos_trabalho

# Problema Proposto:
Depois de realizada uma reunião com um dos representantes de uma certa
empresa de Telecom, foi possível analisar a possibilidade de aplicação de um dos
problemas de otimização em redes, visando a minimização do comprimento total de
cabo de fibra óptica utilizado para arranjo de uma determinada rede de distribuição de
Internet. Salienta-se que, para a rede de distribuição funcionar, todas as estações
devem estar de algum modo conectadas entre si, sem prejudicar a qualidade da
conexão. Com o objetivo do modelo determinado, foi selecionado um bairro onde a
empresa presta serviço para este ser o objeto de estudo. Assim, foram estabelecidas
oito estações de distribuição de Internet.
As distâncias entre essas estações de distribuição são apresentadas na Tab.(1).
Como pode ser visto, a distância entre EST1 (Estação de distribuição 1) até EST2
(Estação de distribuição 2) é de 531 metros. Portanto, a Tab. (1) apresenta os dados
referentes as distâncias entre as estações de distribuição estudadas (EST1, EST2, EST3,
EST5, EST8), uma vez que todas as estações são conectadas entre si e direcionadas a
partir de seu local à residência que utiliza o serviço de Internet da empresa em
questão.

![Screenshot 2023-11-10 at 13 49 34](https://github.com/samuellucas21504/grafos_trabalho/assets/64492946/8bc91fac-db3e-40b0-8864-d489347df5ac)
  
Com o problema pré-determinado, foi elaborada uma rede com as estações
ligadas as suas respectivas estações conectoras. A Fig. (1) apresenta a rede definida
com as distâncias referentes as respectivas estações de distribuição de Internet.

![Screenshot 2023-11-10 at 13 51 46](https://github.com/samuellucas21504/grafos_trabalho/assets/64492946/0648af4a-143f-4168-b1ec-9e9a3434d109)

Após uma análise dos relatórios fornecidos pela empresa de Telecom e o
estudo dos algoritmos de Prim e Kruskall, foi possível determinar uma árvore geradora
mínima através dos algoritmos de Prim e Kruskal.
• Faça a implementação dos algoritmos: Prim e Kruskal
• Apresente a árvore gerada mínima obtida por cada um dos algoritmos.
Represente as ligações entre as estações que venham a se encaixar no objetivo
de minimização da quantidade de fibra óptica utilizada.
• Faça a análise de complexidade e otimização dos algoritmos implementados
• Analisar os respectivos algoritmos e propor uma melhoria na sua
eficiência. Deverão ser feitos testes de desempenho através de análise
gráfica dos custos computacionais (tempo de execução) para identificar
possíveis problemas de desempenho e avaliar a eficiência das
otimizações implementadas.
• Faça e imprima o cálculo do custo em reais do gasto de cabo de fibra óptica
utilizado para o arranjo dessa rede de distribuição de Internet. Pesquise o valor
médio do metro de cabo de fibra ótica.
• Permita testar o código com um número de estações maior.
Cabe ressaltar que, na prática, estações com quantidades maiores de entrada
para novos clientes serão necessárias, pois o atendimento para novos clientes não é
suportado somente pelas estações presentes na árvore geradora mínima. Contudo,
conforme informação passada pela empresa espera-se com este trabalho reconhecer a
utilidade dos algoritmos apresentados para auxílio no processo decisório.
Este trabalho irá contribuir para a área acadêmica, ao divulgar uma aplicação
prática do problema da árvore geradora mínima, e para a área empresarial, visto que a
otimização em redes tem grande importância para as empresas do mesmo ramo ou
ramos semelhantes, e sua utilização pode trazer benefícios financeiros e competitivos
para ambas. Salienta-se que o comprimento total utilizado de cabo pode impactar na
redução dos custos de materiais na distribuição de Internet, caso haja a aplicação dos
resultados encontrados.
