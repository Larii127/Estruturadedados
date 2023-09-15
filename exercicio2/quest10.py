class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


    def aumentar_salario(self, porcentagem):
        aumentar = self.salario * porcentagem
        novoSalario = aumentar + self.salario
        return novoSalario

funcionario1 = Funcionario('Amanda', 1200, 'Rh')
result = funcionario1.aumentar_salario(0.05)
print(result)