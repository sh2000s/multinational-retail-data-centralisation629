The context of this project is that I work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analyzable by current members of the team. In an effort to become more data-driven, my organization would like to make its sales data accessible from one centralized location. My first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralized location and acts as a single source of truth for sales data. I will then query the database to get up-to-date metrics for the business.


Milestone 1: GitHub Setup
In Milestone 1, we focused on setting up the project on GitHub and establishing a version control system. Key tasks included initializing the GitHub repository, configuring Git for version control, creating a .gitignore file to exclude sensitive information, and committing and pushing initial project files to GitHub. This milestone laid the foundation for collaborative development and ensured proper management of project versions.

Milestone 2: Data Handling and Refactoring
Milestone 2 centered around the core functionality of the project—handling sales data from various sources. We created a new database, sales_data, to serve as a centralized repository for sales information. Three utility classes—DataExtractor, DatabaseConnector, and DataCleaning—were introduced to facilitate data extraction, database connection, and data cleaning processes, respectively.

We extracted and cleaned user data from an AWS RDS database, card details from a PDF in an S3 bucket, store details from an API, product details from a CSV file in an S3 bucket, orders data from the sales_data database, and date events data from a JSON file in an S3 bucket. The codebase underwent optimization and refactoring to enhance readability, promote code reuse, and adhere to best practices. These changes contribute to a more maintainable and efficient data handling process.

The README file was updated to reflect the project's current status, including detailed installation instructions, usage guidelines, and an organized file structure overview. The milestones section provides a comprehensive overview of the project's development stages, highlighting completed tasks and achievements.
Multinational-Retail-Data-Centralisation


