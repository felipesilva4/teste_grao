import datetime as dt
from datetime import datetime
from workadays import workdays as wd
import requests
import json
import re

# Esse script pega algumas ações da b3 e mostra quanto renderia se comprasse R$100 por semana durante 36 semanas

class tools():
    def init():
        # URL que calcula na 4devs dias anteriores
        urlData = 'https://www.4devs.com.br/ferramentas_online.php'

        urlBase = 'https://www.infomoney.com.br/cotacoes/ibovespa/historico/'
        #url que fornece historico de cotações
        urlInfoMoney = 'https://www.infomoney.com.br/wp-admin/admin-ajax.php'

        def start():
            dataAtual = datetime.today().strftime("%d/%m/%Y")

            headers = {
                'Host': 'www.4devs.com.br',
                'Origin':'https://www.4devs.com.br',
                'Referer': 'https://www.4devs.com.br/subtrair_dias_em_datas',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }

            #deixei 252 que é o total de dias corridas em 36 semanas
            payload = {
                'acao': "subtrair_dias",
                'txt_data_base': dataAtual,
                'txt_numero_dias': '252'
            }

            data = requests.post(urlData, data = payload, headers=headers)
            idsAcao = ['ITSA4', 'TIMS3', 'CASH3', 'PETR3']

            for idAcao in idsAcao:
                getVariavel = getInfoAcoes(dataAtual, data, idAcao)

            getSelicRenda = getSelic()

        def getSelic():
            aporte = 100
            selic = 4.25
            t = 5/252
            m=0
            i=1
            while(i <= 36):
                m+=aporte
                m = m*(1+selic/100)**t
                i+=1
            print('Valor total na selic: '+str(round(m, 2)))

        #verifica a cotação historica e "compra" a cotação de fechamento a cada 5 pregões
        def getInfoAcoes(dataAtual, dataInicio, idAcao):

            html = requests.get(urlBase)
            quotesPattern = r"quotes_history_nonce\":\"(.*?)\""
            quotes = re.findall(quotesPattern, html.text)
            payload = {
                'page': "0",
                'numberItems': "99999",
                'initialDate': dataInicio,
                'finalDate': dataAtual,
                'action': "more_quotes_history",
                'quotes_history_nonce': quotes[0],
                'symbol': idAcao
            }

            r = requests.post(urlInfoMoney, payload)
            fechamentoPattern = r"timestamp.*?,.*?\".?.?.?.?.?\",\"(.*?).\""
            cotacao = re.findall(fechamentoPattern, r.text)

            aporte = 100
            semanas = 36
            i=1
            j=0
            tam = len(cotacao)
            tam = tam-1
            patrimonio = 0
            #verifica qtd de papeis que pode comprar com o dinheiro que tem na carteira
            #exemplo comprou 9 acoes a 9.01 cada, sobra na carteita 9 e na proxima semana soma os 9 + 100
            while (i < semanas):
                cotacaoDia = cotacao[tam].replace(r",", ".")
                #verifica quantas cotas pode ser compradas
                if (i == 1):
                    carteira = aporte
                    qtd = carteira/float(cotacaoDia)
                    patrimonio = int(qtd)*float(cotacaoDia)
                    carteira = carteira-patrimonio
                    tam = tam-5
                    #se a ação for 120 e na carteira tiver só 110 impede que a contagem erre
                    if(qtd>=1):
                        nAcoes = int(qtd)
                else :
                    carteira += aporte
                    qtd = carteira/float(cotacaoDia)
                    patrimonioDia = int(qtd)*float(cotacaoDia)
                    patrimonio += patrimonioDia
                    carteira = carteira-patrimonioDia
                    tam = tam-5
                    #se a ação for 120 e na carteira tiver só 110 impede que a contagem erre
                    if(qtd>=1):
                        nAcoes += int(qtd)
                i+=1

            cotacaoFinal = cotacao[0].replace(r",", ".")
            patrimonioFinal = float(cotacaoFinal)*nAcoes
            
            valorCarteira = round(carteira, 2)
            valorPatrimonio = round(patrimonioFinal, 2)
            total = valorCarteira+valorPatrimonio
            print('Ações da '+idAcao)
            print('Valor das ações em dinheiro: '+str(valorPatrimonio))
            print('valor que restou em carteira: '+str(valorCarteira))
            print('quantidade de ações: '+str(nAcoes))
            print('total: '+str(round(total,2)))
            print("-------------------------\n\n")



        start()
    inicio = init()
