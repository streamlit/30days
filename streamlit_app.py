import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 Days Of Streamlit（zh-TW 繁體中文版）')

days_list = [f'Day {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('開始挑戰 👇', days_list, key="day", on_change=update_params)

with st.expander("有關 #30DaysOfStreamlit"):
    st.markdown('''
    **#30DaysOfStreamlit** 是一個程式語言挑戰，設計用來幫助你開始建立 Streamlit 應用程式。
    
    特別是，這 30 天內你能夠：
    - 設定一個 coding 環境來建立 Streamlit 應用程式
    - 建立你第一個 Streamlit 應用程式
    - 學習有關所有優秀的 輸入/輸出 部件來用在你的 Streamlit 應用程式
    ''')

# Sidebar
st.sidebar.header('關於')
st.sidebar.markdown('[Streamlit](https://streamlit.io) 是一個 Python 的函式庫，允許使用 Python 建立 可互動、資料驅動 的 web 應用程式。')

st.sidebar.header('資源')
st.sidebar.markdown('''
- [Streamlit 文件](https://docs.streamlit.io/)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Book](https://www.amazon.com/dp/180056550X)（開始 Streamlit for 資料科學）
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)（如何精通 Streamlit for 資料科學）
''')

st.sidebar.header('部署')
st.sidebar.markdown('只需要點幾下，你可以透過 [Streamlit Cloud](https://streamlit.io/cloud) 快速地部署 Streamlit 應用程式')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')
        j = i.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### 圖表')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.image(f'content/images/{df.img[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
