import streamlit as st
import pandas as pd
import requests

# Function to geocode address using Bing Maps Geocoding API
def geocode_address(address, api_key):
    base_url = "http://dev.virtualearth.net/REST/v1/Locations"
    params = {
        "query": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        try:
            resource_sets = data["resourceSets"]
            if len(resource_sets) > 0:
                resources = resource_sets[0]["resources"]
                if len(resources) > 0:
                    point = resources[0]["point"]
                    latitude = point["coordinates"][0]
                    longitude = point["coordinates"][1]
                    return latitude, longitude
        except KeyError:
            pass
    return None, None

# Streamlit UI
def main():
    st.title("Geocode Addresses with Bing Maps API")
    
    # Get Bing Maps API key from user input
    api_key = st.secrets["API_KEY"]
    
    # Single address input
    address_input = st.text_input("Enter an address:")
    
    if address_input and api_key:
        st.write("Geocoding...")
        latitude, longitude = geocode_address(address_input, api_key)
        
        if latitude is not None and longitude is not None:
            st.write("Latitude:", latitude)
            st.write("Longitude:", longitude)
        else:
            st.write("Error: Unable to geocode the address.")
    
    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        # Check if 'Address' column exists
        if 'Address' in df.columns:
            st.write("Original data:")
            st.write(df)
            
            # Geocode addresses
            st.write("Geocoding...")
            df['Latitude'], df['Longitude'] = zip(*df['Address'].apply(lambda x: geocode_address(x, api_key)))
            
            # Display geocoded data
            st.write("Geocoded data:")
            st.write(df)
            
            # Button to download geocoded data
            st.download_button(
                label="Download Geocoded Data",
                data=df.to_csv().encode(),
                file_name="geocoded_data.csv",
                mime="text/csv"
            )
        else:
            st.write("Error: No 'Address' column found in the uploaded CSV file.")

    else:
        st.write("Please upload a CSV file.")

if __name__ == "__main__":
    main()
