# API Advertising + Front-end

Este projeto é parte do material didático da disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** e apresenta uma API implementada no estilo REST, e um Front-End proposto.

### Tecnologias Principais:
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) - Framework web em Python.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Ferramenta de ORM para Python.
- [OpenAPI3](https://swagger.io/specification/) - Especificação para documentação de APIs.
- [SQLite](https://www.sqlite.org/index.html) - Banco de dados embutido/
- [Colab](https://colab.research.google.com/) - Utilizado para a geração do modelo a ser usado.

## API Advertising

Esta API permite a análise de investimentos publicitários, fornecendo insights com base em dados de campanhas em TV, rádio e jornal. Ela recebe informações sobre os valores investidos em cada mídia e retorna a classificação de desempenho, permitindo o acompanhamento da eficácia dos investimentos. A API suporta operações para adicionar novos dados de investimento, consultar os resultados e excluir registros, além de integrar a visualização dos resultados com indicadores visuais de performance (alta, média, baixa). Ideal para empresas que buscam otimizar suas estratégias de marketing com base em dados concretos.

### Instalação

Para instalar as dependências, certifique-se de ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas. 
> Recomenda-se o uso de ambientes virtuais como [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env) pip install -r requirements.txt
```

---
### Executando o servidor

Para iniciar o servidor da API:

```
(env) flask run --host 0.0.0.0 --port 5000
```

Em ambiente de desenvolvimento, utilize o parâmetro --reload para reiniciar automaticamente o servidor após alterações no código fonte:

```
(env) flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no Navegador

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para acessar a API em execução.

---
## Front-End

O front-end desta aplicação permite visualizar e gerenciar dados de investimentos publicitários em TV, rádio e jornal. A interface exibe os resultados das campanhas em uma tabela dinâmica, com indicadores visuais que classificam o desempenho (alta, média, baixa). Também é possível adicionar novos dados, aplicar filtros de performance e excluir registros diretamente da interface, proporcionando uma experiência de uso simples e intuitiva para análise de marketing.

## Como executar 

Para iniciar, basta realizar um clone ou download do repositório e abrir o arquivo `front\index.html`.

---
