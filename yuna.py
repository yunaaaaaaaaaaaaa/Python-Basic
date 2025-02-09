# To run, copy and paste the code below.
# streamlit run yuna.py --server.port 8080 --server.address 0.0.0.0

# streamlit official doc link:
# https://docs.streamlit.io/
import streamlit as st

st.title("The Code Breaker's adventure :sunglasses:")
import streamlit as st

story = """
Once upon a time in a small town, there were six best friends who loved coding. Their after-school club, "The Code Breakers," met every Friday in the coding academy's computer lab. They were taught by The Evil Coding Teacher, a strict but brilliant instructor with a mysterious past.

One day, something strange happened. When the five girls—Yuna, Eugenia, Tara, Eiley, and Alice—arrived at the lab, their sixth member, Elena, was missing. The Evil Coding Teacher stood at the front of the room with a sly grin.

"Elena has moved on to a special assignment," he said cryptically, his fingers tapping against the desk. "You all should focus on your own work."

But the girls knew something was wrong. Elena would never miss a club meeting, and she had been acting nervous the last time they saw her. Yuna noticed Elena’s laptop still on the desk, its screen flashing with lines of strange code.

Determined to find their friend, the girls decided to investigate. They stayed after class, hacking into the academy’s security footage. What they saw sent chills down their spines—The Evil Coding Teacher leading Elena into a hidden door behind the bookshelves.

"We have to save her!" Eugenia whispered.

They followed the clues hidden in Elena’s unfinished code, which led them to an underground lair beneath the academy. The lair was filled with glowing monitors and mechanical arms building something huge—a cybernetic machine. And there, trapped inside a glass chamber, was Elena!

"You shouldn’t be here," The Evil Coding Teacher’s voice boomed as he stepped out of the shadows. "You girls are talented, but you don’t understand real power. Elena does—she’s going to help me create the ultimate AI!"

"Not if we stop you first!" Tara shouted.

Using their coding skills, the girls worked together to override the system. Eiley distracted the security bots while Alice rewrote the door’s access code. Yuna and Eugenia cracked the encryption on Elena’s chamber. Tara typed furiously, inserting a virus into The Evil Coding Teacher’s control system.

Alarms blared as the AI system malfunctioned. Sparks flew, and the chamber unlocked! Elena gasped as she stumbled forward.

"You did it!"

Furious, The Evil Coding Teacher tried to stop them, but Eiley pressed the final key, shutting down the lair’s power. The girls grabbed Elena and ran as the lab collapsed behind them.

The next day, The Evil Coding Teacher had disappeared, leaving behind nothing but a corrupted hard drive. The girls never saw him again, but they knew one thing for sure: The Code Breakers were unstoppable.

And no teacher, no matter how evil, could ever break their bond.
"""

st.write(story)


name = st.text_input("Enter your name")
st.write(name)