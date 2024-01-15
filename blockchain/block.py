import time
import hashlib

class Block:
    def __init__(self, index, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class ExtendedBlock(Block):
    def __init__(self, index, previous_hash, transactions):
        super().__init__(index, previous_hash)
        self.transactions = transactions

    def compute_hash(self):
        transactions_string = "".join([str(tx) for tx in self.transactions])
        block_string = f"{self.index}{self.timestamp}{transactions_string}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Hier können Sie zusätzliche Methoden oder Eigenschaften hinzufügen, die spezifisch für ExtendedBlock sind
