import pandas as pd

# Load the dataset
df = pd.read_csv("emails.csv")
df.columns = df.columns.str.lower()  # make all columns lowercase

# Define spam words with weights (all lowercase keys)
words = {
    "money": 2,
    "free": 3,
    "win": 3, "urgent": 2, "act now": 3, "limited time": 2,
    "click here": 3, "guaranteed": 3, "be your own boss": 3, "billion": 3,
    "free gift": 3, "giveaway": 3, "miracle": 2, "please read": 2, "winner": 3,
    "dear friend": 1, "no cost": 2, "passwords": 3, "unlimited": 2, "buy now": 2,
    "exclusive": 2
}

# Only keep words that exist in your dataframe columns
spam_words = [w for w in words if w in df.columns]

# Calculate weighted spam score
df["spam_Score"] = sum(df[w] * words[w] for w in spam_words)

# Label emails: 1 = spam, 0 = not spam
df["label"] = df["spam_Score"].apply(lambda x: 1 if x > 2 else 0)

# Check results
# print(df[["spam_Score", "label"]].tail())

# print(df[["spam_Score", "label"]])
high_spam = df[df["spam_score"]>2]

print(df.columns)
# df.drop(columns=["spam_score"])
# df.to_csv('emails.csv' , index=False)

print(high_spam[["spam_score","label"]])