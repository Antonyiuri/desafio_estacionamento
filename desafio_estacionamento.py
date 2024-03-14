#Desafio com Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro

'''

Funcionarios = ['Antony','João','Leandro','Gabriel','Francisco','Rebeca','Livia','Paula','Priscila','Ana Caroline']   
turno_dia = ['Antony','João','Francisco','Leandro','Gabriel']
turno_noite = ['Rebeca','Livia','Paula','Priscila','Ana Caroline']
tem_carro = ['Antony','João','Francisco','Leandro','Livia']

lista_1 = set(Funcionarios)
lista_2 = set(turno_dia)
lista_3 = set(turno_noite)
lista_4 = set(tem_carro)

print(lista_4 & lista_3)
print(lista_2 & lista_4)
print(lista_1 ^ lista_4)

#RESPOSTA DA UDEMY:

#Lista1 
pessoas_com_carro = set (tem_carro).intersection(turno_noite)
print((lista1))


#Lista2 
pessoas_com_carro = set (tem_carro).intersection(turno_dia)
print((lista2))


#Lista3 
pessoas_com_carro = set (tem_carro).difference(Funcionarios)
print((lista3)) 