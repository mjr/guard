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
