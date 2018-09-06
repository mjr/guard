# import os
# import fire
# import hashlib
# import json
# import pprint
#
#
# class Guarda(object):
#     """A simple guarda class."""
#
#     def generate_hash(self, data):
#         return hashlib.sha256(data).hexdigest()
#
#     def files(self, path):
#         for file in os.listdir(path):
#             if os.path.isfile(os.path.join(path, file)):
#                 with open('{}/{}'.format(path, file), 'rb') as file_read:
#                     hash = self.generate_hash(file_read.read())
#
#                 yield file, hash
#
#     def save(self, path, data):
#         with open('{}/.guarda'.format(path), 'w') as f:
#             f.write(data)
#
#     def guardar(self, path):
#         dict = []
#         for file, hash in self.files(path):
#             dict.append({'file': file, 'hash': hash})
#
#         dict = json.dumps(dict)
#         self.save(path, dict)
#         pprint.pprint(dict)
#
#     def rastrear(self, path):
#         guarda_check_load = None
#         with open('{}/.guarda'.format(path), 'rb') as file_read:
#             for line in file_read.readlines():
#                 guarda_check_load = line
#         guarda_check = json.loads(guarda_check_load)
#
#         dict_now = []
#         for file, hash in self.files(path):
#             if (file != '.guarda'):
#                 dict_now.append({'file': file, 'hash': hash})
#
#         for dn in dict_now:
#             if not next((item for item in guarda_check if item['file'] == dn['file']), False):
#                 print('arquivo novo -> {}'.format(dn['file']))
#
#         for gc in guarda_check:
#             if not next((item for item in dict_now if item['file'] == gc['file']), False):
#                 print('arquivo deletado -> {}'.format(gc['file']))
#
#         for dn in dict_now:
#             for gc in guarda_check:
#                 if dn['file'] == gc['file']:
#                     if not gc['hash'] == dn['hash']:
#                         print('arquivo alterado -> {}'.format(gc['file']))
#
#     def desativar(self, path):
#         os.remove('{}/.guarda'.format(path))
#
#     def hash(self, i=None, t=None, x=None, path=None, o=None):
#         if i:
#             self.guardar(path)
#         elif t:
#             self.rastrear(path)
#         elif x:
#             self.desativar(path)
#
#         return '>>> Finish! <<<'

    # def hmac(self):
    #     pass
    #
    # def method(self, method='hash', i=None, t=None, x=None, path=None, o=None):
    #     if method == 'hash':
    #         self.hash()
    #     elif method == 'hmac':
    #         self.hmac()
    #
    #     return '>>> Finish! <<<'

# if __name__ == '__main__':
#     fire.Fire(Guarda)
