def getLastStoryChunk(file_path):
  # Read the entire file content
  with open(file_path, 'r') as file:
      content = file.readlines()

  # Reverse the content list to search from the end
  content.reverse()

  last_chunk = []
  date_marker_found = False

  # Search for the last occurrence of the date marker
  for line in content:
      if line.startswith("**Date Written:**"):
          if date_marker_found:
              # We found the previous date, break and reverse the chunk back
              break
          else:
              # The first occurrence of the date marker from the end
              date_marker_found = True
      elif date_marker_found:
          # Collect lines for the last story chunk
          last_chunk.append(line)

  if last_chunk:
      # Since we reversed the lines, reverse them back to the original order
      last_chunk = ''.join(reversed(last_chunk)).strip()
      # Remove trailing "---" if present
      if last_chunk.endswith("---"):
          last_chunk = last_chunk[:-3].strip()
      return last_chunk
  else:
      return None  # No story chunk found