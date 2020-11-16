import pandas as pd
from pandas_profiling import ProfileReport as pr

df_igc_2018 = pd.read_excel("indices/2018/igc_2018.xlsx")
df_igc_2017 = pd.read_excel("indices/2017/igc_2017.xlsx")
df_igc_2016 = pd.read_excel("indices/2016/igc_2016.xlsx")

profile = pr(df_igc_2018, title='IGC de 2018', minimal=True, html={'style':{'full_width':True}})
profile.to_file("igc_2018.html")

profile = pr(df_igc_2017, title='IGC de 2017', minimal=True, html={'style':{'full_width':True}})
profile.to_file("igc_2017.html")

profile = pr(df_igc_2016, title='IGC de 2016', minimal=True, html={'style':{'full_width':True}})
profile.to_file("igc_2016.html")

