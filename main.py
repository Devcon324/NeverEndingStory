import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from src.tools import startStory, writeNextStory

load_dotenv()

PATH_TO_README = "./README.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

if __name__ == '__main__':
  """
  Start the story by writing the first story chunk to the README file.
  Once the stroy has started a flag is created to prevent starting the story again.
  Then write the next story chunk to the README file.
  """
  if not os.path.exists("story_started.flag"):
      startStory(client, PATH_TO_README)
      with open("story_started.flag", "w") as f:
          f.write("Story started on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  writeNextStory(client, PATH_TO_README)
