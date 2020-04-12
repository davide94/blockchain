import hashlib
import json
import unittest
from src.lib import Blockchain


def hash(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()


class TestBlockchain(unittest.TestCase):

    def test_genesis(self):
        blockchain = Blockchain()

        genesis = blockchain.chain[0]
        result = int(hash(genesis), 16)
        max_result = blockchain.target

        self.assertLess(result, max_result, 'Should be lower than target')

    def test_proof_of_work(self):
        blockchain = Blockchain()

        genesis = blockchain.chain[0]
        hash_genesis = hash(genesis)
        block_one = blockchain.mine('something', hash_genesis)

        result = int(hash(block_one), 16)
        max_result = blockchain.target

        self.assertLess(result, max_result, 'Should fulfill proof-of-work')

    def test_previous_hash(self):
        blockchain = Blockchain()

        genesis = blockchain.chain[0]
        hash_genesis = hash(genesis)
        block_one = blockchain.mine('something', hash_genesis)

        hash_block_one = hash(block_one)
        block_two = blockchain.mine('something', hash_block_one)

        expected_result = hash(block_one)
        result = block_two['header']['hash_previous_block']

        self.assertEqual(expected_result, result, 'Should match the actual hash of the previous block')
