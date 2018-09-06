import os
import hashlib
import json
import plac


# Constante com o nome do arquivo para salvar os hash's
NAME_FILE = '.guarda'


# Gera o hash do dado passado utilizando o 'script' de criptografia SHA256
def generate_hash(data):
    return hashlib.sha256(data).hexdigest()


# Lê os arquivos do caminho passado e gera o hash desses arquivos
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            with open('{}/{}'.format(path, file), 'rb') as file_read:
                hash = generate_hash(file_read.read())

            yield file, hash


# Salva o arquivo '.guarda'
def save(path, data):
    with open('{}/{}'.format(path, NAME_FILE), 'w') as f:
        f.write(data)


# Gera os hash's dos arquivos do caminho passado e salva no arquivo '.guarda'
def inspects(path):
    dict = []
    for file, hash in files(path):
        dict.append({'file': file, 'hash': hash})

    dict = json.dumps(dict)
    save(path, dict)


# Analisa se tem arquivos novos ou arquivos deletados
def filter_hash(type, dict_list, dict_list_check):
    messages = []
    for dict_item in dict_list:
        if not next((item for item in dict_list_check if item['file'] == dict_item['file']), False):
            if type == 'new':
                messages.append('ARQUIVO NOVO -> {}'.format(dict_item['file']))
            elif type == 'remove':
                messages.append('ARQUIVO DELETADO -> {}'.format(dict_item['file']))

    return messages


# Analisa os hash's gerados agora com os hash's salvos no arquivo de check
def check_hash(dict_list, dict_list_check):
    messages = []

    for dict_item in dict_list:
        for dict_item_check in dict_list_check:
            if dict_item['file'] == dict_item_check['file']:
                if not dict_item_check['hash'] == dict_item['hash']:
                    messages.append('ARQUIVO ALTERADO -> {}'.format(dict_item_check['file']))

    return messages


# Ler o arquivo com os hash's dos arquivos e convert para um objeto 'dict' do python
def read_check_file(path):
    with open('{}/{}'.format(path, NAME_FILE), 'rb') as file_read:
        for line in file_read.readlines():
            return json.loads(line)


# Ler os arquivos do caminho passado como parâmetro
def read_now_file(path):
    dict_now = []
    for file, hash in files(path):
        if (file != NAME_FILE):
            dict_now.append({'file': file, 'hash': hash})

    return dict_now


# Cria um arquivo passado como parâmetro (--out) e escreve as mensagens da analise dos arquivos nele
def write_report(path, out, messages):
    with open('{}/{}'.format(path, out), 'w') as f:
        for message in messages:
            f.write(message)


# Imprime na tela as mensagens da analise dos arquivos
def display_messages_in_screen(messages):
    for message in messages:
        print(message)


# Analisa se tem algum arquivo novo, se algum arquivo foi alterado ou se teve algum arquivo deletado
def trackings(path):
    dict_list_check = read_check_file(path)
    dict_list = read_now_file(path)

    return filter_hash('new', dict_list, dict_list_check) + check_hash(dict_list, dict_list_check) + filter_hash('remove', dict_list_check, dict_list)


# Remove arquivo com os hash's dos arquivos
def removes(path):
    os.remove('{}/{}'.format(path, NAME_FILE))


def main(
    method: 'method of script',
    password: ('password for hmac', 'flag', 'p'),
    inspect: ('inspect path', 'flag', 'i'),
    tracking: ('tracking path', 'flag', 't'),
    remove: ('remove guarda of path', 'flag', 'x'),
    path: 'path for folder',
    out: ('out report of guarda', 'option', 'o')
):
    if method=='hash':
        # Verifica o parâmetro passado e chama a função de acordo com o parâmetro, por padrão (se o usuário não passar nenhum parâmetro: o caso else) chama a função de inspecionar os arquivos do caminho passado
        if inspect:
            inspects(path)
        elif tracking:
            # Verifica se o usuário passou o parâmetro para criar um arquivo de saida, caso não passe o parâmetro o programa mostra as mensagens na tela
            if out:
                write_report(path, out, trackings(path))
            else:
                display_messages_in_screen(trackings(path))
        elif remove:
            removes(path)
        else:
            inspects(path)

    # HMAC ainda não foi implementado
    elif method=='hmac':
        if password:
            print('password')
        else:
            print('password invalid!')
    else:
        print('unknown method')

if __name__ == '__main__':
    plac.call(main)
