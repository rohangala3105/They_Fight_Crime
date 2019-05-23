import pandas as pd

print("\nMost Occuring Characters : \n")


he_df = pd.read_csv("He_Seniment.csv",encoding='latin1')
she_df = pd.read_csv("She_Seniment.csv",encoding='latin1')

merged_df = pd.concat([he_df,she_df])

top_characters = merged_df['Character'].value_counts().index.tolist()[0:10]
for character in top_characters: print(character.strip())

