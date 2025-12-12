import pandas 

def main():
    """Main function to load and analyze data."""
    file_path = 'data.csv'  # Specify your CSV file path here
    data = load_data(file_path)
    analyze_data(data)
    print("Analysis complete.")
    return data

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

def save_data(data, file_path):
    """Save a pandas DataFrame to a CSV file."""
    try:
        data.to_csv(file_path, index=False)
        print(f"Data successfully saved to {file_path}.")
    except Exception as e:
        print(f"Error saving data: {e}")
    
def analyze_data(data):
    """Perform basic analysis on the DataFrame."""
    if data is not None:
        print("Data Summary:")
        print(data.describe())
        print("\nMissing Values:")
        print(data.isnull().sum())
    else:
        print("No data to analyze.")