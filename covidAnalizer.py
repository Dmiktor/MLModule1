import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_zno_data.csv', sep=';')

df_grouped = df.groupby('year').mean()

df_grouped['average_all'] = df_grouped[['ukrball100', 'mathball100', 'physball100']].mean(axis=1)
plt.figure(figsize=(10, 8))

# Установка фиксированных значений по оси X и Y
years = df_grouped.index

plt.subplot(2, 2, 1)
plt.plot(years, df_grouped['ukrball100'], marker='o', color='black', label='Ukrainian')
plt.title('Average Ukrainian Score by Year')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.ylim(100, 200) 
plt.xticks(years) 
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(years, df_grouped['mathball100'], marker='o', color='black', label='Math')
plt.title('Average Math Score by Year')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.ylim(100, 200) 
plt.xticks(years)   
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(years, df_grouped['physball100'], marker='o', color='black', label='Physics')
plt.title('Average Physics Score by Year')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.ylim(100, 200)
plt.xticks(years) 
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(years, df_grouped['average_all'], marker='o', color='black', label='Average of All Subjects')
plt.title('Average Score by Year (All Subjects)')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.ylim(100, 200)  
plt.xticks(years)  
plt.grid(True)

plt.savefig('average_scores_by_year.png', dpi=300)
plt.tight_layout()
plt.show()