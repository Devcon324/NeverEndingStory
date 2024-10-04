def firstWrite(client):
  first_story = client.chat.completions.create(
    messages=[
      # Set an optional system message. This sets the behavior of the
      # assistant and can be used to provide specific instructions for
      # how it should behave throughout the conversation.
      {
        "role": "system",
        "content": "you are a an experienced creative storyteller and writer. Write in paragraphs like a novel. the output should be written like a novel with completed sentences at the end."
      },
      {
        "role": "user",
        "content": """
          Write a story about Dave the Paladin. All content of this story is to be drawn from the fantasy world of dungeons and dragons. The setting is the world of Faerul.
          Dave begins his journey onboard a wagon with some other peasants going to the town of Bluestone to begin his adventure. Dave has become bored of his days spent at the monastery and seeks the thrill of adventure and quests.
          Tou will write an ongoing unending story of Dave. You can create new characters, you can write dialogues, and you can write about Dave going on quests.
          This story will never end and will keep going forever.
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