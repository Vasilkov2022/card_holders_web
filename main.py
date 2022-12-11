import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("BankChurners.csv")
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

data[['Card_Category']].value_counts()
cards_types = ['Blue', 'Silver', 'Gold', 'Platinum']

def card_type(type_name):
    blue_attrition = data[(data.Attrition_Flag == 'Attrited Customer') & (data.Card_Category == type_name)]
    blue_at_c = blue_attrition.CLIENTNUM.count()
    blue_exi = data[(data.Attrition_Flag == 'Existing Customer') & (data.Card_Category == type_name)]
    blue_total = blue_at_c + blue_exi.CLIENTNUM.count()
    print(blue_exi.CLIENTNUM.count())
    prec = (blue_at_c/blue_total).round(3)*100
    labels = 'Attrited Customer', 'Existing Customer'
    sizes = [prec, 100 - prec]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    fig1.set_facecolor(color=None)
    st.pyplot(fig1)



st.subheader('The piechart shows the proportion of blue cards holders, who abandon the service of the bank')
card_type('Blue')
st.subheader('The piechart shows the proportion of silver cards holders, who abandon the service of the bank')
card_type('Silver')
st.subheader('The piechart shows the proportion of gold cards holders, who abandon the service of the bank')
card_type('Gold')
st.subheader('The piechart shows the proportion of platinum cards holders, who abandon the service of the bank')
card_type('Platinum')
