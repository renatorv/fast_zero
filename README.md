Criando um ambiente virtual
poetry install

poetry add fastapi

python -i fast_zero/app.py

Ativar ambiente virtual
poetry shell

fastapi dev fast_zero/app.py

Ruff: Linter e formatador de código (Formatter)
poetry add --group dev ruff
ruff check .
ruff format .

Pytest
poetry add --group dev pytest pytest-cov
pytest --cov=fast_zero -vv
coverage html

Taskipy
poetry add --group dev taskipy
task --list

ignr -p python > .gitignore
git init .
git add .
git commit -m "Iniciando o projeto"

# Executar um arquivo especifico
python -i fast_zero/schemas.py
>> UserSchema(email='bla') => vai dar erro

# SQLAlchemy 
Contém um ORM (Mapeamento objeto relacional), que permite trabalhar com BD relacionais.
Abstração de BD, usar o msm código Python para todos os BDs,
Segurança: previne SQL Injection
Eficiência no desenvolvimento: gera automaticamente esquemas, migrações

poetry add sqlalchemy

Engine: ponto de contato com o BD estabelecendo o gerenciamento das conexões.
Ela é instânciada com a função create_engine(), que recebe as credenciais do BD

Session: camada intermediaria entre o nosso código e o BD


# Configuração de ambiente e as 12 fatores
Separar as configurações do código
poetry add pydantic-settings

# Migrações [ 1:20 Aula 4 ]
- BD evolutivo
- BD acompanha as alterações do código
- Reverter alterações no schema do BD

poetry add alembic
alembic init migrations

alembic revision --autogenerate -m "create users table"

alembic upgrade head


40 min => https://www.youtube.com/watch?v=_87z5b4szW4&t=1515s