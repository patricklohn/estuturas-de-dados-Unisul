Algoritmo "Devolução"

Var
// Seção de Declarações das variáveis
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
// Seção de Comandos, procedimento, funções, operadores, etc... 
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
Se resultMotivoUm = "True" Então
    EscrevaL("Pedido de devolução APROVADO")
Senão
     EscrevaL("Pedido devolução esta sendo recusado escreva o motivo:")
     Leia(resultMotivoUM)
     EscrevaL("Pedido de devolução RECUSADO motivo: ",resultMotivoUm)
FimSe

EscrevaL("O Numero pedido: ",numeroPedidoDois)
EscrevaL(" E o Numero da compra: ",numeroCompraDois)
EscrevaL(" Com motivo: ",descricaoSolicitacaoDois)
EscrevaL(" Escreva o resultado do departamento: True or False")
Leia(resultMotivoDois)
Se resultMotivoDois = "True" Então
    EscrevaL("Pedido de devolução APROVADO")
Senão
     EscrevaL("Pedido devolução esta sendo recusado escreva o motivo:")
     Leia(resultMotivoDois)
     EscrevaL("Pedido de devolução RECUSADO motivo: ",resultMotivoDois)
FimSe

Fimalgoritmo