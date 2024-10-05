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

PATH_TO_README = "./test.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

def startStory(client):
  first_story  = firstWrite(client)
  first_output = first_story.choices[0].message.content
  first_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(first_story, first_date)
  writeToFile(first_output, first_date, PATH_TO_README)

def writeNextStory(client):
  last_story_chunk = getLastStoryChunk(PATH_TO_README)
  if last_story_chunk:
      print("\nLast story chunk retrieved:")
      print(last_story_chunk, "\n")
  else:
      print("No previous story chunk found.")
  next_story  = nextWrite(client, last_story_chunk)
  next_output = next_story.choices[0].message.content
  next_date   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(next_story, next_date)
  writeToFile(next_output, next_date, PATH_TO_README)

startStory(client)
writeNextStory(client)
