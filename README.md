# Api de Notícias

- Teste: Desenvolvedor Arquiteto
- Autor: Gabriel Castorino

## Introdução

####Detalhes

#####Criar uma API que tenha as seguintes possibilidades:

- Buscar todas as notícias
- Filtrar notícias por palavra-chave no título
- Filtrar notícias por data (início - fim)
- Contar quantas notícias tiveram na última hora

Baseado no retorno do RSS: 

    http://www.valor.com.br/rss
 
#####Importante

- Deverá exigir autenticação/token
- Retornos devem ter a possibilidade de ser em JSON ou XML
- Fazer o uso de testes em código, no projeto, no que couber.
- Disponibilizar a documentação da API do modo que achar mais apropriado.
- Descrever o modo de instalação.
- Pode ser feito uso de qualquer linguagem.
- Ao término, publicar o projeto em um repositório aberto, como Github ou Bitbucket.

## Instalação

Baixe o projeto do git:

```bash
$ git clone https://github.com/gcastorino/crawlerPython3.git
```

Carregar as dependências execute o seguinte comando: 

```bash
$ pip install -r requirements.txt 
```

Executar a aplicação rodando o arquivo:
    
    .\run.py 

## Api

Parâmetros esperados

    api_key: eyJuYW1lIjoiR2FicmllbCBDYXN0b3Jpbm8ifQ
    type_return: json ou xml
    date_start: dateTime
    date_finish: dateTime

Buscar todas as notícias:

    :rota: /news/{auth}/{type_return} 
    :parâmetro auth: string
    :parâmetro type_return: string
    :retorno: Formato será correspondente a solicitado

Filtrar notícias por palavra-chave no título:

    :rota: /news/{auth}/{type_return}/{title} 
    :parâmetro auth: string
    :parâmetro type_return: string
    :parâmetro title: string
    :retorno: Formato será correspondente a solicitado

Filtrar notícias por data (início - fim):

    :rota: /news/{auth}/{type_return}/{date_start}/{date_finish} 
    :parâmetro auth: string
    :parâmetro type_return: string
    :parâmetro date_start: string
    :parâmetro date_finish: string
    :retorno: Formato será correspondente a solicitado
    
Contar quantas notícias tiveram na última hora:

    :rota: /news_count/{auth}/{type_return} 
    :parâmetro auth: string
    :parâmetro type_return: string - json ou xml
    :retorno: Formato será correspondente a solicitado

## Testes de código

Executar testes unitários rodando o arquivo: 

    .\my_app\crawler\teste.py 
