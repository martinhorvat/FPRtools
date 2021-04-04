#!/usr/bin/python3

import sys

path = sys.argv[1]
#label = sys.argv[2]

podatki = []

with open(path, 'r') as file:
	for s in file:
		podatki.append(list(s.replace("\n", '').split('\t')))

'''model = '||'

for _ in len(podatki[0]):
	str += 'c|

model += '|'''

tabela = '\hline\hline\n'

for i in podatki:
	for j in i:
		tabela += j + ' & '
	tabela = tabela[:-3] + "\\\\" + '\n\hline\n'

with open('tabela.txt', 'w') as file:
	file.write(tabela)



