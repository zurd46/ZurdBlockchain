import streamlit as st
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# Funktion zum Laden der Daten
def load_data():
    conn = sqlite3.connect('blockchain.db')
    blocks = pd.read_sql_query('SELECT * FROM blocks', conn)
    transactions = pd.read_sql_query('SELECT * FROM transactions', conn)
    conn.close()
    return blocks, transactions

# Funktion zum Erstellen eines Plots
def plot_block_timestamps(blocks):
    plt.figure(figsize=(10, 6))
    plt.plot(blocks['timestamp'], linestyle='-', marker='o')
    plt.title('Block Timestamps')
    plt.xlabel('Block Index')
    plt.ylabel('Timestamp')
    plt.grid(True)
    return plt

# Streamlit-App
def app():
    st.title('Blockchain Dashboard')

    blocks, transactions = load_data()

    st.header('Blockchain Overview')
    st.write('Blocks:')
    st.dataframe(blocks)

    st.write('Transactions:')
    st.dataframe(transactions)

    st.header('Block Timestamps')
    plot = plot_block_timestamps(blocks)
    st.pyplot(plot)

    # Hier können Sie weitere Analysen und Grafiken hinzufügen

if __name__ == '__main__':
    app()
