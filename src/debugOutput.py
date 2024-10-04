def debugOutput(story, date):
  output            = story.choices[0].message.content
  prompt_tokens     = story.usage.prompt_tokens
  completion_tokens = story.usage.completion_tokens
  total_tokens      = story.usage.total_tokens
  current_datetime  = date
  print(output)
  print("\n################################################")
  print("#############     DEBUG LOGS      ##############")
  print("################################################")
  print("prompt_tokens    = ", prompt_tokens)
  print("output_tokens    = ", completion_tokens)
  print("total_tokens     = ", total_tokens)
  print("current_datetime = ", current_datetime)
  print("################################################\n")