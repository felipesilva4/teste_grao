montanteInicial = 100
aporte = 100
selic = 4.25
t = 5/252
m=0

for(i=0; i<36; i++) {
    m+=aporte
    m = m*(1+selic/100)**t
}

console.log(m)