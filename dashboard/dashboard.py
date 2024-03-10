import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

data_bike_day = pd.read_csv('bike-sharing-data/day_clean.csv')
data_bike_hour = pd.read_csv('bike-sharing-data/hour_clean.csv')

def pertanyaan_1():
    st.markdown("## Pertanyaan 1")
    st.markdown("#### Seberapa besar perbandingan jumlah penyewaan sepeda pada tiap musim ?")
    st.write("Untuk mendapatkan jawaban dari pertanyaan diatas akan di tampilkan visualisasi pie chart yang dapat dilihat pada gambar dibawah ini")
    
     # Menghitung jumlah pengguna sepeda per kategori musim
    data_bike_day_count_season = data_bike_day.groupby('season')['count'].sum().reset_index()

    # membuat pie chart
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(data_bike_day_count_season['count'], labels=data_bike_day_count_season['season'], autopct='%1.1f%%', colors=plt.cm.Paired.colors, startangle=90)
    st.pyplot(fig)
    
    #keterangan
    st.write('Berdasarkan hasil visualisasi diatas, didapatkan hasil:')
    st.write('1. Fall (Musim Gugur): 32.2%')
    st.write('2. Summer (Musim Panas): 27.9%')
    st.write('3. Winter (Musim Dingin): 25.6%')
    st.write('4. Spring (Musim Semi): 14.3%')
    st.write('Perbandingan yang didapatkan cukup signifikan, dengan musim gugur yang menjadi musim favorit penyewaan sepeda, diikuti oleh musim panas dan musim dingin. Musim semi memiliki tingkat penyewaan yang terendah dibandingkan musim lainnya.')
    
def pertanyaan_2():
    st.markdown("## Pertanyaan 2")
    st.markdown("#### Seberapa Besar pengaruh cuaca terhadap penyewaan sepeda ?")
    st.write("Untuk mendapatkan jawaban dari pertanyaan diatas akan di tampilkan visualisasi bar chart yang dapat dilihat pada gambar dibawah ini")
    data_bike_day_count_weathersit = data_bike_day.groupby('weathersit')['count'].sum().reset_index()

    # Mengidentifikasi semua kategori cuaca yang mungkin
    semua_cuaca = ['Clear, Few clouds, Partly cloudy, Partly cloudy',
                    'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                    'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                    'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog']

    # Membuat dataframe dengan semua kategori cuaca dan menggabungkannya dengan data yang dihitung sebelumnya
    semua_cuaca = pd.DataFrame({'weathersit': semua_cuaca})
    data_bike_day_count_weathersit = pd.merge(semua_cuaca, data_bike_day_count_weathersit, on='weathersit', how='left').fillna(0)

    # Menggunakan variabel yang berbeda untuk plot
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(data_bike_day_count_weathersit['weathersit'], data_bike_day_count_weathersit['count'], color=['pink', 'dodgerblue', 'orange', 'limegreen'])

    # Menambahkan legenda pada diagram
    label_legenda = {'Clear, Few clouds, Partly cloudy, Partly cloudy': 'Clear, Few clouds, Partly cloudy, Partly cloudy',
                    'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist': 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                    'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds': 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                    'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog': 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'}
    warna_legenda = ['pink', 'dodgerblue', 'orange', 'limegreen']
    handles = [plt.Rectangle((0, 0), 1, 1, color=color, label=label) for color, label in zip(warna_legenda, label_legenda.values())]
    ax.legend(handles=handles, title='', loc='lower right', bbox_to_anchor=(1.25, -0.32))

    # Menambahkan Jumlah sebenarnya diatas bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    ax.set_xticks([]) 
    ax.set_xlabel('cuaca')
    ax.set_ylabel('Jumlah Penyewaan Sepeda dalam hari')
    ax.set_title('Perbandingan Jumlah Pengguna Sepeda Tiap Musim (hari)')
    st.pyplot(fig)
    
    #keterangan
    st.write('Dari data diatas dapat didapatkan hasil')
    st.write('1. Clear, Few clouds, Partly cloudy, Partly cloudy: 8.714 kali penyewaan')
    st.write('2. Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist: 8.362 kali penyewaan')
    st.write('3. Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds: 4639 kali penyewaan')
    st.write('4. Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog: 0 kali penyewaan')
    st.write('Cuaca memberikan pengaruh yang signifikan terhadap penyewaan sepeda, dimana penyewaan tertinggi terdapat pada cuaca 1 (Clear, Few clouds, Partly cloudy, Partly cloudy)'
             'kemudian disusul oleh cuaca 2 (Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist),'
             'Kemudian disusul oleh cuaca 3 (Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds)yang perbedaannya cukup jauh'
             'Bahkan pada musim 4 (Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog) tidak ada penyewaan sama sekali. '
             'dari hasil yang didapatkan diatas, cuaca sangat mempengaruhi jumlah penyewaan sepeda')
    
def pertanyaan_3():
    st.markdown("## Pertanyaan 3")
    st.write("#### Pada Bulan Berapa Penyewaan Sepeda Terbanyak ? ")
    st.write('Untuk mendapatkan jawaban dari pertanyaan diatas akan di tampilkan visualisasi bar chart yang dapat dilihat pada gambar dibawah ini')
    
    data_bike_day_count_month = data_bike_day.groupby('month')['count'].max()
    # Membuat diagram batang
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(data_bike_day_count_month.index, data_bike_day_count_month, color=plt.cm.Paired.colors)

    # Menambahkan label diatas bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

    ax.set_title('Penyewaan maximum setiap bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah penyewaan')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)
    
    #keterangan
    st.write('Pada visualisasi diatas ditampilkan jumlah maximum penyewaan pada setiap bulan yang ada,'
             'Dari keseluruhan penyewaan maximum tiap bulan, didapatkan hasil penyewaan tertinggi terjadi pada bulan september, yaitu sebanyak 8.714 kali penyewaan')
