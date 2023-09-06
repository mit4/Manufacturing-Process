import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_pickle("../../data/interim/Primary output data.pkl")

data.info()

# grouped_columns = {first_word: [col for col in data.columns if col.startswith(first_word + '.')] for first_word in set(col.split('.')[0] for col in data.columns)}


def plot_columns_by_prefix(data, prefix, title):
    """
    Create line plots for columns with a specified prefix in their names.

    Args:
        data (pd.DataFrame): Input DataFrame containing columns to plot.
        prefix (str): The prefix used to filter columns.
        title (str): The title for the line plot.

    Returns:
        None
    """
    columns = [col for col in data.columns if col.startswith(prefix)]

    plt.figure(figsize=(12, 6))  # Adjust figure size if needed
    plt.title(f"Line Plot for {title}")
    for column in columns:
        plt.plot(data.index, data[column], label=column)
    plt.xlabel("Datetime")
    plt.ylabel("Value")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()


def group_columns_by_property(data, prefix):
    """
    Group prefix columns by unique properties.

    Args:
        data (pd.DataFrame): Input DataFrame containing Machine columns.

    Returns:
        dict: A dictionary where keys are unique properties and values are lists of columns.
    """
    unique_properties = list(
        set(
            map(
                lambda col: col.split(".", 1)[1],
                filter(lambda col: col.startswith(prefix), data.columns),
            )
        )
    )

    property_columns = {}

    for prop in unique_properties:
        prop_columns = [col for col in data.columns if col.endswith(f"{prop}")]
        property_columns[prop] = prop_columns

    return property_columns


def plot_property_groups(data, property_groups):
    """
    Create line plots for each group of columns representing a property.

    Args:
        data (pd.DataFrame): Input DataFrame.
        property_groups (dict): Dictionary where keys are properties and values are lists of columns.

    Returns:
        None
    """
    for prop, columns in property_groups.items():
        plt.figure(figsize=(12, 6))
        plt.title(f"Line Plot for Property: {prop}")
        for column in columns:
            plt.plot(data.index, data[column], label=column)
        plt.xlabel("Datetime")
        plt.ylabel("Value")
        plt.legend(loc="best")
        plt.grid(True)
        plt.show()


# Create line plot of columns name
plot_columns_by_prefix(data, "AmbientConditions", "Ambient Conditions")
plot_columns_by_prefix(data, "FirstStage", "First Stage")

# Create a list of unique properties
unique_properties_machine = group_columns_by_property(data, "Machine")
unique_properties_output = group_columns_by_property(data, "Stage")

# Create line plot of columns grouped by property
plot_property_groups(data, unique_properties_machine)
plot_property_groups(data, unique_properties_output)
