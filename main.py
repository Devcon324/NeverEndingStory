import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
from src.tools import firstWrite, nextWrite
from src.utils import debugOutput, writeToFile, getLastStoryChunk

PATH_TO_README = "./README.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

def startStory(client: Groq) -> None:
  """
  Start the story by writing the first story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  """
  first_story:  dict = firstWrite(client)
  first_output: str  = first_story.choices[0].message.content
  first_date:   str  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(story=first_story, date=first_date)
  writeToFile(
    date=first_date,
    output=first_output,
    file_path=PATH_TO_README
  )

def writeNextStory(client: Groq) -> None:
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
  next_story:  dict = nextWrite(client, last_story_chunk)
  next_output: str  = next_story.choices[0].message.content
  next_date:   str  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
