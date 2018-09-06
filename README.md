# Guard

## Como rodar o `script`?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute o `script`.

```console
git clone https://github.com/mjr/guard.git wsec
cd wsec
python3 -m venv .wsec
source .wsec/bin/activate
pip install -r requirements.txt
python guard.py hash [OPTION (-i, -t ou -x)] [PATH]
```


## Descrição do `script`

```console
usage: guard.py [-h] [-p] [-i] [-t] [-x] [-o OUT] method path

positional arguments:
  method             method of script
  path               path for folder

optional arguments:
  -h, --help         show this help message and exit
  -p, --password     password for hmac
  -i, --inspect      inspect path
  -t, --tracking     tracking path
  -x, --remove       remove guarda of path
  -o OUT, --out OUT  out report of guarda
```
