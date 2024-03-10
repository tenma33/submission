import streamlit as st


# Judul dashboard
st.title("VISUALISASI DATA BIKE")

 
st.write(
    """
    1.  Visualisasi Bar perbandingan pengguna sepeda tiap musim data bike
    Dari Hasil Visualisasi pada pertanyaan 1 didapatkan bahwa pada data bike dan hour mempunyai data yang sama yaitu pengunaan terbanyak terdapat pada musim 3 dan terendah pada musim 1, namun pada data ini tidak dijelaskan keterangan musimnya, yang 3 musim apa, begitupun nilai lainnya, akan didapatkan keterangan lebih jelas jika nilai dari musimnya di ketahui.
    """
)
# Tampilkan gambar lokal
st.image('bar_bike_day.png', caption="Gambar Lokal", use_column_width=True)

st.write(
    """
    2.  Visualisasi Bar perbandingan pengguna sepeda tiap bulan
    ada visualisasi data kedua didapatkan hasil sama pula, penggunaan yang terbanyak terdapat pada bulan 8 dengan jumlah sekitar 360.000
    """
)
# Tampilkan gambar lokal
st.image('plot_bike_day.png', caption="Gambar Lokal", use_column_width=True)

