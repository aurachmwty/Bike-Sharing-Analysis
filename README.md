Bike Sharing Dashboard

Deskripsi Proyek

Proyek ini adalah dashboard interaktif berbasis Streamlit yang menganalisis pola penggunaan sepeda berdasarkan dataset Bike Sharing. Dashboard ini menyajikan berbagai visualisasi untuk menggali wawasan terkait pola penyewaan sepeda berdasarkan musim, cuaca, serta tren penggunaan harian dan jam tertentu.

Fitur Dashboard

Distribusi Penyewaan Berdasarkan Musim → Boxplot untuk melihat tren penyewaan sepeda berdasarkan musim.

Tren Penyewaan Per Bulan → Line chart untuk menunjukkan rata-rata jumlah penyewaan setiap bulan dalam setahun.

Pengaruh Cuaca terhadap Penyewaan → Scatter plot untuk melihat hubungan antara kondisi cuaca dan jumlah penyewaan.

Pola Penyewaan Sepeda Berdasarkan Jam → Heatmap untuk melihat jam-jam sibuk berdasarkan kondisi cuaca.

Dataset yang Digunakan

Dataset yang digunakan berasal dari Bike Sharing Dataset, dengan dua file utama:

day.csv → Data harian penyewaan sepeda.

hour.csv → Data per jam penyewaan sepeda.

Persyaratan Instalasi

Pastikan Anda memiliki Python dan pustaka berikut terinstal:

pip install streamlit pandas matplotlib seaborn

Cara Menjalankan Dashboard

Clone repository atau pindahkan file proyek ke komputer lokal.

Buka terminal atau command prompt, masuk ke direktori proyek.

Jalankan perintah berikut untuk memulai Streamlit:

streamlit run dashboard.py

Dashboard akan terbuka di browser dengan alamat http://localhost:8501.