
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk memuat dan menggabungkan dataset
@st.cache_data  # Mengganti st.cache dengan st.cache_data
def load_data():
    # Memuat dataset Aotizhongxin, Changping, Dingling
    df_all = pd.read_csv("clean_df_all.csv")
    return df_all

# Panggil fungsi untuk memuat data
df_all = load_data()

# Sidebar untuk navigasi
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.selectbox("Pilih Analisis:", ["Home", "Pertanyaan Satu", "Pertanyaan Dua", "Pertanyaan Tiga", "Pertanyaan Empat"])

# Home Section
if menu == "Home":
    st.title("Air Quality Dataset")
    st.markdown("""
Proyek Analisis Data: Air Quality Dataset\n
Nama: Naufal Rafid Muhammad Faddila\n
Email: naufal.rafid.mf@gmail.com\n
ID Dicoding: naufalrafid
    """)

elif menu == "Pertanyaan 1":
    st.title("Bagaimana pengaruh kecepatan angin (WSPM) terhadap penyebaran konsentrasi PM2.5 selama musim Panas (juni hingga agustus)?")

    # Cek apakah dataset berhasil dimuat
    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:

        st.subheader("Hubungan Kecepatan Angin dengan Persebaran PM2.5")

        df_all['month'] = df_all['date_time'].dt.month

        dry_season_data = df_all[df_all['month'].isin([6, 7, 8])]

        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='WSPM', y='PM2.5', data=dry_season_data)
        plt.title('Hubungan Kecepatan Angin (WSPM) dengan PM2.5 Selama Musim Kemarau (Juni hingga Agustus)')
        plt.xlabel('Kecepatan Angin (WSPM)')
        plt.ylabel('Konsentrasi PM2.5')
        st.pyplot(plt)

        st.subheader("Hubungan Kecepatan Angin (WSPM) dengan PM2.5 Selama Musim Kemarau (Juni hingga Agustus)")
        dry_season_data = df_all[df_all['month'].isin([6, 7, 8])]

        monthly_avg = dry_season_data.groupby(['year', 'month']).agg({'WSPM': 'mean', 'PM2.5': 'mean'}).reset_index()

        plt.figure(figsize=(12, 6))
        sns.lineplot(x='WSPM', y='PM2.5', hue='month', data=dry_season_data, marker='o', palette='coolwarm')
        plt.title('Hubungan Kecepatan Angin (WSPM) dengan PM2.5 Selama Musim Kemarau (Juni hingga Agustus)')
        plt.xlabel('Kecepatan Angin (WSPM)')
        plt.ylabel('Konsentrasi PM2.5')
        plt.legend(title='Bulan', labels=['Juni', 'Juli', 'Agustus'])
        st.pyplot(plt)
        

elif menu == "Pertanyaan 2":
    st.title("Bagaimana pengaruh konsentrasi NO2 dan CO sebagai polutan yang dihasilkan kendaraan bermotor terhadap kualitas udara ?")

    # Cek apakah dataset berhasil dimuat
    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:
        st.subheader("Rata-rata Bulanan Konsentrasi Polutan")
    
        df_all['date_time_month'] = df_all['date_time'].dt.to_period('M')

        monthly_avg = df_all.groupby('date_time_month').agg({
            'CO': 'mean', 
            'NO2': 'mean',
            'PM2.5': 'mean',
            'PM10': 'mean',
            'SO2': 'mean',
            'O3': 'mean'
        }).reset_index()

        monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

        plt.figure(figsize=(14, 8))

        sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
        sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
        sns.lineplot(x='date_time_month', y='PM2.5', data=monthly_avg, label='PM2.5', color='green')
        sns.lineplot(x='date_time_month', y='PM10', data=monthly_avg, label='PM10', color='purple')
        sns.lineplot(x='date_time_month', y='SO2', data=monthly_avg, label='SO2', color='orange')
        sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='cyan')

        plt.title('Rata-rata Bulanan Konsentrasi Polutan')
        plt.xlabel('Bulan')
        plt.ylabel('Konsentrasi Polutan')

        plt.xticks(ticks=monthly_avg['date_time_month'], labels=monthly_avg['date_time_month'].dt.strftime('%Y-%m'), rotation=45)

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
    


