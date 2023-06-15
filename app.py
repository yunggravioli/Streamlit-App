import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

uploaded_file = st.sidebar.file_uploader("Choose a file")

st.title("Exploratory Data Analysis")
st.caption("Upload a file through the sidebar and choose a column to analyze")
st.divider()

if uploaded_file is not None:
  # Can be used wherever a "file-like" object is accepted:
  df = pd.read_csv(uploaded_file)


  st.write(f"The given data has {df.shape[0]} rows and {df.shape[1]} columns ")

  st.write('Below are the data types present in this dataset:')
  st.write(df.dtypes.value_counts())

  show_df = st.checkbox("Show Full Data Frame", key="show_df")

  if show_df:
    st.write(df)

  # Only showing the Categorical Option if categorical data exists
  if 'object' in df.dtypes.values:
    column_type = st.sidebar.selectbox('Select Data Type',
                                      ("Numerical", "Categorical"))
  else:
    column_type = "Numerical"

  st.divider()

  if column_type == "Numerical":
    numerical_column = st.sidebar.selectbox(
        'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

    # Numeric five number summary
    st.markdown("**The Current column is numeric so we can list the five number summary**")
    show_summary = st.checkbox("Show Five Number Summary", key="numerical_summary")
    if show_summary:
      st.write(df[numerical_column].describe()[3:8])

    # Histogram
    choose_color = st.color_picker('Pick a Color', "#EA7375")
    choose_opacity = st.slider(
        'Color Opacity', min_value=0.0, max_value=1.0, step=0.05, value=0.70)

    hist_bins = st.slider('Number of bins', min_value=5,
                          max_value=150, value=30)
    hist_title = st.text_input('Set Title', 'Histogram')
    hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

    fig, ax = plt.subplots()
    ax.hist(df[numerical_column], bins=hist_bins,
            edgecolor="black", color=choose_color, alpha=choose_opacity)
    ax.set_title(hist_title)
    ax.set_xlabel(hist_xtitle)
    ax.set_ylabel('Count')

    st.pyplot(fig)
    filename = "plot.png"
    fig.savefig(filename,dpi = 300)

    # Display the download button
    with open("plot.png", "rb") as file:
      btn = st.download_button(
          label="Download image",
          data=file,
          file_name="antonio.png",
          mime="image/png"
      )
    
  if column_type == "Categorical":
    categorical_column = st.sidebar.selectbox(
      'Select a Column', df.select_dtypes('object').columns)
    
    # Pie Chart
    qualitative_cmaps = ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2',
                      'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
                      'tab20c']
    choose_color = st.selectbox('Choose a color map', qualitative_cmaps)
    st.write('Your color choice is:', choose_color)

    hist_title = st.text_input('Set Title', 'Histogram')
    
    categorical_counts = df[categorical_column].value_counts()
    categorical_counts_ind = df[categorical_column].value_counts().index

    fig, ax = plt.subplots()

    cmap = plt.cm.get_cmap(choose_color)
    num_colors = len(categorical_counts)
    colors = [cmap(i % cmap.N) for i in range(num_colors)]

    ax.pie(categorical_counts, labels=categorical_counts_ind, 
          wedgeprops = { 'linewidth' : 0, 'edgecolor' : 'white' }, colors = colors)

    ax.set_title(categorical_column)

    st.pyplot(fig)
    filename = "plot.png"
    fig.savefig(filename,dpi = 300)

    # Display the download button
    with open("plot.png", "rb") as file:
      btn = st.download_button(
          label="Download image",
          data=file,
          file_name="antonio.png",
          mime="image/png"
      )