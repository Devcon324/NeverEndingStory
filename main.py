import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
import time
load_dotenv()
from src.firstWrite import firstWrite
from src.nextWrite import nextWrite
from src.prevStory import getLastStoryChunk
from src.writeToFile import writeToFile
from src.debugOutput import debugOutput

PATH_TO_README = "./README.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

def startStory(client):
  """
  Start the story by writing the first story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  """
  first_story  = firstWrite(client)
  first_output = first_story.choices[0].message.content
  first_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(first_story, first_date)
  writeToFile(
    date=first_date,
    output=first_output,
    file_path=PATH_TO_README
  )

def writeNextStory(client):
  """
  Write the next story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  """
  last_story_chunk = getLastStoryChunk(PATH_TO_README)
  if last_story_chunk:
      print("\nLast story chunk retrieved shown below:")
      print(last_story_chunk, "\n")
  else:
      print("No previous story chunk found.")
  next_story  = nextWrite(client, last_story_chunk)
  next_output = next_story.choices[0].message.content
  next_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(next_story, next_date)
  writeToFile(
    date=next_date,
    output=next_output,
    file_path=PATH_TO_README
  )

if __name__ == '__main__':
  if not os.path.exists("story_started.flag"):
      startStory(client)
      with open("story_started.flag", "w") as f:
          f.write("Story started on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  writeNextStory(client)
