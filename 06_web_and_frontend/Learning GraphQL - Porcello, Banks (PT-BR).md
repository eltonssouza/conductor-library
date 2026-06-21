# Aprendendo GraphQL
### Busca Declarativa de Dados para Aplicações Web Modernas
**Eve Porcello e Alex Banks**

> **Tradução em português (PT-BR).** O arquivo original em inglês está em `Learning GraphQL - Porcello, Banks.md`, na mesma pasta. Tradução em andamento — esta é a primeira parcela.

*Learning GraphQL, de Eve Porcello e Alex Banks. Copyright © 2018 Moon Highway, LLC. Publicado por O'Reilly Media, Inc. ISBN 978-1-492-03071-3. Primeira edição, agosto de 2018.*

---

## Prefácio

### Agradecimentos

Este livro não seria um livro sem a ajuda de muitas pessoas excepcionais. Tudo começou com a ideia de Ally MacDonald, nossa editora em *Learning React*, que nos incentivou a escrever *Learning GraphQL*. Tivemos então muita sorte de trabalhar com Alicia Young, que conduziu o livro até a impressão. Obrigado a Justin Billing, Melanie Yarbrough e Chris Edwards, que apararam todas as arestas durante uma edição de produção extremamente minuciosa. Ao longo do processo, tivemos a sorte de receber feedback de Peggy Rayzis e Sashko Stubailo, da equipe da Apollo, que compartilharam suas percepções e dicas valiosas sobre os recursos mais recentes. Obrigado também a Adam Rackis, Garrett McCullough e Shivi Singh, que foram excelentes editores técnicos. Escrevemos este livro sobre GraphQL porque amamos GraphQL. Achamos que você também vai amar.

### Convenções Usadas neste Livro

As seguintes convenções tipográficas são usadas neste livro: *Itálico* indica termos novos, URLs, endereços de email, nomes de arquivos e extensões de arquivos. `Largura constante` é usada para listagens de programas, bem como dentro de parágrafos para se referir a elementos de programa como nomes de variáveis ou funções, bancos de dados, tipos de dados, variáveis de ambiente, instruções e palavras-chave. **`Largura constante em negrito`** mostra comandos ou outro texto que deve ser digitado literalmente pelo usuário. *`Largura constante em itálico`* mostra texto que deve ser substituído por valores fornecidos pelo usuário ou determinados pelo contexto.

**DICA** — Este elemento indica uma dica ou sugestão.

**NOTA** — Este elemento indica uma observação geral.

**AVISO** — Este elemento indica um alerta ou advertência.

---

## Capítulo 1. Bem-vindo ao GraphQL

Antes de a Rainha da Inglaterra o nomear cavaleiro, Tim Berners-Lee era programador. Ele trabalhava no CERN, o laboratório europeu de física de partículas na Suíça, e estava cercado por um grande número de pesquisadores talentosos. Berners-Lee queria ajudar seus colegas a compartilhar ideias, então decidiu criar uma rede na qual os cientistas pudessem publicar e atualizar informações. O projeto acabou se tornando o primeiro servidor web e o primeiro cliente web, e o navegador "WorldWideWeb" (mais tarde renomeado para "Nexus") foi lançado no CERN em dezembro de 1990.

Com seu projeto, Berners-Lee tornou possível que pesquisadores visualizassem e atualizassem conteúdo web em seus próprios computadores. "WorldWideWeb" era HTML, URLs, um navegador e uma interface WYSIWYG na qual atualizar o conteúdo.

Hoje, a internet não é apenas HTML em um navegador. A internet são notebooks. São relógios de pulso. São smartphones. É um chip de identificação por radiofrequência (RFID) no seu passe de teleférico. É um robô que dá petiscos ao seu gato enquanto você está fora da cidade.

Os clientes são mais numerosos hoje, mas ainda buscamos fazer a mesma coisa: carregar dados em algum lugar o mais rápido possível. Precisamos que nossas aplicações tenham bom desempenho porque nossos usuários nos cobram um padrão elevado. Eles esperam que nossos apps funcionem bem sob qualquer condição: de 2G em celulares básicos até internet de fibra ultrarrápida em desktops de tela grande. Apps rápidos facilitam que mais pessoas interajam com o nosso conteúdo. Apps rápidos deixam nossos usuários felizes. E, sim, apps rápidos nos dão dinheiro.

