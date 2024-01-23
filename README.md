Multinational-Retail-Data-Centralisation

The context of this project is that I work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analyzable by current members of the team. In an effort to become more data-driven, my organization would like to make its sales data accessible from one centralized location. My first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralized location and acts as a single source of truth for sales data. I will then query the database to get up-to-date metrics for the business.

Milestones
Milestone 1: Set up the environment
Used GitHub to track changes to my code and save them online in a GitHub repo
Milestone 2: Extract and clean the data from the data sources
Initialized a new database locally called Sales_database to store the extracted data through pgadmin4.

Created three Python scripts for data extraction, data cleaning, and database connector, each with its own class.

Data Extraction Methods
Developed methods to extract data from sources, including CSV files, an API, and an S3 bucket.
Extracted user data from an AWS RDS database and cleaned it, handling NULL values, date errors, incorrectly typed values, and rows with incorrect information.
Extracted user card details from a PDF stored in an AWS S3 bucket, cleaned the data, and uploaded it to the database.
Retrieved store data through an API, cleaned it, and uploaded the dataframe to the Sales_data database in pgAdmin.
Extracted product information from CSV files in an S3 bucket, cleaned the data frame, and uploaded it to the database.
Extracted and cleaned the orders table stored in an AWS RDS database, then uploaded the dataframe to the database.
Extracted details of each sale from a JSON file stored on S3, cleaned the data, and uploaded it to the database.

Milestone 3: Create the database schema
Ensured that all tables within the sales_database had correct columns and were cast of the correct type.
Added primary keys to all dimension tables, then created foreign keys in the orders_table to reference the primary keys in other tables.
Used SQL to create foreign key constraints, completing the star-based database schema.

Milestone 4: Querying the Data
Used SQL to get up-to-date metrics from the data, answering the following questions:
How many stores does the business have and in which countries?
Which locations currently have the most stores?
Which months produce the most sales typically?
How many sales are coming from online?
What percentage of sales come through each type of store?
Which month in each year produced the most sales?
What is our staff headcount?
Which German store type is selling the most?
How quickly is the company making sales?




