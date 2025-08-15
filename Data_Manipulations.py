import pandas as pd

spam_df = pd.read_csv("spam_emails.csv")
ham_df = pd.read_csv("ham_emails.csv")

df = pd.concat([spam_df, ham_df], ignore_index=True)

# Save the merged file
df.to_csv("emails.csv", index=False)

print("Merged into emails.csv successfully.")
