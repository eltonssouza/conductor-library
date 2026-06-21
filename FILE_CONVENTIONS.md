# Convenções de Arquivos e Pastas / File & Folder Conventions

> Este documento explica o padrão de organização, **nomenclatura** e **formatação interna** dos arquivos `.md` da pasta `to-brain`. Serve de guia para manter a consistência ao adicionar novos arquivos.
>
> This document explains the organization, **naming** and **internal formatting** standard of the `.md` files in the `to-brain` folder. Use it as a guide to keep things consistent when adding new files.

---

## 1. Estrutura geral

A pasta é dividida em dois grandes blocos, separados por um prefixo numérico de dois dígitos no nome de cada subpasta:

```
to-brain/
├── 00_academic_curriculum/      ← bloco ACADÊMICO (listas de leitura bilíngues)
├── 01_languages_and_fundamentals/ ┐
├── 02_algorithms_and_data_structures/  │
├── 03_design_and_architecture/     │
├── 04_engineering_and_practices/    │
├── 05_databases/          │  bloco PROFISSIONAL
├── 06_web_and_frontend/           │  (livros completos por tema)
├── 07_devops_sre_operations/     │
├── 08_distributed_systems/    │
├── 09_security_and_privacy/  │
├── 10_ai_and_llm/                 │
├── 11_management_product_process/  │
├── 12_design_ux/                ┘
├── README.md                    ← índice navegável de todo o acervo
├── FILE_CONVENTIONS.md    ← este arquivo
├── ROLES_AND_ACRONYMS.md       ← glossário de cargos
└── AGENTS_AND_SKILLS_BY_ROLE.md ← prompts de Agent + Skill por cargo
```

**Regra do prefixo `NN_`:** toda subpasta começa com dois dígitos seguidos de `_`. O número define a ordem de exibição. O bloco acadêmico ocupa o `00_`; os blocos profissionais vão de `01_` a `12_`, agrupados por tema (na ordem aproximada de uma formação em Engenharia da Computação: linguagens → algoritmos → design → engenharia → dados → web → operações → segurança → IA → gestão → design).

**Nome das pastas:** `NN_palavras_separadas_por_underscore`, em português, minúsculas, sem acento e sem espaços.

---

## 2. Pasta `00_academic_curriculum/` — arquivos BILÍNGUES

São listas de leitura por disciplina (de um currículo de Ciência/Engenharia da Computação). **Cada arquivo contém os dois idiomas no mesmo documento.**

### Nomenclatura
```
NN_slug_em_ingles.md
```
- `NN` = número da disciplina no currículo (mantém a numeração original; por isso há saltos, ex.: 01, 02, 03, 05, … 34).
- `slug_em_ingles` = identificador curto em inglês, minúsculas, com underscore (ex.: `digital_circuits`, `theory_of_computation`).

Exemplos: `01_digital_circuits.md`, `18_database.md`, `31_theory_of_computation.md`.

### Estrutura interna (formato bilíngue)
```markdown
# NN — Título em Português / English Title

> **Arquivo bilíngue (PT-BR / EN)** — lista de leitura da disciplina.
> **Bilingual file (PT-BR / EN)** — course reading list.

---

## 🇧🇷 Português — Título em Português

<conteúdo completo em português>

---

## 🇺🇸 English — English Title

<full content in English>
```

Regras:
- O **H1** traz o número + título nos dois idiomas, separados por ` / `.
- Duas seções **H2**, uma por idioma, marcadas com a bandeira (`🇧🇷` / `🇺🇸`), separadas por `---`.
- O conteúdo de cada idioma preserva a formatação original (tabelas de metadados do livro, imagens, etc.).

### Anatomia de cada entrada de livro (dentro de cada seção de idioma)

Cada disciplina lista vários livros recomendados. **Cada livro é uma entrada** que segue sempre o mesmo template:

```markdown
<hr>

## <Nome do Livro>

<p align="center">
  <img src="<url da capa>" width="550px">
</p>

<table align="center">
    <tr><th>Título</th><td>...</td></tr>
    <tr><th>Autores</th><td>...</td></tr>
    <tr><th>Ano de Publicação</th><td>...</td></tr>
    <tr><th>Edição</th><td>...</td></tr>
    <tr><th>ISBN</th><td>...</td></tr>
</table>

### Descrição

<p align="justify">
<texto descritivo do livro>
</p>
```

Elementos fixos da entrada, na ordem:
1. **`<hr>`** — separador que abre cada entrada de livro.
2. **`## <Nome>`** — título do livro como H2.
3. **Capa centralizada** — `<p align="center">` com `<img ... width="550px">`.
4. **Tabela de metadados** — `<table align="center">` com exatamente estes campos (rótulo em `<th>`, valor em `<td>`):

   | 🇧🇷 Português | 🇺🇸 English |
   |--------------|------------|
   | Título | Title |
   | Autores | Authors |
   | Ano de Publicação | Publication Year |
   | Edição | Edition |
   | ISBN | ISBN |
5. **`### Descrição` / `### Description`** — seguido de um `<p align="justify">` com o resumo do livro.

