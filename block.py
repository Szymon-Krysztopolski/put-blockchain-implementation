import json
import base64
import mock
import manager
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64


class BlockEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return o.decode('unicode_escape')
        return o.__dict__

class Block:
    def __init__(self, block_name: str, timestamp: str, transactions: str, signer: str, signature: str, prev_block=None) -> None:
        self.block_name = block_name
        self.timestamp = timestamp
        self.transactions = transactions
        self.signer = signer
        self.signature = signature
        self.prev_block = prev_block

    def to_JSON(self):
        return json.dumps(self, indent=4, cls=BlockEncoder)

    def set_block_name(self, name: str):
        self.block_name = name

    def get_block_name(self) -> str:
        return self.block_name

    def set_timestamp(self, sign: str):
        self.timestamp = sign

    def get_timestamp(self) -> str:
        return base64.b64decode(self.timestamp)

    def set_transactions(self, transactions: list):
        self.transactions = transactions

    def get_transactions(self) -> list:
        return self.transactions
    
    def get_signature(self) -> str:
        return self.signature
    
    def set_timestamp(self, signature: str):
        self.signature = signature

    def set_prev_block(self, prev_block: str):
        self.prev_block = prev_block

    def get_prev_block(self) -> str:
        return self.prev_block
    
    def validate_block(self) -> bool:
        public_keys = mock.get_public_keys() + manager.get_system_public_keys()
        for pk in public_keys:
            try:
                # Verify the signature using the public key and PSS padding
                signature = base64.b64decode(self.signature)
                message = self.block_name.encode()
                
                public_key = serialization.load_pem_public_key(
                    pk.encode()
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
                pass
            
        return False
        
