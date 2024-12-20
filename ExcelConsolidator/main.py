import pandas as pd
import os
import glob
import warnings
warnings.filterwarnings('ignore')
# use glob to get all the csv files
# in the folder
path = os.getcwd() + '\Input'
print(path)
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
df_consolidate = pd.DataFrame()
# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_excel(f,dtype=object)
    print(df.shape)
    # print filename
    print('File Name:', f.split("\\")[-1])
    period  = f.split("\\")[-1]
    print(period)
    df['Period'] = period.split(".")[0]
    df = df.groupby(['Buyer Email Address','Period'])[['Sale Amount']].sum().reset_index()
    print(df['Sale Amount'])
    df_consolidate = df_consolidate.append(df)

print(df_consolidate.tail())
df_consolidate_pivot= df_consolidate.pivot(index='Buyer Email Address', columns='Period', values='Sale Amount')
print(df_consolidate_pivot.tail())

df_consolidate_pivot.to_excel('Consolidated.xlsx')