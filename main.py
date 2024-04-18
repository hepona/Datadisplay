import streamlit as st
import pandas as pd
from chart import *
from choose_stat import *

st.title("Import your .CSV file here:")
st.markdown("---")
st.write("How does it work?")
lst = [
    "Import a CSV file, don't forget to check that delimiter is set correctly and the columns are defined in the right format",
    "Select the columns you want to work on (X and Y)",
    "Done! ✔️",
]
for i in lst:
    st.markdown("- " + i)
file = st.file_uploader("Choose a .csv file", type=["csv"])
na_value = st.text_input('Enter the character that represent null value if there is any', '',placeholder='for exemple "?"')
if file is not None:
    col1, col2 = st.columns(2)
    try:

        df = pd.read_csv(file, engine="python", na_values= na_value)
        df = df.dropna()
    except Exception as e:
        print("Error: Please check the file format or delimiter.")
        st.error(f"Error: {e}")
        # exit(1)

    with col2:
        val_head = 5
        num_line = st.slider(
            "Number of lines", min_value=1, max_value=len(df), value=val_head
        )
        head = df.head(num_line)

        x = st.selectbox("Select X value", df.columns)
        y = st.selectbox("Select Y value", df.columns)
        x_dtype = df[x].dtype
        y_dtype = df[y].dtype
        # print(x_dtype, y_dtype)

        type_chart = st.selectbox(
            "Select chart type",
            [
                "Histogram",
                "Line plot",
                "Pie",
                "Boxplot",
                "KDE plot",
                "Bar plot",
                "Scatter plot",
                "Heatmap",
                "Violin plot",
            ],
        )
        st.header(type_chart)
        # print(len(head))
        if len(head) < 2:
            st.error(
                "Insufficient data points. Please choose a different dataset or adjust the number of lines.",
                icon="⚠️",
            )
        else:
            choose(type_chart, head, x, y)
        with col1:
            st.header("Dataframe")
            st.dataframe(head)
            table_stat(df, x)
            table_stat(df, y)


