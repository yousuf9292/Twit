import pandas as pd
from tweets import get_all_tweets
from data_cleaning import *
import base64
import time
import streamlit as st


# Twiterr handles of selected left-leaning US/UK publishing houses

def csv_downloader(data, new_filename):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    csv_filename = f"{new_filename}_tweets.csv"
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_filename}">Click Here!!</a>'
    st.markdown(href,unsafe_allow_html=True)

# def download_link(object_to_download, download_filename, download_link_text):
#     """
#     Generates a link to download the given object_to_download.

#     object_to_download (str, pd.DataFrame):  The object to be downloaded.
#     download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
#     download_link_text (str): Text to display for download link.

#     Examples:
#     download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
#     download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

#     """
#     if isinstance(object_to_download, pd.DataFrame):
#         object_to_download = object_to_download.to_csv(index=False)

#     # some strings <-> bytes conversions necessary here
#     b64 = base64.b64encode(object_to_download.encode()).decode()

#     return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

