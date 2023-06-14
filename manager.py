import os, json
import secrets
import hashlib
import base64
from datetime import datetime

from block import Block
from user import User
import mock


BLOCK_DIR = ""
Blok_list = []

def init(block_dir: str, generate_blocks: bool) -> None:
    global BLOCK_DIR, Blok_list

    BLOCK_DIR = block_dir
    
    if not os.path.exists(BLOCK_DIR):
        os.mkdir(BLOCK_DIR)
    
    first_block_exists_check(generate_blocks)
    Blok_list = create_block_ordered_list()

def get_block_list() -> list:
    return Blok_list

def first_block_exists_check(generate_blocks: bool) -> None:
    if not os.listdir(BLOCK_DIR):
        add_block_to_blockchain(SYSTEM_USER, ["INIT BLOCK"], "INIT")

        if generate_blocks:
            mock.generate_blocks(10)

def is_winner(hash: str) -> bool: # Winner can add block to blockchain
    return hash.startswith("0")

def generate_block_hash() -> str:
        random_value = secrets.token_hex(16)
        hash_object = hashlib.sha256()
        hash_object.update(random_value.encode())

        return hash_object.hexdigest()

def add_block_to_blockchain(user: User, transactions: list, new_block_name=None) -> None:
    global Blok_list

    prev_block = None
    if new_block_name == None:
        new_block_name = generate_block_hash()
    
    if len(Blok_list) > 0:
        prev_block = Blok_list[-1].get_block_name()
        
    new_block = Block(
        new_block_name,
        base64.b64encode(user.encrypt(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))).decode('utf-8'),
        transactions,
        user.get_username(),
        base64.b64encode(user.sign(new_block_name)).decode('utf-8'),
        prev_block
    )

    Blok_list.append(new_block)
    save_block_to_file(new_block)
    print("Block added successfully.", new_block_name)

def save_block_to_file(block: Block) -> None:
    file_path = os.path.join(BLOCK_DIR, block.get_block_name() + ".json")
    with open(file_path, "w") as file:
        file.write(block.to_JSON())

def create_block_ordered_list() -> list:
    blocks = get_blocks_from_directory()
    sorted_blocks = [blocks.pop("INIT")]

    while len(blocks) > 0:
        for key in blocks.keys():
            if blocks[key].get_prev_block() == sorted_blocks[-1].get_block_name():
                sorted_blocks.append(blocks.pop(key))
                break

    return sorted_blocks

def get_blocks_from_directory() -> dict:
    block_dict = {}

    for file_name in os.listdir(BLOCK_DIR):
        file_path = os.path.join(BLOCK_DIR, file_name)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                block_data = json.load(file)
                block = Block(**block_data)
                if block.validate_block():
                    block_dict[block.block_name] = block
                else:
                    print("Non valid block", file_name, "will not be included in a blockchain")

    return block_dict

def check_owner_of_block(user: User, block: Block) -> bool: # Owner adds block to blockchain
    try:
        return is_timestamp(user.decrypt(block.get_timestamp()))
    except ValueError:
        return False
    

def is_timestamp(string: str) -> bool:
    try:
        datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def get_system_public_keys() -> list:
     return [SYSTEM_USER.get_public_key()]
    
