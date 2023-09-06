import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_and_preprocess_csv(csv_path):
    """
    Read a CSV file, convert the 'time_stamp' column to datetime, and set it as the index.

    Parameters:
        csv_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame with the 'time_stamp' column set as the index.
    """
    # Read the CSV file
    data = pd.read_csv(csv_path)

    # Convert the 'time_stamp' column to datetime
    data["time_stamp"] = pd.to_datetime(data["time_stamp"])

    # Set 'time_stamp' as the index
    data = data.set_index("time_stamp")

    return data


# Provide the path to your CSV file
csv_path = "../../data/raw/continuous_factory_process.csv"

# Call the function to read and preprocess the CSV
data = read_and_preprocess_csv(csv_path)


def filter_columns_by_keyword(data, keyword):
    """
    Filter DataFrame columns based on a keyword.

    Parameters:
        data (pd.DataFrame): The input DataFrame.
        keyword (str): The keyword to exclude from column names.

    Returns:
        pd.DataFrame: The DataFrame with columns containing the keyword removed.
    """

    # Filter columns based on the keyword
    data = data.loc[:, ~data.columns.str.contains("keyword")]

    return data


# Data for primary output and remove Setpoint columns
df1 = data.iloc[:, :71]
df1 = df1.loc[:, ~df1.columns.str.contains("Setpoint")]

# Data for primary output and remove Setpoint columns
df2 = data.iloc[:, 71:]
df2 = df2.loc[:, ~df2.columns.str.contains("Setpoint")]

df1.to_pickle("../../data/interim/Primary output data.pkl")
df2.to_pickle("../../data/interim/Secondary output data.pkl")
