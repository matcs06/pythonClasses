'''

classe: m1_lab1.py

descricao: Listar os 8 caracteres do nome do vereador para fazer o login de acesso aos sistemas

autor: Clodonil Honorio Trigo

email: clodonil@nisled.org

data: 04 de julho de 2018

'''



# importa a lib para obter as tabelas da Wikipedia

from lib.scrapy_table import Scrapy_Table



# Variavel com o link da tabela

url="https://www.flextool.com.br/tabela_cores.html"



# Inicia a class para obter a tabela

site_connect = Scrapy_Table(url)



# Pegando a tabela 5 (Vereadores em exercicio)

tables = site_connect.get_tables(2)

  

# Listando o conteudo da tabela

for linha in tables[1:]:



     # Obtendo o nome. Esta na primeira posicao da lista

     nome = linha[0]



     # Imprimindo os caracteres da posicao 0 ate 8 

     print(linha)





     #Outras formas de fazer a mesma coisa

     #print(nome[:8])

 

     #Para retirar os espacos em branco de uma string

     #print(nome[:8].replace(' ',''))