def pertanyaan_4():
    st.markdown("## Pertanyaan 4")
    st.write("#### Pada pukul Berapa Penyewaan Sepeda Banyak Terjadi ?")
    st.write('Untuk mendapatkan jawaban dari pertanyaan diatas akan di tampilkan visualisasi line chart yang dapat dilihat pada gambar dibawah ini')
    data_bike_hour_count_hour = data_bike_hour.groupby('hour')['count'].mean()

    # Membuat plot garis dengan warna biru cerah
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(range(24), data_bike_hour_count_hour.values, marker='o', linestyle='-', color='dodgerblue')  # Menggunakan range(24) untuk sumbu x dari 0 sampai 23

    # Menambahkan label dan judul
    ax.set_xlabel('Jam')
    ax.set_ylabel('Rata-rata Penyewaan Sepeda')
    ax.set_title('Rata-rata Penyewaan Sepeda setiap Jam')

    # Menandai titik tertinggi
    jam_tertinggi = data_bike_hour_count_hour.idxmax()
    rata_rata_tertinggi = data_bike_hour_count_hour.max()
    ax.annotate(f'Rata-rata Penyewaan {round(rata_rata_tertinggi, 2)}',
                xy=(jam_tertinggi, rata_rata_tertinggi),
                xytext=(jam_tertinggi + 0.5, rata_rata_tertinggi + 5),
                arrowprops=dict(facecolor='red', shrink=0.05))

# Menentukan batas sumbu x untuk setiap jam
    ax.set_xticks(range(24))
    plt.grid(True)
    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

    # Keterangan
    st.write('Visualisasi linechart sebelumnya merupakan hubungan antara rata-rata penyewaan tiap jam  sepeda dengan jam.' 
             'Dari hasil visualisasi tersebut didapatkan bahwa rata-rata penyewaan tertinggi terdapat pada pukul 17.00 dengan rata-rata penyewaan 461,45')
def main():
    st.title("Bike Sharing")
    st.sidebar.title("Bike Sharing Dashboard")
    st.sidebar.image('bicycle.png')
    menu_options = ["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4"]
    selected_menu = st.sidebar.selectbox("Pilih Pertanyaan", menu_options)

    

    # Navigasi antar pertanyaan
    if selected_menu == "Pertanyaan 1":
        pertanyaan_1()
    elif selected_menu == "Pertanyaan 2":
        pertanyaan_2()
    elif selected_menu == "Pertanyaan 3":
        pertanyaan_3()
    elif selected_menu == "Pertanyaan 4":
        pertanyaan_4()

if __name__ == "__main__":
    main()
