import streamlit as st
import requests
from requests_oauthlib import OAuth1
import json
import pandas as pd

# App title and description
st.title("NetSuite SuiteQL Query UI")
st.write("This app allows you to run SuiteQL queries dynamically against the NetSuite API.")

# Sidebar for credentials
st.sidebar.header("NetSuite Credentials")
consumer_key = st.sidebar.text_input(
    "Consumer Key", 
    value=""
)
consumer_secret = st.sidebar.text_input(
    "Consumer Secret", 
    value="", 
    type="password"
)
token_key = st.sidebar.text_input(
    "Token Key", 
    value=""
)
token_secret = st.sidebar.text_input(
    "Token Secret", 
    value="", 
    type="password"
)
realm = st.sidebar.text_input("Realm/Account ID", value="123456")

# Main page for the SuiteQL query
st.subheader("Query Settings")
query_input = st.text_area(
    "SuiteQL Query", 
    value="SELECT * FROM employee", 
    height=100
)

# Run the SuiteQL query when the "Run Query" button is clicked
if st.button("Run Query"):
    # Set up the OAuth1 session
    oauth = OAuth1(
        client_key=consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=token_key,
        resource_owner_secret=token_secret,
        realm=realm,
        signature_method='HMAC-SHA256'
    )
    
    # Define the endpoint and query payload
    url = f'https://{realm}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql'
    payload = {"q": query_input}
    headers = {
        'Prefer': 'transient',
        'Content-Type': 'application/json'
    }
    
    # Execute the query
    with st.spinner("Executing query..."):
        response = requests.post(url, auth=oauth, json=payload, headers=headers)
    
    # Handle the response
    if response.status_code == 200:
        employees = response.json()
        st.success("Query executed successfully!")
        
        # Extract the data under 'items' key
        employee_data = employees.get('items', [])
        if employee_data:
            # Convert to DataFrame and display as a table
            df = pd.DataFrame(employee_data)
            st.dataframe(df)
        else:
            st.write("No data available.")
        
        # Prepare JSON and CSV for download
        json_str = json.dumps(employees, indent=2)
        if employee_data:
            csv_data = df.to_csv(index=False)
        else:
            csv_data = "No data to convert to CSV."

        # Download buttons
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="netsuite_employees.json",
            mime="application/json"
        )
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="netsuite_employees.csv",
            mime="text/csv"
        )
    else:
        st.error(f"Failed to retrieve records: {response.status_code}")
        st.error(response.text)
