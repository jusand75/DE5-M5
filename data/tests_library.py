import pandas as pd
import unittest

#write unittest script
#create dataframe with 2 columns of dates
#apply function to dataframe to create third column
#compare values in thriird column to expected values.

df = pd.read_csv("data/books_clean.csv", usecols=["Book checkout", "Book Returned"])
#print(df)


# class TestOperations(unittest.TestCase):

#     def setUp(self):
#        self.myCalc = Calculator(8,2)

#     def test_sum(self):
#         self.assertEqual(self.myCalc.get_sum(), 10, "The answer is wrong")

#     def test_difference(self):
#         self.assertEqual(self.myCalc.get_difference(), 6, "The answer is wrong")

#     def test_product(self):
#         self.assertEqual(self.myCalc.get_product(), 16, "The answer is wrong")

#     def test_quotient(self):
#         self.assertEqual(self.myCalc.get_quotient(), 4, "The answer is wrong")

#if __name__ == "__main__":
    
    #unittest.main()