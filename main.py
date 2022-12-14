import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("BankChurners.csv")
# data.columns = ['Clients', 'Attrition_Flag', 'Customer age', 'Gender', 'Number of dependents', 'Educational Qualification', 'Martial status', 'income category', 'Card category', 'Period of relationship with bank', 'Total no. of products', 'No. of months inactive', 'No. of Contacts', 'Credit Limit', 'Total Revolving Balance', 'Open to Buy Credit Line', 'Change in Transaction Amount', 'Total Transaction Amount', 'Total Transaction Count', 'Change in Transaction Count', 'Average Card Utilization Ratio']
# print(data)
st.title('Mid-term report')
st.header('The problem is that some customers of the bank refuse credit services of the bank. I have a hypothesis that people with graetest credit limit and elder people refuse bank credit servises.')
st.subheader('Credit cards holders analys')
st.write('Table short info')
st.write(data.head())
st.header('This chart shows numbers of existing customers of specific age')
st.bar_chart(data[(data.Attrition_Flag == 'Existing Customer')]['Customer_Age'].value_counts())
#
# fig = plt.figure(figsize=(10, 4))
# sns.boxplot(data=data, x='Education_Level', y='Credit_Limit')
# st.pyplot(fig)
st.header('The graph shows existing customers and attrited customers, their ages and credit limit')
fig = px.scatter(data, x="Customer_Age", y="Credit_Limit", color="Attrition_Flag",
                 marginal_x="box", marginal_y="violin")
st.plotly_chart(fig)

data[['Card_Category']].value_counts()
cards_types = ['Blue', 'Silver', 'Gold', 'Platinum']

def card_type(type_name):
    blue_attrition = data[(data.Attrition_Flag == 'Attrited Customer') & (data.Card_Category == type_name)]
    blue_at_c = blue_attrition.CLIENTNUM.count()
    blue_exi = data[(data.Attrition_Flag == 'Existing Customer') & (data.Card_Category == type_name)]
    blue_total = blue_at_c + blue_exi.CLIENTNUM.count()
    # print(blue_exi.CLIENTNUM.count())
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
# print(ages)

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
st.subheader('The pie chart shows the proportion of single customers, who abandoned services of bank and those, who are still its customers')
piechart(n_as, n_es, 'Single')
st.subheader('The pie chart shows the proportion of divorced customers, who abandoned services of bank and those, who are still its customers')
piechart(n_ad, n_ed, 'Divorced')

st.subheader('The histogram below shows a quantity of both types of costumers of the bank according their income per 12 months')
fig = px.histogram(data, x='Income_Category', category_orders=dict(Income_Category=["Less than $40K", '$40K - $60K', "$60K - $80K", '$80K - $120K', '$120K +']))
data = data[data['Income_Category'] != 'Unknown']
st.pyplot(fig)

st.subheader('The histogram below shows a quantity of existing costumers of the bank according their income per 12 months')
inc_ex = data[data['Attrition_Flag'] == 'Existing Customer']
fig = px.histogram(inc_ex, x='Income_Category', category_orders=dict(Income_Category=["Less than $40K", '$40K - $60K', "$60K - $80K", '$80K - $120K', '$120K +']))
data = data[data['Income_Category'] != 'Unknown']
st.pyplot(fig)

st.subheader('The histogram below shows a quantity of attrited costumers of the bank according their income per 12 months')
inc_at = data[data['Attrition_Flag'] == 'Attrited Customer']
fig = px.histogram(inc_at, x='Income_Category', category_orders=dict(Income_Category=["Less than $40K", '$40K - $60K', "$60K - $80K", '$80K - $120K', '$120K +']))
data = data[data['Income_Category'] != 'Unknown']
st.pyplot(fig)

st.subheader('Comparing this graphs, we cannot see a big difference between them all.')
st.subheader('Now I will try to find some consequences by taking education varible.')

st.subheader('The diagram shows results of all customers')
data = data[data['Education_Level'] != 'Unknown']
fig = px.histogram(data, x='Education_Level')
st.pyplot(fig)

st.subheader('The diagram shows results of existing customers ')
data = data[data['Education_Level'] != 'Unknown']
inc_ex = data[data['Attrition_Flag'] == 'Existing Customer']
fig = px.histogram(inc_ex, x='Education_Level')
st.pyplot(fig)

st.subheader('The diagram shows results of attrited customers ')
data = data[data['Education_Level'] != 'Unknown']
inc_ex = data[data['Attrition_Flag'] == 'Attrited Customer']
fig = px.histogram(inc_ex, x='Education_Level', category_orders=dict(Education_Level=["High School", 'Graduate', "Uneducated", 'College', 'Post-Graduate', 'Doctorate']))
st.pyplot(fig)

st.subheader('Graphs show that propotions are approximately equal. By the way, comparing the number of doctorate people and the number of graduated people, who refused using credit card, we can see that the second one is 5 times greater than the first group of people. Comparing the sames columns, but in the diagram of existing costumers, the proportion is equal to 7. That confirms my proposition about degree of customers.')
st.subheader()
st.header('As graphs show the age and credit limits have no effect on existing of customers. However, it is important to mention that people with platium cards refuse bank servises more often.')
st.header('What is more, the marital status also has no effect on attrition of customers')
st.header('In addition, analysis shows that married people hold credit cards more often than others')
