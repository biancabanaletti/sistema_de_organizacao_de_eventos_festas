# Sistema-de-Organizaçao-de-Eventos-e-Festas
Este projeto foi desenvolvido para a avaliação final de TOO e demonstra de forma organizada os Pilares da Programação Oriendada a Objetos.
É um sistema que consiste em organizar eventos e festas. Foram implementados o Factory Pattern, padrão adicional Strategy, UML de classes e aplicação dos pilares de POO.

Objetivo do Sistema:

Permite gerenciar e organizar diferentes tipos de eventos e festas, incluindo:
Cadastro de eventos (Casamento, Festa Infantil, Evento Corporativo, entre outros);
Lista de convidados;
Lista de fornecedores;
Controle de tarefas;
Ordenação de tarefas utilizando Strategy;
Criação dos eventos utilizando Factory.

Descrição de cada classe:

Convidados: Representa uma pessoa convidada para o evento. Armazena o nome do convidado; Controla a presença confirmada (True/False); Permite confirmar presença; Define uma saída organizada quando impresso (repr).

Tarefa: Representa uma tarefa que deve ser realizada no evento. Descrição da tarefa; Responsável pela tarefa; Status de conclusão (True/False).

Fornecedor: Representa empresas ou prestadores contratados para o evento. Armazena: nome do fornecedor, tipo de serviço (buffet, decoração, etc) e custo estimado do serviço.

Evento: É a classe principal dos eventos. Armazena: nome do evento, data, local, lista de convidados, lista de tarefas e lista de fornecedores.
Possui métodos para: adicionar convidados, confirmar presença, adicionar tarefas e adicionar fornecedores.

Factory: Implementa o Factory no projeto. Cria eventos de: casamento, festa infantil e corporativo.

Strategy: Define ordenação para listas de tarefas. Ordenar por: descrição, responsável e status.

Main: Arquivo principal do sistema. É usado para executar o programa e demonstrar as funcionalidades.

Pilares de POO:

Abstração: A classe Evento é abstrata e representa o conceito geral de qualquer tipo de evento.

Encapsulamento: Atributos e comportamentos pertencem a classes específicas, mantendo a organização e proteção.

Herança: Está presente nas classes Casamento, FestaInfantil e EventoCorporativo.

Polimorfismo: Cada tipo de evento implementa o método descricao_tipo() de forma diferente.

Padrões de Projeto usados:
Factory Pattern: O Factory Pattern é um padrão de projeto criacional usado quando queremos criar objetos sem expor diretamente a lógica de criação.
Usado para criar automaticamente o tipo correto de evento. Arquivo: Factory.py

Strategy: O Strategy Pattern é um padrão de projeto comportamental usado quando queremos trocar o comportamento de um método em tempo de execução, sem alterar o código da classe.
Usado para ordenar tarefas de diferentes formas. Arquivo: Strategy.py

Tipos de Strategy usados:
Ordenar por descrição
Ordenar por responsável
Ordenar por status (pendente/concluída, true/false)

Estrutura dos Arquivos
Convidado.py = Classe Convidado.
Fornecedor.py = Classe Fornecedor.
Tarefa.py = Classe Tarefa.
Strategy.py = Strategy Pattern.
Evento.py = Classe abstrata + subclasses.
Factory.py = Factory Pattern.
Main.py = Execução e testes.

Como executar o Projeto:

Certificar que todos os arquivos.py estão na pasta

Abra o terminal na pasta do projeto (Main.py)

Execute: phyton Main.py

A saída mostrará: Criação dos eventos, Adição de convidados, fornecedores e tarefas, Ordenação das tarefas com diferentes estratégias, Saída formatada e organizada.

<img width="636" height="851" alt="image" src="https://github.com/user-attachments/assets/c748f3d2-2e4e-4e6a-9e4f-c1d989c9cd0a" />

Diagrama UML:

<img width="1039" height="708" alt="diagramaUML" src="https://github.com/user-attachments/assets/ce71ff5b-fb8e-4bab-b14c-f1892f5ba4ab" />
