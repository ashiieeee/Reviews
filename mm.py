import pandas as pd
# Read our dataset using read_csv()
review = pd.read_csv('reviews.csv')
review = bbc_text.rename(columns = {'text': 'review'}, inplace = False)
review.head()