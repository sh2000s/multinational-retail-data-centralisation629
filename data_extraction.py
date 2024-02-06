import pandas as pd
import requests
import boto3
from io import BytesIO

class DataExtractor:
    @staticmethod
    def extract_from_csv(csv_path):
        return pd.read_csv(csv_path)

    @staticmethod
    def extract_from_api(api_url):
        response = requests.get(api_url)
        return response.json()

    @staticmethod
    def extract_from_s3(s3_bucket, s3_key):
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        return pd.read_csv(BytesIO(obj['Body'].read()))

