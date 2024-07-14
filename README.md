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
Click on the image below for video demonstration 👇

[![ProphAIcy Demonstration](https://github.com/user-attachments/assets/fd955f1c-0f50-4665-83ca-5de43504b3be)
)](https://youtu.be/axbWaOkE9SM)


# Tools Used : 

![Streamlit](https://github.com/user-attachments/assets/120a0414-6100-4c12-972b-e028454c2654) ![Pandas](https://github.com/user-attachments/assets/28d97b46-c4cd-4cf9-b853-8051929c4c47) ![Seaborn](https://github.com/user-attachments/assets/20af27bf-822f-4b3b-8f0b-a81c3ecf75d5) ![PandasAI](https://github.com/user-attachments/assets/2a0c263a-55fc-4564-8798-b65ef339ea42) ![Gemini](https://github.com/user-attachments/assets/93bdf1c4-69ca-404e-9e5d-15ebc7cf0564) ![VS Code](https://github.com/user-attachments/assets/82c44c5b-807e-4fbd-b3ab-633a814d753c)


# Skills

Web Development, Generative AI, Frontend, API Integration, Data Visualization, Data Analysis
   
   
