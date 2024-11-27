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

**Date Written:** 2024-11-26 19:42:32

The sun was just starting to peek over the horizon as the creaky wooden wagon rattled down the dirt road, carrying a handful of weary peasants to the bustling town of Bluestone. Among them was Dave, a young Paladin from the Order of the Radiant Dawn, who had left the seclusion of his monastery in search of adventure and excitement. With his gleaming silver armor and radiant aura, he stood out starkly amongst the worn-out travelers. The wagon's other occupants eyed him with a mix of curiosity and suspicion, whispering amongst themselves about the sight of the divine warrior traveling with common folk.

As the morning wore on, the wagon journeyed deeper into the heart of the Sword Coast, passing rolling fields of wheat and gold, dotted with tiny villages and bustling markets. The sweet scent of fresh bread and roasting meats wafted from cooking fires, enticing the travelers with the promise of a warm meal at the day's end. As the riders rode on, Dave conversed with his fellow travelers, listening intently to their stories of hardship and woe, his eyes filled with compassion and kindness. There was the shy peasant girl named Elara, who sought to reunite with her estranged brother in Bluestone; Thomas, the burly blacksmith, who was shipping goods to set up a new forge in town; and Helmut, an eccentric merchant who spoke excitedly of exotic goods from far-off lands.

"So, young Paladin, what brings you to our humble town?" Thomas asked, eyeing Dave's shining armor in awe. "Aren't you a bit...exotic for the monastery?" Dave chuckled, running a hand through his short blond hair, "I craved adventure and guidance, something more than devoting my days to chanting hymns and polishing silverware. I'm here to aid those in need, offer my sword arm to the town of Bluestone, and bring the light of justice to the world beyond." Elara smiled warmly, though Helmut merely raised an eyebrow at the Paladin's grand ambitions. "Well, friend, you've come to the right place," the merchant replied. "Bluestone is filled with more problems than there are nails in these creaky floorboards."

As the conversation flowed on, the group began to discuss prospects of Bluestone, sharing tales of tavern brawls, local feuds, and mythical rumors of the Lizardfolk that were said to raid caravans from the nearby Mirkwood Forest. As the wagon wheels rolled along the bumpy road, a chill wind swept through the landscape, carrying the acrid stench of smoke and burning wood. Dave sat higher in his seat, an uncanny urge growing in his chest as the signs of dark magic began to accumulate on the horizon. A faint tendril of chaos shrouded the town ahead, urging Dave, ever the noble Paladin, to spring forth into action.

As the town of Bluestone finally materialized before the wagon's wheels, Dave felt his senses on high alert. Tall timbers for large town gates came into view, overhung with glinting metal accents crafted in a wild array of patterns. Large torches kindled both sides of these gates that guarded the gate entrance into the town of Bluestone. A faded grandeur touched by a dash of dark terror to mark signs of smoldering strife painted all features of what once was, centuries ago; great, proud and resplendent, Bluestone.

---

**Date Written:** 2024-11-26 19:53:16

As the wooden wagon creaked to a halt before the imposing gates of Bluestone, the travelers' hushed conversations turned to murmurs of concern and trepidation. A thick layer of grime coated the once-majestic gate, and the metal accents that danced across its surface now gleamed with a faint, malevolent light. The large torches that flanked the entrance cast flickering shadows on the walls, imbuing the air with an eerie sense of foreboding. The very atmosphere within Bluestone seemed to writhe and twist, like a living entity suffering beneath the weight of some ancient evil.

As Dave descended from the wagon, his eyes scanned the surrounding area, taking in the huddled clusters of villagers, the blackened ruins of buildings, and the ash-stained cobbles. The once-proud town square now resembled a war-torn battleground, with the thatched roofs of nearby homes patched and torn. Amidst this landscape of desolation, a lone figure stood sentinel – a burly town guard, dressed in worn armor, with a heavy hand resting on the hilt of his sword. He eyed the wagon's passengers warily, his expression a blend of suspicion and curiosity.

"What business do you have in Bluestone?" the guard growled, his voice like gravel beneath the wagon's wheels. Elara, the shy peasant girl, timidly stepped forward, introducing herself and her traveling companions. As the guard's gaze settled upon Dave, his expression softened ever so slightly – a fleeting hint of hope within the depths of his weathered face. "A Paladin, you say?" he muttered, his eyes narrowing as he studied Dave's gleaming armor. "We could use someone with your...particular set of skills. There's been trouble in the area, and I reckon you might be just the sort of folk we need."

The guard's words hung in the air, as if an unspoken challenge awaited Dave's response. Thomas, the burly blacksmith, took this opportunity to grab his wooden chest and request permission to proceed to the local market, while Helmut, the eccentric merchant, began to barter with one of the local traders, exchanging exotic tales for coin. Elara, sensing an undercurrent of tension, kept a guarded distance, her eyes darting between Dave and the town guard.

Dave, however, sensed that something was amiss – that beneath the surface of Bluestone's crumbling façade lay a web of secrets, ancient grudges, and untold dangers. His heart swelled with determination as he took a deep breath, the air heavy with the promise of adventure and the weight of duty. The path ahead was shrouded in uncertainty, but one thing was clear: the time for Dave, the young Paladin, to make his mark on the world had finally arrived.
