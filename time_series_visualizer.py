
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=["date"])

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

df = df[(df["value"]> df["value"].quantile(0.025)) & (df["value"] < df["value"].quantile(0.975))]
df.head()

def draw_line_plot():
# Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.

    fig = df.plot('date','value',
                title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", 
                xlabel = "Date",
                ylabel = "Page views",
                kind="line",
                color="red",
                figsize=(15,8))
                
    return fig 

draw_line_plot()

def draw_bar_plot():
# Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

    df["day"] = df["date"].dt.day

    df["month"] = df["date"].dt.month_name()
    df["month"] = pd.Categorical(df["month"],categories=['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December'])
    df["year"] = df["date"].dt.year

    df_grouped = df.groupby(["year","month"], observed=True)["value"].mean().unstack()
    df_grouped

    fig2 = df_grouped.plot(xlabel="Years",
                        ylabel="Avg per month",
                        kind="bar",
                        figsize=(10,10))
    plt.legend(title="Months")
    return fig2
draw_bar_plot()

def draw_box_plot():
# Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

    fig3 = plt.figure(figsize=(25,10))

    plt.subplot(1,2,1)
    sns.boxplot(x='year',
                    y='value',
                    hue="year",
                    data=df,
                    palette="pastel",
                    legend=False
                    ).set(
                        xlabel="Year",
                        ylabel="Page views",
                        title="Year-wise Box Plot (Trend)"
                    )

    plt.subplot(1,2,2)
    sns.boxplot(x='month',
                    y='value',
                    hue="month",
                    data=df,
                    palette="pastel",
                    legend=False
                    ).set(
                        xlabel="Month",
                        ylabel="Page views",
                        title="Month-wise Box Plot (Seasonality)"
                    )   
    return fig3
draw_box_plot()
