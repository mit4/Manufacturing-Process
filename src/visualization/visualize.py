import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_pickle("../../data/interim/Primary output data.pkl")

data.info()

# grouped_columns = {first_word: [col for col in data.columns if col.startswith(first_word + '.')] for first_word in set(col.split('.')[0] for col in data.columns)}


def plot_columns_by_prefix(data, prefix):
    """
    Create line plots for columns with a specified prefix in their names.

    Args:
        data (pd.DataFrame): Input DataFrame containing columns to plot.
        prefix (str): The prefix used to filter columns.
        title (str): The title for the line plot.

    Returns:
        None
    """
    output_dir = "../../reports/figures/plots"
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    columns = [col for col in data.columns if col.startswith(prefix)]

    plt.figure(figsize=(12, 6))  # Adjust figure size if needed
    plt.title(f"Line Plot for {prefix}")
    for column in columns:
        plt.scatter(
            data.index, data[column], s=2, label=column
        )  # s specifies marker size
    plt.xlabel("Datetime")
    plt.ylabel("Value")
    plt.legend(loc="best")
    plt.grid(True)

    # Save the plot to a file
    output_file = os.path.join(output_dir, f"scatter_plot_{prefix}.png")
    plt.savefig(output_file, dpi=300, bbox_inches="tight")

    # Display the plot
    plt.show()


def plot_property_groups(data, prefix):
    """
    Group prefix columns by unique properties and create scatter plots for each group.

    Args:
        data (pd.DataFrame): Input DataFrame containing Machine columns.
        prefix (str): Prefix to filter and group columns.

    Returns:
        None
    """
    output_dir = "../../reports/figures/plots"
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Group columns by unique properties
    unique_properties = list(
        set(
            map(
                lambda col: col.split(".", 1)[1],
                filter(lambda col: prefix in col, data.columns),
            )
        )
    )

    for prop in unique_properties:
        prop_columns = [col for col in data.columns if col.endswith(f"{prop}")]
        plt.figure(figsize=(12, 6))
        plt.title(f"Scatter Plot for Property: {prop}")
        for column in prop_columns:
            label = column.split(".")[
                -1
            ]  # Use the last part of the column name as the label
            plt.scatter(data.index, data[column], s=2, label=label)
        plt.xlabel("Datetime")
        plt.ylabel("Value")
        plt.legend(loc="best")
        plt.grid(True)

        # Save the plot to a file (removing existing file if it exists)
        output_file = os.path.join(output_dir, f"scatter_plot_{prop}.png")
        if os.path.exists(output_file):
            os.remove(output_file)
        plt.savefig(output_file, dpi=300, bbox_inches="tight")

        # Display the plot
        plt.show()


# Create line plot of columns name
plot_columns_by_prefix(data, "AmbientConditions")
plot_columns_by_prefix(data, "FirstStage")

# Create line plot of columns grouped by property
plot_property_groups(data, "Machine")
plot_property_groups(data, "Output")
