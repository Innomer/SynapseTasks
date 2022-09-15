from operator import truediv


modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']
indices=list()
characters=list()
#1n2
for ind,name in enumerate(modern_family):
    indices.append(ind)
    characters.append(name.lower().replace('_','-'))

#3
n=lambda a : len(a)
print(n(input()))

temp=list(map(n,characters))
print(temp)

#4
indices=list(map(sum,(zip(indices,temp))))

#5
indices.sort(reverse=True)

#6
Phew_finally=dict(zip(indices,characters))
print(Phew_finally)