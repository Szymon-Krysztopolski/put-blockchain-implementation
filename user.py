from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64, hashlib, secrets


class User:   
    def __init__(self, name=None, password=None, public_key=None, private_key=None) -> None:
        self.username = name
        self.password = password
        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, text: str) -> str:
        public_key = serialization.load_pem_public_key(
            self.public_key.encode()
        )

        encrypted_message = public_key.encrypt(
            text.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_message

    def decrypt(self, cipher: str) -> str:
        private_key = serialization.load_pem_private_key(
            self.private_key.encode(),
            password=None
        )

        decrypted_message = private_key.decrypt(
            cipher,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

        return decrypted_message
    
    def sign(self, message: str) -> str:
        private_key = serialization.load_pem_private_key(
            self.private_key.encode(),
            password=None
        )
        message = message.encode()
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature

    def verify_signature(self, signature: str, message: str) -> bool:
        try:
            # Verify the signature using the public key and PSS padding
            
            signature = base64.b64decode(signature)
            message = message.encode()
            
            public_key = serialization.load_pem_public_key(
                self.public_key.encode()
            )
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            return True
        except Exception:
            return False


    def valid_credentials(self, login: str, password: str) -> bool:
        return login == self.username and password == self.password

    def get_base64_hash(self): # Hash needed to challenge
        random_value = secrets.token_hex(16)
        hash_object = hashlib.sha256()
        input_bytes = random_value.encode('utf-8')
        hash_object.update(input_bytes)
        hash_digest = hash_object.digest()
        base64_hash = base64.b64encode(hash_digest)

        return base64_hash.decode('utf-8')

    def get_username(self) -> str:
        return self.username

    def set_username(self, value: str):
        self.username = value

    def get_password(self) -> str:
        return self.password

    def set_password(self, value: str):
        self.password = value

    def get_public_key(self):
        return self.public_key

    def set_public_key(self, value):
        self.public_key = value

    def get_private_key(self):
        return self.private_key
