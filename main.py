import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("BankChurners.csv")
# data.columns = ['Clients', 'Attrition_Flag', 'Customer age', 'Gender', 'Number of dependents', 'Educational Qualification', 'Martial status', 'income category', 'Card category', 'Period of relationship with bank', 'Total no. of products', 'No. of months inactive', 'No. of Contacts', 'Credit Limit', 'Total Revolving Balance', 'Open to Buy Credit Line', 'Change in Transaction Amount', 'Total Transaction Amount', 'Total Transaction Count', 'Change in Transaction Count', 'Average Card Utilization Ratio']
# print(data)
st.title('Mid-term report')
st.subheader('Credit cards holders analys')
st.write('Table short info')
st.write(data.head())
st.write('This chart shows numbers of existing customers of specific age')
st.bar_chart(data[(data.Attrition_Flag == 'Existing Customer')]['Customer_Age'].value_counts())
#
# fig = plt.figure(figsize=(10, 4))
# sns.boxplot(data=data, x='Education_Level', y='Credit_Limit')
# st.pyplot(fig)

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
    fig1.set_facecolor(color='orange')

    st.pyplot(fig1)



st.subheader('The piechart shows the proportion of blue cards holders, who abandon the service of the bank')
card_type('Blue')
st.subheader('The piechart shows the proportion of silver cards holders, who abandon the service of the bank')
card_type('Silver')
st.subheader('The piechart shows the proportion of gold cards holders, who abandon the service of the bank')
card_type('Gold')
st.subheader('The piechart shows the proportion of platinum cards holders, who abandon the service of the bank')
card_type('Platinum')

st.subheader('The diagram shows the quantity of refused customers of different marital statuses')

ages = st.slider(
    'Select a range of ages',
    18, 80, (25, 75))
a = ages[0]
b = ages[1]
st.write('Age:', str(ages[0]) + '-' + str(ages[1]))
print(ages)

st.bar_chart(data[(data.Attrition_Flag == 'Attrited Customer') & ((data.Customer_Age >= int(a)) & (data.Customer_Age <= int(b)))]['Marital_Status'].value_counts())

st.subheader('The diagram shows the quantity of existing customers of different marital statuses')



st.bar_chart(data[(data.Attrition_Flag == 'Existing Customer') & ((data.Customer_Age >= int(a)) & (data.Customer_Age <= int(b)))]['Marital_Status'].value_counts())

st.subheader('The pie chart shows the proportion of married customers, who abandoned services of bank and those, who are still its customers')
def status(holder, status):
    stat = status
    exi_mrried = data[(data.Attrition_Flag == holder) & (data.Marital_Status == status)]
    q_am = exi_mrried.CLIENTNUM.count()
    return q_am

def piechart(a, b, c):
    prec = (a/(a+b)).round(3)*100
    labels = (str(c) + '  ' + 'Attrited Customer'), (str(c) + ' ' +'Existing Customer')
    sizes = [prec, 100 - prec]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels = labels, autopct='%1.1f%%')
    ax1.axis('equal')

    fig1.set_facecolor(color='orange')

    st.pyplot(fig1)

n_am = status('Attrited Customer', 'Married')
n_as = status('Attrited Customer', 'Single')
n_ad = status('Attrited Customer', 'Divorced')
n_em = status('Existing Customer', 'Married')
n_es = status('Existing Customer', 'Single')
n_ed = status('Existing Customer', 'Divorced')

piechart(n_am, n_em, 'Married')