import glob
import os
import urllib.request

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1("content", "*.md")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown("# ৩০ দিনে স্ট্রিমলিট্ ")

days_list = [f"Day {x}" for x in md_files]

query_params = st.experimental_get_query_params()

try:
    if query_params and query_params["challenge"][0] in days_list:
        st.session_state.day = query_params["challenge"][0]
except KeyError:
    st.session_state.day = days_list[0]

selected_day = st.selectbox(
    "Start the Challenge 👇", days_list, key="day", on_change=update_params
)

with st.expander("#30DaysOfStreamlit সম্পর্কিত"):
    st.markdown(
        """
    **#30DaysOfStreamlit** হল একটি কোডিং চ্যালেঞ্জ যা আপনাকে Streamlit অ্যাপ তৈরি শুরু করতে সাহায্য করার জন্য ডিজাইন করা হয়েছে।
    
    বিশেষ করে, আপনি সক্ষম হবেন:
    - স্ট্রিমলিট্ অ্যাপস তৈরি করার জন্য একটি কোডিং পরিবেশ সেট আপ করুন
    - আপনার প্রথম স্ট্রিমলিট্ অ্যাপ তৈরি করুন
    - আপনার স্ট্রিমলিট্ অ্যাপের জন্য ব্যবহার করার জন্য সমস্ত দুর্দান্ত ইনপুট/আউটপুট উইজেট সম্পর্কে জানুন
    """
    )

# Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    "[স্ট্রিমলিট্](https://streamlit.io) হল একটি পাইথন লাইব্রেরি যা পাইথনে ইন্টারেক্টিভ, ডেটা-চালিত ওয়েব অ্যাপ্লিকেশন তৈরি করতে দেয়"
)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [স্ট্রিমলিট্ ডকুমেন্টেশন](https://docs.streamlit.io/)
- [চিট শীট](https://docs.streamlit.io/library/cheatsheet)
- [বই](https://www.amazon.com/dp/180056550X) (ডেটা সায়েন্সের জন্য স্ট্রিমলিট্ দিয়ে শুরু করা)
- [ব্লগ](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (ডেটা সায়েন্সের জন্য কীভাবে স্ট্রিমলিট্ আয়ত্ত করবেন)
"""
)

st.sidebar.header("Deploy")
st.sidebar.markdown(
    "আপনি মাত্র কয়েকটি ক্লিকে [স্ট্রিমলিট্ কমিউনিটি ক্লাউড](https://streamlit.io/cloud) ব্যবহার করে দ্রুত স্ট্রিমলিট্ অ্যাপ স্থাপন করতে পারেন।"
)

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f"# 🗓️ {i}")
        j = i.replace(" ", "")
        with open(f"content/{j}.md", "r") as f:
            st.markdown(f.read(), encoding="utf-8")
        if os.path.isfile(f"content/figures/{j}.csv") == True:
            st.markdown("---")
            st.markdown("### Figures")
            df = pd.read_csv(f"content/figures/{j}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
