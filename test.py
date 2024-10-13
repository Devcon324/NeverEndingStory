def read_last_chunk_after_separator(file_path):
  separator = '---'
  with open(file_path, 'r') as file:
    content = file.read()

  parts = content.split(separator)
  if len(parts) > 1:
    lines = parts[-1].strip().split('\n')
    return '\n'.join(lines[1:]).strip()
  else:
    return ""

# Example usage
if __name__ == "__main__":
  print('Running test...')
  file_path = 'testw.md'
  last_chunk = read_last_chunk_after_separator(file_path)
  print(last_chunk)