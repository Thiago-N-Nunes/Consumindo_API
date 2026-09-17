import requests as r
import json

url =  'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = r.get(url)

if response.status_code == 200:
    print('Conexão bem sucedida')
    dados_json = response.json()#Aqui está transformando a resposta da API em Json
    print(dados_json)
    dados_restaurantes = {}#Aqui vai receber todos os dados do restaurante
    for item in dados_json: #Pra cada item dentro da API
        nome_restaurante = item['Company'] #Nome do restaurante vai receber o valor do que está referenciado dentro da chave
        if nome_restaurante not in dados_restaurantes:#Se o restaurante não tiver dentro da lista dados restaurante
            dados_restaurantes[nome_restaurante] = []#Cada item dentro de dados_restaurante recebe uma lista vazia

        else:
            ...
        dados_restaurantes[nome_restaurante].append({
            'Item' : item['Item'],
            'Preço' : item['price'],
            'Descrição' : item['description']
        })
        #Cada produto dentro da lista vazia referente a oq foi encontrado na API vai receber os valore passados dentro dos colchetes, cada um dentro das chaves sendo cada produto um dicionario, sendo assim cada item dentro do dicionario dados restaurante é uma lista de dicionarios, com dicionarios correspondentes ao nome de cada restaurante
        #McDonald's = [{'Item' : 'BigMac', 'Preço' : 35, 'Descrição' : 'Dois hamburgueres,Alface,Queijo, Molho especial...'}, {...}, {...}] - Exemplo 

for nome_restaurante,dados in dados_restaurantes.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)

# ^- Aqui basicamente: Para cada lista de dados dentro de lista dados_restaurantes, primeiro gera um arquivo json com o nome da lista
#    Com open(nome do arquivo no modo de escrever):
#    json.dump[crie um json](dados de cada produto, no arquivo que estamos criando.json e com uma identação de 4 linhas de um produto para o outro) 