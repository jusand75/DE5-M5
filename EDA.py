import pandas as pd

#pull the csv files into pandas
books = pd.read_csv("data/03_Library Systembook.csv")


#remove any lines that have NaN value in the book title
books = books.dropna(subset=["Books"])

#replace the '2 weeks' string with a value of 14
books["Days allowed to borrow"] = books["Days allowed to borrow"].map({
    "2 weeks": 14
})

#Remove quotes from Book checkout column (includes function to replace impossible value)
def fix_invalid_date(x):
    if x == "32/05/2023":
        return "31/05/2023"
    return x
books["Book checkout"] = books["Book checkout"].apply(fix_invalid_date)
books["Book checkout"] = books["Book checkout"].str.replace('"', '', regex=True)

#convert date strings to datetime format
date_cols = ["Book checkout", "Book Returned"]
books[date_cols] = books[date_cols].apply(pd.to_datetime, dayfirst=True, errors="coerce")

#add column to calculate days on loan
books["Days on Loan"] = (books["Book Returned"] - books["Book checkout"]).dt.days

#load customers file 
customers = pd.read_csv("data/03_Library SystemCustomers.csv")

#remove NaN value entries in the Customers data
customers_cleaned = customers.dropna()

#create cleaned csv files
books.to_csv("books_cleaned.csv")
customers_cleaned.to_csv("customers_cleaned.csv")