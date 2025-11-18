# Sistema-de-Organizaçao-de-Eventos-e-Festas
Este projeto foi desenvolvido para a avaliação final de TOO e demonstra de forma organizada os Pilares da Programação Oriendada a Objetos.
É um sistema que consiste em organizar eventos e festas. Foram implementados o Factory Pattern, padrão adicional Singleton, UML de classes e aplicação dos pilares de POO.

Objetivo do Sistema
Permite gerenciar e organizar diferentes tipos de eventos e festas, incluindo:
Cadastro de eventos (Casamento, Festa Infantil, Evento Corporativo, entre outros);
Lista de convidados;
Lista de fornecedores;
Controle de tarefas;
Ordenação de tarefas utilizando Strategy;
Criação dos eventos utilizando Factory.

Pilares de POO
Abstração: A classe Evento é abstrata e representa o conceito geral de qualquer tipo de evento.
Encapsulamento: Atributos e comportamentos pertencem a classes específicas, mantendo a organização e proteção.
Herança: Está presente nas classes Casamento, FestaInfantil e EventoCorporativo.
Polimorfismo: Cada tipo de evento implementa o método descricao_tipo() de forma diferente.

Padrões de Projeto usados
Factory Pattern: O Factory Pattern é um padrão de projeto criacional usado quando queremos criar objetos sem expor diretamente a lógica de criação.
Usado para criar automaticamente o tipo correto de evento. Arquivo: Factory.py
Strategy: O Strategy Pattern é um padrão de projeto comportamental usado quando queremos trocar o comportamento de um método em tempo de execução, sem alterar o código da classe.
Usado para ordenar tarefas de diferentes formas. Arquivo: Strategy.py
Tipos de Strategy usados:
Ordenar por descrição
Ordenar por responsável
Ordenar por status (pendente/concluída, true/false)

Estrutura dos Arquivos
Convidado.py = Classe Convidado
Fornecedor.py = Classe Fornecedor
Tarefa.py = Classe Tarefa
Strategy.py = Strategy Pattern
Evento.py = Classe abstrata + subclasses
Factory.py = Factory Pattern
Main.py = Execução e testes

Como executar o Projeto
Certificar que todos os arquivos .py estão na pasta
Abra o terminar nessa pasta
Execute: phyton Main.py
A saída mostrará: Criação dos eventos, Adição de convidados, fornecedores e tarefas, Ordenação das tarefas com diferentes estratégias, Saída formatada e organizada.
