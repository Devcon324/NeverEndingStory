import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from src.tools import startStory, writeNextStory
from src.update import commitToGithub
import yaml

load_dotenv()
with open("settings.yaml", 'r') as file:
  try:
    settings = yaml.safe_load(file)
  except yaml.YAMLError as exc:
    print(exc)

PATH_TO_README = settings['path-to-readme']
MODEL = settings['model']

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

if __name__ == '__main__':
  """
  Start the story by writing the first story chunk to the README file.
  Once the stroy has started a flag is created to prevent starting the story again.
  Then write the next story chunk to the README file.
  """
  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("date.yaml", "a") as f:
    f.write(f"commit-date: {date}\n")
  commitToGithub(file_to_commit='date.yaml', date=date)

  if not os.path.exists("story_started.flag"):
      startStory(client=client, model=MODEL, file_path=PATH_TO_README)
      with open("story_started.flag", "w") as f:
          f.write("Story started on: " + date)
  else:
    writeNextStory(client=client, model=MODEL, file_path=PATH_TO_README)

  # Commit the changes to the README file to the GitHub repository.
  # sudo crontab -e
  commitToGithub(file_to_commit=PATH_TO_README, date=date)
