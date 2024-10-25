import pandas as pd

# Загрузка данных
df_2018 = pd.read_csv('Data/OpenDataZNO2018/OpenData2018.csv', sep=';', low_memory=False, encoding='cp1125')
df_2019 = pd.read_csv('Data/OpenDataZNO2019/Odata2019File.csv', sep=';', low_memory=False, encoding='cp1125')
df_2020 = pd.read_csv('Data/OpenDataZNO2020/Odata2020File.csv', sep=';', low_memory=False, encoding='cp1125')
df_2021 = pd.read_csv('Data/OpenDataZNO2021/Odata2021File.csv', sep=';', low_memory=False, encoding='cp1125')

# Добавляем год в каждый DataFrame
df_2018['Year'] = 2018
df_2019['Year'] = 2019
df_2020['Year'] = 2020
df_2021['Year'] = 2021

columns_to_keep = ['ukrball100', 'mathball100', 'physball100', 'year']  

raw_data_list = [df_2018, df_2019, df_2020, df_2021]

def clean_data(df):
    df.columns = df.columns.str.lower()

    missing_columns = [col for col in columns_to_keep if col not in df.columns]
    
    if missing_columns:
        print(f"Warning: Missing columns {missing_columns}. Skipping this dataframe.")
        return None  
    df = df.drop_duplicates()
    df = df.dropna(subset=['ukrball100', 'mathball100', 'physball100'])  

    for col in ['ukrball100', 'mathball100', 'physball100']:
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

    df = df[columns_to_keep] 
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    return df

filtered_data_list = [clean_data(df) for df in raw_data_list if clean_data(df) is not None]

df_all = pd.concat(filtered_data_list)

df_all.to_csv('cleaned_zno_data.csv', index=False, sep=';')

print("CSV file 'cleaned_zno_data.csv' created successfully.")