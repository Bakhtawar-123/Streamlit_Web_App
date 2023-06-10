import streamlit as st
import pandas as pd
import plotly.express as px

# Create a sample DataFrame
data = pd.read_csv(r'C:\Users\sobia\OneDrive\Desktop\streamlit_dashboard\Advertising.csv')
df = pd.DataFrame(data)

# Set up the Streamlit app
st.title('Sales Prediction using Various Advertisement')

# Display the DataFrame
st.write('Data:')
st.dataframe(df)

# Create an animated bar chart using Plotly Express
fig = px.bar(df, x='Sales', y=['TV', 'Radio', 'Newspaper'], animation_frame=df.index,
             range_y=[0, df[['TV', 'Radio', 'Newspaper']].max().max() * 1.1],
             title='Sales Contribution by Advertising Medium Over Time')
fig.update_layout(xaxis_title='Sales', yaxis_title='Advertising Medium')

# Display the animated graph using Streamlit
st.write('Animated Graph:')
st.plotly_chart(fig)
st.header("Enjoy exploring the predictions!")
