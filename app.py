import streamlit as st
import pickle
import matplotlib.pyplot as plt

st.set_page_config(
    layout="wide",
    page_title="Analysis Web App"
)
@st.cache_data()
def read_data():
    with open("data/data.pkl", "rb") as f:
        data = pickle.load(f)
    return data

# @st.cache_data()
# def freq_data():
#     with open("data/freq_dist.pkl", "rb") as f:
#         freq_dist = pickle.load(f)
#     return freq_dist

@st.cache_data()
def ngram_data():
    with open("data/ngram.pkl", "rb") as f:
        ngram_dist = pickle.load(f)
    return ngram_dist[:20]

df = read_data()
ngram = ngram_data()

with st.container(border=True, height=850):
    st.image("img/ilustrasi.png", use_column_width=True, )

st.title("ANALISA BERITA KEPRESIDENAN TENTANG IBUKOTA BARU")
with st.container(border=True, height=800):
    col_1, col_2 = st.columns(2)
    with col_1:
        st.text("""Terlihat dari data ngram kalau pada beberapa waktu terakhir, 
                presiden joko widodo sedang memberikan konsentrasinya pada bidang perumahan di Ibukota baru Indonesia""")

    with col_2:
        labels, values =zip(*ngram.items())
        index = range(len(labels))

        plt.figure(figsize=(10,5))
        plt.bar(index, values)
        plt.xticks(index, labels, rotation=90)
        plt.title("Ngram Freq")
        plt.xlabel("Ngram")
        plt.ylabel("Frekuensi")

        st.pyplot(plt)


with st.container(border=True, height=500):
    pass
with st.container(border=True, height=500):
    pass