import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings  ## untuk mengabaikan perintah warning pada seaborn

warnings.filterwarnings("ignore")
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal'
        }

df = pd.read_csv("Mall_Customers.csv")
data = df.dropna(subset=['CustomerID', 'Gender', 'Annual Income'])


def histogram():
    dt=data.sort_values(by=['Age'])
    dt=dt[dt['Age']==5,10]
    x = dt['Age']
    y = dt['Spending Score']
    
    fig, ax = plt.subplots()
    ax.bar(x, y, 0.8, color='yellow')
    plt.title("Rata-rata Konsumtif dalam Belanja di Mall Berdasarkan Umur", fontdict=font)
    plt.xlabel("Umur", fontdict=font)
    plt.ylabel("Skor Konsumtif", fontdict=font)
    plt.show()


def kde():
    sns.FacetGrid(df, hue="Gender", size=7).map(sns.kdeplot, "Age", shade=True).add_legend()

    plt.xlabel('Umur', fontsize=14, fontdict=font)
    plt.show()


def box_plot():
    sns.boxplot(data['Gender'], data['Spending Score'])
    plt.show()

def linearRegression(data):
    x2 = []
    y2 = []
    xy = []
    n = len(data[0])
    for x in data[0]:
        x2.append(x ** 2)
    for y in data[0]:
        y2.append(y ** 2)

    i = 0
    while i < n:
        dump = data[0][i] * data[1][i]
        xy.append(dump)
        i += 1
    jmlhx = sum(data[0])
    jmlhy = sum(data[1])
    jmlhx2 = sum(x2)
    jmlhxy = sum(xy)
    a = ((jmlhy * jmlhx2) - (jmlhx * jmlhxy)) / (n * jmlhx2 - (jmlhx ** 2))
    b = ((n * jmlhxy) - (jmlhx * jmlhy)) / (n * jmlhx2 - (jmlhx ** 2))
    return a, b


def scatter_plot(dataProses):
    a, b = linearRegression(dataProses)
    print("Nilai a = %.4f" % a)
    print("Nilai b = %.4f" % b)

    def f1(keanggotaan, a, b):
        hit = []
        for x in keanggotaan:
            y = b * x + a
            hit.append(y)
        return hit

    plt.scatter(dataProses[0], dataProses[1], label='Data Aktual', s=10)
    plt.plot(dataProses[0], f1(dataProses[0], a, b), c='k', label='Hasil Regresi', linewidth=0.5)
    plt.title("Hasil Regresi Linear Sederhana", fontdict=font)
    plt.ylabel("Skor Konsumtif",fontdict=font)
    plt.xlabel("Umur", fontdict=font)
    plt.legend()
    fig = plt.figure(1)
    fig.canvas.set_window_title("regresi sederhana")
    plt.show()


def menu():
    loop = True
    while loop:
        try:
            print("=========== Visualisasi Data ===========")
            print("= 1. Histogram                         =")
            print("= 2. Kernel Density Estimation         =")
            print("= 3. Box Plot                          =")
            print("= 4. Regresi Linear                    =")
            print("= 5. exit                              =")
            pilihan = int(input("Masukkan pilihan : "))

            if pilihan == 1:
                histogram()

            elif pilihan == 2:
                kde()

            elif pilihan == 3:
                box_plot()

            elif pilihan == 4:
                scatter_plot([data['Age'], data['Spending Score']])

            elif pilihan == 5:
                loop = False

            else:
                print("Masukkan pilihan yang telah tersedia.")
                input("Tekan Enter untuk Melanjutkan...")

        except ValueError:
            print("Masukkan pilihan dengan angka.")
            input("Tekan Enter untuk Melanjutkan...")


menu()
