import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to draw the plot
def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color='blue')

    # Create first line of best fit (using all data)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, res.intercept + res.slope * years_extended, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit (from year 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = pd.Series(range(2000, 2051))
    plt.plot(years_2000_extended, res_2000.intercept + res_2000.slope * years_2000_extended, 'green', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (do not modify)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
