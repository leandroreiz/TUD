import csv
import urllib.request

def collect(url):
  """Receives a `string` with a URL as parameter and returns a `DictReader[str]` as result."""
  # Download the CSV file from the URL
  response = urllib.request.urlopen(url)

  # Read the CSV file from the response
  csv_data = response.read().decode('utf-8')

  # Create a CSV reader
  csv_dict = csv.DictReader(csv_data.splitlines(), delimiter=',', fieldnames=['age', 'workclass', 'final_weight', 'education', 'education_number', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income'])

  return csv_dict

def preprocess(data):
  '''Receives a `DictReader[str]` and removes whitespace from the values contained within it. Returns a `list` with the dictionaries cleaned.
  '''
  # Create an empty list
  cleaned_data = [];

  # Iterate over the rows of the data
  for row in data:
    # Strip the whitespace from the values in the row
    row_stripped = {key: value.strip() for key, value in row.items()}

    # Convert numeric values to integers
    for key, value in row_stripped.items():
      if value.isnumeric():
        row_stripped[key] = int(value)

    # Append the rows with the stripped whitespaces to the list
    cleaned_data.append(row_stripped)

  # Return the list cleaned
  return cleaned_data
