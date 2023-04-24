import streamlit as st
import pandas as pd
import altair as alt

# Load the dataset
df = pd.read_csv('datafile (1).csv')

# Set the page title
st.set_page_config(page_title='Crop Cost and Yield Data', layout='wide')

# Create a title for the app
st.title('Crop Cost and Yield Data')

# Create a sidebar with options for the user to select
options = ['Cost of Cultivation A2+FL', 'Cost of Cultivation C2', 'Cost of Production C2']
selected_option = st.sidebar.selectbox('Select an option:', options)

# Group the data by crop and state
grouped_data = df.groupby(['Crop', 'State']).mean().reset_index()

# Create a chart of the selected option by crop and state
if selected_option == 'Cost of Cultivation A2+FL':
    chart = alt.Chart(grouped_data).mark_bar().encode( x='State',y='Cost of Cultivation (`/Hectare) A2+FL',color='Crop')
elif selected_option == 'Cost of Cultivation C2':
    chart = alt.Chart(grouped_data).mark_bar().encode(x='State',y='Cost of Cultivation (`/Hectare) C2',color='Crop')
elif selected_option == 'Cost of Production C2':
    chart = alt.Chart(grouped_data).mark_bar().encode(x='State',y='Cost of Production (`/Quintal) C2',color='Crop')
#elif selected_option == 'Yield (Quintal/ Hectare)':
 #   chart = alt.Chart(grouped_data).mark_bar().encode(x='State',y='Yield (Quintal/ Hectare)',color='Crop')

# Display the chart
st.altair_chart(chart, use_container_width=True)

# Display the raw data
st.subheader('Raw Data')
st.write(df)
