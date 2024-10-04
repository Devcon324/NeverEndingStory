def writeToFile(output, date, file_path):
  print("writing to ", file_path)
  # Open the README.md file in append mode and add the output to the end
  with open(file_path, "a") as file:
    file.write("\n")  # Add double line breaks between each output part
    file.write(f"---\n**Date Written:** {date}\n\n")  # Add a separator and timestamp
    file.write(output)
    file.write("\n")  # Add double line breaks between each output part