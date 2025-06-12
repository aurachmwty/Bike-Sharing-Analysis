import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load dataset
day_df =pd.read_csv("dashboard/day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

hour_df = pd.read_csv("dashboard/hour.csv")
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar controls
st.sidebar.title("Bike Sharing Analysis")
start_date = st.sidebar.date_input("Mulai Tanggal", day_df['dteday'].min())
end_date = st.sidebar.date_input("Akhir Tanggal", day_df['dteday'].max())

season_filter = st.sidebar.multiselect(
    "Pilih Musim:", [1, 2, 3, 4], default=[1, 2, 3, 4],
    format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1]
)

weather_filter = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca:", [1, 2, 3], default=[1, 2, 3],
    format_func=lambda x: ["Cerah", "Berawan", "Hujan/Sangat Buruk"][x-1]
)

hour_filter = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, (0, 23))

option = st.sidebar.selectbox("Pilih Analisis:", [
    "Distribusi Penyewaan Berdasarkan Musim",
    "Tren Penyewaan Per Bulan",
    "Pengaruh Cuaca terhadap Penyewaan",
    "Pola Penyewaan Sepeda Berdasarkan Jam"
])

# Filter dataset
day_filtered = day_df[(day_df['dteday'] >= pd.Timestamp(start_date)) &
                       (day_df['dteday'] <= pd.Timestamp(end_date)) &
                       (day_df['season'].isin(season_filter))]

hour_filtered = hour_df[(hour_df['dteday'] >= pd.Timestamp(start_date)) &
                         (hour_df['dteday'] <= pd.Timestamp(end_date)) &
                         (hour_df['weathersit'].isin(weather_filter)) &
                         (hour_df['hr'].between(hour_filter[0], hour_filter[1]))]

# Visualizations
if option == "Distribusi Penyewaan Berdasarkan Musim":
    st.title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=day_filtered, palette='Set2', ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
    st.pyplot(fig)

elif option == "Tren Penyewaan Per Bulan":
    st.title("Tren Rata-Rata Penyewaan Sepeda Per Bulan")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='mnth', y='cnt', data=day_filtered, ci=None, marker='o', color='b', ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.grid()
    st.pyplot(fig)

elif option == "Pengaruh Cuaca terhadap Penyewaan":
    st.title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='weathersit', y='cnt', data=hour_filtered, alpha=0.5, hue='weathersit', palette='coolwarm', ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["Cerah", "Berawan", "Hujan/Sangat Buruk"])
    ax.legend(title="Kondisi Cuaca")
    st.pyplot(fig)

elif option == "Pola Penyewaan Sepeda Berdasarkan Jam":
    st.title("Pola Penggunaan Sepeda Berdasarkan Jam dan Kondisi Cuaca")
    hour_pivot = hour_filtered.pivot_table(values='cnt', index='hr', columns='weathersit', aggfunc='mean')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(hour_pivot, cmap='YlGnBu', annot=True, fmt='.1f', ax=ax)
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jam")
    st.pyplot(fig)