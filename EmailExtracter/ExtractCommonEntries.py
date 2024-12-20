import pandas as pd

# List of CSV file paths
csv_files = [
    'ZoomParticipantsJBC0624/participants_83925869884_10th_June.csv',
    'ZoomParticipantsJBC0624/participants_83925869884_11th_June.csv',
    'ZoomParticipantsJBC0624/participants_83925869884_12th_June.csv',
    'ZoomParticipantsJBC0624/participants_83925869884_13th_June.csv',
    'ZoomParticipantsJBC0624/participants_83925869884_14th_June.csv'
]

# Read each CSV file into a DataFrame
dfs = [pd.read_csv(file) for file in csv_files]

# Add a helper column for counting occurrences
for df in dfs:
    df['Helper'] = df['Name (Original Name)']

# Concatenate all DataFrames
concatenated = pd.concat(dfs)

# Count occurrences of each name
name_counts = concatenated['Helper'].value_counts()

# Identify names that appear in all DataFrames (i.e., 5 times)
common_names = name_counts[name_counts >= 4].index

# Filter the concatenated DataFrame to only include these common names
common_entries = concatenated[concatenated['Helper'].isin(common_names)]

# Drop the helper column
common_entries = common_entries.drop(columns=['Helper'])

# Save the result to a new CSV file
common_entries.to_csv('common_entries.csv', index=False)

print("Common entries have been saved to 'common_entries.csv'.")
