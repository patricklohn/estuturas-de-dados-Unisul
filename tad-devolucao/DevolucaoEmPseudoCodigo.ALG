Algoritmo "Devolu��o"

Var
// Se��o de Declara��es das vari�veis
numeroPedidoUm: Inteiro;
numeroPedidoDois: Inteiro;
numeroCompraUm: Inteiro;
numeroCompraDois: Inteiro;
descricaoSolicitacaoUM: caracter;
resultDepartamentoUM: caracter;
resultMotivoUM: caracter;
descricaoSolicitacaoDois: caracter;
resultDepartamentoDois: caracter;
resultMotivoDois: caracter;


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
numeroPedidoUm <- 1456
numeroPedidoDois <- 1500
numeroCompraUm <- 50
numeroCompraDois <- 60
descricaoSolicitacaoUM <- "Devolvi pois estava quebrado!"
descricaoSolicitacaoDois <- "Devolvi pois estava usado!"

EscrevaL("O Numero pedido: ",numeroPedidoUm)
EscrevaL(" E o Numero da compra: ",numeroCompraUM)
EscrevaL(" Com motivo: ",descricaoSolicitacaoUm)
EscrevaL(" Escreva o resultado do departamento: True or False")
Leia(resultMotivoUM)
Se resultMotivoUm = "True" Ent�o
    EscrevaL("Pedido de devolu��o APROVADO")
Sen�o
     EscrevaL("Pedido devolu��o esta sendo recusado escreva o motivo:")
     Leia(resultMotivoUM)
     EscrevaL("Pedido de devolu��o RECUSADO motivo: ",resultMotivoUm)
FimSe

EscrevaL("O Numero pedido: ",numeroPedidoDois)
EscrevaL(" E o Numero da compra: ",numeroCompraDois)
EscrevaL(" Com motivo: ",descricaoSolicitacaoDois)
EscrevaL(" Escreva o resultado do departamento: True or False")
Leia(resultMotivoDois)
Se resultMotivoDois = "True" Ent�o
    EscrevaL("Pedido de devolu��o APROVADO")
Sen�o
     EscrevaL("Pedido devolu��o esta sendo recusado escreva o motivo:")
     Leia(resultMotivoDois)
     EscrevaL("Pedido de devolu��o RECUSADO motivo: ",resultMotivoDois)
FimSe

Fimalgoritmo