def getLastStoryChunk(file_path) -> str:
  """
  Get the last story chunk from the README file.
  Args:
    file_path (str): The path to the README file
  Returns:
    str: The last story chunk from the README file
  """
  separator = '---'
  with open(file_path, 'r') as file:
    content = file.read()

  parts = content.split(separator)
  if len(parts) > 1:
    lines = parts[-1].strip().split('\n')
    return '\n'.join(lines[1:]).strip()
  else:
    return "No previous story found!"