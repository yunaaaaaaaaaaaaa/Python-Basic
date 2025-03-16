# To run, copy and paste the code below.
# streamlit run yuna.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/
import streamlit as st

st.title("No Poverty")

story = """
In this game, you have to give people money, food, or a house to the poor people, depending on their situation and their needs. 
You have to use your brain to decide whether people need help and what they need. 

"""

st.write(story)

st.image("1.png")                        