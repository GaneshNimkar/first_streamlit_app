import streamlit
import pandas
import snowflake.connector


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Moms Healty Dinner")
streamlit.header("Breakfast favorits")
streamlit.text("🥣 Omega 3 blueberry")
streamlit.text(" 🥗 Kale,Spanish,Rocket Smoothie")
streamlit.text(" 🐔 Eggs boiled")
streamlit.text("🥑🍞 Avacado tost")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruit_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# Normalize JSON 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Create dataframe
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUITYVICE")
my_data_row = my_cur.fetchone()
streamlit.text("My fruit list contains:")
streamlit.dataframe(my_data_row)
