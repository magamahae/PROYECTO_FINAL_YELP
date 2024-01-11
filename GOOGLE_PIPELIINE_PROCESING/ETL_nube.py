import os
import pandas as pd
from google.cloud import bigquery
from textblob import TextBlob


def process_yelp_files(event, context):
    """Processes Yelp files in a Cloud Storage bucket."""

    path = event['bucket'] + '/' + event['name']
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        main_folder, file_name = os.path.split(file_path)
        table_name, _ = os.path.splitext(file_name)

        if main_folder == "Yelp":
            try:
                if table_name == "reviews":
                    df = pd.read_json(file_path)
                    # Transformaciones para la tabla "reviews"
                    df.drop(columns=["cool", "funny", "useful"], inplace=True)
                    df.rename(columns={"stars": "rating"}, inplace=True)
                    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
                    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                    df['feeling'] = df['opinion'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')
                elif table_name == "business":
                    df = pd.read_parquet(file_path)
                    # Transformaciones para la tabla "business"
                    df = df.loc[:, ~df.columns.duplicated()]
                    df['state'] = df['state'].shift(-3)
                    df.loc[150343, 'state'] = 'IN'
                    df.loc[150344, 'state'] = 'IL'
                    df.loc[150345, 'state'] = 'FL'
                    df["platform"] = "yelp"
                    df = df[df["state"].isin(["IL", "CA", "TX", "NY", "FL"])]
                    df = df[df['categories'].str.contains('restaurants')]
                    df.drop(columns=["postal_code", "is_open", "attributes", "hours"], inplace=True)
                    df.drop_duplicates(inplace=True)
                elif table_name == "user":
                    df = pd.read_parquet(file_path)
                    # Transformaciones para la tabla "user"
                    df.drop_duplicates(inplace=True)
                    df.drop(columns=["Unnamed: 0", "name", "yelping_since", "funny", "cool", "elite", "fans", "average_stars", "compliment_hot", "compliment_more", "compliment_profile", "compliment_cute", "compliment_list", "compliment_note", "compliment_plain", "compliment_cool", "compliment_funny", "compliment_writer", "compliment_photos"], inplace=True)
                elif table_name == "tip":
                    df = pd.read_json(file_path)
                    # Transformaciones para la tabla "tip"
                    df['feeling'] = df['text'].apply(lambda x: classify_comment2(x) if pd.notnull(x) else 'No message')

                # Carga los datos transformados a BigQuery
                df.to_gbq('dataset.table', project_id='my-project-id', if_exists='append', location='us')
                print(f'{table_name} processed successfully!')

            except Exception as e:
                print(f'Error processing {file_path}: {e}')


def classify_comment2(comment):
    if comment is None:
        return 'No message'
    else:
        sentiment = TextBlob(comment).sentiment.polarity
        if sentiment > 0:
            return 'Positive'
        elif sentiment < 0:
            return 'Negative'
        else:
            return 'Neutral'
