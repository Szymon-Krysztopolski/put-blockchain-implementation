import itertools
import random
import sys

import mock
import manager
from user import User
from block import Block

GENERATE_BLOCKS = True

BLOCK_DIR = "./blocks"
SYSTEM_USER = User()
current_user = User()
User_list = []


def main():
    while True:
        menu()
        switch_case(input("Your choice: "))

def menu() -> None:
    print(f"\nYour are logged as {current_user.get_username()}")
    print("1. Change user")
    print("2. Add transactions")
    print("3. Show owners of current blocks")

def switch_case(case):
    if case == '1':
        change_user()
    elif case == '2':
        add_transactions()
    elif case == '3':
        show_owners()
    elif case == 'e':
        exit(0)
    else:
        return 'Invalid case'

def change_user() -> None:
    global current_user

    login = input("Login: ")
    password = input("Password: ")

    for i in range(len(User_list)):
        user = User_list[i]
        if user.valid_credentials(login, password):
            current_user = user
            return
    print("Wrong credentials!")

def add_transactions() -> None:
    challenge_order = list(range(1, len(User_list)))
    random.shuffle(challenge_order)
    
    size = int(input("How many transactions do you want to generate: "))
    new_transactions = [current_user.get_username() + ": ------ " + element for element in random.sample(mock.get_lorem(), min(5, size))]

    active_challange = True
    while active_challange:
        for i in challenge_order:
            user = User_list[i]
            if manager.is_winner(user.get_base64_hash()):
                manager.add_block_to_blockchain(user, new_transactions)
                active_challange = False
                break

def show_owners() -> None:
    block_list = manager.get_block_list()

    for block, user in itertools.product(block_list, User_list):
        if(manager.check_owner_of_block(user, block)):
            print("User: {:<12} Block: {:<10} Is valid: {:<10}".format(user.get_username(), block.get_block_name(), user.verify_signature(block.get_signature(), block.get_block_name())))

def init():  # Lazy loading
    global SYSTEM_USER, User_list, current_user

    manager.init(BLOCK_DIR, GENERATE_BLOCKS)
    SYSTEM_USER = manager.SYSTEM_USER
    User_list = [SYSTEM_USER] + mock.get_users()
    current_user = SYSTEM_USER

def remove_blocks():
    import os
    import glob

    files = glob.glob('blocks/*')
    for f in files:
        os.remove(f)
    print("Startup cleanup completed")

if __name__ == "__main__":
    # remove_blocks()
    if ("--init" in sys.argv):
        remove_blocks()
    init()
    main()
