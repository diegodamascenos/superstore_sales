# Análise de vendas (Superstore Sales)

## Objetivo do Estudo
Com o intuito de aprimorar e mostrar os conhecimentos que venho adquirindo durante minha jornada de estudos em Data Science e Analysis, realizei uma análise exploratória dos dados de vendas de uma loja fictícia do setor de varejo, cujas vendas são dos anos de 2015 a 2018.

Neste sentido, busquei detalhar os indicativos de desempenho de vendas, analisando os principais dados a respeito deste Dataset. A fim de recomendar soluções, indicar investimentos (tempo e capital) nos produtos com bons desempenhos de vendas, e minimizar quaisquer que sejam os erros neste cenário.<hr>



## Fonte dos Dados
- Todos os dados  podem ser encontrados no dataset <a href='https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting' target='_blank'>Superstore Sales Dataset</a>, no kaggle ou no link disponível abaixo:
    - https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
<hr>



## Tecnologias utilizadas na análise:
<div>
    <img align= "center" alt ="Pyhon" src= https://img.icons8.com/?size=50&id=13441&format=png&color=000000>
    <img align= "center" alt ="Pandas" src= https://img.icons8.com/?size=50&id=xSkewUSqtErH&format=png&color=000000>
    <img align= "center" alt ="Matplotlib" src= https://github.com/user-attachments/assets/bf202433-d354-44c0-9f9d-8de140d61b96>
    <img align= "center" alt ="NumPy" src= https://img.icons8.com/?size=50&id=aR9CXyMagKIS&format=png&color=000000>
</div>

## Pontos Principais da Análise
### Análise de **Vendas por Ano:**
- Nos resultados das vendas de 2016, houve uma queda **4.26%** nas vendas.
- As vendas de 2017 em relação ao ano de 2018, obteve um de crescimento de **20.3%**.
- No cenário geral, a taxa de crescimento anual foi de **10,76% a.a**.

Resultados indicados no gráfico:


![vendas_ano](https://github.com/user-attachments/assets/56ad2a76-bb77-4d4f-ad70-d96af755693e)



### Análise de **Vendas por Mês:**
- Os meses que correspondem ao ano de 2018, foram os que obtiveram melhores resultados de vendas.
- Apenas Maio e Dezembro de 2017, os resultados foram melhores que os mesmos meses de 2018.
- Apesar da queda descrita na análise anterior, o ano de 2016, manteve uma boa média de vendas em relação ao ano de 2015, dominando praticamente um semestre destas vendas.
- Novembro é o mês com maior índice de vendas, o que indica que é possível recomendar ações em torno deste mês, a fim de maximizar as vendas.

Resultados indicados no gráfico:


![vendas_mes](https://github.com/user-attachments/assets/93ded791-fee6-450e-b0a4-b7a9e70e40a2)



### Análise de **Categoria mais Vendida**
- Um declínio nas vendas de todas as categorias no ano de 2016, em relação ao ano anterior.
- Neste ano, a categoria mais vendida foram móveis (artigos para casa), com faturamento na casa de R$ 164.000,00, porém, ainda abaixo do ano anterior.
- Já em 2017 e 2018, os artigos de tecnologia voltaram a liderar as vendas por categorias, com um enorme salto e uma ampla vantagem as demais categorias.
- Indicativos de uma alta demanda de produtos da categoria de tecnologia e materiais de escritório para o ano de 2019 devido ao crescimento exponencial nas vendas destes.
- Manteve-se boa média nas vendas de artigos para casa (móveis), com uma leve crescente nas demandas destes produtos, mas ainda assim, abaixo das demais categorias ofertadas.

Resultados indicados no gráfico:



![vendas_categoria](https://github.com/user-attachments/assets/e400f6b1-f1ca-4d04-97d5-ee3c320f904d)



### Análise de **Produtos mais Vendidos**
Abaixo, é possível observar dois aspectos importantes sobre os dados, e informações valiosas para o negócio. 
- Os produtos de tecnologia, tem uma demanda muito superior as demais categorias, conforme gráfico abaixo.
- Nem todos os produtos apresentados, se mantém com bons desempenhos de vendas, ou são produtos estáveis neste quesito.

Resultados indicados no gráfico:



![produtos_mais_vendidos](https://github.com/user-attachments/assets/f3a253f1-3ced-449a-8681-ae3d8c019427)



### Análise de **Produtos mais vendidos por Ano**
Conforme observado acima, existe a necessidade de analisar e concluir quais os produtos tiveram bons desempenhos de vendas durante todos os anos, ou, que tiveram bons desempenhos somente em um ano específico, ou até mesmo qual foi o ano deste bom desempenho.

Isto se faz necessário devido ao impacto que geraria um investimento em um produto que já não vende mais, ou tem um retorno abaixo do investimento. Esta abordagem leva em consideração a avaliação de quais serão as estratégias adotadas no intuito de maximizar as vendas dos produtos com maior demanda durante todos os anos, e aqueles que venderam no último ano em diante. Para assim, distingui-los dos produtos que não tem mais um bom desempenho de vendas.

Abaixo, é possível resumir as informações em um gráfico, detalhando os resultados das vendas de produtos, e seus respectivos desempenhos durante os anos de 2015 a 2018.

É possível visualiazar através do gráfico que, entre os produtos mais vendidos, existem também produtos que foram vendidos em apenas um ano, e até mesmo, produtos vendidos somente no primeiro ano da análise.

Principais observações e conclusões: <br>

- Cisco TelePresence System EX90 Videoconferencing Unit:
    - Como terceiro item da lista, vendeu somente no ano de 2015. Pode-se considerar como produto que não gera mais tanta receita. O que exclui a necessidade de um investimento maior neste produto.
    
- Fellowes PB500 Electric Puch Plastic Comb Binding Machine:
    - Como segundo item da lista, este produto apresenta um bom desempenho no ano de 2016, uma queda no ano de 2017, e um crescimento em 2018, porém, ainda assim gerando um receita inferior ao ano de 2016. O que indica que não venderá tão bem no ano de 2019, poupando um investimento de estoque, e direcionando energia em outros produtos em ascensão.

- Canon ImageCLASS 2200 Advanced Copier;
    - Como primeiro item da lista, este está em uma crescente nas vendas, e 2019 superará as vendas dos anos anteriores. É indicado que haja um investimento em marketing e capital superior ao ano de 2018, pois se trata de um produto com alta demanda de mercado, e grande potencial de retorno monetário.

- High Speed Automatic Eletric Letter Opener:
    - Mostrado como último item da lista, se mostra com boa projeção de vendas. Mas é importante observar o comportamento destas vendas, que tem um bom desempenho de vendas ano sim, e ano não. Desta forma, é recomendado que seja um produto observado e não descartado, com investimendo moderado. <br>
  É um produto que apresenta instabilidade de mercado, mas pode surpreender nas vendas de 2019, já que se trata de um produto que tem boas vendas, itercalando entre um ano bom, e um ano ruim.


O gráfico elaborado, apresenta os resultados de vendas dos produtos durante os anos registrados na análise. É possível visualizar que alguns destes,venderam em grande volume no primeiro ano e não obteve mais bons resultados de vendas. Por outro lado, outros produtos com bons indicativos de vendas para o próximo ano.


![produtos_vendas_ano](https://github.com/user-attachments/assets/87ddeb48-46ca-4c37-82ec-bc1d6f1e1d1c)
