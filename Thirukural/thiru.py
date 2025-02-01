import streamlit as st
import pandas as pd
df = pd.read_csv("Thirukural1.csv")
df.head()

result = pd.DataFrame()

st.title("Thirukural Search")
search_type = st.radio("Search by:", ["Chapter Name", "Section Name"])


if search_type == "Chapter Name":
    chapter = st.text_input("Enter Chapter Name")
    result = df[df["Chapter Name"].str.contains(chapter, case=False, na=False)]
elif search_type == "Section Name":
    section = st.text_input("Enter Section Name")
    result = df[df["Section Name"].str.contains(section, case=False, na=False)]

# Display results
if not result.empty:
    st.write(f"### {result['Concept Name'].values[0]}")
    st.write(f"**Section:** {result['Section Name'].values[0]}")
    st.write(f"**Verse (Tamil):**")
    st.write(result["Verse"].values[0])
    st.write(f"**Translation (English):**")
    st.write(result["Translation"].values[0])
    st.write(f"**Explanation (Tamil):**")
    st.write(result["Explanation"].values[0])
else:
    st.write("No matching results found.")
