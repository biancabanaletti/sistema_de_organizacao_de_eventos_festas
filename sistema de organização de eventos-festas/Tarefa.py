class Tarefa:

    def __init__(self, descricao: str, responsavel: str | None = None): #tarefa do evento com descrição o responsável pelo evento e conclusão (se foi feito ou não)
        self.descricao = descricao
        self.responsavel = responsavel
        self.concluida = False

    def concluir(self) -> None: #marca como concluída
        self.concluida = True

    def reabrir(self) -> None:
        self.concluida = False

    def __repr__(self):
        return (
            f"tarefa: {self.descricao}. "
            f"responsável: {self.responsavel}. "
            f"concluída? {self.concluida}")