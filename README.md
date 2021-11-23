# Teste Técnico Back-end

Calcula rendimentos de acordo com a taxa selic de 4.25% a.a.

## Requisitos
* python3.6 +
* node 16.8.0

## Como executar
* python: criar uma venv com os comandos python-m venv venv ou virtualenv -p /usr/bin/python3.8 venv ou virtualenv -p python3 myenv
* ativar a venv com $ source venv/bin/activate
* Executar o comando: $ pip install -r requirements.txt ou  $ pip3 install -r requirements.txt
* rodar o script python3 testeTools.py

* testeTools.py além de calcular a selic, ele também calcula caso o dinheiro tivesse sido aplicado em renda váriavel, especificamente nas ações: 'ITSA4', 'TIMS3', 'CASH3', 'PETR3'.
* pode inserir ou remover mais ações, basta alterar a lista 'idsAcao' em testeTools.py
* Pode ser inserido mais códigos de ações ou FIIS, foi feito apenas como um "plus", devido o teste ser muito breve
* Não há necessidade da venv caso não deseja avaliar o testeTools, apenas execute: python3 teste.py com python 3.6+

* Versão em node basta apenas executar:$ node index.js