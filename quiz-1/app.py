import streamlit as st
from encrypt import vigenere_encrypt, playfair_encrypt, hill_encrypt

st.title("Kriptografi Sederhana")

pilihan = st.selectbox("Pilih opsi:", ("Vigenere Cipher", "Playfair Cipher", "Hill Cipher"))

uploaded_file = st.file_uploader("Unggah file plain text (opsional)", type=["txt"])

if uploaded_file is not None:
    plain_text_parsed = uploaded_file.read().decode("utf-8")
    plain_text = st.text_input("Masukkan plain text : ", value=plain_text_parsed)

else:
    plain_text = st.text_input("Masukkan plain text : ")

key_text = st.text_input("Masukkan kunci : ")



if st.button("Proses Enkripsi", type='primary'):
    if not plain_text:
        st.error("Isi terlebih dahulu plain text")
        st.stop()
    
    if not key_text:
        st.error("Isi terlebih dahulu key text")
        st.stop()
    
    if not all(char.isalpha() for char in key_text):
        st.error("Kunci hanya boleh mengandung karakter alfabet.")
        st.stop()

    if pilihan != "Hill Cipher" and len(key_text) < 12:
        st.error("Kunci minimal terdiri dari 12 karakter")
        st.stop()

    trimmed_plain_text = plain_text.replace(" ", "")
    trimmed_key_text = key_text.replace(" ", "")
    
    if pilihan == "Vigenere Cipher":
        st.write("Memproses enkripsi menggunakan Vigenere Cipher...")
        hasil_enkripsi = vigenere_encrypt(trimmed_plain_text, trimmed_key_text)
        st.success(f"Hasil enkripsi: {hasil_enkripsi}")

    elif pilihan == "Playfair Cipher":
        st.write("Memproses enkripsi menggunakan Playfair Cipher...")
        hasil_enkripsi = playfair_encrypt(trimmed_plain_text, trimmed_key_text)
        st.success(f"Hasil enkripsi: {hasil_enkripsi}")

    elif pilihan == "Hill Cipher":
        st.write("Memproses enkripsi menggunakan Hill Cipher...")
        if len(trimmed_key_text) != 4:
            st.error("Untuk Hill Cipher, kunci harus terdiri dari 4 karakter.")
        else:
            hasil_enkripsi = hill_encrypt(trimmed_plain_text, trimmed_key_text)
            st.success(f"Hasil enkripsi: {hasil_enkripsi}")
    else:
        st.error("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")


st.markdown("---")
st.markdown("Dibuat oleh Karindra Rafi Linux H. / TI 22")