> Observação: os rótulos da tabela e o título da descrição mudam de idioma conforme a seção (`🇧🇷` usa "Título/Autores/.../Descrição"; `🇺🇸` usa "Title/Authors/.../Description"). O `<hr>`, a imagem centralizada e a tabela são idênticos em estrutura nos dois idiomas.

---

## 3. Pastas `01_*` a `12_*` — livros completos PROFISSIONAIS

São extrações de livros completos, agrupados por tema. **Por padrão, o conteúdo está em inglês** (idioma original da maioria).

### Nomenclatura
```
Título do Livro - Sobrenome do(s) Autor(es).md
```
Padrão "Título - Autor", legível por humanos, com maiúsculas e espaços normais. Regras:
- Título limpo e reconhecível (remova ruído de nomes de download: ISBNs, `z-lib`, `_compress`, códigos de editora).
- Edição entre parênteses quando relevante: `(2nd Ed)`, `(3rd Ed)`, `(7th Ed)`.
- Autor(es) pelo sobrenome após ` - `; vários autores separados por vírgula.

Exemplos:
- `Clean Architecture - Martin.md`
- `Designing Data-Intensive Applications - Kleppmann.md`
- `CSS in Depth (2nd Ed) - Grant.md`
- `REST in Practice - Webber, Parastatidis, Robinson.md`

### Formatação interna do arquivo original (livro completo)

Diferente do bloco acadêmico, **os arquivos de livro original NÃO seguem um template rígido**. São o **texto integral extraído** do livro (de EPUB/PDF) e convertido para `.md`. Características esperadas:
- O conteúdo segue a estrutura natural do livro: front matter (copyright, sumário), capítulos e seções.
- A marcação markdown é **mínima e irregular** — pode haver títulos (`#`, `##`), mas grande parte é texto corrido em parágrafos.
- Podem aparecer **artefatos de extração**: caracteres estranhos (ex.: `�`), espaçamento anormal entre letras, quebras de linha herdadas do PDF, imagens não preservadas. Isso é esperado e não deve ser "consertado" manualmente sem necessidade.
- **Regra de ouro:** o arquivo original em inglês é mantido **intacto** como fonte. Toda padronização/limpeza acontece na versão traduzida.

### Versões traduzidas (bilíngue por arquivos separados)
A tradução para português **não** é embutida no arquivo original. Ela vai em um **arquivo irmão** na mesma pasta, com o sufixo ` (PT-BR)`:
```
Learning GraphQL - Porcello, Banks.md         ← original em inglês (intacto)
Learning GraphQL - Porcello, Banks (PT-BR).md ← tradução em português
```
Esse é o modelo de "bilíngue" adotado para os livros: **um arquivo por idioma**, lado a lado.

**Template interno do arquivo `(PT-BR)`** — diferente do original, a tradução é markdown limpo e padronizado:
```markdown
# <Título do Livro em Português>
### <Subtítulo em Português>
**<Autores>**

> **Tradução em português (PT-BR).** O arquivo original em inglês está em
> `<nome do arquivo original>.md`, na mesma pasta. Tradução em andamento — esta é a parcela N.

*<linha de copyright/edição do original>*

---

## <Capítulo / Seção>

<texto traduzido em parágrafos limpos; blocos de código preservados em ``` ```; termos técnicos mantidos quando convém>

---

> ⏳ **Continuação pendente** — A tradução segue a partir de "<próxima seção>".
```

Regras da tradução:
- **H1** = título do livro em português; subtítulo em **H3**; autores em **negrito**.
- Um **blockquote de cabeçalho** identifica que é tradução e aponta para o arquivo original.
- Blocos de **código, comandos e identificadores** são preservados como no original (não traduzir código).
- Quando a tradução é feita em partes, termina com um **marcador de continuação** (`⏳ Continuação pendente`) indicando o ponto de retomada.

---

## 4. Arquivos na raiz

Documentos de apoio que descrevem ou indexam o acervo. Nome em `MAIUSCULAS_COM_UNDERSCORE.md` (exceto `README.md`):
- `README.md` — índice navegável de todas as pastas e arquivos.
- `FILE_CONVENTIONS.md` — este guia de padrões.
- `ROLES_AND_ACRONYMS.md` — glossário de cargos de tecnologia (sigla + nome).
- `AGENTS_AND_SKILLS_BY_ROLE.md` — prompt de Agent + Skill para cada cargo.

---

## 5. Resumo rápido (regras)

| Item | Padrão |
|------|--------|
| Pasta | `NN_palavras_minusculas_sem_acento` |
| Disciplina acadêmica | `NN_slug_ingles.md`, **bilíngue no mesmo arquivo** (seções 🇧🇷/🇺🇸) |
| Livro profissional | `Título (Edição) - Autor.md`, em inglês |
| Tradução de livro | arquivo irmão com sufixo ` (PT-BR)` |
| Doc de apoio (raiz) | `MAIUSCULAS_COM_UNDERSCORE.md` |
| Acentos/espaços em nome de pasta | não usar |
| Ordem | definida pelo prefixo numérico `NN_` |
