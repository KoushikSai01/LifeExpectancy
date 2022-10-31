import seaborn as sns
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import streamlit as st
from scipy.stats import zscore

l=pd.read_csv("LifeExpectancyData.csv")

st.write("""
# ✨ Life Expectancy ✨. 
### The goal is to see how Life Expectancy varies in each country and can we predict the life expectancy in a country by seeing the status of the country.
""")
l1 = l.copy()
l12= l.isnull()

imputer=SimpleImputer(missing_values=np.nan,strategy='mean',fill_value=None)
l['Life expectancy ']=imputer.fit_transform(l[['Life expectancy ']])
l['Adult Mortality']=imputer.fit_transform(l[['Adult Mortality']])
l['Alcohol']=imputer.fit_transform(l[['Alcohol']])
l['Hepatitis B']=imputer.fit_transform(l[['Hepatitis B']])
l[' BMI ']=imputer.fit_transform(l[[' BMI ']])
l['Polio']=imputer.fit_transform(l[['Polio']])
l['Total expenditure']=imputer.fit_transform(l[['Total expenditure']])
l['Diphtheria ']=imputer.fit_transform(l[['Diphtheria ']])
l['GDP']=imputer.fit_transform(l[['GDP']])
l['Population']=imputer.fit_transform(l[['Population']])
l[' thinness  1-19 years']=imputer.fit_transform(l[[' thinness  1-19 years']])
l[' thinness 5-9 years']=imputer.fit_transform(l[[' thinness 5-9 years']])
l['Income composition of resources']=imputer.fit_transform(l[['Income composition of resources']])
l['Schooling']=imputer.fit_transform(l[['Schooling']])

option = st.radio(
    "What would you like to do",
    ('See Authors plots','Use Interactive Plot','See the Dataset'))

if option == 'See Authors plots':
    st.write("### Here I am trying to see how the Life Expectancy changed over the years for the developed and developing countries.")
    
    fig1=plt.figure(figsize=(10,5))
    sns.histplot(data=l,x= "Life expectancy ")
    st.write("Histogram plot")
    st.pyplot(fig1)
    st.write("Count plot of the life expectancy across all countries.")

    fig5=plt.figure(figsize=(10,5))
    sns.scatterplot(data=l, x="Life expectancy ", y="percentage expenditure",hue='Status', palette='rocket')
    st.write("Scatter plot")
    st.pyplot(fig5)
    st.write("Plot depicting how much developed and developing countries spend on health as a percentage of GDP per capita.")


    fig4=plt.figure(figsize=(10,5))
    sns.lineplot(data=l, x="Year", y="Life expectancy ",hue='Status')   
    st.write("Line plot")
    st.pyplot(fig4)
    st.write("Progress of Life expectancy in developed and developing countries over the years")

    fig2=plt.figure(figsize=(10,5))
    sns.lineplot(data=l, x="GDP", y="Life expectancy ",hue='Status',)
    st.write("Line plot")
    st.pyplot(fig2)

elif option == 'See the Dataset':

    st.write("### Initial Data")
    st.write(l1)

    st.write("The Data in the dataset and their description is given below")
    st.write("Country - contains name of the country.")
    st.write("Year - The year in which the values are recorded ")
    st.write("Status - the status of the country - i.e Developed or Developing")
    st.write("Life Expectancy - Life expectancy in age")
    st.write("Adult Mortality - Probability of adults(male and female) dying between ages 15 and 60 out of 1000 people")
    st.write("Infant Deaths - Number of Infant Deaths per 1000 population")
    st.write("Alcohol - Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)")
    st.write("Percentage expenditure - Expenditure on health as a percentage of Gross Domestic Product per capita(%)")
    st.write("Hepatitis B - Hepatitis B (HepB) immunization coverage among 1-year-olds (%)")
    st.write("Measels - Measles - number of reported cases per 1000 population")
    st.write("BMI - Average Body Mass Index of entire population")
    st.write("Under 5 Deaths - Number of under-five deaths per 1000 population")
    st.write("Polio - Polio (Pol3) immunization coverage among 1-year-olds (%)")
    st.write("Total Expenditure - General government expenditure on health as a percentage of total government expenditure (%)")
    st.write("Diptheria - Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)")
    st.write("HIV/AIDS - Deaths per 1 000 live births HIV/AIDS (0-4 years)")
    st.write("GDP - Gross Domestic Product per capita (in USD)")
    st.write("Population - Population of the country")
    st.write("Thinness 1-19 years - Prevalence of thinness among children and adolescents for Age 10 to 19 (% )")
    st.write("Thinness 5-9 years - Prevalence of thinness among children for Age 5 to 9(%)")
    st.write("Income Composition of resources - Human Development Index in terms of income composition of resources (index ranging from 0 to 1)")
    st.write("Schooling - Number of years of Schooling(years)")
    
    
    st.write("The null values are at positions as below")
    st.write(l12)

    st.write("### Data after mean imputation")
    st.write(l)

    st.write("To verify there are no Null values")
    st.write(l.isnull())



elif option == 'Use Interactive Plot':
    ip1 = st.radio(
        "Do an interactive of all attributes or just Country against other attributes ?",
        ('All','Country'))

    if ip1 == 'All':
        st.write("Select the x axis and y axis to make the interactive plot")
        select_option_1= st.selectbox("x axis feature?", l.columns)
        st.write('You selected:', select_option_1)
            #choosing option-2 from the dropdown
            
            # choosing which plot
            
        select_option_2= st.selectbox("y axis feature?", l.columns)
        st.write('You selected:', select_option_2)

        k=alt.Chart(l).mark_circle().encode(
        x=select_option_1,
        y=select_option_2,
        color='Year',
        tooltip=[select_option_1,select_option_2,'Year',"Life expectancy "]
        ).interactive()
        st.altair_chart(k)


    else:
        st.sidebar.title("""
        # Country wise plots 
        Select the Country and attributes to see how Life Expectancy varies with others in each countries 
        """)

        # allow user to choose which portion of the data to explore
        choice_country = st.sidebar.selectbox(
            "Select the Country of your choice",
            l["Country"].unique())
            

        cols = ['Life expectancy ', 'Adult Mortality',
        'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
        'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',
        'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',
        ' thinness  1-19 years', ' thinness 5-9 years',
        'Income composition of resources', 'Schooling']

        choice = st.sidebar.selectbox(
            "Select an attribute to see how it varied over the years",
            cols)
        st.sidebar.write("Use the slider on the right to vary the duration")

        color = st.select_slider(
            'Select the period during which you want to know the data',
            options= l["Year"].unique())

        st.write('Selected till', color)



        timeline = []
        temp_data = l.where(l['Country'] == choice_country).dropna()
        req_data = temp_data.where(temp_data['Year'] <= color).dropna()

        # do the visuslization for req_data as time series plots


        reqchart = alt.Chart(req_data).mark_area().encode(
            x='Year:N',
            y= choice,
            tooltip=["Life expectancy ",'Year',choice,'Status'],
        ).interactive()

        # Display both charts together
        st.altair_chart((reqchart).interactive(), use_container_width=True)
