import sqlite3
from blockchain.block import ExtendedBlock
from blockchain.transaction import Transaction

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # Verwendung von Anführungszeichen um 'index', da es ein reserviertes Wort in SQLite ist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                "index" INTEGER PRIMARY KEY,
                previous_hash TEXT,
                timestamp REAL,
                hash TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                block_index INTEGER,
                sender TEXT,
                receiver TEXT,
                amount REAL,
                FOREIGN KEY(block_index) REFERENCES blocks("index")
            )
        ''')
        self.conn.commit()

    def add_block(self, block):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO blocks ("index", previous_hash, timestamp, hash) 
            VALUES (?, ?, ?, ?)
        ''', (block.index, block.previous_hash, block.timestamp, block.hash))
        self.conn.commit()

    def add_transaction(self, transaction, block_index):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO transactions (block_index, sender, receiver, amount) 
            VALUES (?, ?, ?, ?)
        ''', (block_index, transaction.sender, transaction.receiver, transaction.amount))
        self.conn.commit()

    def get_blocks(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM blocks')
        return cursor.fetchall()

    def get_transactions(self, block_index=None):
        cursor = self.conn.cursor()
        query = 'SELECT * FROM transactions'
        params = ()
        if block_index is not None:
            query += ' WHERE block_index = ?'
            params = (block_index,)
        cursor.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
