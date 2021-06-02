# ateliware_challenge
Desafio técnico para desenvolvedores em repositório público[5]!

Esse desafio proporcionou a oportunidade de trabalhar com a API do GitHub em Python!

A aplicação é capaz de procurar repositórios escolhidos pelo usuário em uma entrada de texto do tipo 'input tags' que contém até 51 linguagens (O desafio propunha apenas 5)! E por meio de um botão[1] a lógica back-end atua para cadastrar novos repositórios ou atulizar os já cadastrados [6] em um banco instanciado em postGreSQL [7] e retorna um novo por linguagem. 

O sort é feito com base no maior número de estrelas por repositório, o front-end em HTML e JS recebe por meio de jinjas os dados do back-end e os estrutura em dois datatables, o primeiro com os repositórios encontrados pela busca e o segundo com todos os repositórios já pesquisados listados[2], contendo diversos detalhes específicos[3]. Sob o nome de cada repositório há um hiperlink direcionando à sua respectiva página no GitHub e os datatables são atualizados na tela sem que seja necessário redirecionar para novas páginas, utilizando requisições assíncronas de JS (AJAX). 

Afim de garantir que tudo isso funcione sem que o desenvolvedor tenha que testar os pontos chave, em tests.py existem testes automatizados[9]!

Instruções de Deploy [11] na AWS[8]:



Requisitos propostos pela Ateliware:

[1] Botão para buscar e armazenar os repositórios destaques de 5 linguagens à sua escolha;
[2] Listar os repositórios encontrados;
[3] Visualizar os detalhes de cada repositório.
[4] Deve ser uma aplicação totalmente nova;
[5] A solução deve estar em um repositório público do GitHub;
[6] A aplicação deve armazenar as informações encontradas;
[7] Utilizar PostgreSQL, MySQL ou SQL Server;
[8] O deploy deve ser realizado, preferencialmente, no Heroku, AWS ou no Azure;
[9] A aplicação precisa ter testes automatizados;
[10] Preferenciamente dockerizar a aplicação; -- X
[11] Por favor atualizar o readme da aplicação com passo a passo com instrução para subir o ambiente.
