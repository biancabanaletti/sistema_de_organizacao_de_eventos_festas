class Fornecedor:

    def __init__(self, nome: str, tipo: str, custo_estimado: float):
        self.nome = nome
        self.tipo = tipo
        self.custo_estimado = custo_estimado

    def __repr__(self): #apresentação clara do objeto
        return f"{self.nome} — {self.tipo}, valor: R${self.custo_estimado:.2f}"