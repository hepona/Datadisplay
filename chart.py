import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns


"""charts"""
warn = "⚠️"


def pie(data, x, y):
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    """create a pie chart"""
    if x_dtype in ["float64", "int64", "datetime64[ns]"]:
        st.error("X should always be a string (category)", icon=warn)
    elif y_dtype == "object":
        st.error("Y should always be a number (value)", icon=warn)
    elif x == y:
        st.error("Please choose a X value different than Y", icon=warn)
    elif x_dtype == "object" and y_dtype == "object":
        st.error("X and Y cannot be both of type string (category)", icon=warn)
    else:
        fig = px.pie(data, names=x, values=y)
        st.plotly_chart(fig)


def line_plot(data, x, y):
    """create a line plot"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype not in ["float64", "int64", "datetime64[ns]"]:
        st.error(
            "X should be a numeric variable for a line plot.",
            icon=warn,
        )
    elif y_dtype not in ["float64", "int64", "datetime64[ns]"]:
        st.error("Y should be a numeric variable for a line plot.", icon=warn)
    else:
        st.line_chart(data, x=x, y=y)


def histogram(data, x, y=None):
    """create histogram chart"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x == y:
        st.error("X and Y should be different", icon=warn)
    elif x_dtype == "object":
        st.error("X should be a numeric variable for an histogram", icon=warn)
    elif y and y_dtype == "object":
        st.error("Y should be a numeric variable for an histogram", icon=warn)
    else:
        if y:
            fig = px.histogram(data, x=x, y=y)
        else:
            fig = px.histogram(data, x=x)
        st.plotly_chart(fig, use_container_width=True)


def boxplot(data, x, y):
    """create boxplot chart"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype != "object" or y_dtype == "object":
        st.error(
            "X should be a categorical variable and Y should be a numeric variable for a boxplot",
            icon=warn,
        )
    elif x == y:
        st.error("X and Y should be different", icon=warn)
    else:
        fig = px.box(data, x=x, y=y, points="all")
        st.plotly_chart(fig)


def bar_plot(data, x, y):
    """create bar plot"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype != "object" or y_dtype == "object":
        st.error(
            "X should be a categorical variable and Y should be a numeric variable for a bar plot",
            icon=warn,
        )
    else:
        st.bar_chart(data=data, x=x, y=y)


def kde_plot(data, x, y):
    """create kde plot"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype == "object" or y_dtype == "object":
        st.error(
            "X and Y should be numeric variable for a KDE plot",
            icon=warn,
        )
    elif x == y:
        st.error("X and Y should be different", icon=warn)
    else:
        fig = px.density_contour(data, x=x, y=y)
        st.plotly_chart(fig)


def scatter_chart(data, x, y):
    """create scatter chart"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype == "object" or y_dtype == "object":
        st.error(
            "X and Y should be numeric variable for a scatter plot",
            icon=warn,
        )
    elif x == y:
        st.error("X and Y should be different", icon=warn)
    else:
        st.scatter_chart(data, x=x, y=y)


def violin_plot(data, x, y):
    """create violin plot"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype != "object" or y_dtype == "object":
        st.error(
            "X should be a categorical variable and Y should be a numeric variable for a violin plot",
            icon=warn,
        )
    elif x == y:
        st.error("X and Y should be different", icon=warn)
    else:
        fig = px.violin(data, x=x, y=y)
        st.plotly_chart(fig)


def heatmap(data, x, y):
    """create heatmap"""
    x_dtype = data[x].dtype
    y_dtype = data[y].dtype
    if x_dtype != "object" or y_dtype != "object":
        st.error(
            "X and Y should be a categorical variable for a Heatmap",
            icon=warn,
        )
    elif x == y:
        st.error("X and Y should be different", icon=warn)
    else:
        fig = px.imshow(data)
        st.plotly_chart(fig, theme="streamlit")
