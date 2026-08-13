def ativacao_degrau(z):
    if z >= 0:
        return 1
    return 0

# se o hóspede tem direito ou não de upgrade do tipo de quarto
def decidir_upgrade(x1, x2): 
    w1 = 0.8 #peso para os dias hospedados
    w2 = 0.3 #peso para o gasto total
    bias = -7.0 #Resistência natural para conceder o upgrade

    #Cálculo linear (z)
    z = (x1 * w1) + (x2 * w2) + bias

    #Aplicação da ativação
    decisao = ativacao_degrau(z)
    return decisao

#Validacao com cenários de teste
print("Hospede com dias=8, gasto=7: ", decidir_upgrade(8,7)) #Esperado 1
print("Hospede com dias=4, gasto=3: ", decidir_upgrade(4,3)) #Esperado 0
