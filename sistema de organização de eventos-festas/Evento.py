from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date
from typing import List

from Convidado import Convidado
from Fornecedor import Fornecedor
from Tarefa import Tarefa
from Strategy import OrdenarPorDescricao


class Evento(ABC):
    _next_id = 1 #gera id automático

    def __init__(self, nome: str, data_evento: date, local: str):
        self._id = Evento._next_id
        Evento._next_id += 1

        self.nome = nome
        self.data_evento = data_evento
        self.local = local

        self.convidados: List[Convidado] = []
        self.fornecedores: List[Fornecedor] = []
        self.tarefas: List[Tarefa] = []

        self.ordenacao_strategy = OrdenarPorDescricao()

    @property #métodos em atributos
    def id(self):
        return self._id

    def adicionar_convidado(self, convidado: Convidado) -> None:
        self.convidados.append(convidado)

    def remover_convidado(self, nome: str) -> bool:
        for c in self.convidados:
            if c.nome == nome:
                self.convidados.remove(c)
                return True
        return False

    def confirmar_presenca(self, nome: str) -> bool:
        for c in self.convidados:
            if c.nome == nome:
                c.confirmar()
                return True
        return False

    def adicionar_fornecedor(self, fornecedor: Fornecedor) -> None:
        self.fornecedores.append(fornecedor)

    def adicionar_tarefa(self, tarefa: Tarefa) -> None:
        self.tarefas.append(tarefa)

    def tarefas_pendentes(self) -> List[Tarefa]:
        return [t for t in self.tarefas if not t.concluida]

    #strategy ordena
    def ordenar_tarefas(self) -> List[Tarefa]:
        return self.ordenacao_strategy.ordenar(self.tarefas)

    def set_ordenacao_strategy(self, strategy) -> None:
        self.ordenacao_strategy = strategy

    @abstractmethod
    def descricao_tipo(self) -> str:
        pass

    def resumo(self) -> str:
        return (
            f"Evento(id={self.id}, nome='{self.nome}', tipo='{self.descricao_tipo()}', "
            f"data={self.data_evento.isoformat()}, local='{self.local}', "
            f"convidados={len(self.convidados)}, fornecedores={len(self.fornecedores)}, "
            f"tarefas_pendentes={len(self.tarefas_pendentes())})"
        )

class Casamento(Evento):
    def descricao_tipo(self) -> str:
        return "Casamento"

class FestaInfantil(Evento):
    def descricao_tipo(self) -> str:
        return "Festa Infantil"

class EventoCorporativo(Evento):
    def descricao_tipo(self) -> str:
        return "Evento Corporativo"