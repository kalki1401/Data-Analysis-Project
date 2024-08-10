import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

#DATA LOADING
df=pd.read_csv(r'C:\Users\DELL\Downloads\archive (4)\ds2.csv')
# Data Cleaning
df.dropna(inplace=True)  # Remove missing values


# Set page configuration
st.set_page_config(page_title="E-commerce Data Analysis 🛍️", layout="wide")

# # Sidebar for user input
st.sidebar.header('User Input Features')
selected_country = st.sidebar.selectbox('Select Country', df['country'].unique())
selected_metric = st.sidebar.selectbox('Select Metric', ['meanproductsliked', 'topbuyerratio', 'femalebuyersratio', 'meanfollowers'])
show_data = st.sidebar.checkbox('Show Raw Data', value=True)

# Filter data based on user input
filtered_df = df[df['country'] == selected_country]

# Multi-page navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Visualizations", "Download Data", "Custom Analysis"])

if page == "Overview":
    st.title('E-commerce Data Analysis')
    st.write('## Data Overview')
    if show_data:
        st.write(df.head())

elif page == "Visualizations":
    st.title('Data Visualizations')

    # Create columns for the plots
    col1, col2 = st.columns(2)

    with col1:
        # Plot 1: Mean Products Liked by Country
        st.write('### Mean Products Liked by Country')
        fig1 = px.bar(df, x='country', y='meanproductsliked', title='Mean Products Liked by Country')
        st.plotly_chart(fig1)

        # Plot 3: Female Buyers Ratio by Country
        st.write('### Female Buyers Ratio by Country')
        fig3 = px.bar(df, x='country', y='femalebuyersratio', title='Female Buyers Ratio by Country')
        st.plotly_chart(fig3)

    with col2:
        # Plot 2: Top Buyer Ratio by Country
        st.write('### Top Buyer Ratio by Country')
        fig2 = px.bar(df, x='country', y='topbuyerratio', title='Top Buyer Ratio by Country')
        st.plotly_chart(fig2)

        # Plot 4: Mean Followers by Country
        st.write('### Mean Followers by Country')
        fig4 = px.bar(df, x='country', y='meanfollowers', title='Mean Followers by Country')
        st.plotly_chart(fig4)


elif page == "Download Data":
    st.title('Download Filtered Data')
    st.write('## Filtered Data')
    st.write(filtered_df)

    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )

elif page == "Custom Analysis":
    st.title('Custom Analysis')
    st.write('## Create Your Own Analysis')

    # User input for custom analysis
    x_axis = st.selectbox('Select X-axis', df.columns)
    y_axis = st.selectbox('Select Y-axis', df.columns)
    plot_type = st.selectbox('Select Plot Type', ['scatter', 'line', 'bar'])

    if plot_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f'Scatter Plot of {y_axis} vs {x_axis}')
    elif plot_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis, title=f'Line Plot of {y_axis} vs {x_axis}')
    else:
        fig = px.bar(df, x=x_axis, y=y_axis, title=f'Bar Plot of {y_axis} vs {x_axis}')

    st.plotly_chart(fig)

# Custom Theme
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)