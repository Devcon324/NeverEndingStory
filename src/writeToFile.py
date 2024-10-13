def writeToFile(date, output, file_path):
  try:
    print("writing to ", file_path)
    # Open the README.md file in append mode and add the output to the end
    with open(file_path, "a") as file:
      # Add double line breaks between each output part
      file.write("\n")
      # Add a separator and timestamp
      file.write(f"---\n\n**Date Written:** {date}\n\n")
      file.write(output)
      file.write("\n")
      # debug print
      print("Done writing to ", file_path)
  except Exception as e:
    print(f"An error occurred: {e}")