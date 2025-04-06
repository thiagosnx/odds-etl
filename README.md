# 🏟️ Histórico de jogos ETL - Python + SQLite

Projeto simples de ETL (Extract, Transform, Load) que coleta dados de partidas de futebol usando a API da [Football-Data.org](https://www.football-data.org/), transforma os dados relevantes e armazena em um banco de dados SQLite para futuras análises.

---

## 📌 Funcionalidades

- 🔁 Requisição de partidas via API REST (ex: Premier League)
- 🧹 Transformação de dados em estrutura limpa com `pandas`
- 💾 Armazenamento em banco de dados SQLite (`matches.db`)
- ⚙️ Estrutura modular: `extract.py`, `transform.py`, `load.py`, `etl.py`

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/thiagosnx/odds-etl.git
cd odds-etl
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure seu token de API no .env


### 4. Execute o ETL
```bash
py etl.py
```



