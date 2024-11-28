{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Menentukan Library yang digunakan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'matplotlib'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m \n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m  \u001b[38;5;21;01mplt\u001b[39;00m \n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mseaborn\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01msns\u001b[39;00m \n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmissingno\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mmsno\u001b[39;00m \n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'matplotlib'"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "import matplotlib.pyplot as  plt \n",
    "import seaborn as sns \n",
    "import missingno as msno \n",
    "import sklearn\n",
    "print(sklearn.__version__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Load dataset\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"musik.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. menampilkan info dari dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 736 entries, 0 to 735\n",
      "Data columns (total 33 columns):\n",
      " #   Column                        Non-Null Count  Dtype  \n",
      "---  ------                        --------------  -----  \n",
      " 0   Timestamp                     736 non-null    object \n",
      " 1   Age                           735 non-null    float64\n",
      " 2   Primary streaming service     735 non-null    object \n",
      " 3   Hours per day                 736 non-null    float64\n",
      " 4   While working                 733 non-null    object \n",
      " 5   Instrumentalist               732 non-null    object \n",
      " 6   Composer                      735 non-null    object \n",
      " 7   Fav genre                     736 non-null    object \n",
      " 8   Exploratory                   736 non-null    object \n",
      " 9   Foreign languages             732 non-null    object \n",
      " 10  BPM                           629 non-null    float64\n",
      " 11  Frequency [Classical]         736 non-null    object \n",
      " 12  Frequency [Country]           736 non-null    object \n",
      " 13  Frequency [EDM]               736 non-null    object \n",
      " 14  Frequency [Folk]              736 non-null    object \n",
      " 15  Frequency [Gospel]            736 non-null    object \n",
      " 16  Frequency [Hip hop]           736 non-null    object \n",
      " 17  Frequency [Jazz]              736 non-null    object \n",
      " 18  Frequency [K pop]             736 non-null    object \n",
      " 19  Frequency [Latin]             736 non-null    object \n",
      " 20  Frequency [Lofi]              736 non-null    object \n",
      " 21  Frequency [Metal]             736 non-null    object \n",
      " 22  Frequency [Pop]               736 non-null    object \n",
      " 23  Frequency [R&B]               736 non-null    object \n",
      " 24  Frequency [Rap]               736 non-null    object \n",
      " 25  Frequency [Rock]              736 non-null    object \n",
      " 26  Frequency [Video game music]  736 non-null    object \n",
      " 27  Anxiety                       736 non-null    float64\n",
      " 28  Depression                    736 non-null    float64\n",
      " 29  Insomnia                      736 non-null    float64\n",
      " 30  OCD                           736 non-null    float64\n",
      " 31  Music effects                 728 non-null    object \n",
      " 32  Permissions                   736 non-null    object \n",
      "dtypes: float64(7), object(26)\n",
      "memory usage: 189.9+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Mengecek dan menangani missing values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Timestamp                         0\n",
      "Age                               1\n",
      "Primary streaming service         1\n",
      "Hours per day                     0\n",
      "While working                     3\n",
      "Instrumentalist                   4\n",
      "Composer                          1\n",
      "Fav genre                         0\n",
      "Exploratory                       0\n",
      "Foreign languages                 4\n",
      "BPM                             107\n",
      "Frequency [Classical]             0\n",
      "Frequency [Country]               0\n",
      "Frequency [EDM]                   0\n",
      "Frequency [Folk]                  0\n",
      "Frequency [Gospel]                0\n",
      "Frequency [Hip hop]               0\n",
      "Frequency [Jazz]                  0\n",
      "Frequency [K pop]                 0\n",
      "Frequency [Latin]                 0\n",
      "Frequency [Lofi]                  0\n",
      "Frequency [Metal]                 0\n",
      "Frequency [Pop]                   0\n",
      "Frequency [R&B]                   0\n",
      "Frequency [Rap]                   0\n",
      "Frequency [Rock]                  0\n",
      "Frequency [Video game music]      0\n",
      "Anxiety                           0\n",
      "Depression                        0\n",
      "Insomnia                          0\n",
      "OCD                               0\n",
      "Music effects                     8\n",
      "Permissions                       0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Mengecek missing values\n",
    "print(data.isnull().sum())\n",
    "\n",
    "#Mengisi missing values untuk kolom numerik dengan rata-rata\n",
    "data['Hours per day'] = data['Hours per day'].fillna(data['Hours per day'].mean())\n",
    "\n",
    "# Drop baris dengan missing values di kolom penting\n",
    "data = data.dropna(subset=['Fav genre', 'Age', 'Anxiety', 'Depression', 'Insomnia', 'OCD'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Memastikan format data \n",
    "    pastikan kolom memiliki tipe data yang benar terutama untuk \n",
    "    variabel yang digunakan dalam model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pastikan kolom usia dan jam mendengarkan musik numerik\n",
    "data['Age'] = pd.to_numeric(data['Age'], errors='coerce')\n",
    "data['Hours per day'] = pd.to_numeric(data['Hours per day'], errors='coerce')\n",
    "\n",
    "# Pastikan kolom genre adalah kategorikal\n",
    "data['Fav genre'] = data['Fav genre'].astype('category')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Menangani Outlier\n",
    "    Cek dan tangani data yang tidak masuk akal (terlalu kecil/\n",
    "    terlalu besar) atau jam mendengarkan musik perhari yang tidak \n",
    "    masuk akal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Hapus outlier pada kolom Age dan Hours per day\n",
    "data = data[(data['Age'] > 10) & (data['Age'] < 100)]\n",
    "data = data[(data['Hours per day'] >= 0) & (data['Hours per day'] <= 24)]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Encoding untuk Variabel Kategorikal\n",
    "   Variabel kategorikal seperti Fav genre perlu dikonversi menjadi \n",
    "   format numerik atau encoding agar dapat digunakan oleh model \n",
    "   machine learning."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import OneHotEncoder\n",
    "\n",
    "# One-hot encoding untuk genre\n",
    "encoder = OneHotEncoder(handle_unknown='ignore')\n",
    "encoded_genre = pd.DataFrame(encoder.fit_transform(data[['Fav genre']]).toarray(), columns=encoder.get_feature_names_out(['Fav genre']))\n",
    "\n",
    "# Gabungkan kembali ke data utama\n",
    "data = pd.concat([data.reset_index(drop=True), encoded_genre.reset_index(drop=True)], axis=1)\n",
    "\n",
    "# Drop kolom asli 'Fav genre'\n",
    "data = data.drop(columns=['Fav genre'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Menyiapkan dataset\n",
    "    Pisahkan data menjadi fitur (X) dan target (y) untuk model \n",
    "    machine learning."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fitur\n",
    "X = data[['Age', 'Hours per day'] + list(encoded_genre.columns)]  # Tambahkan kolom hasil encoding\n",
    "\n",
    "# Target\n",
    "y = data[['Anxiety', 'Depression', 'Insomnia', 'OCD']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Menyimpan data yang telah diproses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Simpan dataset bersih\n",
    "data.to_csv(\"cleaned_musik.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
