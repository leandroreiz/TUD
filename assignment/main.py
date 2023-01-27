# Imports
import dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def main():
  # Collect the data online
  raw_data = dataset.collect('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')

  # Preprocess the data
  data = dataset.preprocess(raw_data)

  # Create a pandas DataFrame from the rows
  df = pd.DataFrame(data)

  # Convert the categorical features into numerical values using pandas' get_dummies function
  df = pd.get_dummies(df)

  # The input data is all the columns except the target column
  X = df.drop(['income_<=50K', 'income_>50K'], axis=1)

  # The output data is the target column
  y = df[['income_<=50K', 'income_>50K']]

  # Split the data into training and test sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

  # Create the random forest classifier and train it on the training data
  classifier = RandomForestClassifier()
  classifier.fit(X_train, y_train)

  # Test the classifier on the test data
  predictions = classifier.predict(X_test)

  # Evaluate the accuracy of the classifier
  accuracy = (predictions == y_test).mean()

  # Printing results
  print('Accuracy for incomes less or equal than 50K: {:.2f}%'.format(accuracy['income_<=50K'] * 100))
  print('Accuracy for incomes greater than 50K: {:.2f}%'.format(accuracy['income_>50K'] * 100))
  print('Total Accuracy: {:.2f}%'.format(((accuracy['income_<=50K'] + accuracy['income_>50K']) * 100) / 2))


if __name__ == '__main__':
  main()
