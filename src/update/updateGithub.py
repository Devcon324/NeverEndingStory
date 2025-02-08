import os

def commitToGithub(file_to_commit: str, date: str) -> None:
  """
  Commit the changes to the README file to the GitHub repository.
  Args:
    date (str): The current date and time
  """
  story_flag = "./story_started.flag"
  if not file_to_commit:
      print("No file to commit.")
      return
  os.system("echo #####################################################################################")
  os.system("echo 'Checking git status...'")
  os.system("git status")
  os.system("echo #####################################################################################")
  os.system(f"echo 'Adding {file_to_commit} and {story_flag} to staging area...'")
  os.system(f"git add {file_to_commit} {story_flag}")
  os.system("echo #####################################################################################")
  os.system("echo 'Checking git status again...'")
  os.system("git status")
  os.system("echo #####################################################################################")
  os.system(f"echo 'Committing changes with message: Story update on {date}'")
  os.system(f'git commit -m "Story update on {date}"')
  os.system("echo #####################################################################################")
  os.system("echo 'Pushing changes to GitHub...'")
  os.system("git push")
  os.system("echo #####################################################################################")
