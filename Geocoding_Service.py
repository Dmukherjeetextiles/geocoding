import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

# Function to geocode address
def geocode_address(address):
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(address)
        return location.latitude, location.longitude
    except Exception as e:
        return None, None

# Streamlit UI
def main():
    st.title("Geocode Addresses")
    
    # Single address input
    address_input = st.text_input("Enter an address:")
    
    if address_input:
        st.write("Geocoding...")
        latitude, longitude = geocode_address(address_input)
        
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
            df['Latitude'], df['Longitude'] = zip(*df['Address'].apply(geocode_address))
            
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
