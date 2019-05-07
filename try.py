import pandas as pd
import locale

df = pd.read_csv("http://stats.moe.gov.tw/files/detail/103/103_student.csv")

locale.setlocale(locale.LC_NUMERIC, "")
df["男生計"] = df["男生計"].apply(locale.atof)
df["女生計"] = df["女生計"].apply(locale.atof)
