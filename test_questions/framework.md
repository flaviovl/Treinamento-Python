Bibliotecas Python – Perguntas de entrevista em Python

1. Explique o que é o Flask e seus benefícios?

     Resposta:  Flask é um microframework web para Python baseado na licença BSD “Werkzeug, Jinja2 e boas intenções”. Werkzeug e Jinja2 são duas de suas dependências. Isso significa que terá pouca ou nenhuma dependência de bibliotecas externas. Isso torna a estrutura leve enquanto há uma pequena dependência para atualização e menos bugs de segurança.

     Uma sessão basicamente permite que você se lembre de informações de uma solicitação para outra. Em um frasco, uma sessão usa um cookie assinado para que o usuário possa ver o conteúdo da sessão e modificá-lo. O usuário pode modificar a sessão apenas se tiver a chave secreta Flask.secret_key.

2. Django é melhor que Flask?
     Django e Flask mapeiam as URLs ou endereços digitados nos navegadores da web para funções em Python. 

     O Flask é muito mais simples comparado ao Django, mas o Flask não faz muito por você, o que significa que você precisará especificar os detalhes, enquanto o Django faz muito por você, onde você não precisaria fazer muito trabalho. O Django consiste em código pré-escrito, que o usuário precisará analisar, enquanto o Flask permite que os usuários criem seu próprio código, portanto, simplificando o entendimento do código. Tecnicamente, ambos são igualmente bons e ambos contêm seus próprios prós e contras.

3. Mencione as diferenças entre Django, Pyramid e Flask.

     Flask é um “microframework” construído principalmente para um pequeno aplicativo com requisitos mais simples. No frasco, você precisa usar bibliotecas externas. O frasco está pronto para uso.
     Pyramid é construído para aplicações maiores. Ele fornece flexibilidade e permite que o desenvolvedor use as ferramentas certas para seu projeto. O desenvolvedor pode escolher o banco de dados, estrutura de URL, estilo de modelagem e muito mais. A pirâmide é configurável pesada.
     O Django também pode ser usado para aplicativos maiores, como o Pyramid. Inclui um ORM.
     Q87 . Discuta a arquitetura do Django.
     Resposta:  Django MVT Padrão:

     Django Architecture - Perguntas da entrevista em Python - EdurekaFigura:  Perguntas da entrevista em Python – Arquitetura do Django 

     O desenvolvedor fornece o Model, a view e o template, então apenas mapeia para uma URL e o Django faz a mágica para servir ao usuário.

4. Explique como você pode configurar o banco de dados no Django.
     Você pode usar o comando edit mysite/setting.py, é um módulo python normal com nível de módulo representando as configurações do Django.

O Django usa SQLite por padrão; é fácil para os usuários do Django, pois não exigirá nenhum outro tipo de instalação. No caso de sua escolha de banco de dados ser diferente das seguintes chaves no item 'padrão' DATABASE para corresponder às configurações de conexão do banco de dados.

Engines : você pode alterar o banco de dados usando 'django.db.backends.sqlite3' , 'django.db.backeneds.mysql', 'django.db.backends.postgresql_psycopg2', 'django.db.backends.oracle' e assim em
Nome : O nome do seu banco de dados. No caso se você estiver usando SQLite como seu banco de dados, nesse caso, banco de dados será um arquivo em seu computador, Nome deve ser um caminho absoluto completo, incluindo o nome do arquivo desse arquivo.
Se você não estiver escolhendo SQLite como seu banco de dados, então configurações como Senha, Host, Usuário, etc. devem ser adicionadas.
O Django usa SQLite como banco de dados padrão, ele armazena dados como um único arquivo no sistema de arquivos. Se você tem um servidor de banco de dados – PostgreSQL, MySQL, Oracle, MSSQL – e quer usá-lo ao invés do SQLite, então use as ferramentas de administração do seu banco de dados para criar um novo banco de dados para seu projeto Django. De qualquer forma, com seu banco de dados (vazio) no lugar, tudo o que resta é dizer ao Django como usá-lo. É aqui que entra o arquivo settings.py do seu projeto.

Adicionaremos as seguintes linhas de código ao arquivo setting.py :

DATABASES = {
     'default': {
          'ENGINE' : 'django.db.backends.sqlite3',
          'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}

5. Dê um exemplo de como você pode escrever uma VIEW no Django?
     Resposta:  É assim que podemos usar escrever uma visão no Django:

     from django.http import HttpResponse
     import datetime
     
     def Current_datetime(request):
          now = datetime.datetime.now()
          html = "It is now %s/body/html % now
          return HttpResponse(html)
     Retorna a data e hora atuais, como um documento HTML

6. Mencione em que consistem os templates do Django.
     Resp:  O modelo é um arquivo de texto simples. Ele pode criar qualquer formato baseado em texto como XML, CSV, HTML, etc. Um template contém variáveis ​​que são substituídas por valores quando o template é avaliado e tags (% tag %) que controlam a lógica do template.

     Django Template - Perguntas de entrevista em Python - EdurekaFigura:  Perguntas da entrevista em Python – Modelo Django

7. Explicar o uso de sessão no framework Django?
     Resposta: O  Django fornece uma sessão que permite armazenar e recuperar dados por visitante do site. O Django abstrai o processo de envio e recebimento de cookies, colocando um cookie de ID de sessão no lado do cliente e armazenando todos os dados relacionados no lado do servidor.

     Django Framework - Perguntas de entrevista em Python - EdurekaFigura: Perguntas da entrevista em Python – Django Framework

     Portanto, os dados em si não são armazenados no lado do cliente. Isso é bom do ponto de vista da segurança.

8.  Liste os estilos de herança no Django.

     Resposta:  No Django, existem três estilos de herança possíveis:

     Classes básicas abstratas: Este estilo é usado quando você deseja que a classe pai contenha apenas informações que você não deseja digitar para cada modelo filho.
     Herança de várias tabelas: Este estilo é usado se você estiver subclassificando um modelo existente e precisar que cada modelo tenha sua própria tabela de banco de dados.
     Modelos de proxy: Você pode usar este modelo, se quiser apenas modificar o comportamento do modelo no nível Python, sem alterar os campos do modelo.
     A seguir, neste blog de perguntas de entrevista em Python, vamos dar uma olhada nas perguntas relacionadas ao Web Scraping