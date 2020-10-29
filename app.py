import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import seaborn as sns


def main():
    st.title('Wireless Access Point Security Encryption')
    st.text('Using Streamlit==0.52.1+')

    activities=['EDA', 'Plot', 'Model Building', 'About']
    choice= st.sidebar.selectbox('Select Activity', activities)

    if choice=='EDA':
        st.subheader('Exploratory Data Analysis')

        data=st.file_uploader('Upload Dataset', type=["csv", "txt"])

        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Show shape"):
                st.write(df.shape)

            if st.checkbox("Show columns"):
                all_columns=df.columns.to_list()
                st.write(all_columns)

            if st.checkbox('Select Columns To Show'):
                all_columns=df.columns.to_list()
                selected_columns=st.multiselect('Select Columns', all_columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            if st.checkbox("Show summary"):
                st.write(df.describe())

            if st.checkbox("Show value counts"):
                st.write(df.iloc[:,-1].value_counts())

    elif choice=='Plot':
        st.subheader('Data Visualization')
        data = st.file_uploader('Upload Dataset', type=['csv', 'txt'])

        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox('Correlation with Seaborn'):
                st.write(sns.heatmap(df.corr(), annot=True))
                st.pyplot()

            if st.checkbox('Pie Chart'):
                all_columns=df.columns.to_list()
                columns_to_plot = st.selectbox('Select 1 Column', all_columns)
                pie_plot=df[columns_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(pie_plot)
                st.pyplot()

            all_columns_names = df.columns.to_list()
            type_of_plot = st.selectbox("Select type of Plot", ["area", "bar", "line"])
            selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)            

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names[0]))

                if type_of_plot == 'area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot == 'bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot == 'line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)


                #custom plot 
                elif type_of_plot:
                    cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
                    st.write(cust_plot)
                    st.pyplot()



            

    elif choice=='Model Building':
        st.subheader('Building ML Model')

    elif choice=='About':
        st.subheader('About')


if __name__=='__main__':
    main()
