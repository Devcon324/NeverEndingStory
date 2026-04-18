import os
from groq import Groq, RateLimitError
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

PATH_TO_STORY = settings.get("path-to-story") or settings.get(
  "path-to-readme", "./STORY.md"
)
MODEL = settings['model']

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

if __name__ == '__main__':
  """
  Start the story by writing the first story chunk to STORY.md.
  Once the story has started a flag is created to prevent starting the story again.
  Then write the next story chunk to STORY.md.
  """
  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("date.yaml", "a") as f:
    f.write(f"commit-date: {date}\n")
  commitToGithub(file_to_commit='date.yaml', date=date)

  try:
    if not os.path.exists("story_started.flag"):
        startStory(client=client, model=MODEL, file_path=PATH_TO_STORY)
        with open("story_started.flag", "w") as f:
            f.write("Story started on: " + date)
    else:
        writeNextStory(client=client, model=MODEL, file_path=PATH_TO_STORY)

    # Commit story changes to the GitHub repository.
    # sudo crontab -e
    commitToGithub(file_to_commit=PATH_TO_STORY, date=date)
  except RateLimitError as e:
    print()
    print("Groq rate limit or quota reached (for example tokens-per-day).")
    print(f"Message: {e.message}")
    print(
      "This run only updated and pushed date.yaml; STORY.md was not changed."
    )
    print()
