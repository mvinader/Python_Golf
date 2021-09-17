import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.write(f"""Estadísticas sobre los resultados de Tiger Woods""")

#PANDAS AS .HTML
tabla=pd.read_html('https://www.foxsports.com/golf/tiger-woods-player-stats?category=shots&groupId=1')
print(tabla)

#PANDAS AS .CSV
"""df = pd.read_clipboard()
df.to_excel("ShotsStats_TigerWoods.xlsx")
df.to_csv("ShotsStats_TigerWoods.csv")"""

datos = pd.read_csv("ShotsStats_TigerWoods.csv")
datos.describe()
datos.head()

datos[["EV", "AVG", "DR", "AVGDR", "ACC", "PUTT/H", "BIRD/R", "H/EAG"]].plot(kind="bar", subplots=True, title="Estadísticas para Tiger Woods")
grafico=datos[["EV", "AVG", "DR", "AVGDR", "ACC", "PUTT/H", "BIRD/R", "H/EAG"]].plot(kind="bar", title="Estadísticas para Tiger Woods")
plt.show()
#plt.savefig(fname=r"C:\Users\maviv", format='png')

st.dataframe(datos.iloc[:,[1,2,3,4,5,6,7,8,9]])
#st.bar_chart(datos)
#st.pyplot(datos)