# The NeverEnding Story

## What is this?

We follow **Dave**, our Programmed Paladin on his adventure!

This is an **self-continuing** story that is **automatically updated 3x a day to this GitHub repository.**
**Enjoy you morning coffee and read where dave is at!** The story is updated at **12:00 AM, 8:00 AM, 4:00 PM Eastern Standard Time**

### [Click Here to Read Dave's Story Below](#the-story-of-dave-the-programmed-paladin)

Built with **Generative Artificial Intelligence** using **Meta's llama3.1 70b Large Language Model**. This project accomplishes these steps:

1. Start a story with an initial story chunk (some paragraphs).
2. Continue writing the next story chunk using the previous story chunk as context.
3. Write the stories to this README.md file with dated entries.
4. Automate the git commands to commit and push to this repository.
5. Cronjob the script to run 24x a day

### Features I found cool when building

#### Groq API

**Using [Groq](https://groq.com/) for LLM's is intuitive and easy.** the syntax and responses received from the model are easily understood and can allow for great debugging. Groq was also chosen over [OpenAI's GPT models](https://openai.com/api/) because Groq is **free** and has **fast-inference's** meaning the story generation is extremely fast.

The fact this model is free (hopefully for a long time) allows for the great learning and exploration of using LLM's to make projects like this that **experiment with how models behave when in a continuous conversation and creating content akin to a writing style and theme.**

As Groq introduces newer models, perhaps the story may become more fluid over time.

#### Algorithms

I had to really design and think about how the story generation will be organized so that the LLM can parse the recent stories. I knew i needed to separate eah story so i separated them by the markdown line `---\n`

In my learning i optimized retrieving the latest story. This was done by sending a pointer to the end of file and use a reading window (buffer) that will expand its memory only when the story separator is not within the window. Once found, the most recent story chunk is retrieved and cleaned to hold the story text to give the LLM context for the next story.

#### Python Packaging

I learned how to properly use `__init__.py` and create sub-packages within the project such as `utils`, `tools`, and `update`

#### Automated git commits and push to GitHub

One very interesting feature i learned is that i can use system calls to send git commands such as `git add`, `git commit`, and `git push origin master`. This proved useful to keep updating the repository as the script runs without human input (apart form setting up SSH keys for secure connections)

The other feature is that cronjobs on Linux are very useful to run the script as a background process, simply requiring a workstation to be online. This can be done by editing the cronjob file with the following command:

```bash
crontab -e
```

**Note:** the cronjobs need to be in the following format (with script running every day at time 16:00)

```bash
00 16 * * * cd /path/to/repository ; source path/to/venv/bin/activate ; path/to/venv/bin/python3 /path/to/repository/main.py
```

This cronjob essentially runs the command to cd to the repository, spin up the python virtual environment, then use that virtual environments python version to execute the main script.

## Now enough of the technical stuff... Lets see how Dave is doing

## The Story of Dave the Programmed Paladin

---

---

**Date Written:** 2024-10-29 18:34:59

As the sun dipped below the horizon, casting a warm orange glow over the bustling town of Willowdale, the air grew thick with the smell of smoke and roasting meats. Travelers and locals alike made their way to the town square, where the sound of laughter and music filled the air. At the center of the square stood the ancient wooden sign of the Golden Griffin Inn, creaking in the gentle breeze. The inn's warm lights spilled out into the square, beckoning weary travelers to come and rest by the fire.

To the north of the town square, the rolling hills and verdant forests of the Whispering Woods beckoned to those seeking adventure and mystery. Tales of ancient magic and long-lost civilizations whispered through the trees, drawing seekers of fortune and knowledge to the woods' dark depths. Rumors swirled of strange occurrences and eerie apparitions, forcing even the bravest of souls to think twice before venturing into the woods' clutches. And yet, a faint sense of promise hovered over the trees like a ghostly moon, drawing dreamers and explorers into its depths, like moths to a flickering flame.

Within the Golden Griffin's walls, a fire crackled and spat in the hearth, warming the faces of travelers clustered around the bar. A weathered half-elf named Ryker, clad in worn leather armor, sipped a mug of ale, listening intently as the local townsfolk shared tales of the Whispering Woods' secrets. Nearby, a trio of dwarves clinked tankards together, their thick beards woven with tiny bones and glittering gemstones that seemed to wink in the firelight. A young woman named Lilith, dressed in worn velvet and her fingers stained with the ink of a scholar, pored over dusty tomes in the corner, chasing the whispered promise of a lost library hidden within the woods' labyrinthine depths.
