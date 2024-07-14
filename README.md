# ProphAIcy
ProphAIcy is a simple web app built with Streamlit that summarizes and visualizees your raw data into meaningful insights with help of Pandas and Seaborn. It also uses PandasAI powered with Gemini to let you speak with your data!
# Project Structure
```
├── app.py       # contains the Entire App Code written in Streamlit
├── setup.sh
├── requirements.txt
└── README.md

```
# Steps for App Installation
1. Clone the App

     ``` git clone https://github.com/pranayvaranasi/ProphAIcy ```

2. Create the Virtual Environment and Activate it

    ``` python3 -m venv streamlit_env ```

    ```source streamlit_env/bin/activate```

3.  Install Necessary Libraries

    ```pip3 install -r requirements.txt```

4. Set your Google Gemini API key in app.py code and save it
  
5.  Set basic environmental variables

    ``` export STREAMLIT_APP= app.py ```

    ```export STREAMLIT_ENV=development ```
    
7. Run the Application

   ``` python3 app.py ```

# App Overview

1. **Dataset Upload:**
   - User uploads dataset (usually in CSV format) to ProphAIcy.
   - Upon upload, ProphAIcy shows  the head of the dataset—the first few rows.

2. **Summarization:**
   - When the user clicks "Summarize," ProphAIcy summarizes on the uploaded content.
   - Similary, user can see Null Values, Value Counts, Missing Values etc

3. **Visualization:**
   - User can jump to Visualization section by clicking on the arrow in top left
   - Users can click on  multiple options like Bar graph, Pie Chart, Box Plot etc to visualize 
     their dataset
4. **Chat with Dataset:**
   - A Text Box is provided in the end of both Visualization and Summarization section to let 
     users chat with their dataset

# Demonstration 
   
   
   
