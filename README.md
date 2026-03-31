# Pipeline de Engenharia de Dados – Diagnóstico de Evasão Acadêmica

Este projeto implementa uma pipeline completa de engenharia de dados para ingestão, validação, transformação e disponibilização de dados acadêmicos, com foco na geração de indicadores como evasão, desempenho e frequência.

---

## Objetivo

Construir uma pipeline automatizada que:

* Extraia dados de uma API externa
* Valide a integridade dos datasets
* Aplique limpeza e transformações
* Gere indicadores de negócio
* Exporte dados prontos para consumo no Power BI

---

## Arquitetura do Projeto

```
data/
├── raw/        # Dados brutos (API)
├── refined/    # Dados tratados e prontos para análise

src/
├── config.py
├── ingestao_api.py
├── ingestao.py
├── limpeza.py
├── validacao.py
├── transformacao.py
├── indicadores.py
├── exportar_dados_powerbi.py
├── carga_dados_sql.py

main.py
requirements.txt
```

---

## Fluxo da Pipeline

```
Extração → Validação → Limpeza → Transformação → Indicadores → Exportação → SQL
```

---

## Etapa 1: Ingestão de Dados

* Consome API REST (`GET /dataset?format=csv`)
* Salva automaticamente em `data/raw`
* Gera:

  * CSV bruto
  * Metadados (`.json`)
  * Schema (`.json`)

---

## Etapa 2: Validação

Validações aplicadas:

* Número mínimo de registros
* Colunas obrigatórias
* Estrutura do dataset

A pipeline é interrompida caso haja inconsistências.

---

## Etapa 3: Limpeza

* Padronização de nomes de colunas
* Conversão de datas
* Remoção de duplicados
* Remoção de colunas completamente nulas

---

## Etapa 4: Transformação

Geração de datasets intermediários:

* Matrícula
* Frequência
* Desempenho
* Consolidação por curso

---

## Etapa 5: Indicadores

Indicadores gerados:

* Taxa de comparecimento
* Taxa de aprovação
* Taxa de evasão prevista
* Frequência média
* Desempenho médio

---

## Etapa 6: Exportação

Os dados são exportados em dois formatos:

* Parquet (otimizado para performance)
* CSV (compatível com diversas ferramentas)

Local de saída:

```
data/refined/
```

Arquivos gerados:

* consolidado_*.parquet / .csv
* matricula_*.parquet / .csv
* frequencia_*.parquet / .csv
* desempenho_*.parquet / .csv
* indicadores_*.parquet / .csv

---

## Etapa 7: Persistência SQL

* Banco: SQLite
* Tabela base: `base`
* View: `vw_curso_consolidado`

---

## Requisitos

Arquivo `requirements.txt`:

```
pandas
requests
python-dotenv
pyarrow
```

---

## Como Executar

### 1. Clonar o repositório

```
git clone <seu-repositorio>
cd <seu-repositorio>
```

### 2. Criar ambiente virtual

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Configurar variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
DATAMISSION_API_TOKEN=seu_token_aqui
```

### 5. Executar a pipeline

```
python main.py
```

---

## Integração com Power BI

Os arquivos disponíveis em `data/refined/` podem ser utilizados diretamente no Power BI para criação de dashboards analíticos.

---

## Tecnologias Utilizadas

* Python
* Pandas
* Requests
* SQLite
* PyArrow

---

## Diferenciais do Projeto

* Pipeline end-to-end automatizada
* Validação de dados antes do processamento
* Estrutura em camadas (raw e refined)
* Geração de indicadores analíticos
* Exportação otimizada para ferramentas de BI
* Execução idempotente

---

## Possíveis Evoluções

* Orquestração com Airflow
* Deploy em ambiente cloud
* Integração com Data Lake
* Monitoramento e logging estruturado
* Dashboard analítico em Power BI

---
