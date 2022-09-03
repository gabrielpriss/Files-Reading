# Boas-vindas ao repositório do Job Insights!

<details>
  <summary><strong> Leitura de Arquivos</strong></summary><br />
  Neste projeto desenvolvido durante o curso da Trybe, implementei análises de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask.

</details>

# Requisitos

## 1 - Função `read`
> **Implementado em:** `src/jobs.py`

Função responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

- Recebe um _path_ (uma string com o caminho para um arquivo).
- Abre o arquivo e lê seus conteúdos.
- Trata o arquivo como CSV.
- Retorna lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.


## 2 - Função `get_unique_job_types`
> **Implementado em:** `src/insights.py`

Identificar quais tipos de empregos existem.

- Receber o _path_ do arquivo csv com os dados.
- Invocar a função `jobs.read` com o _path_ recebido para obter os dados.
- Retorna uma lista de valores únicos presentes na coluna `job_type`.


## 3 - Implemente a função `get_unique_industries`
> **Implementado em:** `src/insights.py`

Identifica quais indústrias estão representadas no conjunto de dados.

- A função obtem os dados da mesma forma que o requisito 2.
- Retorna uma lista de valores únicos presentes na coluna `industry`.
- Desconsidera valores vazios

## 4 - Função `get_max_salary`
> **Implementado em:** `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. A função encontra o maior valor de todas as faixas.

- A função obtem os dados da mesma forma que o requisito 2.
- Ignora os valores ausentes.
- Retorna *um valor inteiro* com o maior salário presente na coluna `max_salary`.

## 5 - Função `get_min_salary`
> **Implementado em:** `src/insights.py`

 Encontra o menor valor de todas as faixas.

- A função obtem os dados da mesma forma que o requisito 2.
- Ignora os valores ausentes.
- Retorna *um valor inteiro* com o menor salário presente na coluna `min_salary`.


## 6 - Função `filter_by_job_type`
> **Implementado em:** `src/insights.py`

Permite que a pessoa usuária possa filtrar os empregos por tipo de emprego na aplicação web.

- A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- Recebe uma string `job_type` como segundo parâmetro.
- Retorna uma lista com todos os empregos onde a coluna `job_type` corresponde ao parâmetro `job_type`.

## 7 - Função `filter_by_industry`
> **Implementado em:** `src/insights.py`

Permite uma filtragem por indústria.

- A função deve recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- Recebe uma string `industry` como segundo parâmetro.
- Retorna uma lista de dicionários com todos os empregos onde a coluna `industry` corresponde ao parâmetro `industry`.


## 8 - Função `matches_salary_range`
> **Implementado em:** `src/insights.py`

Confere que o salário procurado está dentro da faixa salarial daquele emprego. Confere se a faixa salarial faz sentido -- se o valor mínimo é menor que o valor máximo.

- A função recebe um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`.
- Recebe um inteiro `salary` como segundo parâmetro.
- Lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- A função retorna `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.


## 9 - Função `filter_by_salary_range`
> **Implementado em:** `src/insights.py`

Usa a função auxiliar implementada no requisito anterior -- descarta os empregos que apresentarem faixas salariais inválidas.

- A função recebe uma lista de dicionários `jobs` como primeiro parâmetro.
- Recebe um inteiro `salary` como segundo parâmetro.
- Ignora os empregos com valores inválidos para `min_salary` ou `max_salary`.
- Retorna uma lista com todos os empregos onde o salário `salary` estiver entre os valores da coluna `min_salary` e `max_salary`.

## 10 - Implementa a página de um job
> **Implementado em:** `src/routes_and_views.py`

Cria uma página que irá exibir todas as informações de um job em específico

- A função é ligada com a rota `/job/<index>`.
- Recebe um parâmetro `index`.
- Chama a `read` para ter uma lista com todos os jobs.
- Chama a `get_job`, declarada no arquivo `src/more_insights.py`, para selecionar um job específico pelo `index`.
- Renderiza o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.
</details>
