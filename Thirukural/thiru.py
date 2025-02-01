import streamlit as st
import pandas as pd
df = pd.read_csv("Thirukural1.csv")
df.head()
print(df.columns)
result = pd.DataFrame()

st.title("Thirukural Search")
search_type = st.radio("Search by:", ["ChapterName", "SectionName"])


if search_type == "ChapterName":
    chapter = st.text_input("Enter ChapterName")
    result = df[df["ChapterName"].str.contains(chapter, case=False, na=False)]
elif search_type == "SectionName":
    section = st.text_input("Enter SectionName")
    result = df[df["SectionName"].str.contains(section, case=False, na=False)]

# Display results
if not result.empty:
    st.write(f"### {result['ChapterName'].values[0]}")
    st.write(f"**Section:** {result['SectionName'].values[0]}")
    st.write(f"**Verse (Tamil):**")
    st.write(result["Verse"].values[0])
    st.write(f"**Translation (English):**")
    st.write(result["Translation"].values[0])
    st.write(f"**Explanation (Tamil):**")
    st.write(result["Explanation"].values[0])
else:
    st.write("No matching results found.")
