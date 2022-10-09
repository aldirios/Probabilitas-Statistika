import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import warnings ##untuk mengabaikan perintah warning pada seaborn
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set(style="white",color_codes=True)

def histogram():    
    akta=pd.read_csv("akta.csv")
    akta=akta.groupby('nama_kabupaten_kota')
    akta=akta[['jumlah']].mean()
    
    x =np.arange(6)
    y =akta['jumlah']
    
    fig,ax=plt.subplots()
    ax.bar(x,y,color='yellow')
    plt.title("Rata-rata Pembuatan Akta kematian Daerah D.K.I Jakarta tahun 2019")
    plt.xlabel("Kabupaten")
    plt.ylabel("Jumlah")
    plt.xticks(rotation=90)
    ax.set_xticklabels([0]+list(akta.index))
    plt.show()

def kde():
    akta=pd.read_csv("akta.csv")
    sns.FacetGrid(akta,hue="nama_kabupaten_kota",size=6).map(sns.kdeplot,"jumlah").add_legend()
    plt.show()
    
    
def menu():
    x=1
    while x==1:
        print("=========== Visualisasi Data ===========")
        print("= 1. Histogram                         =")
        print("= 2. Kernel Density Estimation         =")
        print("= 3. exit                              =")    
        try:
            pilihan=int(input("Masukkan pilihan : "))
        except ValueError:
            print ("Masukkan pilihan dengan angka.")
            input ("Tekan Enter untuk Melanjutkan...")
            x=1
        if pilihan==1:
            histogram()
            x=1
        elif pilihan==2:
            kde()
            x=1
        elif pilihan==3:
            x=0
        else:
            x=1
            
menu()