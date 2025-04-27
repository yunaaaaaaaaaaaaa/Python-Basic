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
encoded_image_1 = get_base64_image(image_path)

# Path to the second image file.
image_path_2 = "2.png"  # Change this to your second image file path.
# Encode the second image to a base64 string.
encoded_image_2 = get_base64_image(image_path_2)
# HTML code that displays the image with an overlay clickable area.

# Add a Streamlit button to start the game
start_button = st.button('Start')

# HTML code that displays the image with an overlay clickable area.
if start_button:
    # When 'Start' is clicked, hide the red box
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
        /* Initially the clickable area has the red border */
        .clickable-area {{
          position: absolute;
          top: 270px;         /* Distance from the top of the container */
          left: 35px;       /* Distance from the left of the container */
          width: 150px;      /* Width of the clickable area */
          height: 50px;     /* Height of the clickable area */
          cursor: pointer;   /* Change the mouse pointer to indicate clickable area */
          border: 2px solid red; /* Red border to visually identify the clickable area */
        }}
        /* When the start button is clicked, hide the clickable area */
        .hidden {{
          display: none;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <!-- Display the image using the base64 encoded string -->
        <img id="dynamicImage" src="data:image/jpeg;base64,{encoded_image_1}" width="600" alt="Clickable Image">
        <!-- Div element that acts as the clickable overlay area -->
        <div class="clickable-area" id="clickable-area" onclick="changeImage()"></div>
      </div>
      <script>
        // Function that is executed when the clickable area is clicked.
        function changeImage() {{
          // Get the image element by its ID.
          var imageElement = document.getElementById("dynamicImage");
          
          // Change the image source to the second image.
          imageElement.src = "data:image/jpeg;base64,{encoded_image_2}";
          
          // Hide the clickable red box once the image changes.
          document.getElementById("clickable-area").classList.add("hidden");
        }}
      </script>
    </body>
    </html>
    """
else:
    # HTML code with the red box visible before "Start" is clicked.
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
        <img id="dynamicImage" src="data:image/jpeg;base64,{encoded_image_1}" width="600" alt="Clickable Image">
        <!-- Div element that acts as the clickable overlay area -->
        <div class="clickable-area" id="clickable-area" onclick="changeImage()"></div>
      </div>
      <script>
        // Function that is executed when the clickable area is clicked.
        function changeImage() {{
          // Get the image element by its ID.
          var imageElement = document.getElementById("dynamicImage");
          
          // Change the image source to the second image.
          imageElement.src = "data:image/jpeg;base64,{encoded_image_2}";
          
          // Hide the clickable red box once the image changes.
          document.getElementById("clickable-area").classList.add("hidden");
        }}
      </script>
    </body>
    </html>
    """

    # Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)