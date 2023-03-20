import pandas as pd

# import dataset
dataset = pd.read_csv("Coursera.csv")

# dataset information
dataset.shape
dataset.info
dataset.head(5)

# select features
dataset = dataset.drop(columns=['University', 'Course Rating', 'Course URL'])
dataset.head(5)

# data preprocessing
dataset['Course Name'] = dataset['Course Name'].str.replace(' ',',')
dataset['Course Name'] = dataset['Course Name'].str.replace(',,',',')
dataset['Course Name'] = dataset['Course Name'].str.replace(':','')
dataset['Course Description'] = dataset['Course Description'].str.replace(' ',',')
dataset['Course Description'] = dataset['Course Description'].str.replace(',,',',')
dataset['Course Description'] = dataset['Course Description'].str.replace('_','')
dataset['Course Description'] = dataset['Course Description'].str.replace(':','')
dataset['Course Description'] = dataset['Course Description'].str.replace('(','')
dataset['Course Description'] = dataset['Course Description'].str.replace(')','')
dataset['Skills'] = dataset['Skills'].str.replace('(','')
dataset['Skills'] = dataset['Skills'].str.replace(')','')