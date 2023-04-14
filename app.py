import streamlit as st
from PIL import Image
import pandas as pd

def main():
    st.markdown("<h1 style='text-align: center; color: grey;'> &#127802; IRIS  &#127802; </h1>", unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image('iris.jpg')
        st.markdown('#')
        st.markdown('#')

    with st.expander("Vedi dati"):
        df = pd.read_csv('iris.csv')
        st.write(df)
    
    st.download_button('Download file',data='iris.csv', mime='text/csv', file_name='iris.csv')
        


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1556557753-4d7eb13e06c4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWluaW1hbGlzdCUyMGZsb3dlcnxlbnwwfHwwfHw%3D&w=1000&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

    
        
        
    
            
    
    







if __name__ == "__main__":
    main()