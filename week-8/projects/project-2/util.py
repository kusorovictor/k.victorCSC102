import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
  
  
# Display the first few rows of the dataframe
def display_rows(num_rows, df):
  for i in range(num_rows):
    print(df.iloc[i])
    print("\n")

#Display the first few columns of the dataframe
def display_columns(num_columns, df):
  for i in range(num_columns):
    print(df.iloc[:, i])
    print("\n")
    

#Display the first few rows of the dataframe with header    
def display_rows_header(num_rows, df):
  for i in range(num_rows):
    print(df.iloc[i].to_string(header = True, index = False))
    print("\n")
    
    
# Display all the required info from the dataset    
def display_all(file_path):
  df = load_data(file_path)
  
  print("First 7 rows of the dataset:")
  display_rows(7, df)
  
  print("First 3 columns of the dataset: ")
  display_columns(3, df)
  
  print("First row of the dataset with header: ")
  display_rows_header(1, df)