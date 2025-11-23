class Convidado:

    def __init__(self, nome: str, email: str | None = None): #convidado que possiu nome email e controle de presença
        self.nome = nome
        self.email = email
        self.presenca_confirmada = False

    def confirmar(self) -> None: #confirma a presença do convidado
        self.presenca_confirmada = True

    def cancelar_confirmacao(self) -> None: #cancela a presença confirmada
        self.presenca_confirmada = False

    def __repr__(self) -> str:
        return f"Convidado(nome='{self.nome}', email='{self.email}', confirmado={self.presenca_confirmada})"
    
    def __repr__(self):
        return f"{self.nome} (presença: {self.presenca_confirmada})"
