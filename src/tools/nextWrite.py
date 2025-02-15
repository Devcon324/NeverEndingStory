from groq import Groq

DEFAULT: str = "You are a brave adventurer who has been tasked with retrieving a powerful artifact from a dangerous dungeon. You have been traveling for days and have finally arrived at the entrance of the dungeon. The entrance is dark and foreboding, but you know that the artifact lies deep within. You take a deep breath and step inside, ready to face whatever challenges lie ahead."

def nextWrite(client: Groq, model: str, prev_story: str = DEFAULT) -> dict:
  """
  Write the next story chunk to the README file.
  Args:
    client (Groq): The Groq client object
    previousStory (str): The previous story chunk
  Returns:
    dict: The response from the Groq API
  """
  next_story = client.chat.completions.create(
    messages=[
      # Set an optional system message. This sets the behavior of the
      # assistant and can be used to provide specific instructions for
      # how it should behave throughout the conversation.
      {
        "role": "system",
        "content": "You are an experienced Dungeon Master and creative storyteller. Write in paragraphs like a novel, with completed sentences at the end. Your storytelling should be immersive, engaging, and rich with details, akin to a Dungeons and Dragons campaign."
      },
      {
        "role": "user",
        "content": prev_story,
      }
    ],
    model=model,
    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=1.0,

    # The maximum number of tokens to generate. Requests can use up to
    # 32,768 tokens shared between prompt and completion.
    max_tokens=8000,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,
  )
  return next_story