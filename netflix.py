import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from PIL import Image
logo = Image.open('logo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run netflix.py 
st.set_page_config(page_title="NetFlix  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = ["21A21A6112-G.Renuka", "21A21A6139-M.Venkat", "21A21A6155-T.Navya Sri","21A21A6143-P.Annapurna","21A21A6118-J.Chaithanya Manoj","21A21A6149-P.Riteesh Varma","21A21A6121-M.Jagadeesh"]
st.title("Exploratory Data Analysis on NetFlix Data Set")
# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")

# File upload

uploaded_file = st.file_uploader("Choose a NetFlix Dataset csv")

if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
    # Set up the Streamlit app
    st.title('Exploratory Data Analysis of the Netflix Dataset')
    st.title('Choose Your Options')
    # Display options in the sidebar
    option = st.selectbox('Select an option', ['NetFlix Data Analysis Basic Information', 'View Summary', 'View Visualization','Queries Based on Netflix Data Set'])
    # View the data
    if option == 'NetFlix Data Analysis Basic Information':
        st.title("NetFlix Data Analysis Basic Information")
        if st.checkbox('Dimensions and Shape of the Data Set'):
            st.write("SHAPE :", data.shape)
        if st.checkbox('Data Types Pressnt in the Data Set'):
            st.write("DATA TYPES :", data.dtypes)
        if st.checkbox('Columns Pressnt in the Data Set'):
            st.write("COLUMNS :", data.columns)
        if st.checkbox('No of rows and columns in the data set'):
            st.write("Number of rows : ",len(data))
            st.write("Number of columns : ",len(data.columns))
        if st.checkbox('Show unique values in Category column'):
            st.write(data['Category'].unique())
        if st.checkbox('Show unique values in Title column'):
            st.write(data['Title'].unique())
        if st.checkbox('Show unique values in Director column'):
            st.write(data['Director'].unique())
        if st.checkbox('Show unique values in Cast column'):
            st.write(data['Cast'].unique())
        if st.checkbox('Show unique values in Country column'):
            st.write(data['Country'].unique())
        if st.checkbox('Show unique values in Release_Date column'):
            st.write(data['Release_Date'].unique())
        if st.checkbox('Show unique values in Duration column'):
            st.write(data['Duration'].unique())
        if st.checkbox('Show unique values in Type column'):
            st.write(data['Type'].unique())
    # View the summary statistics
    elif option == 'View Summary':
        st.write(data.describe())
    # View the visualization
    elif option == 'View Visualization':
        # Choose the type of visualization
        plot_type = st.selectbox('Select a plot type', ['Histogram', 'Boxplot', 'Scatter Plot'])
        # Display the visualization
        if plot_type == 'Histogram':
            data['Date'] = pd.to_datetime(data['Release_Date'])
            # extract the year from the datetime object
            data['Year'] = data['Date'].dt.year
            # Create a histogram of the release dates
            fig, ax = plt.subplots()
            ax.hist(data['Year'], bins=30)
            # Set the chart title and labels
            ax.set_title("Distribution of Netflix Content Release Dates")
            ax.set_xlabel("Year")
            ax.set_ylabel("Count")
            # Display the chart in the Streamlit app
            st.pyplot(fig)
        elif plot_type == 'Boxplot':
            data['Date'] = pd.to_datetime(data['Release_Date'])
            # extract the year from the datetime object
            data['Year'] = data['Date'].dt.year
            # Create a boxplot of the release date
            fig, ax = plt.subplots()
            sns.boxplot(x=data['Year'],y=data['Category'], ax=ax)
            ax.set_title('Boxplot of Netflix Release Date by Year')
            ax.set_xlabel('Year')
            ax.set_ylabel('Category')

            # Show the plot in Streamlit
            st.pyplot(fig)

        elif plot_type == 'Scatter Plot':
            x_var = st.selectbox("x-axis variable",data.columns)
            y_var = st.selectbox("y-axis variable",data.columns)
            fig,ax=plt.subplots()
            ax.scatter(data[x_var],data[y_var])
            ax.set_xlabel(x_var)
            ax.set_ylabel(y_var)
            ax.set_title(f"{x_var} vs {y_var}")
            st.pyplot(fig)
    if option == 'Queries Based on Netflix Data Set':
        st.title("Queries on Data Set")
        # Question 1
        if st.checkbox('Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.'):
            st.write("Original shape:", data.shape)
            data.drop_duplicates(inplace = True) 
            st.write("New shape:", data.shape)
        # Question 2
        if st.checkbox('Is there any Null Value present in any column ? Show with Heat-map.'):
            st.write(data.isnull().sum())
            sns.heatmap(data.isnull(), cmap='viridis')
        # Question 3
        if st.checkbox('For "House of Cards", what is the Show Id and Who is the Director of this show ?'):
            st.write(data[data['Title'].isin(['House of Cards'])][['Show_Id', 'Director']])
        # Question 4
        if st.checkbox('In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.'):
            data['Date_N'] = pd.to_datetime(data['Release_Date'])
            year_wise_data = data['Date_N'].dt.year.value_counts()
            st.bar_chart(year_wise_data)
        # Question 5
        if st.checkbox('How many Movies & TV Shows are in the dataset ? Show with Bar Graph.'):
            category_wise_data = data['Category'].value_counts()
            st.bar_chart(category_wise_data)
        # Question 6
        if st.checkbox('Show all the Movies that were released in year 2000.'):
            # convert the date string to datetime object
            # #data['Date'] = pd.to_datetime(data['Release_Date'], format='%d-%b-%y')
            data['Date'] = pd.to_datetime(data['Release_Date'])
            # extract the year from the datetime object
            data['Year'] = data['Date'].dt.year
            st.write(data[(data['Category'] == 'Movie') & (data['Year']==2000)]['Title'])
        # Question 7
        if st.checkbox('Show only the Titles of all TV Shows that were released in India only.'):
            st.write(data[ (data['Category']=='TV Show') & (data['Country']=='India') ]['Title'])
        # Question 8
        if st.checkbox('Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?'):
            st.write(data['Director'].value_counts().head(10))
        # Question 9
        if st.checkbox('What are the different Ratings defined by Netflix ?'):
            st.write(data['Rating'].unique())
        # Question 9.1
        if st.checkbox('How many Movies got the "TV-14" rating, in Canada ?'):
            st.write(data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14') & (data['Country']=='Canada')].shape[0])
        # Question 9.2
        if st.checkbox('How many TV Show got the "R" rating, after year 2018 ?'):
            data['Date'] = pd.to_datetime(data['Release_Date'])
            data['Year'] = data['Date'].dt.year
            st.write(data[(data['Category']=='TV Show') & (data['Rating']=='R') & (data['Year'] > 2018)].shape[0])
        # Question 10
        if st.checkbox('What is the maximum duration of a Movie/Show on Netflix ?'):
            data['Minutes'] = data['Duration'].apply(lambda x: int(x.split()[0]))
            st.write(data['Minutes'].max())
        # Question 11
        if st.checkbox('Which individual country has the Highest No. of TV Shows ?'):
            tvshow_data = data[data['Category'] == 'TV Show']
            st.write(tvshow_data['Country'].value_counts().head(1))
        # Question 12
        if st.checkbox('How can we sort the dataset by Year ?'):
            st.write(data.sort_values(by = 'Year'))
        if st.checkbox('Sort dataset by Year in descending order'):
            st.write(data.sort_values(by = 'Year', ascending = False))
        #Question 13
        if st.checkbox('Find all the instances where : Category is "Movie" and Type is "Dramas" or Category is "TV Show" and Type is "Kids TV"'):
            Category_1 = st.text_input("categroy_1")
            Category_2 = st.text_input("category_2")
            type_1 = st.text_input("type_1")
            type_2 = st.text_input("type_2")
            st.write(data[(data['Category'] == Category_1) & (data['Type'] == type_1) | (data['Category'] == Category_2) & (data['Type'] == type_2)])

