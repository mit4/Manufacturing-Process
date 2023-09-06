import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_pickle("../../data/interim/Primary output data.pkl")

import pandas as pd
import numpy as np


def clean_time_series(series, threshold=2):
    # Calculate the mean and standard deviation of the series
    mean = series.mean()
    std = series.std()

    # Identify outliers based on the threshold
    outliers = (series - mean).abs() > threshold * std

    # Replace outliers with NaN
    series[outliers] = np.nan

    # Fill missing values with linear interpolation
    series.interpolate(method="linear", inplace=True)

    return series


cleaned_series = clean_time_series(data["Stage1.Output.Measurement0.U.Actual"])
plt.plot(data["Stage1.Output.Measurement0.U.Actual"])
plt.plot(cleaned_series)
