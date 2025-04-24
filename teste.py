class folha_pagamento:
    def __init__(self):
        self.sb = float(input("Digite aqui seu salário bruto: "))
        self.sm = 1518
        self.vt = 206.8
        self.inss_valor = self.calcular_inss()
        self.fgts = self.sb * 0.08
        self.ferias = (self.sb+self.sb/3)/12
        self.decimo_terceiro = self.sb/12

    def calcular_inss(self):
        if self.sb <= 1518:
            return self.sb * 0.075
        elif self.sb <= 2793.88:
            return self.sb * 0.09
        elif self.sb <= 4190.83:
            return self.sb * 0.12
        elif self.sb <= 8157.41:
            return self.sb * 0.14
        else:
            return 828.39  # Valor fixo caso ultrapasse

    def inss(self):
        print(f"-INSS: R${self.inss_valor:.2f}")

    def resultado(self):
        salario_liquido = self.sb - self.inss_valor - self.vt - self.fgts - self.ferias - self.decimo_terceiro
        print(f"Salário bruto: R${self.sb:.2f}")
        print(f"INSS: {self.inss_valor}")
        print(f"Vale transporte: {self.vt}")
        print(f"FGTS: {self.fgts}")
        print(f"Férias 1/12: {self.ferias}")
        print(f"13º salário: {self.decimo_terceiro}")

        print(f"Total de descontos: R${self.inss_valor + self.vt + self.fgts + self.ferias + self.decimo_terceiro:.2f}")
        print(f"Seu salário líquido é: R${salario_liquido:.2f}")

folha = folha_pagamento()
folha.resultado()