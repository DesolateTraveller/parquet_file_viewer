import streamlit as st
import pandas as pd
#---------------------------------------------------------------------------------------------------------------------------------
### Title for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Parquet File Viewer | v0.2 ",
                    layout="wide",
                    page_icon="📑",            
                    initial_sidebar_state="auto")
#---------------------------------------------------------------------------------------------------------------------------------
### Description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .title-large {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-small {
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .version-badge {
        text-align: center;
        display: inline-block;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 1.15rem;
        margin-top: 8px;
        margin-bottom: 0px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">Parquet File Viewer</div>
        <div class="version-badge">v0.2</div>
    </div>
    """,
    unsafe_allow_html=True)

#----------------------------------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F0F2F6;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        z-index: 100;
    }
    .footer p {
        margin: 0;
    }
    .footer .highlight {
        font-weight: bold;
        color: blue;
    }
    </style>
    <div class="footer">
        <p>© 2026 | Created by : <span class="highlight">Avijit Chakraborty</span> <a href="mailto:avijit.mba18@gmail.com"> 📩 </a> | <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span> </p>
    </div>
    """,unsafe_allow_html=True)

#<span class="highlight">Thank you for visiting the app | This app is created for internal use, unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span>
#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

st.divider()

col1, col2 = st.columns((0.15, 0.85))
with col1:
    
    with st.container(border=True):
        
        def monitor_memory():
            """Monitor memory usage"""
            import psutil
            process = psutil.Process()
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / 1024 / 1024
            return memory_mb
        memory_usage = monitor_memory()
        
        if memory_usage <= 1000:
            st.markdown(f"<div style='color:green; font-size:18px;'>🟢 Memory Usage: {memory_usage:.1f} MB</div>", unsafe_allow_html=True)
        elif memory_usage <= 2000:
            st.markdown(f"<div style='color:#FFA500; font-size:18px;'>🟡 Memory Usage: {memory_usage:.1f} MB</div>", unsafe_allow_html=True)
        elif memory_usage <= 3000:
            st.markdown(f"<div style='color:orange; font-size:18px;'>🟠 Memory Usage: {memory_usage:.1f} MB</div>", unsafe_allow_html=True)
            st.info("Memory usage is getting high. Consider saving your work.")
        else:
            st.markdown(f"<div style='color:red; font-size:18px;'>🔴 Memory Usage: {memory_usage:.1f} MB</div>", unsafe_allow_html=True)
            st.warning("⚠️ High memory usage detected! Consider restarting the application to free up resources.")
          
    with st.container(border=True):

        uploaded_file = st.file_uploader("📁 **:blue[Choose file]**", type=["parquet"])

        if uploaded_file is not None:
            st.success("Data loaded successfully!")
            st.divider()
            show_stats = st.checkbox("Show basic statistics", key="show_stats")
            show_columns = st.checkbox("Show column names", key="show_columns")

with col2:
    if uploaded_file is not None:
        try:
            df = pd.read_parquet(uploaded_file)

            st.markdown("##### 📊 Data Preview")
            st.dataframe(df.head(10))

            if show_stats:
                
                st.divider()
                st.markdown("##### 📊 Data Summary")
                st.write(df.describe())
            
            if show_columns:
                
                st.divider()
                st.markdown("##### 📋 Column Names")
                st.write(df.columns.tolist())

        except Exception as e:
            st.error(f"Error reading the Parquet file: {e}")
    else:
        st.info("Please upload a Parquet file to begin.")

#---------------------------------------------------------------------------------------------------------------------------------    

    
