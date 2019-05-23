from textblob import TextBlob
import pandas as pd

he_df = pd.DataFrame()
she_df = pd.DataFrame()

with open('merged.txt') as file:
    for line in file:
        line = line.replace('They fight crime!','')
        
        line_split = line.split(" ")
        
        if(line_split[0] == "He's"):
            new_line = " ".join(line_split[1:])
            he_df = he_df.append({'Character':new_line,'Sentiment':TextBlob(new_line).sentiment.polarity}, ignore_index=True)
        
        if(line_split[0] == "She's"):
            new_line = " ".join(line_split[1:])
            she_df = she_df.append({'Character':new_line,'Sentiment':TextBlob(new_line).sentiment.polarity}, ignore_index=True)
    

he_df  = he_df.sort_values(['Sentiment'], ascending=[False]).reset_index(drop=True)
she_df  = she_df.sort_values(['Sentiment'], ascending=[False]).reset_index(drop=True)

he_df.to_csv ('He_Seniment.csv', index = None, header=True)
she_df.to_csv ('She_Seniment.csv', index = None, header=True)


print(he_df.head())
print(he_df.tail())
print(she_df.head())
print(she_df.tail())


pos_str = "He's "+he_df['Character'].iloc[0].strip()+" She's "+she_df['Character'].iloc[0].strip()+" They fight crime!"
neg_str = "He's "+he_df['Character'].iloc[-1].strip()+" She's "+she_df['Character'].iloc[-1].strip()+" They fight crime!"

print("\nPositive String : "+pos_str)
print("\nNegative String : "+neg_str)