SYSTEM_USER = User("System",
                       "myP@ss123",
                       """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzpSYx+M6EAPCggp2PKKq
suBJyMvmz34Aa+pLemmcQ4iUeG+9gFl16++FcHAfNQtB4BlJXExY6NHoIkt2lcMC
13ttnMrAcdJwp+av1C3gj0WwwcyO7e3rR/sqiJ6Vh+Y9lZtfsUX4nSkExIUPmXt3
2O8q4jNqyj0OAJNhtD04IkId4DFmzWevNb+HH6wN35jzy1D2j08cXVdzE3oDdnqw
81rF8DFE0Vsn/VGjDK3Iu46PF0XApEOYwhEF0L4xhjLQLrHawc1Ij77V17PPvyfa
N6JAki0u6me91s17NM3yNiNsYfOyfpBhdH/WpY+tHVZGvH7NJ+xNQAcrgFhj64C6
JwIDAQAB
-----END PUBLIC KEY-----

""",
                       """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDOlJjH4zoQA8KC
CnY8oqqy4EnIy+bPfgBr6kt6aZxDiJR4b72AWXXr74VwcB81C0HgGUlcTFjo0egi
S3aVwwLXe22cysBx0nCn5q/ULeCPRbDBzI7t7etH+yqInpWH5j2Vm1+xRfidKQTE
hQ+Ze3fY7yriM2rKPQ4Ak2G0PTgiQh3gMWbNZ681v4cfrA3fmPPLUPaPTxxdV3MT
egN2erDzWsXwMUTRWyf9UaMMrci7jo8XRcCkQ5jCEQXQvjGGMtAusdrBzUiPvtXX
s8+/J9o3okCSLS7qZ73WzXs0zfI2I2xh87J+kGF0f9alj60dVka8fs0n7E1AByuA
WGPrgLonAgMBAAECggEAA3jY5ocpqyo9Ay2E1jkPsGj3pIHU08j03dt2wEx1HWd2
w11xbG5Ufo4sinq/84bIaSlTo9L+rY8VnTnyeMrpydBfw8JeoKseTJwieWj5/L55
nZBAGLymdzO//8LWlY2nnFObtKGN76pIU7s+y2AZYBKJAHtHwLVs/lJ70mky/9Rf
4/Ay+xeihg3YflIbDw7Zcv0z1BWvZC2mJmFzcblVV0yGnY024Jd6Ii5uPCVddyKw
QmzqQCEtsHMDw9Y1twP/doh9jARUqtg/NjySpiRBK7kK3kCM/a2DyD1qupoZsLwz
HgCM9O3TfgTHnrbcX4oRY42krwHWVUWS2ndEwCUuPQKBgQD792FC5H5qc8EqFbVA
PsPwx8/rNd9ZkqE5Oem4IeufyS5c5nvgkWncn899jq7pY2L0aAWULPhPbnJ3tJB2
f4m61jDc662oKrrCSJeMz70zfRyPqjeHgUr0pYTXdorVG5BjokJdWcb+BUk0lawr
gwo6tpXAh3YTZhKLFdcXAeDXOwKBgQDR4zbiayZ7VI8HH+dgPbr66reWQ5Y6+s+2
/vVRN1OrzZbCCHhIwRSRhDCXAb+/RYqvOfWHcbuVLc4mQdXAUa34Dgb1How8TRj6
7WcfypobSaMvnhJqlQljkeuRB6CXRg+GNBdeyyBxw4PglPK1dBRJAKxzjLO8UxAj
Xr1xxQkyBQKBgHgZVAzUaMVI43ux2TEEOdUdCKfuh8VkNODYD+UqlesVs7moSseh
yDnXGsmYJxsrulEQ/AfC36DM3lbchDdXV0jtK2FCHQYZR+evPj1qD57pNaHs2ocG
Q7oU4xrocAhgGRTElKl2T3lo/5nG9cfPsCKIQR0B9HAOqSwOfvWCea9dAoGBAIFk
A6fdyqFpZatMvcUVCTo6jOczz1+Y04jK8M0awJg/a9s+gXjInzd+OL4/M8hkxLR1
lKnlMXEsBdSL7YxcTlWHwD5IkMdz+BxpUpPEwPBlmxZ16oCOVHVvtbt46kWXyWZA
os+rhdrcX2aKLH40i3Td13J8oSlOQ7qqYzvJ7ntJAoGADHMKww27m4UlSrTcosqz
1o3J7WiSwRbGHktKEWgM1ITzaiG5zAuBOhLROfLnTS8KQLtHv+YtxG9hSFS7EOEZ
ZPFuOQg3N7MqJU744vkz/PhkWFgpY5O2rjXQnslmjGBsG44bYAvAPWbbUWICAkx9
dQNjyPp36G50rZ1bK9Xj9sY=
-----END PRIVATE KEY-----
"""
                       )