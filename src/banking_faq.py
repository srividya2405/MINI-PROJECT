import pandas as pd

faq_df = pd.read_csv("banking_faq.csv")

FAQS = dict(
    zip(
        faq_df["Question"].str.lower(),
        faq_df["Answer"]
    )
)