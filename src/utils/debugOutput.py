def debugOutput(story: str, date: str) -> None:
  output: str            = story.choices[0].message.content
  prompt_tokens: int     = story.usage.prompt_tokens
  completion_tokens: int = story.usage.completion_tokens
  total_tokens: int      = story.usage.total_tokens
  current_datetime: str  = date

  print("\n################################################")
  print("#############   Generated story   ##############")
  print("################################################")
  print(output)
  print("\n################################################")
  print("#############     DEBUG LOGS      ##############")
  print("################################################")
  print("prompt_tokens    = ", prompt_tokens)
  print("output_tokens    = ", completion_tokens)
  print("total_tokens     = ", total_tokens)
  print("current_datetime = ", current_datetime)
  print("################################################\n")