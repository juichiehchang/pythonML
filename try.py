import pandas as pd
import locale

df = pd.read_csv("http://stats.moe.gov.tw/files/detail/103/103_student.csv")

locale.setlocale(locale.LC_NUMERIC, "")
df["�k�ͭp"] = df["�k�ͭp"].apply(locale.atof)
df["�k�ͭp"] = df["�k�ͭp"].apply(locale.atof)
