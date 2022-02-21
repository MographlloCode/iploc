# IPLoc API :round_pushpin:
### Essa API tem como intuito localizar todas as informações sobre um IP inserido através de requisição em uma API Externa (IPAPI)

## Instalação

Você deve começar clonando o repositório GIT:

```sh
$ git clone https://github.com/MographlloCode/iploc.git
$ cd iploc
```

Em seguida crie um ambiente virtual e o ative:

```sh
$ python -m venv venv
$ source venv/Scripts/activate
```

Então instale as dependencias utitlizando `pip`:

```sh
(env)$ pip install -r requirements.txt
```

Note que `(venv)` na frente da linha de comando serve para sinalizar que seu ambiente virtual está ativo.

Uma vez instaladas as dependências, rode o servidor local do projeto:

```sh
(env)$ cd iploc
(env)$ python manage.py runserver
```
A primeira página será a pagina de rotas da API `http://127.0.0.1:8000/`.

Nela você vai encontrar dois endpoints, um responsável por buscar as informações de um determinado IP e o outro responsável por listar os ips procurados.

## Seções

Existem três urls base que podem ser acessadas em um primeiro momento.

### Documentação

A primeira é a `http://127.0.0.1:8000/doc`, nela você encontra a documentação da API com a definicão de cada View e Modelo do projeto.

### Buscar IP

A segunda é a `http://127.0.0.1:8000/ip`, nela você insere o ip com até 15 digitos (com pontuação) e o mesmo é requisitado por uma API Externa. Ao finalizar a requisição você será redirecionado para `http://127.0.0.1:8000/listaip/{ip_que_voce_buscou}`, nessa View você terá acesso a todos os dados do IP que foi inserido previamente.

### Lista de IPs

Por último temos a `http://127.0.0.1:8000/ip_dados`, ela lista todos os IPs que foram inputados até o presente momento.
