# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch, MagicMock
from blockchain import Chain, Block, Transaction, Memento
import hashlib

class TestChain(unittest.TestCase):

    def test_proof_work_invalid_block(self):
        chain = Chain(4)
        prev_hash = hashlib.sha256(b'prev').digest()
        block = Block(Transaction('A', 'B', 60), prev_hash)
        with patch.object(Block, 'mining') as mock_mining:
            mock_mining.return_value = None
            block.prev_block = hashlib.sha256(b'other').digest()
            result = chain.proof_work(block)
            self.assertFalse(result)

    def test_mining(self):
        chain = Chain(4)
        with patch.object(Block, 'mining') as mock_mining:
            mock_mining.return_value = None
            chain.create_transaction('A', 'B', 60)
            result = chain.mining()
            self.assertEqual(result, 'Bloque inválido')

class TestBlock(unittest.TestCase):

    def test_mining(self):
        block = Block(Transaction('A', 'B', 60), hashlib.sha256(b'prev').digest())
        with patch.object(block, '_hash') as mock_hash:
            mock_hash.hexdigest.return_value = '0' * 64
            block.mining(4)
            self.assertEqual(type(block._nonce), int)

class TestTransaction(unittest.TestCase):

    def test_transaction_str(self):
        transaction = Transaction('A', 'B', 60)
        expected_str = 'A:B'
        self.assertEqual(str(transaction), expected_str)

class TestMemento(unittest.TestCase):

    def test_get_chain(self):
        chain = Chain(4)
        memento = Memento(chain)
        self.assertEqual(memento.get_chain(), chain)

if __name__ == '__main__':
    unittest.main()
