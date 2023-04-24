import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set page title
st.set_page_config(page_title='Crop Production Dashboard')


# Load data
data = pd.read_csv('datafile (2).csv')

# Rename columns
data.columns = ['Crop', 'Production_2006_07', 'Production_2007_08', 'Production_2008_09', 'Production_2009_10', 'Production_2010_11',
                'Area_2006_07', 'Area_2007_08', 'Area_2008_09', 'Area_2009_10', 'Area_2010_11',
                'Yield_2006_07', 'Yield_2007_08', 'Yield_2008_09', 'Yield_2009_10', 'Yield_2010_11']

# Set page title
#st.set_page_config(page_title='Crop Production Dashboard')

# Set sidebar
st.sidebar.header('Filter Data')
crop_list = data['Crop'].unique()
crop_filter = st.sidebar.multiselect('Select Crop(s)', crop_list)

# Filter data
filtered_data = data[data['Crop'].isin(crop_filter)]

# Visual 1: Production by Year
st.header('Production by Year')
prod_columns = ['Production_2006_07', 'Production_2007_08', 'Production_2008_09', 'Production_2009_10', 'Production_2010_11']
prod_data = filtered_data[prod_columns].sum()
st.bar_chart(prod_data)

# Visual 2: Area by Year
st.header('Area by Year')
area_columns = ['Area_2006_07', 'Area_2007_08', 'Area_2008_09', 'Area_2009_10', 'Area_2010_11']
area_data = filtered_data[area_columns].sum()
st.bar_chart(area_data)

# Visual 3: Yield by Year
st.header('Yield by Year')
yield_columns = ['Yield_2006_07', 'Yield_2007_08', 'Yield_2008_09', 'Yield_2009_10', 'Yield_2010_11']
yield_data = filtered_data[yield_columns].mean()
st.bar_chart(yield_data)

# Visual 4: Production vs. Area
st.header('Production vs. Area')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Production_2010_11', y='Area_2010_11', hue='Crop', ax=ax)
st.pyplot(fig)

# Visual 5: Yield vs. Area
st.header('Yield vs. Area')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Yield_2010_11', y='Area_2010_11', hue='Crop', ax=ax)
st.pyplot(fig)

# Visual 6: Production by Crop
st.header('Production by Crop')
prod_by_crop = filtered_data.groupby('Crop')[prod_columns].sum()
st.bar_chart(prod_by_crop)





# Show filtered data
st.header('Filtered Data')
st.write(filtered_data)
