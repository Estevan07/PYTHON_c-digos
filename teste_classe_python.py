class Aluno:
    def __init__(self, altura, estilo, cabelo,escola):
        self.altura= altura
        self.diametro= diametro
        self.cabelo= cabelo
        self.escola=escola
    def escola_passada(self,lista_escolas):
        if self.escola in lista_escolas:
            print("novidade")
        else:
            print("diferente")

operacoes=True
lista_escolas=["sao carlos", "sao jose", "ribeirao preto"]
while (operacoes):
    resposta=str(input("realizar o cadastro de novo aluno? "))
    if resposta == "yes":
        altura=int(input("altura: "))
        diametro=int(int(input("diametro: ")))
        cabelo=str(input("cabelo: "))
        escola_passada=str(input("escola passada: "))
    else:
        operacoes=False


aluno = Aluno (altura, diametro,cabelo,escola_passada)
print(aluno.altura)   
print(aluno.diametro)
print(aluno.cabelo)

aluno.escola_passada(lista_escolas)