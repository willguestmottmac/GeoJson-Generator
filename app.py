import streamlit as st
import folium
import geopandas as gpd
from folium.plugins import Draw
from streamlit_folium import folium_static

# Choose projection as WGS 84
projection = "EPSG:4326"

def main():
    # Title of the Streamlit app
    st.title('GeoJson Export Tool')

    # Sidebar with instructions 
    st.sidebar.markdown('# Instructions')
    st.sidebar.markdown('1. Draw a shape on the map by selecting a shape from the options provided (Polygon, Line etc.).')
    st.sidebar.markdown('2. After drawing the shape, click the Export and Download Polygon button to export and download the shape as a GeoJSON file.')
    
    # Create a folium map of the world
    m = folium.Map(location=[0, 0], zoom_start=2, prefer_canvas=True)

    # Create Draw object
    draw = Draw(export=True)

    # Add the Draw control
    draw.add_to(m)

    # Display the map in the Streamlit app
    folium_static(m)


if __name__ == "__main__":
    main()
