class Funcionario:
    def __init__(self, nome, salario, idade, cpf):
        self.__nome = nome
        self.__salario = salario
        self.__idade = idade
        self.__cpf = cpf
    def pegar_nome(self):
        print(f"O nome do(a) funcionário(a) é: {self.__nome}")
    def pegar_salario(self):
        print(f"O salario do(a) funcionário(a) {self.__nome} é de : R$ {self.__salario}")
    def pegar_idade(self):
        print(f"A idade do(a) funcionário(a) é de {self.__idade}")
    def pegar_cpf(self):
        print(f"O cpf do(a) funcionário(a) {self.__nome} é: {self.__cpf}")
class Funcionario_comum(Funcionario):
    pass
class Gerente(Funcionario):
    pass 
    def __init__(self, nome, salario, idade, departamento, cpf):
        super().__init__(nome, salario, idade,  cpf)
        self.departamento = departamento

    def pegar_nome(self):
        print(f"O nome do(a) gerente é: {self._Funcionario__nome}")
    def pegar_salario(self):
        print(f"O salario do(a) gerente {self._Funcionario__nome} é de : R$ {self._Funcionario__salario}")
    def pegar_idade(self):
        print(f"A idade do(a) gerente é de {self._Funcionario__idade}")
    def pegar_dep(self):
        print(f"O departamento em que o (a) gerente trabalha é de {self._Funcionario__departamento}")
    def pegar_cpf(self):
        print(f"O cpf do(a) funcionário(a) {self._Funcionario__nome} é: {self._Funcionario__cpf}")
#Objetos:
func_01 = Funcionario_comum("Cláudio", 3500, 26, "4002-8922")
func_01.pegar_nome()
func_01.pegar_idade()
func_01.pegar_salario()
func_01.pegar_cpf()
#Obeto 02:
gerente_01 = Gerente("João", 10000, 35, "TI", "234-36346")
gerente_01.pegar_nome()
gerente_01.pegar_idade()
gerente_01.pegar_salario()
gerente_01.pegar_cpf()