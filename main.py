import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/andrei_vasilkov/hse_dataset_project_december/BankChurners.csv")
# print(data)
st.title('Mid-term report')
st.subheader('Credit cards holders analys')
st.write('Table short info')
st.write(data.head())
st.write('This chart shows numbers of existing customers of specific age')
st.bar_chart(data[(data.Attrition_Flag == 'Existing Customer')]['Customer_Age'].value_counts())

fig = plt.figure(figsize=(10, 4))
sns.boxplot(data=data, x='Education_Level', y='Credit_Limit')
st.pyplot(fig)

fig = px.scatter(data, x="Customer_Age", y="Credit_Limit", color="Attrition_Flag",
                 marginal_x="box", marginal_y="violin",
                  title="example")
st.plotly_chart(fig)
