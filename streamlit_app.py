import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title("My Moms Healty Dinner")
streamlit.header("Breakfast favorits")
streamlit.text("🥣 Omega 3 blueberry")
streamlit.text(" 🥗 Kale,Spanish,Rocket Smoothie")
streamlit.text(" 🐔 Eggs boiled")
streamlit.text("🥑🍞 Avacado tost")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
stremlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

