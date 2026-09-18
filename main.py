from fastapi import FastAPI, Query
import requests as r

app = FastAPI()

@app.get('/api/ola_mundo')#Aqui indica que a partir da rota passada dentro dos parenteses, vai ser usado um metodo get que realizará a função passada abaixo dele
def hello():
    '''
    Endpoint para aparecer Hello World
    '''
    return {'Olá':'Mundo'} #Retorna dentro do Json Olá Mundo

#Função de retornar restaurante
@app.get('/api/restaurantes/')#Pra usar a query, preciso colocar o ? após a barra pra iniciar a pesquisa
def pegar_restaurante(restaurante:str = Query(None)): #Faz com que funcione até se o caminho depois da barra tiver vazio funcione, e permite fazer pesquisas
    '''
    Endpoint que recebe todos os cardapios dos restaurante
    '''
    url =  'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = r.get(url)

    if response.status_code == 200:
        dados_json = response.json()#Aqui está transformando a resposta da API em Json
        if restaurante is None:#Se a busca de restaurante tiver vazia
            return {'dados' : dados_json}#Vai listar os restaurantes e os dados deles
        
        dados_restaurante = []#Aqui vai receber todos os dados do restaurante[{item: '', preco:'', descrição : ''}]
        for item in dados_json: #Pra cada item dentro da API
            if item['Company'] == restaurante: #Se o restaurante passado for igual ao um da lista de restaurantes
                dados_restaurante.append({
                    'Item' : item['Item'],
                    'Preço' : item['price'],
                    'Descrição' : item['description']
                })# Os dados do restaurante vão receber as informações da API correspondente ao restaurante requerido
        return {'Restaurante' : restaurante,'Cardapio': dados_restaurante}#Aqui, exibe do nome do restaurante pesquisado e os dados dos produtos do restaunte em questão.
    else:
        return {'ERRO' : f'{response.status_code} - {response.text}'}
        