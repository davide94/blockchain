import hashlib
import json
from time import time


class Blockchain:
    target = 0x0001000000000000000000000000000000000000000000000000000000000000

    def __init__(self):
        self.chain = []
        self.mine('Hi, i\'m Genesis!', '0000000000000000000000000000000000000000000000000000000000000000')

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def insert_block(self, block):
        self.chain.append(block)
        return block

    def proof_of_work(self, block):
        return int(self.hash(block), 16) < self.target

    def mine(self, payload, hash_previous_block):
        block = {
            'header': {
                'hash_previous_block': hash_previous_block,
                'timestamp': int(time() * 1000),
                'nounce': 0
            },
            'payload': payload
        }

        while True:
            if self.proof_of_work(block):
                break
            block['header']['nounce'] += 1

        self.chain.append(block)
        return block

    def is_valid(self):
        previous_block = None
        for block in self.chain:
            if previous_block is None:
                previous_block = block
                continue

            if not self.hash(previous_block) == block['header']['hash_previous_block']:
                return False
            if not self.proof_of_work(block):
                return False

            previous_block = block
        return True
