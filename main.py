from covid19dh import covid19
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

negara  = input("Nama Negara  : ")

try:
    x, src = covid19(negara,verbose=False)

except:
        print("Koneksi Gagal!")
        quit()

if (str(x) == "None"):
    print("Negara Tidak Ada Dalam Index")

else:
    def  prepare(datatable):
        df = pd.DataFrame(datatable)
        pil =  df.loc[:,['administrative_area_level_1','date','confirmed','deaths','people_vaccinated']]
        # mean = pil[['confirmed','deaths','people_vaccinated']].mean()
        # pil[['confirmed','deaths','people_vaccinated']] = pil[['confirmed','deaths','people_vaccinated']].fillna(mean)
        pil  = pil.rename(columns={'administrative_area_level_1':'Country'})
        return pil

    def first(datatable1):
        df1 = prepare(datatable1)
        df1.to_csv("{}-Covid19.csv".format(negara),index=False)

    def second(datatable2):
        df2 = prepare(datatable2)
        # df2.describe()
        df2_sec = df2[['date','confirmed','deaths','people_vaccinated']]
        figure(figsize=(10, 5), dpi=80)
        plt.ticklabel_format(style='plain',axis='y')
        plt.plot(df2_sec.date,df2_sec.confirmed)
        plt.plot(df2_sec.date,df2_sec.deaths)
        plt.xlabel('Perbulan - Sekarang')
        plt.ylabel('Total Kasus')
        plt.legend(['Kasus','Meninggal'])
        

        return plt.show()

    def third():
        quit()


    print("Negara Ditemukan")
    print("1.Export Ke Csv File")
    print("2.Tampilkan Visual")
    print("0.Keluar") 
 
    choice = int(input("Pilih Sesuai Angka : "))
    if (choice == 1):
        first(x)
    elif (choice==2):
        second(x)
    else:
        third()
    df_x = prepare(x)
    print(df_x[['confirmed']].sum(),df_x[['deaths']].sum(),df_x[['people_vaccinated']].sum())
