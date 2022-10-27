import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & Blueberry oat meal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐓 Hard Boiled Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
     # take the json version of the response and normalize it
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
     #streamlit.text(fruityvice_response.json()) #just writes data to screen
     # Reads fruitycice_response in normalzed format and loads in tabular format
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized
#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      # Display
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

  
# don't run anything past here while we troubleshoot
streamlit.stop()

#import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("SELECT * from fruit_load_list")
          return my_cur.fetchall()
# Add a button to load the ruit
If streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
#streamlit.dataframe(my_data_rows)
fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
