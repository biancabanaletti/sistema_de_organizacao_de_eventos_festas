from datetime import date
from Evento import Casamento, FestaInfantil, EventoCorporativo, Evento

class EventoFactory: #factory responsável por criar diferentes tipos de eventos com string

    @staticmethod #decorador
    def criar_evento(tipo: str, nome: str, data_evento: date, local: str, **kwargs) -> Evento:
        tipo_formatado = tipo.strip().lower()

        if tipo_formatado in ("casamento", "wedding"):
            return Casamento(nome=nome, data_evento=data_evento, local=local, **kwargs)

        elif tipo_formatado in ("festa infantil", "festa_infantil", "infantil", "aniversario"):
            return FestaInfantil(nome=nome, data_evento=data_evento, local=local, **kwargs)

        elif tipo_formatado in ("corporativo", "evento corporativo", "empresa"):
            return EventoCorporativo(nome=nome, data_evento=data_evento, local=local, **kwargs)

        class EventoGenerico(Evento): #se o evento não existir cria um genérico/aleatório
            def descricao_tipo(self) -> str:
                return "Genérico"

        return EventoGenerico(nome=nome, data_evento=data_evento, local=local, **kwargs) #argumentos nomeados