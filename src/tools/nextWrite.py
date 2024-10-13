from groq import Groq

def nextWrite(client: Groq, previousStory: str) -> dict:
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
        "content": previousStory,
      }
    ],
    model="llama3-70b-8192",
    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.5,

    # The maximum number of tokens to generate. Requests can use up to
    # 32,768 tokens shared between prompt and completion.
    max_tokens=8000,

    # Controls diversity via nucleus sampling: 0.5 means half of all
    # likelihood-weighted options are considered.
    top_p=1,
  )
  return next_story