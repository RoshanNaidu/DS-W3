import seaborn as sns
import pandas as pd


# update/add code below ...

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)



import pandas as pd

# Load the dataset directly from the URL in exercises.ipynb
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

# Verify the data is loaded
print(df_bellevue.head())

# Task 1: Return sorted column names by missing values
def task_1():
    # First, clean the 'gender' column (assuming it contains missing values or incorrect entries)
    if 'gender' in df_bellevue.columns:
        # Replace any non-valid entries in 'gender' (if necessary) or drop rows with missing 'gender'
        df_bellevue['gender'] = df_bellevue['gender'].fillna('Unknown')
    
    # Sort columns based on the number of missing values (descending order: most missing to least missing)
    missing_values = df_bellevue.isnull().sum()
    sorted_columns = missing_values.sort_values(ascending=False).index.tolist()
    
    print(f"Sorted columns by missing values: {sorted_columns}")
    return sorted_columns

# Task 2: Return a DataFrame with year and total admissions
def task_2():

    # Print column names to debug
    print("Columns in df_bellevue:", df_bellevue.columns)
    
    # Create a new column 'admissions' with a value of 1 for each row
    df_bellevue['admissions'] = 1
    
    # Convert 'date_in' to datetime format if it's not already
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    
    # Extract the year from the 'date_in' column
    df_bellevue['year'] = df_bellevue['date_in'].dt.year
    
    # Group by 'year' and sum admissions
    total_admissions = df_bellevue.groupby('year')['admissions'].sum().reset_index()
    total_admissions.columns = ['year', 'total_admissions']
    
    print(f"Yearly admissions:\n{total_admissions}")
    return total_admissions

# Task 3: Return average age for each gender
def task_3():
    if 'gender' not in df_bellevue.columns or 'age' not in df_bellevue.columns:
        print("Error: 'gender' or 'age' column missing.")
        return None
    
    # Group by 'gender' and calculate average age
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
    
    print(f"Average age by gender:\n{avg_age_by_gender}")
    return avg_age_by_gender

# Task 4: Return the 5 most common professions
def task_4():
    if 'profession' not in df_bellevue.columns:
        print("Error: 'profession' column missing.")
        return None
    
    # Get the top 5 most common professions
    most_common_professions = df_bellevue['profession'].value_counts().head(5)
    
    # Convert the Series to a list
    most_common_professions_list = most_common_professions.index.tolist()
    
    print(f"Top 5 most common professions:\n{most_common_professions}")
    return most_common_professions_list