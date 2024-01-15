from blockchain.block import Block
from blockchain.transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0")
        self.chain.append(genesis_block)

    def add_block(self, block):
        self.chain.append(block)

    def is_valid(self):
        # Validierung der Blockchain
        pass

class ExtendedBlockchain(Blockchain):
    def __init__(self, db_file):
        super().__init__()
        self.db_file = db_file
        self.pending_transactions = []
        self.reward = 1  # Die Belohnung für das "Mining" eines neuen Blocks
