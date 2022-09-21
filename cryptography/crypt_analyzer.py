from decrypter import Decrypter
from encrypter import Encrypter

class CryptographicAnalyzer(object):

    def __init__(self, method_mapper: dict):
        self.method_mapper: dict = method_mapper
        self.names = list(self.method_mapper.keys())
        self.analyzers: dict = {"encrypters": {name: Encrypter(name, self.method_mapper[name]) for name in self.names},
        "decrypters": {name: Decrypter(name, self.method_mapper[name]) for name in self.names}}
        self.active_decrypter: Decrypter = Decrypter("", None)
        self.active_encrypter: Encrypter = Encrypter("", None)

    def __str__(self) -> str:
        return str(self.analyzers)
    
    def __repr__(self) -> str:
        return str(self)
    
    def decrypt(self, decrypt_args: tuple) -> str:
        return self.active_decrypter.decrypt(decrypt_args)

    def encrypt(self, encrypt_args: tuple) -> str:
        return self.active_encrypter.encrypt(encrypt_args)

    def get_active_analyzer(self) -> tuple:
        return self.active_decrypter, self.active_encrypter

    def set_active_analyzer(self, name: str):
        self.active_decrypter = self.analyzers["decrypter"][name]
        self.active_encrypter = self.analyzers["encrypter"][name]
    
    
