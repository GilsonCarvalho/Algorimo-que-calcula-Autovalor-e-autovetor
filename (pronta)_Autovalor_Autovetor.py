# Autor - Gilson Carvalho Filho - Engenharia Civil UFAL - 21/09/2021
# Pra você conseguir rodar esse código você precisa instalar a biblioteca "numpy"
# O código foi feito para no máximo 7 iterações, mas ele pode ser facilmente alterado para suportar mais, caso necessário
# Atenção! divisão por zero, quebra o algorítimo

import numpy as np
l=int(input("Insira o número de linhas: "))
c=int(input("Insira o número de colunas: "))
a=np.zeros((l,c), dtype=int)
u=len(a)
for i in range(u):
	for j in range(len(a[i])):
		x=float(input("Insira o elemento [{}][{}]: ".format(i+1,j+1)))
		a[i][j]=x
e=float(input("Insira o erro: "))
print("Insira o número referênte ao método desejado: ")
print("[1] Método das potências.")
print("[2] Método das portências inversas.")
q=int(input())


#Método das potências

if (q==1):

#----------------------------------------------------------------------------------------------
#k=0
	print("k=0, passo 1ª")
	y0=np.ones((c,1))
	print("Yo= ")
	print(y0)
	z1=a.dot(y0)
	print("z1=A.Yo")
	print(z1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 2ª")
	lamb1=np.zeros((c,1))
	for i in range(0,len(z1)):
		if (y0[i]!=0):
			lamb1[i]=(z1[i])/(y0[i])
		else:
			lamb1[i]=0
	print("Lambda 1= ")
	print(lamb1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 3ª pulado")
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 4ª")
	z1modul=np.ones((len(z1),1))
	for i in range(len(z1)):
		z1modul[i]=((z1[i])**2)**(1/2)
	alfa1=z1modul.max()
	print("alfa1=max(z1) ")
	print(alfa1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 5ª")
	y1=np.ones((len(z1),1))
	for i in range(len(z1)):
		y1[i]=(z1[i])/(alfa1)
	print("y1=")
	print(y1)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=1

	print("k=1, passo 1ª")
	z2=a.dot(y1)
	print("z2=A.Y1")
	print(z2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 2ª")
	lamb2=np.zeros((c,1))
	for i in range(0,len(z2)):
		if (y1[i]!=0):
			lamb2[i]=(z2[i])/(y1[i])
		else:
			lamb2[i]=0
	print("Lambda 2= ")
	print(lamb2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 3ª")
	p=np.ones((len(z2),1))
	for i in range(len(z2)):
		p[i]=(lamb2[i]-lamb1[i])/(lamb2[i])
	pmod=np.ones((len(z2),1))
	for i in range(len(z2)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor máximo é {}".format(lamb2[pmod.argmin()]))
		print("Seu autovetor é y1: ")
		print(y1)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 4ª")
	z2modul=np.ones((len(z2),1))
	for i in range(len(z2)):
		z2modul[i]=((z2[i])**2)**(1/2)
	alfa2=z2modul.max()
	print("alfa2=max(z2) ")
	print(alfa2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 5ª")
	y2=np.ones((len(z2),1))
	for i in range(len(z2)):
		y2[i]=(z2[i])/(alfa2)
	print("y2=")
	print(y2)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=2

	print("k=2, passo 1ª")
	z3=a.dot(y2)
	print("z3=A.Y2")
	print(z3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 2ª")
	lamb3=np.zeros((c,1))
	for i in range(0,len(z3)):
		if (y2[i]!=0):
			lamb3[i]=(z3[i])/(y2[i])
		else:
			lamb3[i]=0
	print("Lambda 3= ")
	print(lamb3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 3ª")
	p=np.ones((len(z3),1))
	for i in range(len(z3)):
		p[i]=(lamb3[i]-lamb2[i])/(lamb3[i])
	pmod=np.ones((len(z3),1))
	for i in range(len(z3)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor é {}".format(lamb3[pmod.argmin()]))
		print("Seu autovetor é y2: ")
		print(y2)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 4ª")
	z3modul=np.ones((len(z3),1))
	for i in range(len(z3)):
		z3modul[i]=((z3[i])**2)**(1/2)
	alfa3=z3modul.max()
	print("alfa3=max(z3) ")
	print(alfa3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 5ª")
	y3=np.ones((len(z3),1))
	for i in range(len(z3)):
		y3[i]=(z3[i])/(alfa3)
	print("y3=")
	print(y3)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=3

	print("k=3, passo 1ª")
	z4=a.dot(y3)
	print("z4=A.Y3")
	print(z4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 2ª")
	lamb4=np.zeros((c,1))
	for i in range(0,len(z4)):
		if (y3[i]!=0):
			lamb4[i]=(z4[i])/(y3[i])
		else:
			lamb4[i]=0
	print("Lambda 4= ")
	print(lamb4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 3ª")
	p=np.ones((len(z4),1))
	for i in range(len(z4)):
		p[i]=(lamb4[i]-lamb3[i])/(lamb4[i])
	pmod=np.ones((len(z4),1))
	for i in range(len(z4)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor é {}".format(lamb4[pmod.argmin()]))
		print("Seu autovetor é y3: ")
		print(y3)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 4ª")
	z4modul=np.ones((len(z4),1))
	for i in range(len(z4)):
		z4modul[i]=((z4[i])**2)**(1/2)
	alfa4=z4modul.max()
	print("alfa4=max(z4) ")
	print(alfa4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 5ª")
	y4=np.ones((len(z4),1))
	for i in range(len(z4)):
		y4[i]=(z4[i])/(alfa4)
	print("y4=")
	print(y4)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=4

	print("k=4, passo 1ª")
	z5=a.dot(y4)
	print("z5=A.Y4")
	print(z5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 2ª")
	lamb5=np.zeros((c,1))
	for i in range(0,len(z5)):
		if (y4[i]!=0):
			lamb5[i]=(z5[i])/(y4[i])
		else:
			lamb5[i]=0
	print("Lambda 5= ")
	print(lamb5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 3ª")
	p=np.ones((len(z5),1))
	for i in range(len(z5)):
		p[i]=(lamb5[i]-lamb4[i])/(lamb5[i])
	pmod=np.ones((len(z5),1))
	for i in range(len(z5)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor é {}".format(lamb5[pmod.argmin()]))
		print("Seu autovetor é y4: ")
		print(y4)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 4ª")
	z5modul=np.ones((len(z5),1))
	for i in range(len(z5)):
		z5modul[i]=((z5[i])**2)**(1/2)
	alfa5=z5modul.max()
	print("alfa5=max(z5) ")
	print(alfa5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 5ª")
	y5=np.ones((len(z5),1))
	for i in range(len(z5)):
		y5[i]=(z5[i])/(alfa5)
	print("y5=")
	print(y5)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=5

	print("k=5, passo 1ª")
	z6=a.dot(y5)
	print("z6=A.Y5")
	print(z6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 2ª")
	lamb6=np.zeros((c,1))
	for i in range(0,len(z6)):
		if (y5[i]!=0):
			lamb6[i]=(z6[i])/(y5[i])
		else:
			lamb6[i]=0
	print("Lambda 6= ")
	print(lamb6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 3ª")
	p=np.ones((len(z6),1))
	for i in range(len(z6)):
		p[i]=(lamb6[i]-lamb5[i])/(lamb6[i])
	pmod=np.ones((len(z6),1))
	for i in range(len(z6)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor é {}".format(lamb6[pmod.argmin()]))
		print("Seu autovetor é y5: ")
		print(y5)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 4ª")
	z6modul=np.ones((len(z6),1))
	for i in range(len(z6)):
		z6modul[i]=((z6[i])**2)**(1/2)
	alfa6=z6modul.max()
	print("alfa6=max(z6) ")
	print(alfa6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 5ª")
	y6=np.ones((len(z6),1))
	for i in range(len(z6)):
		y6[i]=(z6[i])/(alfa6)
	print("y6=")
	print(y6)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=6

	print("k=6, passo 1ª")
	z7=a.dot(y6)
	print("z7=A.Y6")
	print(z7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 2ª")
	lamb7=np.zeros((c,1))
	for i in range(0,len(z7)):
		if (y6[i]!=0):
			lamb7[i]=(z7[i])/(y6[i])
		else:
			lamb7[i]=0
	print("Lambda 7= ")
	print(lamb7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 3ª")
	p=np.ones((len(z7),1))
	for i in range(len(z7)):
		p[i]=(lamb7[i]-lamb6[i])/(lamb7[i])
	pmod=np.ones((len(z7),1))
	for i in range(len(z7)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if(pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor é {}".format(lamb7[pmod.argmin()]))
		print("Seu autovetor é y6: ")
		print(y6)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 4ª")
	z7modul=np.ones((len(z7),1))
	for i in range(len(z7)):
		z7modul[i]=((z7[i])**2)**(1/2)
	alfa7=z7modul.max()
	print("alfa7=max(z7) ")
	print(alfa7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 5ª")
	y7=np.ones((len(z7),1))
	for i in range(len(z7)):
		y7[i]=(z7[i])/(alfa7)
	print("y7=")
	print(y7)
	print("------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------

#Método das potências inversas

if (q==2):

#k=0
	print("k=0, passo 1ª")
	y0=np.ones((c,1))
	print("Yo= ")
	print(y0)
	ainv=np.linalg.inv(a)
	z1=ainv.dot(y0)
	print("z1=Ainv.Yo")
	print(z1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 2ª")
	lamb1=np.zeros((c,1))
	for i in range(0,len(z1)):
		if (y0[i]!=0):
			lamb1[i]=(z1[i])/(y0[i])
		else:
			lamb1[i]=0
	print("Lambda 1= ")
	print(lamb1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 3ª pulado")
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 4ª")
	z1modul=np.ones((len(z1),1))
	for i in range(len(z1)):
		z1modul[i]=((z1[i])**2)**(1/2)
	alfa1=z1modul.max()
	print("alfa1=max(z1) ")
	print(alfa1)
	print("------------------------------------------------------------------------------------")
	print("k=0, passo 5ª")
	y1=np.ones((len(z1),1))
	for i in range(len(z1)):
		y1[i]=(z1[i])/(alfa1)
	print("y1=")
	print(y1)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=1

	print("k=1, passo 1ª")
	z2=ainv.dot(y1)
	print("z2=Ainv.Y1")
	print(z2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 2ª")
	lamb2=np.zeros((c,1))
	for i in range(0,len(z2)):
		if (y1[i]!=0):
			lamb2[i]=(z2[i])/(y1[i])
		else:
			lamb2[i]=0
	print("Lambda 2= ")
	print(lamb2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 3ª")
	p=np.ones((len(z2),1))
	for i in range(len(z2)):
		p[i]=(lamb2[i]-lamb1[i])/(lamb2[i])
	pmod=np.ones((len(z2),1))
	for i in range(len(z2)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb2[pmod.argmin()])**(-1)))
		print("Seu autovetor é y1: ")
		print(y1)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 4ª")
	z2modul=np.ones((len(z2),1))
	for i in range(len(z2)):
		z2modul[i]=((z2[i])**2)**(1/2)
	alfa2=z2modul.max()
	print("alfa2=max(z2) ")
	print(alfa2)
	print("------------------------------------------------------------------------------------")
	print("k=1, passo 5ª")
	y2=np.ones((len(z2),1))
	for i in range(len(z2)):
		y2[i]=(z2[i])/(alfa2)
	print("y2=")
	print(y2)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=2

	print("k=2, passo 1ª")
	z3=ainv.dot(y2)
	print("z3=Ainv.Y2")
	print(z3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 2ª")
	lamb3=np.zeros((c,1))
	for i in range(0,len(z3)):
		if (y2[i]!=0):
			lamb3[i]=(z3[i])/(y2[i])
		else:
			lamb3[i]=0
	print("Lambda 3= ")
	print(lamb3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 3ª")
	p=np.ones((len(z3),1))
	for i in range(len(z3)):
		p[i]=(lamb3[i]-lamb2[i])/(lamb3[i])
	pmod=np.ones((len(z3),1))
	for i in range(len(z3)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb3[pmod.argmin()])**(-1)))
		print("Seu autovetor é y2: ")
		print(y2)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 4ª")
	z3modul=np.ones((len(z3),1))
	for i in range(len(z3)):
		z3modul[i]=((z3[i])**2)**(1/2)
	alfa3=z3modul.max()
	print("alfa3=max(z3) ")
	print(alfa3)
	print("------------------------------------------------------------------------------------")
	print("k=2, passo 5ª")
	y3=np.ones((len(z3),1))
	for i in range(len(z3)):
		y3[i]=(z3[i])/(alfa3)
	print("y3=")
	print(y3)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=3

	print("k=3, passo 1ª")
	z4=ainv.dot(y3)
	print("z4=Ainv.Y3")
	print(z4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 2ª")
	lamb4=np.zeros((c,1))
	for i in range(0,len(z4)):
		if (y3[i]!=0):
			lamb4[i]=(z4[i])/(y3[i])
		else:
			lamb4[i]=0
	print("Lambda 4= ")
	print(lamb4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 3ª")
	p=np.ones((len(z4),1))
	for i in range(len(z4)):
		p[i]=(lamb4[i]-lamb3[i])/(lamb4[i])
	pmod=np.ones((len(z4),1))
	for i in range(len(z4)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb4[pmod.argmin()])**(-1)))
		print("Seu autovetor é y3: ")
		print(y3)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 4ª")
	z4modul=np.ones((len(z4),1))
	for i in range(len(z4)):
		z4modul[i]=((z4[i])**2)**(1/2)
	alfa4=z4modul.max()
	print("alfa4=max(z4) ")
	print(alfa4)
	print("------------------------------------------------------------------------------------")
	print("k=3, passo 5ª")
	y4=np.ones((len(z4),1))
	for i in range(len(z4)):
		y4[i]=(z4[i])/(alfa4)
	print("y4=")
	print(y4)
	print("------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------
#k=4

	print("k=4, passo 1ª")
	z5=ainv.dot(y4)
	print("z5=Ainv.Y4")
	print(z5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 2ª")
	lamb5=np.zeros((c,1))
	for i in range(0,len(z5)):
		if (y4[i]!=0):
			lamb5[i]=(z5[i])/(y4[i])
		else:
			lamb5[i]=0
	print("Lambda 5= ")
	print(lamb5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 3ª")
	p=np.ones((len(z5),1))
	for i in range(len(z5)):
		p[i]=(lamb5[i]-lamb4[i])/(lamb5[i])
	pmod=np.ones((len(z5),1))
	for i in range(len(z5)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb5[pmod.argmin()])**(-1)))
		print("Seu autovetor é y4: ")
		print(y4)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 4ª")
	z5modul=np.ones((len(z5),1))
	for i in range(len(z5)):
		z5modul[i]=((z5[i])**2)**(1/2)
	alfa5=z5modul.max()
	print("alfa5=max(z5) ")
	print(alfa5)
	print("------------------------------------------------------------------------------------")
	print("k=4, passo 5ª")
	y5=np.ones((len(z5),1))
	for i in range(len(z5)):
		y5[i]=(z5[i])/(alfa5)
	print("y5=")
	print(y5)

#----------------------------------------------------------------------------------------------
#k=5

	print("k=5, passo 1ª")
	z6=ainv.dot(y5)
	print("z6=Ainv.Y5")
	print(z6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 2ª")
	lamb6=np.zeros((c,1))
	for i in range(0,len(z6)):
		if (y5[i]!=0):
			lamb6[i]=(z6[i])/(y5[i])
		else:
			lamb6[i]=0
	print("Lambda 6= ")
	print(lamb6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 3ª")
	p=np.ones((len(z6),1))
	for i in range(len(z6)):
		p[i]=(lamb6[i]-lamb5[i])/(lamb6[i])
	pmod=np.ones((len(z6),1))
	for i in range(len(z6)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb6[pmod.argmin()])**(-1)))
		print("Seu autovetor é y5: ")
		print(y5)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 4ª")
	z6modul=np.ones((len(z6),1))
	for i in range(len(z6)):
		z6modul[i]=((z6[i])**2)**(1/2)
	alfa6=z6modul.max()
	print("alfa6=max(z6) ")
	print(alfa6)
	print("------------------------------------------------------------------------------------")
	print("k=5, passo 5ª")
	y6=np.ones((len(z6),1))
	for i in range(len(z6)):
		y6[i]=(z6[i])/(alfa6)
	print("y6=")
	print(y6)

#----------------------------------------------------------------------------------------------
#k=6

	print("k=6, passo 1ª")
	z7=ainv.dot(y6)
	print("z7=Ainv.Y6")
	print(z7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 2ª")
	lamb7=np.zeros((c,1))
	for i in range(0,len(z7)):
		if (y6[i]!=0):
			lamb7[i]=(z7[i])/(y6[i])
		else:
			lamb7[i]=0
	print("Lambda 7= ")
	print(lamb7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 3ª")
	p=np.ones((len(z7),1))
	for i in range(len(z7)):
		p[i]=(lamb7[i]-lamb6[i])/(lamb7[i])
	pmod=np.ones((len(z7),1))
	for i in range(len(z7)):
		pmod[i]=((p[i])**2)**(1/2)
	pmin=pmod.min()
	if (pmin<e):
		print("O problema acaba aqui!!!")
		print("O Autovalor mínimo é {}".format((lamb7[pmod.argmin()])**(-1)))
		print("Seu autovetor é y6: ")
		print(y6)
		quit()
	else:
		print("P= ")
		print(p)
		print("O valor mínimo de P em módulo é: ")
		print(pmod.min())
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 4ª")
	z7modul=np.ones((len(z7),1))
	for i in range(len(z7)):
		z7modul[i]=((z7[i])**2)**(1/2)
	alfa7=z7modul.max()
	print("alfa7=max(z7) ")
	print(alfa7)
	print("------------------------------------------------------------------------------------")
	print("k=6, passo 5ª")
	y7=np.ones((len(z7),1))
	for i in range(len(z7)):
		y7[i]=(z7[i])/(alfa7)
	print("y7=")
	print(y7)