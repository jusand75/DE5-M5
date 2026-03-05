import pandas as pd

#pull the csv files into pandas
books = pd.read_csv("data/03_Library Systembook.csv")

#Track initial rows count
initial_book_rows = len(books)

#remove any lines that have NaN value in the book title
books = books.dropna(subset=["Books"])
books_rows_after_drop = len(books)
books_rows_dropped = initial_book_rows - books_rows_after_drop

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
#books["Days on Loan"] = (books["Book Returned"] - books["Book checkout"]).dt.days

def dataEnrich(df, col1, col2, outputCol):
    df[outputCol] = (df[col1] - df[col2]).dt.days
    return df

enrichedDF = dataEnrich(df= books, outputCol="Days on Loan", col1= "Book Returned", col2= "Book checkout" )

#metric to check length of file (no of rows)
print(f"There are {len(books)} rows in this dataset")

#load customers file 
customers = pd.read_csv("data/03_Library SystemCustomers.csv")

#remove NaN value entries in the Customers data
customers_cleaned = customers.dropna()

initial_customer_rows = len(customers)
customer_drop_count = 0 #counter for number of rows
customers_clean = customers.dropna() #drop #NA rows
customer_rows_after_drop = len(customers_clean)
customer_rows_dropped = initial_customer_rows - customer_rows_after_drop #calculate drop count

#create cleaned csv files
# enrichedDF.to_csv("data/books_cleaned.csv")
# customers_cleaned.to_csv("data/customers_cleaned.csv")

# To output create a dictionary with the metrics, turn it into a dataframe, use pd.to_csv('filepath')

#----------------------------- # Collect metrics # -----------------------------
metrics = {
  "Books: Initial Row Count": initial_book_rows,
  "Books: Row count after drop": books_rows_after_drop,
  "Books: Rows Dropped": books_rows_dropped,
  "Books: Data Types": books.dtypes.astype(str).to_dict(),
  #"books_unique": books.

  "Customers: Initial Row Count": initial_customer_rows,
  "Customers: Row count after drop": customer_rows_after_drop,
  "Customers: Rows Dropped": customer_rows_dropped,
  "Customers: Data Types": customers.dtypes.astype(str).to_dict() } 

#create dataframe from metrics list
metrics_df = pd.DataFrame.from_dict(metrics, orient="index", columns=["value"])

#create csv fle called 'metrics.csv' from dataframe
metrics_df.to_csv("metrics.csv")