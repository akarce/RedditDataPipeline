import os  # Add this import
import pandas as pd
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter: str, limit=None):
    # Connecting to Reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Ceyhun Akar Agent')
    # Extracting data from Reddit
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # Transform
    post_df = transform_data(post_df)
    # Load data to CSV
    subreddit_output_path = f'{OUTPUT_PATH}/{subreddit}'  # New path per subreddit
    os.makedirs(subreddit_output_path, exist_ok=True)  # Ensure directory exists
    file_path = f'{subreddit_output_path}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path
