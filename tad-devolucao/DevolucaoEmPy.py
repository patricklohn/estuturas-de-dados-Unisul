numeroPedidoUm = 1456
numeroPedidoDois = 1500
numeroCompraUm = 50
numeroCompraDois = 60
descricaoSolicitacaoUM = "Devolvi pois estava quebrado!"
descricaoSolicitacaoDois = "Devolvi pois estava usado!"

print("O Numero pedido: ", numeroPedidoUm)
print(" E o Numero da compra: ", numeroCompraUm)  
print(" Com motivo: ", descricaoSolicitacaoUM)
print(" Escreva o resultado do departamento: True or False")

resultDepartamentoUM = input()   

if resultDepartamentoUM == "True":
    print("Pedido de devolução APROVADO")
else:
    print("Pedido de devolução está sendo recusado, escreva o motivo:")
    resultMotivoUM = input()
    print("Pedido de devolução RECUSADO motivo: ", resultMotivoUM)

print("O Numero pedido: ", numeroPedidoDois)
print(" E o Numero da compra: ", numeroCompraDois)  
print(" Com motivo: ", descricaoSolicitacaoDois)
print(" Escreva o resultado do departamento: True or False")

resultDepartamentoDois = input()   

if resultDepartamentoDois == "True":
    print("Pedido de devolução APROVADO")
else:
    print("Pedido de devolução está sendo recusado, escreva o motivo:")
    resultMotivoDois = input()
    print("Pedido de devolução RECUSADO motivo: ", resultMotivoDois)