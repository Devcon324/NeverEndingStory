import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
from src.tools import startStory, writeNextStory

load_dotenv()

PATH_TO_README = "./README.md"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

def commitToGithub(file_to_commit: str, date: str) -> None:
  """
  Commit the changes to the README file to the GitHub repository.
  Args:
    date (str): The current date and time
  """
  if not file_to_commit:
      print("No file to commit.")
      return
  os.system("echo '#####################################################################################'")
  os.system("echo 'Checking git status...'")
  os.system("git status")
  os.system("echo '#####################################################################################'")
  os.system(f"echo 'Adding {file_to_commit} to staging area...'")
  os.system(f"git add {file_to_commit}")
  os.system("echo '#####################################################################################'")
  os.system("echo 'Checking git status again...'")
  os.system("git status")
  os.system("echo '#####################################################################################'")
  os.system(f"echo 'Committing changes with message: Story update on {date}'")
  os.system(f'git commit -m "Story update on {date}"')
  os.system("echo '#####################################################################################'")
  os.system("echo 'Pushing changes to GitHub...'")
  os.system("git push")
  os.system("echo '#####################################################################################'")

if __name__ == '__main__':
  """
  Start the story by writing the first story chunk to the README file.
  Once the stroy has started a flag is created to prevent starting the story again.
  Then write the next story chunk to the README file.
  """
  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  if not os.path.exists("story_started.flag"):
      startStory(client, PATH_TO_README)
      with open("story_started.flag", "w") as f:
          f.write("Story started on: " + date)
  writeNextStory(client, PATH_TO_README)
  commitToGithub(PATH_TO_README, date)
  # sudo crontab -e
  # 59 23 * * * cd /mnt/d/GitHub/The-NeverEnding-Story ; /usr/bin/env /usr/bin/python3 /mnt/d/GitHub/The-NeverEnding-Story/main.py