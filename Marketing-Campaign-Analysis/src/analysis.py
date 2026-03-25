# src/analysis.py

from preprocessing import preprocess_pipeline
from database import create_connection, create_table
import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "marketing.csv")


def generate_insights(conn):
    insights = []

    # 1. Overall response
    overall = pd.read_sql("SELECT AVG(y) as rate FROM campaign_data", conn)
    rate = overall['rate'][0]

    insights.append(f"Overall campaign response rate is {round(rate*100,2)}%.")

    # 2. Best age group
    age = pd.read_sql("""
        SELECT age_group, AVG(y) as rate
        FROM campaign_data
        GROUP BY age_group
        ORDER BY rate DESC
        LIMIT 1
    """, conn)

    insights.append(f"Highest response observed in age group {age.iloc[0,0]}.")

    # 3. Campaign effectiveness
    camp = pd.read_sql("""
        SELECT campaign, AVG(y) as rate
        FROM campaign_data
        GROUP BY campaign
        ORDER BY rate DESC
        LIMIT 1
    """, conn)

    insights.append(f"Campaign with fewer contacts performs better (Campaign #{camp.iloc[0,0]}).")

    return insights


def main():
    # Step 1: Preprocess
    df = preprocess_pipeline(DATA_PATH)

    # Step 2: Save to DB
    conn = create_connection()
    create_table(conn, df)

    # Step 3: Generate insights
    insights = generate_insights(conn)

    # Step 4: Save insights to file
    output_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "insights.txt"), "w") as f:
        for i in insights:
            f.write(i + "\n")

    print("Insights saved!")

    # Step 5: Save cleaned data
    df.to_csv(os.path.join(output_dir, "cleaned_data.csv"), index=False)


if __name__ == "__main__":
    main()