Levar dados de um servidor ao cliente de forma rápida e previsível é a história da web — passado, presente e futuro. Embora este livro recorra frequentemente ao passado para dar contexto, estamos aqui para falar de soluções modernas. Estamos aqui para falar do futuro. Estamos aqui para falar de GraphQL.

### O que é GraphQL?

GraphQL é uma linguagem de consulta para suas APIs. É também um runtime para atender consultas com seus dados. O serviço GraphQL é agnóstico em relação ao transporte, mas normalmente é servido por HTTP. Para demonstrar uma consulta GraphQL e sua resposta, vamos dar uma olhada na SWAPI, a API de Star Wars. A SWAPI é uma API REST (Representational State Transfer) que foi encapsulada com GraphQL. Podemos usá-la para enviar consultas e receber dados. Uma consulta GraphQL pede apenas os dados de que precisa.

Sempre que uma consulta é executada contra um servidor GraphQL, ela é validada contra um sistema de tipos. Todo serviço GraphQL define tipos em um schema GraphQL. Você pode pensar em um sistema de tipos como uma planta (blueprint) dos dados da sua API, sustentada por uma lista de objetos que você define. Por exemplo, a consulta de pessoa mostrada antes é sustentada por um objeto `Person`:

```graphql
type Person {
  id: ID!
  name: String
  birthYear: String
  eyeColor: String
  gender: String
  hairColor: String
  height: Int
  mass: Float
  skinColor: String
  homeworld: Planet
  species: Species
  filmConnection: PersonFilmsConnection
  starshipConnection: PersonStarshipConnection
  vehicleConnection: PersonVehiclesConnection
  created: String
  edited: String
}
```

O tipo `Person` define todos os campos, junto com seus tipos, que estão disponíveis para consulta sobre a Princesa Leia. No Capítulo 3, nos aprofundamos no schema e no sistema de tipos do GraphQL.

GraphQL é frequentemente chamado de linguagem de busca de dados declarativa. Com isso, queremos dizer que os desenvolvedores listam seus requisitos de dados como *quais* dados precisam, sem se concentrar em *como* vão obtê-los. Existem bibliotecas de servidor GraphQL em diversas linguagens, incluindo C#, Clojure, Elixir, Erlang, Go, Groovy, Java, JavaScript, .NET, PHP, Python, Scala e Ruby. Neste livro, focamos em como construir serviços GraphQL com JavaScript. Todas as técnicas que discutimos ao longo deste livro são aplicáveis ao GraphQL em qualquer linguagem.

### A Especificação do GraphQL

GraphQL é uma especificação (spec) para comunicação cliente-servidor. O que é uma spec? Uma spec descreve as capacidades e características de uma linguagem. Nos beneficiamos das especificações de linguagem porque elas fornecem um vocabulário comum e boas práticas para o uso da linguagem pela comunidade.

Um exemplo bastante notável de spec de software é a spec do ECMAScript. De tempos em tempos, um grupo de representantes de empresas de navegadores, empresas de tecnologia e da comunidade em geral se reúne e define o que deve ser incluído (e deixado de fora) da spec do ECMAScript. O mesmo vale para o GraphQL. Um grupo de pessoas se reuniu e escreveu o que deveria ser incluído (e deixado de fora) da linguagem. Isso serve como diretriz para todas as implementações do GraphQL.

Quando a spec foi lançada, os criadores do GraphQL também compartilharam uma implementação de referência de um servidor GraphQL em JavaScript — `graphql.js`. Ela é útil como modelo, mas o objetivo dessa implementação de referência não é determinar qual linguagem você usa para implementar seu serviço. É apenas um guia. Depois de compreender a linguagem de consulta e o sistema de tipos, você pode construir seu servidor em qualquer linguagem que quiser.

### Princípios de Design do GraphQL

Embora o GraphQL não seja controlador quanto a como você constrói sua API, ele oferece algumas diretrizes sobre como pensar em um serviço:

