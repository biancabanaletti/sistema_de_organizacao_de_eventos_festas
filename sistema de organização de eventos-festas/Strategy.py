from abc import ABC, abstractmethod
from typing import List

from Tarefa import Tarefa

class OrdenacaoStrategy(ABC): #usado para diferentes formas de organizar tarefas

    @abstractmethod #biblioteca abc
    def ordenar(self, tarefas: List[Tarefa]) -> List[Tarefa]:
        pass

class OrdenarPorDescricao(OrdenacaoStrategy): #ordena por descrição em ordem alfabética
    def ordenar(self, tarefas: List[Tarefa]) -> List[Tarefa]:
        return sorted(tarefas, key=lambda t: t.descricao.lower())

class OrdenarPorResponsavel(OrdenacaoStrategy): #ordena pelo nome do responsável
    def ordenar(self, tarefas: List[Tarefa]) -> List[Tarefa]:
        return sorted(tarefas, key=lambda t: (t.responsavel or "zzz").lower())

class OrdenarPorStatus(OrdenacaoStrategy): #ordena por pendentes e concluídas
    def ordenar(self, tarefas: List[Tarefa]) -> List[Tarefa]:
        return sorted(tarefas, key=lambda t: t.concluida)
    