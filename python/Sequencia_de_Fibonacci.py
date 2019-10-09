# -*- coding: latin1 -*-

print('''  \n \n   
                       ____ 
                      / * *)
                     /    / 
          .__^^^^^__/    /
      ___/              /
      ___              /
          | | ______| |
          |_|       |_| \n \n''')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

linha = '-' * 50
titulo = 'Sequencia de Fibonacci'

print(linha)
print(titulo.center(50))
print(linha, "\n")



print("-"*50, "\n",'''Na matem�tica, a Sucess�o de Fibonacci (tamb�m Sequ�ncia de Fibonacci), � uma sequ�ncia de n�meros inteiros, come�ando normalmente por 0 e 1, na qual, cada termo subsequente corresponde � soma dos dois anteriores. A sequ�ncia recebeu o nome do matem�tico italiano Leonardo de Pisa, mais conhecido por Fibonacci, que descreveu, no ano de 1202, o crescimento de uma popula��o de coelhos, a partir desta. Esta sequ�ncia j� era, no entanto, conhecida na antiguidade.

Os n�meros de Fibonacci s�o, portanto, os n�meros que comp�em a seguinte sequ�ncia (sequ�ncia A000045 na OEIS):

0,1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ... .[nota 1][2].
Em termos matem�ticos, a sequ�ncia � definida recursivamente pela f�rmula abaixo, sendo o primeiro termo F1= 1:

Fn=Fn-1+Fn-2

e valores iniciais

F1=1; F2=1

A sequ�ncia de Fibonacci tem aplica��es na an�lise de mercados financeiros, na ci�ncia da computa��o e na teoria dos jogos. Tamb�m aparece em configura��es biol�gicas, como, por exemplo, na disposi��o dos galhos das �rvores ou das folhas em uma haste,[3] no arranjo do cone da alcachofra, do abacaxi,[4] ou no desenrolar da samambaia.[5]''',"\n","\n","     -https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci","\n", "-"*50, "\n")


x=int(input(" 1 - repetir at� n . 2 - repetir x vezes . 3 - repetir infinitamente . escolha um n�mero:".replace(".", "\n")))
a= 0
b= 1
c=0
print("/\  "*10)
print("  \/"*10)

if x == 1:
  n=int(input("digite o valor maximo da sequencia fibonacci:"))
  print("/\  "*10)
  print("  \/"*10)
  print(a)
  print(b)
  while(1):
    c = a + b
    if c > n:
      break
    a = b
    b = c
    print (c) 
elif x == 2:
  n=int(input("Digite a quantidade de numeros da sequencia fibonacci desejados:"))
  i=3
  print("/\  "*10)
  print("  \/"*10)
  print("1 -",a)
  print("2 -",b)
  for l in range(n-2):
    c = a + b
    a = b
    b = c
    print (i, "-", c)
    i=i+1
elif x == 3:
    print("/\  "*10)
    print("  \/"*10)
    print (a)
    print(b)
    for l in range(n):
     c = a + b
     a = b
     b = c
     print (c)
     n=n+1