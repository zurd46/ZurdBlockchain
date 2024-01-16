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
    fig, ax = plt.subplots(figsize=(8, 4))  # Ändern Sie die Größe des Plots
    ax.plot(blocks.index, blocks['timestamp'], linestyle='-', marker='o')
    ax.set_title('Block Timestamps')
    ax.set_xlabel('Block Index')
    ax.set_ylabel('Timestamp')
    ax.grid(True)
    return fig

# Streamlit-App
def app():
    st.set_page_config(layout="wide")  # Setzt das Layout auf volle Breite
    st.title('Blockchain Dashboard')

    blocks, transactions = load_data()

    # Eine Zeile mit zwei Spalten
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h3 style='text-align: center;'>Blocks Overview</h3>", unsafe_allow_html=True)
        st.table(blocks.style.set_table_styles([{'selector': '', 'props': [('max-width', '1000px')]}]))
    
    with col2:
        st.markdown("<h3 style='text-align: center;'>Transactions Overview</h3>", unsafe_allow_html=True)
        st.table(transactions.style.set_table_styles([{'selector': '', 'props': [('max-width', '1000px')]}]))

    # Neue Zeile für den Plot
    st.header('Detailed Analysis')
    fig = plot_block_timestamps(blocks)
    
    # Plot in der Mitte zentrieren
    st.markdown("<div style='text-align: center;'>"
                "<img src='data:image/png;base64,{}' alt='Block Timestamps Plot' width='800px'>"
                "</div>".format(fig_to_base64(fig)), unsafe_allow_html=True)

    with st.expander("See More Details"):
        st.write("Hier können Sie detaillierte Analysen und weitere Informationen hinzufügen.")

# Funktion zur Konvertierung des Plots in base64
def fig_to_base64(fig):
    import base64
    from io import BytesIO
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    return base64.b64encode(buf.getvalue()).decode("utf-8")

if __name__ == '__main__':
    app()
