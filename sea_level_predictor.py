import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(12, 6))

    # Create scatter plot
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Predict from the first year through 2050
    years = pd.Series(
        range(
            int(df["Year"].min()),
            2051
        )
    )

    predicted = slope * years + intercept

    ax.plot(
        years,
        predicted
    )

    # Line of best fit using data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Predict from 2000 through 2050
    years_recent = pd.Series(
        range(
            2000,
            2051
        )
    )

    predicted_recent = (
        slope_recent * years_recent
        + intercept_recent
    )

    ax.plot(
        years_recent,
        predicted_recent
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot
    fig.savefig("sea_level_plot.png")

    # Return Axes object because the FreeCodeCamp tests expect it
    return ax