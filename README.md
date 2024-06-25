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

