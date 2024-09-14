import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data  
def load_data():
    df_all = pd.read_csv("../clean_df_all.csv")
    df_Aotizhongxin = pd.read_csv("../Air-quality-dataset/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    df_Changping = pd.read_csv("../Air-quality-dataset/PRSA_Data_Changping_20130301-20170228.csv")
    df_Dingling = pd.read_csv("../Air-quality-dataset/PRSA_Data_Dingling_20130301-20170228.csv")
    df_Dongsi = pd.read_csv("../Air-quality-dataset\PRSA_Data_Dongsi_20130301-20170228.csv")
    df_Guanyuan = pd.read_csv("../Air-quality-dataset\PRSA_Data_Guanyuan_20130301-20170228.csv")
    df_Gucheng = pd.read_csv("../Air-quality-dataset\PRSA_Data_Gucheng_20130301-20170228.csv")
    df_Huairou = pd.read_csv("../Air-quality-dataset\PRSA_Data_Huairou_20130301-20170228.csv")
    df_Nongzhanguan = pd.read_csv("../Air-quality-dataset\PRSA_Data_Nongzhanguan_20130301-20170228.csv")
    df_Shunyi = pd.read_csv("../Air-quality-dataset\PRSA_Data_Shunyi_20130301-20170228.csv")
    df_Tiantan = pd.read_csv("../Air-quality-dataset\PRSA_Data_Tiantan_20130301-20170228.csv")
    df_Wanliu = pd.read_csv("../Air-quality-dataset\PRSA_Data_Wanliu_20130301-20170228.csv")
    df_Wanshouxigong =pd.read_csv("../Air-quality-dataset\PRSA_Data_Wanshouxigong_20130301-20170228.csv")

    df_all['date_time'] = pd.to_datetime(df_all['date_time'])
    
    return df_all, df_Aotizhongxin, df_Changping, df_Dingling, df_Dongsi, df_Guanyuan, df_Gucheng, df_Huairou, df_Nongzhanguan, df_Shunyi, df_Tiantan, df_Wanliu, df_Wanshouxigong

df_all, df_Aotizhongxin, df_Changping, df_Dingling, df_Dongsi, df_Guanyuan, df_Gucheng, df_Huairou, df_Nongzhanguan, df_Shunyi, df_Tiantan, df_Wanliu, df_Wanshouxigong= load_data()


st.sidebar.image("../images/logo.png")
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.selectbox("Pilih Menu:", ["Home","Lihat Dataset", "Pertanyaan Satu", "Pertanyaan Dua", "Pertanyaan Tiga", "Pertanyaan Empat", "Kesimpulan"])


if menu == "Home":
    st.title("Air Quality Dataset")
    st.markdown("""
    Proyek Analisis Data: Air Quality Dataset\n
    Nama: Naufal Rafid Muhammad Faddila\n
    Email: naufal.rafid.mf@gmail.com\n
    ID Dicoding: naufalrafid
        """)
    st.subheader("Deskripsi Data")
    st.write(df_all.describe())  
    st.subheader("Dataframe")
    st.dataframe(df_all.head())
elif menu == "Lihat Dataset":
    st.sidebar.title("Dataset")
    dataset = st.sidebar.selectbox("Lihat Dataset:", ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"])

    if dataset == "Aotizhongxin":
        st.title("Aotizhongxin")
        st.subheader("Deskripsi Data")
        st.write(df_Aotizhongxin.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Aotizhongxin.head())

    elif dataset == "Changping":
        st.title("Changping")
        st.subheader("Deskripsi Data")
        st.write(df_Changping.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Changping.head())

    elif dataset == "Dingling":
        st.title("Dingling")
        st.subheader("Deskripsi Data")
        st.write(df_Dingling.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Dingling.head())
    
    elif dataset == "Dongsi":
        st.title("Dongsi")
        st.subheader("Deskripsi Data")
        st.write(df_Dongsi.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Dongsi.head())
    
    elif dataset == "Guanyuan":
        st.title("Guanyuan")
        st.subheader("Deskripsi Data")
        st.write(df_Guanyuan.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Guanyuan.head())
    
    elif dataset == "Gucheng":
        st.title("Gucheng")
        st.subheader("Deskripsi Data")
        st.write(df_Gucheng.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Gucheng.head())
    
    elif dataset == "Huairou":
        st.title("Huairou")
        st.subheader("Deskripsi Data")
        st.write(df_Huairou.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Huairou.head())
    
    elif dataset == "Nongzhanguan":
        st.title("Nongzhanguan")
        st.subheader("Deskripsi Data")
        st.write(df_Nongzhanguan.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Nongzhanguan.head())
    
    elif dataset == "Shunyi":
        st.title("Shunyi")
        st.subheader("Deskripsi Data")
        st.write(df_Shunyi.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Shunyi.head())
    
    elif dataset == "Tiantan":
        st.title("Tiantan")
        st.subheader("Deskripsi Data")
        st.write(df_Tiantan.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Tiantan.head())

    elif dataset == "Wanliu":
        st.title("Wanliu")
        st.subheader("Deskripsi Data")
        st.write(df_Wanliu.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Wanliu.head())
    
    elif dataset == "Wanshouxigong":
        st.title("Wanshouxigong")
        st.subheader("Deskripsi Data")
        st.write(df_Wanshouxigong.describe())  
        st.subheader("Dataframe")
        st.dataframe(df_Wanshouxigong.head())

elif menu == "Pertanyaan Satu":
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
        plt.clf()  

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
        plt.clf()  

elif menu == "Pertanyaan Dua":
    st.title("Bagaimana pengaruh konsentrasi NO2 dan CO sebagai polutan yang dihasilkan kendaraan bermotor terhadap kualitas udara ?")


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
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        plt.clf() 

elif menu == "Pertanyaan Tiga":
    st.title("Bagaimana pengaruh hujan terhadap polutan penyebab polusi udara?")

    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:
        st.subheader("Pengaruh Hujan terhadap Konsentrasi PM2.5")

        df_all['RAIN_GROUP'] = pd.cut(df_all['RAIN'], bins=[0, 1, 4, 8, 10], labels=['No Rain', 'Light Rain', 'Moderate Rain', 'Heavy Rain'])

        plt.figure(figsize=(12, 8))
        sns.boxplot(x='RAIN_GROUP', y='PM2.5', data=df_all)
        plt.title('Boxplot PM2.5 Berdasarkan Intensitas Hujan')
        plt.xticks(rotation=45)
        st.pyplot(plt)
        plt.clf()  

        rain_group_avg = df_all.groupby('RAIN_GROUP')['PM2.5'].mean().reset_index()

        plt.figure(figsize=(12, 6))
        sns.lineplot(x='RAIN_GROUP', y='PM2.5', data=rain_group_avg, marker='o', color='blue')
        plt.title('Rata-rata Konsentrasi PM2.5 Berdasarkan Intensitas Hujan')
        plt.xlabel('Kelompok Intensitas Hujan')
        plt.ylabel('Rata-rata Konsentrasi PM2.5')
        st.pyplot(plt)
        plt.clf() 

elif menu == "Pertanyaan Empat":
    st.title("Bagaimana hubungan antara konsentrasi NO2, dan CO dengan pembentukan O3 ?")

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
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(plt)
        plt.clf()  

        corr_matrix = df_all[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()

        plt.figure(figsize=(10, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Korelasi Antar Polutan')
        st.pyplot(plt)
        plt.clf()  

elif menu == "Kesimpulan":
    st.title("Kesimpulan")

    if df_all.empty:
        st.error("Data tidak tersedia. Pastikan file CSV telah dimuat dengan benar.")
    else:
        st.markdown("""
        Dari analisis di atas, dapat disimpulkan bahwa:

        1. **Kecepatan angin (WSPM)** berperan penting dalam penyebaran polutan. Ketika kecepatan angin tinggi, konsentrasi PM2.5 cenderung menurun karena polutan tersebar lebih luas, sehingga menciptakan tren negatif antara kecepatan angin dan konsentrasi PM2.5 karena polutan terbawa ke kawasan lain. Tetapi jika kecepatan angin sedang maka akan menambah persebaran polutan di kawasan tersebut, sehingga polutan menjadi meningkat bukan menurun.

        2. **Peningkatan konsentrasi CO dan NO₂** sering kali menunjukkan peningkatan aktivitas kendaraan bermotor atau pembakaran bahan bakar fosil. Hal ini menunjukkan bahwa kendaraan bermotor dan bahan bakar fosil berperan besar dalam kontribusi polutan yang menyebabkan polusi udara.

        3. **Hujan** membantu mengurangi konsentrasi polutan, termasuk PM2.5. Polutan terbawa oleh air hujan, menyebabkan penurunan yang signifikan pada distribusi PM2.5. Namun, dalam kondisi hujan lebat, PM2.5 dapat meningkat seiring intensitas hujan karena pengadukan partikel dari permukaan tanah atau reaksi lainnya.

        4. **NO₂ dan CO** mempengaruhi pembentukan O₃. Ketika kadar NO₂ naik, maka kadar O₃ akan menurun dan sebaliknya. NO₂ bisa mengkatalisasi reaksi yang mengurangi konsentrasi O₃ di atmosfer. **Tingkat CO yang tinggi** dapat memperlambat reaksi yang membentuk O₃.
        """)

