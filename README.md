
# Introdução

Esse repositorio é o meu retorno ao desafio técnico da empresa Indicium.

O código que executa a pipeline esta presente na caminho code/run_pipeline.py . Foi escolhido a linguagem python para fazer o pipeline
pela sua  facilidade de conectar a bancos diferentes e suas bibliotecas auxiliares facilitarem tal processo além de ser a linguagem que tenho mais conhecimento.

Como banco de dados de destino foi escolhido um banco MySQL pois é onde tenho mais conhecimento e a  existência de uma imagem docker dele evitando que 
precise instalar aplicações na  minha máquina. Outro ponto que me fez escolher tal banco de dados é a existência de bibliotecas do python que fazem a conexão
de forma facilitada.

Tambem foi utilizado na resolução um "visualizador" de bancos,o adminer, para durante a fase de testes eu conseguir verificar se os bancos foram populados e 
resolução de bugs durante o processo.

Os arquivos foram salvos no formato de tables/fontededados/tabela/data/tabela.csv . Alguns exemplos são 

```
tables/csv/order_details/2022-01-01/order_details.csv
tables/postgres/categories/2022-01-01/categories.csv
tables/postgres/categories/2022-02-01/categories.csv

```


# Entregáveis

As instruções para execução do pipeline encontram-se no bloco Instruções.

O csv com a query foi criado rodado o seguinte comando 

```
python3 code/final_query/execute_final_query.py 
```

O csv resultante é o order_with_details.csv



# Instruções 

Para executar o pipeline será necessario a instalação de [docker-compose](https://docs.docker.com/compose/install/) e que a versão do python sera > 3.


Primeiro passo : Subir os containers do banco de dados MySQL de destino e postgree,onde os dados estão.



```
docker-compose up
```

Espere alguns minutos para que  os containers tenham subido, e que os dados foram carregadas no banco.

Segundo passo : Instalar as bibliotecas necessárias para a realização do pipeline. Execute tal comando no terminal


```
pip install -r requirements.txt
```

Terceiro passo : Com as bibliotecas instaladas, podemos executar a pipeline. Para rodar a pipeline execute tal comando no terminal
```
python3 code/run_pipeline.py
```
Existem mensagens de erro caso haja problemas no pipeline. Caso você precise rodar para algum dia especifico, adicione a flag -d ao comando. Um exemplo de como rodar para dias passados é :

```
python3 code/run_pipeline.py -d "2022-01-01" 

ou 

python3 code/run_pipeline.py --date "2022-01-01" 

```



# Organização do codigo

O código esta organizado da seguinte maneira :

code : Onde se encontra os codigos em python. Neles existe uma pasta para cada passo, e cada passo existe um pasta helpers, com funções auxiliares. 
       Também existe a pasta final_query, contendo o código que executa a query final no banco MySQL.


queries : Pasta onde se encontra as queries utilizadas nesse teste.

tables : Pasta onde será armazenada localmente os dados. Ela é criada ao rodar a pipeline.


