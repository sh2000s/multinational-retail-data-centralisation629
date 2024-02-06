import pandas as pd

class DataCleaning:
    @staticmethod
    def clean_user_data(user_data):
        # Your cleaning logic here
        cleaned_data = user_data.dropna()  # Placeholder example
        return cleaned_data

    @staticmethod
    def clean_card_data(card_data):
        # Your cleaning logic here
        cleaned_data = card_data.drop_duplicates()  # Placeholder example
        return cleaned_data

    @staticmethod
    def clean_store_data(store_data):
        # Your cleaning logic here
        cleaned_data = store_data.fillna(0)  # Placeholder example
        return cleaned_data

    @staticmethod
    def clean_products_data(products_data):
        # Your cleaning logic here
        cleaned_data = products_data.dropna()  # Placeholder example
        return cleaned_data

