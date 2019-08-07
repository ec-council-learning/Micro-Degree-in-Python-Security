import base64
# Haradous Materials
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

class RSADemo(object):
    def __init__(self, key_size = 4096, public_exponent = 65537):
        self.private_key = rsa.generate_private_key(public_exponent = public_exponent, key_size = key_size, backend = default_backend())
        self.public_key = self.private_key.public_key()

    def encrypt(self, plain):
        self.cipher_text_bytes = self.public_key.encrypt(
                    plaintext = plain.encode('utf-8'),
                    padding = padding.OAEP(
                            mgf = padding.MGF1(algorithm = hashes.SHA256()),
                            algorithm = hashes.SHA512(),
                            label = None
                        )
                )
        self.cipher_text = base64.urlsafe_b64encode(self.cipher_text_bytes)

    def decrypt(self, cipher):
        self.decrypted_cipher_text_bytes = self.private_key.decrypt(
                    ciphertext = base64.urlsafe_b64decode(self.cipher_text),
                    padding = padding.OAEP(
                            mgf = padding.MGF1(algorithm = hashes.SHA256()),
                            algorithm = hashes.SHA512(),
                            label = None
                        )
                )
        self.decrypted_cipher_text = self.decrypted_cipher_text_bytes.decode("utf-8")

    @property
    def encrypted(self):
        return self.cipher_text

    @property
    def decrypted(self):
        return self.decrypted_cipher_text

    @property
    def pirv_key(self):
        return self.private_key

    @property
    def publ_key(self):
        return self.public_key

WeWantToEncrypt = "Welcome to the EC Council!"
print("THis is the original: {}".format(WeWantToEncrypt))
Demo = RSADemo()
Demo.encrypt(WeWantToEncrypt)
print(Demo.encrypted)
Demo.decrypt(Demo.encrypted)
print(Demo.decrypted)
