import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "vgsales.csv"

def main():
    print("Loading DAta...")
    df = pd.read_csv(DATA_FILE)

    print("---First 5 rows of Data---")
    print(df.head())

    print("\n--- Data Info ---")
    print(df.info())
    print("\n ---Top 10 Best-Seling Games ---")
    top_10_games = df.sort_values(by="Global_Sales", ascending=False)
    print(top_10_games[['Name', 'Platform', 'Global_Sales']].head(10))

    print("\n Total Sales By Genre")
    genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
    print(genre_sales)

    print("\n --Generating plot...")
    plt.figure(figsize=(12,7))
    genre_sales.plot(kind='bar')

    plt.title("Total Gross Sales By Game Genre")
    plt.xlabel('Genre')
    plt.ylabel('Sales(in Millions)')
    plt.xticks(rotation=45)

    plt.savefig('genre_sale_plt.png', bbox_inches ='tight')
    print("Chart saved as genre_sale_plt.png ")
if __name__ == "__main__" :
    main()