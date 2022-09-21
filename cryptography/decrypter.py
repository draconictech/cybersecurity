class Decrypter(object):

    def __init__(self, name: str, method):
        self.name: str = name
        self.method = method 
    
    def __str__(self) -> str:
        return str(self.name)
    
    def __repr__(self) -> str:
        return str(self)
    
    def decrypt(self, decrypt_args: tuple) -> str:
        if self.method is None:
            return ""

        return self.method(*decrypt_args)