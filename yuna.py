# To run, copy and paste the code below.
# streamlit run yuna.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/



import streamlit as st
import base64

st.title("No Poverty")

story = """
In this game, you have to give people money, food, or a house to the poor people, depending on their situation and their needs. 
You have to use your brain to decide whether people need help and what they need. 
"""
st.write(story)


# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the image file.
image_path = "1.png"  # Change this to your image file path.
# Encode the image to a base64 string.
encoded_image = get_base64_image(image_path)

# HTML code that displays the image with an overlay clickable area.
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    /* Container to hold the image and position the clickable area relative to it */
    .container {{
      position: relative;
      display: inline-block;
    }}
    /* Clickable area overlay positioned over the image */
    .clickable-area {{
      position: absolute;
      top: 270px;         /* Distance from the top of the container */
      left: 35px;       /* Distance from the left of the container */
      width: 150px;      /* Width of the clickable area */
      height: 50px;     /* Height of the clickable area */
      cursor: pointer;   /* Change the mouse pointer to indicate clickable area */
      border: 2px solid red; /* Red border to visually identify the clickable area */
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Display the image using the base64 encoded string -->
    <img src="data:image/jpeg;base64,{encoded_image}" width="600" alt="Clickable Image">
    <!-- Div element that acts as the clickable overlay area -->
    <div class="clickable-area" onclick="handleClick()"></div>
  </div>
  <script>
    // Function that is executed when the clickable area is clicked.
    function handleClick() {{
      // Display a JavaScript alert when the area is clicked.
      window.alert("The clickable area has been clicked!");
    }}
  </script>
</body>
</html>
"""

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
