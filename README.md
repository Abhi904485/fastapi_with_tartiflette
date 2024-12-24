# FastApi With GraphQl & Tartiflette-Asgi

## Install Pyenv

### Install python with Pyenv On Ubuntu
```
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
For Users of the Bash Shell
    echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc

For Zsh Shell Users
    echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.zshrc
    
exec "$SHELL"
pyenv --version
```

### Install python with Pyenv on Mac

```
brew update
brew install pyenv
alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
exec "$SHELL"
pyenv --version
```

### Setup Virtualenv
```
pyenv install 3.12.8
pyenv virtualenv 3.12.8 fastapi_with_tartiflette_asgi
echo fastapi_with_tartiflette_asgi > .python-version
```

### Install python Packages

```
pip install poetry
poetry install --no-root
```


## How to Run
```
uvicorn main:app --reload 
```

## How to Migrate DB
```
alembic revision --autogenerate -m "Initial Migration"

```
### How to Upgrade DB
```
alembic upgrade head
```

### GraphQl UI is accessible at
```
http://127.0.0.1:8000/graphql 
```