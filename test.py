import pandas as pd

# Load the dataset
df = pd.read_csv("emails.csv")
df.columns = df.columns.str.lower()
words = ["money" , "free" , "win" ,  "urgent" , "act now", "limited time", "click here","Guaranteed" , "Be your own boss" , "Billion" , "Free gift" , "Giveaway" , "Miracle", "Please read" , "Winner" ]

spam_words = [w.lower() for w in words if w in df.columns]
df["spam_Score"] = df[spam_words].sum(axis=1)

print(df[["spam_Score"]].tail())
