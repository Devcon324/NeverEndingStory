from src.tools import firstWrite, nextWrite
from src.utils import writeToFile, getLastStoryChunk, debugOutput
from groq import Groq
from datetime import datetime

def generateStory(
    client: Groq = None,
    model: str = None,
    file_path: str = None,
    first_story: bool = False,
    prev_story: str = None
  ) -> None:
  story:  dict = firstWrite(client=client, model=model) if first_story else nextWrite(client=client, model=model, prev_story=prev_story)
  output: str  = story.choices[0].message.content
  date:   str  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  debugOutput(story=story, date=date)
  writeToFile(
    date=date,
    output=output,
    file_path=file_path
  )

def startStory(client: Groq, model: str, file_path: str = None) -> None:
  """
  Start the story by writing the first story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  """
  generateStory(client=client, model=model, first_story=True, file_path=file_path)

def writeNextStory(client: Groq, model: str, file_path: str = None) -> None:
  """
  Write the next story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  """
  last_story_chunk: str = getLastStoryChunk(file_path)
  if last_story_chunk:
      print("\nLast story chunk retrieved shown below:")
      print(last_story_chunk, "\n")
  else:
      print("No previous story chunk found. Writing DEFAULT prev. story chunk.")
      last_story_chunk: str = nextWrite(client=client, model=model).choices[0].message.content
      print(last_story_chunk, "\n")

  generateStory(client=client, model=model, file_path=file_path, first_story=False, prev_story=last_story_chunk)