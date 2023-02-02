streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else: 
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
#streamlit.write('The user entered ', fruit_choice)
    
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
    
# write your own comment - what does this do?
  

#except URLError as e:
  #streamlit.error()

#streamlit.stop()


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")


#streamlit.text("Hello from Snowflake:")



#add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding ', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