- **Hierárquico** — Uma consulta GraphQL é hierárquica. Campos são aninhados dentro de outros campos e a consulta tem o formato dos dados que retorna.
- **Centrado no produto** — O GraphQL é guiado pelas necessidades de dados do cliente e pela linguagem e runtime que dão suporte ao cliente.
- **Tipagem forte** — Um servidor GraphQL é sustentado pelo sistema de tipos do GraphQL. No schema, cada ponto de dado tem um tipo específico contra o qual será validado.
- **Consultas especificadas pelo cliente** — Um servidor GraphQL fornece as capacidades que os clientes têm permissão de consumir.
- **Introspectivo** — A linguagem GraphQL é capaz de consultar o sistema de tipos do servidor GraphQL.

### Origens do GraphQL

Em 2012, o Facebook decidiu que precisava reconstruir os aplicativos móveis nativos da aplicação. Os apps iOS e Android da empresa eram apenas invólucros finos em torno das telas do site móvel. O Facebook tinha um servidor RESTful e tabelas de dados FQL (a versão de SQL do Facebook). O desempenho estava ruim e os apps travavam com frequência. Naquele momento, os engenheiros perceberam que precisavam melhorar a forma como os dados estavam sendo enviados às suas aplicações cliente.

A equipe de Lee Byron, Nick Schrock e Dan Schafer decidiu repensar seus dados a partir do lado do cliente. Eles se propuseram a construir o GraphQL, uma linguagem de consulta que descreveria as capacidades e os requisitos dos modelos de dados para as aplicações cliente/servidor da empresa. Em julho de 2015, a equipe lançou sua especificação inicial do GraphQL e uma implementação de referência do GraphQL em JavaScript chamada `graphql.js`. Em setembro de 2016, o GraphQL deixou seu estágio de "prévia técnica". Isso significava que o GraphQL estava oficialmente pronto para produção, embora já viesse sendo usado havia anos em produção no Facebook. Hoje, o GraphQL alimenta quase toda a busca de dados do Facebook e é usado em produção por IBM, Intuit, Airbnb e outras.

### História do Transporte de Dados

O GraphQL apresenta algumas ideias muito novas, mas todas devem ser compreendidas em um contexto histórico de transporte de dados. Quando pensamos em transporte de dados, estamos tentando entender como passar dados de um lado para o outro entre computadores. Solicitamos alguns dados de um sistema remoto e esperamos uma resposta.

**Chamada de Procedimento Remoto (RPC)** — Na década de 1960, a chamada de procedimento remoto (RPC) foi inventada. Uma RPC era iniciada pelo cliente, que enviava uma mensagem de requisição a um computador remoto para fazer algo. O computador remoto enviava uma resposta ao cliente. Esses computadores eram diferentes dos clientes e servidores que usamos hoje, mas o fluxo de informação era basicamente o mesmo: solicitar dados a partir do cliente, obter uma resposta do servidor.

**Protocolo Simples de Acesso a Objetos (SOAP)** — No fim da década de 1990, o SOAP surgiu na Microsoft. O SOAP usava XML para codificar uma mensagem e HTTP como transporte. O SOAP também usava um sistema de tipos e introduziu o conceito de chamadas orientadas a recursos para dados. O SOAP oferecia resultados razoavelmente previsíveis, mas causava frustração porque suas implementações eram bastante complicadas.

**REST** — O paradigma de API com o qual você provavelmente está mais familiarizado hoje é o REST. O REST foi definido em 2000 na tese de doutorado de Roy Fielding na Universidade da Califórnia–Irvine. Ele descreveu uma arquitetura orientada a recursos na qual os usuários progridem pelos recursos web realizando operações como GET, PUT, POST e DELETE. A rede de recursos pode ser pensada como uma máquina de estados virtual, e as ações (GET, PUT, POST, DELETE) são mudanças de estado dentro da máquina.

O REST nos permite criar um modelo de dados com uma variedade de endpoints, uma abordagem muito mais simples do que as arquiteturas anteriores. Ele forneceu uma nova maneira de lidar com dados na web cada vez mais complexa, mas não impôs um formato específico de resposta de dados. Inicialmente, o REST era usado com XML. Logo depois, a JavaScript Object Notation (JSON) foi desenvolvida e padronizada por Douglas Crockford. O JSON é agnóstico em relação à linguagem e fornece um formato de dados elegante que muitas linguagens diferentes conseguem analisar e consumir.

---

> ⏳ **Continuação pendente** — A tradução segue a partir de "REST Drawbacks" (Desvantagens do REST). A próxima parcela continuará deste ponto.
