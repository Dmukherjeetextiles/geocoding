# geocoding
A simple streamlit application that fetches the coordinates of an address or multiple addresses (provided in a csv file in a column named "Address").

https://address-to-coordinates.streamlit.app/

# Geocode Addresses with Bing Maps API

This Streamlit application allows users to geocode addresses using the Bing Maps Geocoding API. Users can either enter a single address or upload a CSV file containing multiple addresses, and the application will return the corresponding latitude and longitude coordinates.

## Usage

1. **Bing Maps API Key**: Obtain a Bing Maps API key from the [Bing Maps Dev Center](https://www.bingmapsportal.com/).
2. **Clone Repository**: Clone this repository to your local machine.
3. **Install Dependencies**: Install the required Python dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
4. **Run Application**: Run the Streamlit application by executing `streamlit run Geocoding_Service.py` in your terminal.
5. **Enter Address or Upload CSV**: Enter a single address in the text input field or upload a CSV file with an "Address" column.
6. **View Results**: The application will display the geocoded data with latitude and longitude coordinates.
7. **Download Data**: Click the "Download Geocoded Data" button to download the geocoded data as a CSV file.

## Requirements

- Python 3.6+
- Streamlit
- Pandas
- Requests

## License

This project is licensed under the [MIT License](https://github.com/Dmukherjeetextiles/geocoding/blob/main/LICENSE).
