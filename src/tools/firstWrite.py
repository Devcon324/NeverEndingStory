from groq import Groq

def firstWrite(client: Groq) -> dict:
  """
  Write the first story chunk to the README file.
  Args:
    client (Groq): The Groq client object
  Returns:
    dict: The response from the Groq API
  """
  first_story = client.chat.completions.create(
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
        "content": """
          Write an epic and ongoing story about Dave the Paladin, set in the fantasy world of Dungeons and Dragons, specifically in the world of Faerûn. Dave begins his journey onboard a wagon with other peasants heading to the town of Bluestone to start his adventure. Bored of his days at the monastery, Dave seeks the thrill of quests and exploration.
          You will write an unending story of Dave, introducing new characters, crafting dialogues, and detailing his quests and adventures. The story should be continuous and never-ending, filled with rich lore, unexpected twists, and engaging narratives.
        """,
      }
    ],
    model="llama3-70b-8192",
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
  return first_story