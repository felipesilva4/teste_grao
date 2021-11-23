from datetime import datetime
montanteInicial = 100
aporte = 100
selic = 4.25
t = 5/252
m=0
i=1
while(i <= 36):
    m+=aporte
    m = m*(1+selic/100)**t
    print('montante na semana '+str(i)+': '+str(round(m,2)))
    i+=1
print(round(m, 2))


