import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.google_gemini import GoogleGemini
import matplotlib
import numpy as np
import warnings
warnings.filterwarnings("ignore",message="numpy.ufunc size changed")
warnings.filterwarnings("ignore",message="numpy.dtype size changed, may indicate binary incompatibility")

matplotlib.use('Agg')
import seaborn as sns
def main():
    st.title("Visualize and Forecast in a click with ProhAIcy App")
    tasks = ["Summarize", "Visualize"]
    choice =  st.sidebar.selectbox("Select Task", tasks)
    if choice == 'Summarize':
        st.subheader("Summarize with ProphAIcy")
        data = st.file_uploader("Upload Dataset", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            if st.checkbox("Show Shape"):
                st.write(df.shape)
            if st.checkbox("Show Columns"):
                columns = df.columns.to_list()
                st.write(columns)
            if st.checkbox("Show Summary"):
                st.write(df.describe())
            if st.checkbox("Show Selected Columns"):
                selectedcolumns = st.multiselect("Select Columns", columns)
                st.write(df[selectedcolumns])
            if st.checkbox("Correlation Plot"):
                st.write(sns.heatmap(df.corr(), annot=True))
                st.pyplot()
            if st.checkbox("Pie Chart"):
                columns = df.columns.to_list()
                selectcolumns = st.selectbox("Select Column", columns)
                piechart = df[selectcolumns].value_counts().plot.pie(autopct="%1.1f%%")
                st.write(piechart)
                st.pyplot()
            if st.checkbox("Show Missing Values"):
                st.write(df.isnull().sum())
            if st.checkbox("Show Null Values"):
                st.write(df.isna().sum())
            if st.checkbox("Show Data Types"):
                st.write(df.dtypes)
            if st.checkbox("Show Unique Values"):
                st.write(df.nunique())
            if st.checkbox("Show Duplicate Rows"):
                st.write(df.duplicated().sum())
            if st.checkbox("Chat with ProphAIcy"):
                llm= GoogleGemini(api_key='I wish right to API key is basic human right')
                df= SmartDataframe(df,config={'llm':llm})
                query = st.text_input("Ask ProphAIcy a question")
                if query != "":
                        st.write(df.chat(str(query)))
    elif choice == 'Visualize':
        st.subheader("Visualization with ProphAIcy")
        data = st.file_uploader("Upload Dataset", type=["csv", "txt",'xlsx'])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
                st.pyplot()
            columns= df.columns.to_list()
            plot = st.selectbox("Select Plot",["Area","Bar Graph","Line Chart","Line Plot","Histogram","Box Plot"," Boxon Plot", "Kernel Density Estimate", "Pair Plot", "Violin Plot", "Heat Map", "Count Plot", "Pie Chart", "Scatter Plot", "Swarm Plot", "Cat Plot", "Joint Plot"])
            selectedcolumns = st.multiselect("Select Columns to Visualize", columns)
            if st.button("Generate Plot"):
                st.success("Visualizing {} for {}".format(plot,selectedcolumns))
                if plot == "Area":
                    st.area_chart(df[selectedcolumns])
                    st.pyplot()
                elif plot == "Bar Graph":
                    st.bar_chart(df[selectedcolumns])
                    st.pyplot()
                elif plot == "Line Chart":
                    st.line_chart(df[selectedcolumns])
                    st.pyplot()
                elif plot == "Line Plot":
                    for i in selectedcolumns:
                        st.write(sns.lineplot(x=df[i], y=df[i+1]))
                        st.pyplot()
                elif plot == "Histogram":
                    df.hist(selectedcolumns, bins=20)
                    st.pyplot()
                elif plot == "Box Plot":
                    st.write(df[selectedcolumns].boxplot())
                    st.pyplot()
                elif plot == "Boxen Plot":
                    for i in selectedcolumns:
                        st.write(sns.boxenplot(df[i]))
                        st.pyplot()
                elif plot == "Kernel Density Estimate":
                    for i in selectedcolumns:
                        st.write(sns.kdeplot(df[i]))
                        st.pyplot()
                elif plot == "Pair Plot":
                    st.write(sns.pairplot(df))
                    st.pyplot()
                elif plot == "Violin Plot":
                    for i in selectedcolumns:
                        st.write(sns.violinplot(df[i]))
                        st.pyplot()
                elif plot == "Heat Map":
                    st.write(sns.heatmap(df.corr(), annot=True))
                    st.pyplot()
                elif plot == "Count Plot":
                    for i in selectedcolumns:
                        st.write(sns.countplot(df[i]))
                        st.pyplot()
                elif plot == "Pie Chart":
                    for i in selectedcolumns:
                        st.write(df[i].value_counts().plot.pie(autopct="%1.1f%%"))
                        st.pyplot()
                elif plot == "Scatter Plot":
                    for i in selectedcolumns:
                        st.write(sns.scatterplot(x=df[i], y=df[i+1]))
                        st.pyplot()
                elif plot == "Swarm Plot":
                    for i in selectedcolumns:
                        st.write(sns.swarmplot(df[i]))
                        st.pyplot()
                elif plot == "Cat Plot":
                    for i in selectedcolumns:
                        st.write(sns.catplot(x=df[i], y=df[i+1]))
                        st.pyplot()
                elif plot == "Joint Plot":
                    for i in selectedcolumns:
                        st.write(sns.jointplot(x=df[i], y=df[i+1]))
                        st.pyplot()
            if st.checkbox("Visualize with ProphAIcy"):
                llm= GoogleGemini(api_key='I wish right to API key is basic human right')
                df= SmartDataframe(df,config={'llm':llm})
                query = st.text_input("Ask ProphAIcy to visualize")
                if query != "":
                        st.write(df.chat(str(query)))
if __name__ == '__main__':
    main()
                
                
            
