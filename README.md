## Project Setup

**Prerequisites:**

* Python environment with `pip` installed
* Git for version control

**After pulling the repository:**

**1. Database Initialization:**

* **Install Postgres server:** Follow the official documentation (https://www.postgresql.org/download/) to install Postgres on your machine.
* **Run initialization script:** Run the script `initialize-db.sql` to create a database named `neo-project` and a user named `testuser` used by the Django application.
* **Optional: Modify credentials (if needed):** You can change the database name or username in the `initialize-db.sql` script, but remember to update the corresponding values in the Django project's `settings.py` file as well.

**2. Python Environment Initialization:**

* **Install dependencies:** Run `pip install -r requirements.txt` to install the required Python packages.

**3. Data Creation:**

* **Generate client data:** Navigate to the `generateData` directory and run `python generateClients.py` to generate client data.
* **Generate transaction data:** Navigate to the `generateData` directory and run `python generateTransactions.py` to generate transaction data.
* **Note down data path:** Remember the path to the directory containing the generated files as it will be used in the ETL script.

**4. Django Application Initialization:**

* **Ensure Postgres server:** Make sure the Postgres server is running and the database is created.
* **Verify configuration:** Ensure the database configuration in `settings.py` matches your database setup.
  ![image](https://github.com/user-attachments/assets/a9180f77-7f18-42b7-873f-696f811bdbd5)
* **Database migration:** Run `python manage.py migrate` to apply database migrations.
* **Create superuser:** Run `python manage.py createsuperuser` to create a user for API authentication. Note down the username and password you choose.
* **Run ETL script:** Run `python manage.py runetl --source-path="insert the path to the folder containing the clients.csv and transactions.xslx files"`. Replace the placeholder with the actual path. For example, `python manage.py runetl --source-path="C:\Users\Desktop\project-neo-technologies\neoApi"`
* **Start server:** Run `python manage.py runserver` to start the Django development server.

**5. Access Token Acquisition:**

* **POST request:** Make a POST request to the URL `http://127.0.0.1:8000/api/token/` to generate a JWT token.
* **Authentication credentials:** Use the username and password you created in step 4 (createsuperuser) for authentication.
  ![image](https://github.com/user-attachments/assets/04e8bff3-f91a-49fd-b8e3-283ed3ecc75f)
* **Note down token:** Record the access token returned in the response.

**6. API Call:**

* **API endpoint:** Make a request to the URL `http://127.0.0.1:8000/api/transactions` to retrieve transaction data.
* **Client ID parameter:** Specify the `client_id` parameter in the request.
* **Optional parameters:** Optionally, include `start_transaction_date` and `end_transaction_date` parameters to filter transactions by date.
  ![image](https://github.com/user-attachments/assets/32bff75c-8844-40ab-b984-461adde07815)
* **Authorization header:** Include a Bearer token in the request header for authentication (use the token generated in step 5).

## Project Summary

This project offers the following functionalities:

* **API for transactions:** An API endpoint retrieves transaction data for a specific client.
* **JWT authentication:** Secured by a JWT authentication system for access control.
* **Custom ETL task:** A custom management command to execute the ETL job for data loading.
* **ETL tables:** Dedicated tables to track ETL job executions and data quality issues.
* **API pagination:** Implemented pagination functionality to handle large datasets efficiently.
* **Materialized views:** Materialized views are created for efficient retrieval of summarized data.

## Potential Improvements

* **Custom admin screens:** Develop custom admin screens for visualizing data stored in the ETL execution tables.
* **Docker packaging:** Package the solution using Docker for easier deployment (not implemented due to technical limitations on my personal computer).
