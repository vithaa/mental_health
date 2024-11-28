import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import sklearn

# Memuat data
data = pd.read_csv("cleaned_music.sav")

# Menghapus atau mengganti missing values
data['Hours per day'] = data['Hours per day'].fillna(data['Hours per day'].mean())
data = data.dropna(subset=['Age', 'Anxiety', 'Depression', 'Insomnia', 'OCD'])

# Encoding kolom-kolom kategorikal seperti genre musik dan gangguan mental
label_encoder = LabelEncoder()

# Memilih kolom genre musik yang ada
genre_columns = [
    'Fav genre_Classical', 'Fav genre_Country', 'Fav genre_EDM', 'Fav genre_Folk', 
    'Fav genre_Gospel', 'Fav genre_Hip hop', 'Fav genre_Jazz', 'Fav genre_K pop', 
    'Fav genre_Latin', 'Fav genre_Lofi', 'Fav genre_Metal', 'Fav genre_Pop', 
    'Fav genre_R&B', 'Fav genre_Rap', 'Fav genre_Rock', 'Fav genre_Video game music'
]

# Melakukan encoding pada kolom genre
for col in genre_columns:
    data[col] = label_encoder.fit_transform(data[col].astype(str))

# Mengonversi kolom gangguan mental menjadi numerik
mental_health_columns = ['Anxiety', 'Depression', 'Insomnia', 'OCD']
for col in mental_health_columns:
    data[col] = label_encoder.fit_transform(data[col].astype(str))

# Split dataset menjadi fitur dan target
X = data[['Age', 'Hours per day'] + genre_columns]
y = data['Anxiety']  # Misalnya kita ingin memprediksi gangguan kecemasan

# Split data untuk pelatihan dan pengujian model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediksi pada data uji
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Membuat aplikasi Streamlit
st.title("Prediksi Gangguan Mental Berdasarkan Musik Favorit")

# Input dari pengguna
age = st.slider("Usia Responden", min_value=10, max_value=100, value=25)
hours_per_day = st.slider("Jam Mendengarkan Musik per Hari", min_value=0, max_value=24, value=3)

# Pilihan Genre
genre_options = [
    'Classical', 'Country', 'EDM', 'Folk', 'Gospel', 
    'Hip hop', 'Jazz', 'K pop', 'Latin', 'Lofi', 
    'Metal', 'Pop', 'R&B', 'Rap', 'Rock', 'Video game music'
]

fav_genre = st.selectbox("Pilih Genre Musik Favorit", genre_options)

# Membuat kolom untuk genre yang dipilih
genre_column = f"Fav genre_{fav_genre}"

# Menyiapkan data input untuk prediksi
input_data = np.array([age, hours_per_day] + [0]*len(genre_columns))

# Set nilai 1 untuk genre yang dipilih
input_data[2 + genre_options.index(fav_genre)] = 1

# Membuat prediksi
prediction = model.predict([input_data])

# Menampilkan hasil prediksi
st.write(f"Hasil Prediksi: {'Cemas' if prediction[0] == 1 else 'Tidak Cemas'}")
st.write(f"Akurasi Model: {accuracy * 100:.2f}%")