elif menu == "Pertanyaan 3":
    st.title("Bagaimana pengaruh hujan terhadap polutan penyebab polusi udara?")

    # Cek apakah dataset berhasil dimuat
    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:
        st.subheader("Bagaimana pengaruh hujan terhadap polutan penyebab polusi udara?")

        df_all['RAIN_GROUP'] = pd.cut(df_all['RAIN'], bins=[0, 1, 4, 8, 10], labels=['No Rain', 'Light Rain', 'Moderate Rain', 'Heavy Rain'])

        plt.figure(figsize=(12, 8))
        sns.boxplot(x='RAIN_GROUP', y='PM2.5', data=df_all)
        plt.title('Boxplot of PM2.5 by Rain Intensity')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        df_all['RAIN_GROUP'] = pd.cut(df_all['RAIN'], bins=[0, 1, 4, 8, 10], labels=['No Rain', 'Light Rain', 'Moderate Rain', 'Heavy Rain'])

        rain_group_avg = df_all.groupby('RAIN_GROUP')['PM2.5'].mean().reset_index()

        plt.figure(figsize=(12, 6))
        sns.lineplot(x='RAIN_GROUP', y='PM2.5', data=rain_group_avg, marker='o', color='blue')

        plt.title('Rata-rata Konsentrasi PM2.5 Berdasarkan Intensitas Hujan')
        plt.xlabel('Kelompok Intensitas Hujan')
        plt.ylabel('Rata-rata Konsentrasi PM2.5')

        st.pyplot(plt)

    



elif menu == "Pertanyaan 4":
    st.title("Bagaimana hubungan antara konsentrasi NO2, dan CO dengan pembentukan O3 ?")

    # Cek apakah dataset berhasil dimuat
    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:
        st.subheader("Konsentrasi NO2, CO, dan O3 Bulanan")

        df_all['date_time_month'] = df_all['date_time'].dt.to_period('M')

        monthly_avg = df_all.groupby('date_time_month').agg({'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'}).reset_index()

        monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

        plt.figure(figsize=(12, 6))

        sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
        sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
        sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='green')

        plt.title('Konsentrasi NO2, CO, dan O3 Bulanan')
        plt.xlabel('Bulan')
        plt.ylabel('Konsentrasi Polutan (NO2, CO, O3)')
        plt.legend()

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)

        corr_matrix = df_all[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM', 'TEMP', 'RAIN']].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Heatmap Korelasi Antara Variabel Polutan dan Faktor Lingkungan')
        corr_matrix = df_all[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'WSPM', 'TEMP', 'RAIN']].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Heatmap Korelasi Antara Variabel Polutan dan Faktor Lingkungan')
        plt.show()


        st.subheader("Kesimpulan")
        st.markdown("""
        Dari analisis di atas, dapat disimpulkan bahwa:

        1. **Kecepatan angin (WSPM)** berperan penting dalam penyebaran polutan. Ketika kecepatan angin tinggi, konsentrasi PM2.5 cenderung menurun karena polutan tersebar lebih luas, sehingga menciptakan tren negatif antara kecepatan angin dan konsentrasi PM2.5.

        2. **Peningkatan konsentrasi CO dan NO₂** sering kali menunjukkan peningkatan aktivitas kendaraan bermotor atau pembakaran bahan bakar fosil. Hal ini menunjukkan bahwa kendaraan bermotor dan bahan bakar fosil berperan besar dalam kontribusi polutan yang menyebabkan polusi udara.

        3. **Hujan** membantu mengurangi konsentrasi polutan, termasuk PM2.5. Polutan terbawa oleh air hujan, menyebabkan penurunan yang signifikan pada distribusi PM2.5. Namun, dalam kondisi hujan lebat, PM2.5 dapat meningkat sementara karena pengadukan partikel dari permukaan tanah atau reaksi lainnya.

        4. **NO₂ dan CO** mempengaruhi pembentukan O₃. Ketika kadar NO₂ naik, maka kadar O₃ akan menurun dan sebaliknya. NO₂ bisa mengkatalisasi reaksi yang mengurangi konsentrasi O₃ di atmosfer.

        5. **Tingkat CO yang tinggi** dapat memperlambat reaksi yang membentuk O₃.
        """)

