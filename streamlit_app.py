import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title("My Moms Healty Dinner")
streamlit.header("Breakfast favorits")
streamlit.text("🥣 Omega 3 blueberry")
streamlit.text(" 🥗 Kale,Spanish,Rocket Smoothie")
streamlit.text(" 🐔 Eggs boiled")
streamlit.text("🥑🍞 Avacado tost")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)

