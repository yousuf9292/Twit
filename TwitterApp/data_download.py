import base64
import streamlit as st



def csv_downloader(data, new_filename):
    # Generates and names a link to download the given object_to_download
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    csv_filename = f"{new_filename}_tweets.csv"
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_filename}">Click Here!!</a>'
    st.markdown(href,unsafe_allow_html=True)


