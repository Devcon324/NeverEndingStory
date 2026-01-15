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

**Date Written:** 2026-01-15 16:01:58

As the sun rose over the rolling hills of the countryside, a worn wooden wagon creaked and groaned its way down the dirt road, carrying a group of peasants towards the town of Bluestone. Among them was Dave, a young and ambitious paladin, clad in simple leather armor and wielding a holy symbol of his order. His eyes, a piercing blue, shone with a sense of restlessness, for he had grown tired of the monotonous routine of his days at the monastery. The thrill of quests and exploration beckoned, and Dave had finally mustered the courage to leave the familiarity of his cloistered life behind. He sat alongside the other peasants, listening to their tales of woe and hardship, his mind wandering to the adventures that lay ahead. The wagon's driver, a grizzled old man named Thorne, cracked his whip, urging the oxen on as the town of Bluestone began to take shape on the horizon. "Not much longer now, folks," Thorne called out, his voice like a rusty gate, "we'll be arrivin' in Bluestone before nightfall."

As the wagon rumbled on, Dave struck up a conversation with a young half-elf woman named Eira, who sat across from him. Her dark hair was tied back in a ponytail, and her eyes sparkled with a mischievous glint. "What brings you to Bluestone, friend?" she asked, her voice husky and confident. Dave explained his desire to leave the monastery and seek out new experiences, and Eira nodded knowingly. "I'm bound for the same place," she said, "though my reasons are... different. I'm searching for a missing acquaintance, a fellow adventurer who went missing in these parts." Dave's interest was piqued, and he asked Eira to tell him more about her friend and their adventures together. As they talked, the wagon's other passengers began to stir, stretching their limbs and yawning, and Dave noticed a hooded figure sitting at the back of the wagon, who seemed to be listening in on their conversation with an air of intense interest.

The hooded figure, a tall and slender man with piercing green eyes, introduced himself as Arin, a traveling bard. He claimed to have been on the road for weeks, gathering tales and songs to share with the people of Bluestone. Arin's voice was smooth as silk, and his words dripped with a honeyed charm, but Dave sensed that there was more to the bard than met the eye. As the wagon approached the town's gates, the sound of hammering and sawing filled the air, and the smell of freshly baked bread wafted through the streets. The people of Bluestone were a hardy bunch, accustomed to living on the edge of the wilderness, and their town reflected their practical, no-nonsense approach to life. Thorne guided the wagon through the crowded streets, pointing out various landmarks and shops, and eventually came to a stop in front of the local tavern, the Blue Griffin Inn. "This is where we part ways, friends," Thorne said, climbing down from the driver's seat, "may the road rise up to meet ye, and may yer stay in Bluestone be a pleasant one."

As the peasants disembarked, Dave, Eira, and Arin exchanged nods and smiles, their conversation still unfinished. The paladin shouldered his pack, feeling a sense of excitement and trepidation as he stepped into the unknown. The Blue Griffin Inn loomed before them, its wooden sign creaking in the gentle breeze, and the sound of laughter and music spilled out into the street. Dave pushed open the door, his eyes adjusting to the warm, golden light within, and the patrons' faces turned to regard the newcomers. The air was thick with the smell of roasting meat and freshly brewed ale, and the paladin's stomach growled in anticipation. "Welcome to the Blue Griffin, travelers," the barkeep boomed, a stout dwarf with a bushy beard, "what can I get for ye on this fine evening?" And with that, Dave's adventure in Bluestone truly began, as he took his first steps into the unknown, surrounded by strangers who would soon become allies, friends, and perhaps even enemies, in the thrilling tales that were yet to unfold.
