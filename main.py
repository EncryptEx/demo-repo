import pandas 

def load_data(file_path):
    """Load data from a CSV file into a pandas DataFrame."""
    try:
        data = pandas.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pandas.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pandas.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None
    
    
def analyze_data(data):
    """Perform basic analysis on the DataFrame."""
    if data is not None:
        print("Data Summary:")
        print(data.describe())
        print("\nMissing Values:")
        print(data.isnull().sum())
    else:
        print("No data to analyze.")