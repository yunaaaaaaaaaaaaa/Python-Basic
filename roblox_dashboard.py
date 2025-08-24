import re
from urllib.parse import urlparse
import streamlit as st

st.set_page_config(page_title="My Roblox Links Dashboard", page_icon="🎮", layout="wide")
st.title("🎮 My Roblox Links Dashboard")

LINKS = [
    "https://www.roblox.com/games/126884695634066/Grow-a-Garden",
    "https://www.roblox.com/games/17625359962/RIVALS",
    "https://www.roblox.com/ko/games/6445435958/잼민이는-못깨는-타워",
    "https://www.roblox.com/games/15101393044/Dress-To-Impress",
    "https://www.roblox.com/games/116495829188952/Dead-Rails",
    "https://www.roblox.com/games/18130218021/Hell's-Kitchen",
    "https://www.roblox.com/games/6104994594/Pilfering-Pirates",
    "https://www.roblox.com/games/263761432/Horrific-Housing",
    "https://www.roblox.com/games/135619589726492/100-Players-Musical-Chairs",
    "https://www.roblox.com/games/166731267/The-Dropper", 
    "https://www.roblox.com/games/6737970321/Livetopia",
    "https://www.roblox.com/games/91036151820575/Be-a-Nurse",
    "https://www.roblox.com/games/1182833048/Growing-Up",
    "https://www.roblox.com/games/6902912928/GET-TO-THE-TOP",
    "https://www.roblox.com/games/82326514430239/Popmarket-Simulator",
    "https://www.roblox.com/games/16653555262/Rope-Swing-Obby",
    "https://www.roblox.com/games/893973440/Flee-the-Facility",
    "https://www.roblox.com/games/83704201064817/Dig-the-Backyard",
    "https://www.roblox.com/games/86089763581353/World-io"
]

def extract_name(url: str) -> str:
    """Extract game name from Roblox link"""
    try:
        path = urlparse(url).path.strip("/")
        parts = path.split("/")
        if len(parts) >= 3 and parts[0].lower() == "games":
            return parts[2].replace("-", " ")
        return parts[-1].replace("-", " ") if parts else url
    except Exception:
        return url

# Initialize slider values in session_state
for idx in range(len(LINKS)):
    key = f"rating_{idx}"
    if key not in st.session_state:
        st.session_state[key] = 3  # default rating

# Initialize filter in session_state
if "rating_filter" not in st.session_state:
    st.session_state.rating_filter = None

# Mode selector
mode = st.radio("Choose a style mode:", ["Light", "Color"], horizontal=True)

# Define colors and button styles
if mode == "Light":
    colors = ["#ffffff"] * len(LINKS)
    button_bg = "#4CAF50"
    button_text = "#ffffff"
else:
    colors = ["#FFDDC1", "#C1FFD7", "#C1E1FF", "#FFE5C1", "#E6C1FF", "#C1F0FF", "#FFD1DC",
              "#FFF4C1", "#C1FFE6", "#FEC1FF", "#C1FFF9", "#FFE1C1", "#D1FFC1"] * 2
    button_bg = "#ffffff"
    button_text = "#333333"

# --- Filter by Rating ---
selected_filter = st.radio("Filter by Rating", ["Show All", 1, 2, 3, 4, 5], horizontal=True)
st.session_state.rating_filter = None if selected_filter == "Show All" else selected_filter

# Determine which indexes to display
indexes_to_show = []
for idx in range(len(LINKS)):
    key = f"rating_{idx}"
    if st.session_state.rating_filter is None or st.session_state[key] == st.session_state.rating_filter:
        indexes_to_show.append(idx)

# --- Display Games ---
cols_per_row = 3
for i in range(0, len(indexes_to_show), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, idx in enumerate(indexes_to_show[i:i+cols_per_row]):
        col = cols[j]
        link = LINKS[idx]
        slider_key = f"rating_{idx}"
        name = extract_name(link)
        card_bg = colors[idx % len(colors)]
        text_color = "#333333"

        with col:
            # Game card
            st.markdown(
                f"""
                <div style="display:flex;flex-direction:column;
                            justify-content:center;align-items:center;
                            width:100%;height:200px;
                            background-color:{card_bg};
                            border:2px solid #ccc;
                            border-radius:12px;
                            box-shadow:2px 2px 6px rgba(0,0,0,0.1);">
                    <div style="font-size:16px;font-weight:bold;
                                color:{text_color};margin-bottom:8px;">
                        {name}
                    </div>
                    <a href="{link}" target="_blank"
                       style="padding:8px 16px;border-radius:8px;
                              background-color:{button_bg};
                              color:{button_text};
                              text-decoration:none;font-weight:bold;
                              transition:0.3s;">
                        Open Game
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Slider (no value=, just key)
            st.slider(
                label=f"Rate '{name}'",
                min_value=1,
                max_value=5,
                key=slider_key
            )
