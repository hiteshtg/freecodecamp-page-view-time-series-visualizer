import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('~/codes/data_science/code_camp/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index(['date'])

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (12, 12))
    ax.plot(df.index, df['value'], color='red')
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.month
    df_bar['year'] = df.index.year
    
    df_bar = df_bar.groupby(['year', 'month']) ['value'].mean()
    df_bar = df_bar.unstack()
    

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True).figure
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(months, title='Months')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    

    # Draw box plots (using Seaborn)
    ax = plt.subplots(nrows=1, ncols=2)
    fig, (ax1, ax2) = ax
    
    month =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    sns.boxplot(data= df_box, x='month', y='value', ax=ax2, order=month)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
