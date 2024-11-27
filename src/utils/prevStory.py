import src.tools.nextWrite as nextWrite

def getLastStoryChunk(file_path: str) -> str | None:
  """
  Reads file from EOF and gets most recent story separated by '---'
  Optimized to read from the end of the file to the last separator
  Args:
    file_path (str): The path to the README file
  Returns:
    str: The last story chunk from the README file
  """
  try:
    separator = '---\n'
    with open(file_path, 'r', encoding='utf-8') as file:
      file.seek(0, 2)  # move pointer to the end of the file
      chars_left_to_read = file.tell()  # get the full size of file
      buffer_size = 1024  # a reading window that will grow if needed

      buffer = '' # this will be the reading window
      while chars_left_to_read > 0:
        # choose the reading window size, prevents reading the whole file
        read_size = min(buffer_size, chars_left_to_read)
        # send pinter to the left of the reading window
        file.seek(chars_left_to_read - read_size)
        # read the window and store it in buffer
        next_read = file.read(read_size)
        buffer = next_read + buffer
        # update the remaining characters to read
        chars_left_to_read -= read_size

        if separator in buffer:
          print('separator found in buffer')
          break
  except Exception as e:
    print(f"Error: {e}")
    return None

  # now we have the last story chunk containing one or more separators
  last_story_chunk = ''
  parts = buffer.split(separator) # list of all stories in buffer separated by '---'
  if len(parts) > 1:
    lines = parts[-1].strip().split('\n') # list of lines from the last story chunk
    last_story_chunk = '\n'.join(lines[1:]).strip() # join the lines not including date on line 0
    return last_story_chunk

  else:
    print("No previous story chunk found.")
    return None