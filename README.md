# NetSuite SuiteQL Streamlit App

This is a Streamlit app that lets you run SuiteQL queries against a NetSuite account using OAuth 1.0 credentials.

## Features

- Dynamically input NetSuite credentials (Consumer Key, Consumer Secret, Token Key, Token Secret, and Realm).
- Enter and run SuiteQL queries in the main page.
- Displays query results in a table format.
- Download the response as JSON or CSV.

## Installation

1. **Clone this repository** (or download the ZIP and extract it):
    ```bash
    git clone https://github.com/YOUR_USERNAME/netsuite-suiteql-app.git
    cd netsuite-suiteql-app
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

4. **Access in your browser**:
   - After running the command above, Streamlit will provide a local URL (usually http://localhost:8501).
   - Open that URL in your browser to use the app.

## Usage

1. Enter your NetSuite OAuth credentials in the sidebar:
    - Consumer Key
    - Consumer Secret
    - Token Key
    - Token Secret
    - Realm

2. In the main page, update the SuiteQL query as needed.  
3. Click **Run Query**.  
4. View results in the data table.  
5. Download JSON or CSV using the provided buttons.

## Contributing

Feel free to open issues or pull requests if you have suggestions or want to improve this project!

## License

[MIT License](LICENSE)
