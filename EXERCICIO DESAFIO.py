#ENTRADA DE DADOS

slmin=float(input("Digite o salario: "))
turno=str(input("Digite o turno (M,V,N):"))
cargo=str(input("Digite o cargo (O,G): "))
horas=float(input("Digite o total de horas trabalhadas: "))

#1º OPERADOR RELACIONAL (VALIDAÇÃO DA ENTRADA DE DADOS)
if turno=="M":
    calc=slmin*10/100
elif turno=="V":
    calc=slmin*15/100
elif turno=="N":
    calc=slmin*12/100
else:
    print("Turno inválido")

#ATRIBUIÇÃO DE VARIAVEL
slbruto=calc*horas

#2ºOPERADOR RELACIONAL (IMPOSTO SOB O SLMIN E VALIDAÇÃO DA ENTRADA DE DADOS)

if cargo=="O":
    if slbruto>=300:
        imposto=slbruto*(5/100)
    else:
        imposto=slbruto*(3/100)
elif cargo=="G":
    if slbruto>=400:
        imposto=slbruto*(6/100)
    else:
        imposto=slbruto*(4/100)
else:
    print("Cargo inválido.")

#3ºOPERADOR RELACIONAL (GRATIFICAÇÃO)

if turno=="N" and horas>80:
    grat=50
else:
    grat=30

#4ºOPERADOR RELACIONAL (AUX ALIMENTAÇÃO)

if cargo=="O" and calc<=25:
    aux_alim=50
else:
    aux_alim=30

#2ªATRIBUIÇÃO DE VARIAVEL

sliquido=(slbruto-imposto)+aux_alim+grat

#5ºOPERADOR RELACIONAL (PRINT DE MENSAGEM)

if sliquido<350:
    print("Mal renumerado.")
elif sliquido>350 and sliquido<600:
    print("Normal.")
else:
    print("Bem remunerado.")

#PRINT DE TODOS OS DADOS

print ("O coeficiente é de: ", calc, ("reais"))
print("O salario bruto é de: ",slbruto, ("reais"))
print("O imposto sobre o salario bruto é de: ", imposto, ("reais"))
print("A gratificação é de: ", grat, ("reais"))
print("O Auxilio de alimentação é de: ", aux_alim, ("reais"))
print("O salario líquido é de: ", sliquido, ("reais"))
    
