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

**Date Written:** 2024-11-26 19:54:19

The sun was setting over the rolling hills of the countryside, casting a warm orange glow over the bustling wagon train. Dave, a young and ambitious paladin, sat perched on the edge of a wooden wagon, his eyes fixed on the horizon as the wheels creaked and groaned beneath him. He wore a suit of battered leather armor and carried a sturdy warhammer across his knees, his hands drumming a rhythmic beat on the handle as he bounced along the rough terrain.

To his left sat Elara, a young half-elf with a mischievous glint in her eye, her hair tied back in a loose braid and her fingers deftly weaving a wooden flute from a length of tender ash. She played a lively tune, the notes skipping and dancing like a leaf on a breeze as the wagon bounced along. To Dave's right sat Old Tom, a grizzled veteran of countless battles, his face etched with scars and his eyes squinting into the sunlight as he sharpened a worn blade with a whetstone.

"Bluestone's just ahead, lads and lasses," Old Tom declared, his voice like worn leather, "and I reckon we'll be lucky to make it in one piece. Roads ain't what they used to be, and I've heard tell of bandits and orcs on the prowl." Elara's flute playing faltered for a moment, her eyes darting nervously towards the paladin, before she shifted back into her lively tune. Dave, meanwhile, simply smiled and nodded, his hand resting on the pommel of his warhammer.

The wagon train crested a small hill, and as they descended into the valley below, the town of Bluestone came into view. Nestled in the heart of a deep valley, surrounded by towering mountains that seemed to lean in on it, the town was a patchwork of brightly colored buildings and chaotic streets. Smoke curled up from the town's many chimneys, mingling with the sweet scent of baking bread and the stench of butchered meat.

As the wagon train approached the town's main gate, a pair of sturdy guards eyed the travelers warily, their hands resting on the hafts of their spears. One of the guards, a burly man with a thick beard and a scar above his eyebrow, hopped down from the gatehouse and strode towards the wagon. "Halt, travelers! Who are you, and what business do you have in Bluestone?" he boomed, eyeing Dave's warhammer and Elara's flute with a mixture of curiosity and suspicion.

Old Tom stood up, his eyes squinting as he stretched his back, and bowed low to the guard. "Ah, good fellow, we're just a group of humble travelers seeking to earn a buck in your fair town. This young fellow here's a paladin, from the monastery in the north – he's here to take on some local quests, and perhaps bring a bit of justice to the area." The guard's eyes flickered to Dave, his expression softening ever so slightly as he took in the paladin's chiseled features and gleaming armor. "Ah, well, in that case, you're welcome in Bluestone. Just be careful, travelers – there's been rumors of strange happenings out in the valley. Tools gone missing, strange noises at night, and that kind of thing. Can't quite put our finger on it, but we've had to increase the night watch just in case."

As the guard finished speaking, Elara's flute playing grew softer, her eyes darting up at Dave with a curious glint. "Sounds like there's a bit of work to be done, then," she whispered, her voice barely audible over the rattling wagon. Dave smiled, a fierce light igniting in his eyes as he nodded in agreement. The gods, it seemed, were already guiding his path – and the adventure was only just beginning.

---

**Date Written:** 2024-11-26 19:55:00

As the wagon train rumbled through the gates of Bluestone, the warm scent of baking bread and the soft murmur of the townspeople filled the air, enveloping the travelers in a sense of welcome and possibility. The paladin, Dave, smiled as he nodded to the guard, his eyes taking in the vibrant market scene unfolding before him, the stalls selling everything from glittering gemstones to handwoven woolens. The town itself was a tiny sanctuary, nestled deep within the heart of the valley, shielded by the towering mountains that seemed to hold their breath in eager anticipation.

As they made their way deeper into the town, Elara slid the wooden flute back into its makeshift leather case, her eyes never leaving Dave's determined expression. Old Tom, ever the seasoned traveler, took the reins of their wagon, guiding the weary animals towards the nearby livery stable. The wagons halted before a sturdy wooden sign that announced, in bold, golden letters: The Steaming Vat Inn. "Looks like Old Tom's taste for a fine pint is finally going to be satisfied," Elara whispered with a sly grin, pointing towards the steaming copper vat that bubbled and spewed foam from its central keg.

With Old Tom leading the way, they entered the warm confines of the Steaming Vat Inn, where music and laughter spilled into the air like colorful ribbons. Stepping inside, the aromas of beer and roast meat mingled on their senses, making their stomachs rumble in anticipation of the coming feast. Patrons' faces, bearing scars and weathered features alike, looked up to inspect the travelers, their voices raising above the din in murmurs of conversation, stories and debates swirling about them.

Dave navigated the packed room with a familiar smile, his armor – worn from miles of travel and countless tests – catching curious glances as he strode purposefully through the room. Old Tom sought out a soft stool at the wooden counter, commanding the attention of a rugged barmaid as he ordered a round of ale for the trio. She raised an eyebrow as Elara selected a stringed lute resting against the inn's wall, launching into a haunting melody that flowed through the air like honey.

As the sounds rose around them, the crowd itself began to stir, patrons taking to the hall's central dance floor to laugh, spin, and leap into reckless partnerships, joy infectious and free. An open spot was cleared for the weary paladin to join in the fray, the atmosphere radiating raw camaraderie, pulsing and breathing with the easy spirit that only communal laughter could foster.

One traveler in particular, standing near the keg-lit corner, caught Dave's notice – a grizzled hunter sporting scratched animal hide and holding a bent wooden bow, peering in hushed tones with the barmaid. Eyes meeting, a silent exchange blossomed as the pair raised tankards together – drinking a silent toast to the town's peace and quiet respite from yet unknown challenges, looming ahead – still shrouded in darkness and veiled uncertainty, the mysteries silently flowing through smoke-veiled streets, entwining under the radiant twilight of Bluestone.

---

**Date Written:** 2024-11-26 19:56:52

As the night's merriment danced around them, the grizzled hunter approached Dave with a cautious air, as if sizing him up. His eyes, a piercing brown that seemed to hold the wisdom of the wilderness, assessed the paladin's worn armor and the determination etched on his face. The hunter's hair, flecked with threads of silver, fell to his shoulders like a wild mane, and the scratches on his cheek told the tale of a lifetime spent traversing the untamed lands.

"You're not from around here, traveler," the hunter said in a low, gravelly voice, his words laced with a hint of curiosity. "What brings you to Bluestone, and what is it that weighs so heavily on your mind?" The paladin hesitated for a moment, considering the depth of the hunter's words. Something about the man's earthy scent and the quiet wisdom in his eyes put Dave at ease. He reached for the ale-stained wooden mug set before him and took a slow, measured sip, allowing the ale to wash down the fatigue of the journey.

"The road has been long, and the nights cold," Dave replied, his voice carrying the weight of the world. "We've been searching for a way to vanquish the shadows that loom beyond the valley. Tales speak of an ancient evil that stirs in the heart of the mountains, and we seek to know the truth behind it." The hunter's eyes narrowed, his fingers tightening around the tankard in his hand. For a moment, the din of the inn seemed to recede, and the paladin felt the weight of the hunter's attention.

"I've lived these mountains all my life," the hunter said finally, his words measured. "I know their secrets, and the stories they whisper in the darkness. There is indeed a presence stirring in the depths of the mountains – an ancient power that only the brave and the foolhardy dare to confront." He glanced around the room, ensuring they were not overheard. "Meet me outside, by the old windmill on the outskirts of town, if you wish to hear the truth behind the whispers." The words hung in the air like a promise of adventure and danger, waiting to be seized by those brave enough to face the unknown.

Old Tom, sensing the air of intrigue, sidled up to the pair, a discerning glint in his eye. Elara, still playing the lute, seemed to sense the subtle shift in the atmosphere, her fingers subtly changing the melody's tempo. As the music whispered and swirled around them, the paladin felt the threads of fate weaving together in a pattern both familiar and unknown – beckoning them deeper into the heart of the valley and toward the shadows that loomed beyond.

---

**Date Written:** 2024-11-26 20:01:08

As the hunter's words faded away, the warmth of the inn and the murmur of hushed conversations seemed to close in once more, like a softly falling curtain. Dave felt a strange sense of resolve taking root within him, as if the journey that had brought him to Bluestone had merely been a series of steps leading him to this precise moment. He set his mug down, the ale within remaining untouched, and his eyes met the hunter's once more. In that fleeting glance, a silent understanding was forged, a spark of courage and determination kindling between them like a beacon in the darkness.

Old Tom, sensing the tense energy emanating from the pair, nodded discreetly and withdrew into the crowd, his knowing eyes disappearing behind a haze of pipe smoke and raucous laughter. The music, still thrumming through the air, seemed to subtly shift, as if Elara too had sensed the whisper of secrets being shared. Her melody grew more brooding, the lute's notes wailing like the mournful cries of distant wolves, while the shadows cast by the fire danced and capered around them, as if alive.

Beyond the inn, the windmill loomed like a sentinel, its once-sturdy sails fallen and broken, its wooden frame worn and weary. Yet, in the flickering moonlight, it seemed to take on a new significance – an ancient guardian standing watch over the valley, its worn facade whispering secrets on the wind. As Dave rose from his seat, his armor creaking softly in the sudden silence, the paladin knew that this forsaken windmill was to be the threshold of their next step into the unknown.

The tavernkeeper, ever attentive to the needs of his patrons, sidled over to refill the paladin's mug, his bushy eyebrows furrowed with concern. "You be careful, traveler," he warned in a low tone, "the mountains don't take kindly to strangers. Dark rumors abound about the thing stirring in those peaks – talk of beasts born of shadow and blood, and terrible rituals that conjure unspeakable horrors." His eyes widened ever so slightly. "Be wary of the old hunter too. He's lived those mountains for nigh on three decades, but there's stories about him, how he's been... altered by the very lands he claims to know so well."

Dave smiled, the weight of unknown dangers pressing down upon him, but his eyes remained steadfast, illuminated by the fire's golden light. He took the refilled mug in hand, the ale within its depths a symbol of brief comfort, a fleeting comfort in the darkness ahead. His gaze lingered for a moment on Elara, who raised an eyebrow in a soft gesture of understanding. "Until the windmill," he said, his voice almost lost in the din, but not quite, as if whispers of fate still lingered on his lips.

---

**Date Written:** 2024-11-26 20:07:07

The windmill's silhouette cut an imposing figure against the silver-illuminated sky, its weathered boards etched like a gaunt face bereft of warmth. As Dave stepped outside into the crisp night air, the cooler breeze rustled his hair and invigorated his senses, carrying with it whispers of the mountain's arcane whispers. Elara emerged beside him, the soft lilt of her voice mingling with the gentle swaying of her hair as the lute was slung over her shoulder, her fingers strumming soft silences as if tuning herself to the evening's stillness.

Beyond the windmill's crumbling facade, the shadows bled into a gloom-filled ravine, like Nature's very maw waiting to swallow the unwary traveler. Thin wisps of mist dissipated and reformed as the paladin passed, as though spirit fingers were grasping to retouch the world of the living. With Old Tom stepping from the tavern's doorway, the age-worn wooden bracing that girdled the windmill seemed almost to straighten as he gave Dave a solemn, approving nod – an unsaid message for both listener and companion in the darkness ahead.

Though age laid heavily on Tom, the spirit of yesteryears seemed re-constituted within his frame as they made for the ruined windmill, leading them across weathered flagstones under latticed patterns cast down by broken, angled roof supports overhead. Those angles shadowing upon their ground glided with slow pace as evening gave over to night; this caused much as uncertain an increase to come for that world held beside their own very feet. Ahead, indistinct scratchings like some arcane incantations scrawled dimly along heavy gray blocks buttressing the central grind – Old Tom observed this impassively as lead gusts brushed past his swaying cloak though his quiet lips twisted softly against unmentioned pain.

---

**Date Written:** 2024-11-26 21:00:04

The trees surrounding the windmill seemed to lean in, as if drawn by the weight of whispered secrets, their leaves rustling in hushed tones as the group made their way closer to the ancient structure. The air grew thick with the scent of damp earth and moss, the musty smell of decay wafting from the cracks in the windmill's masonry like the exhalation of a forgotten crypt. Elara's fingers continued to weave an ethereal melody on her lute, the notes seeming to conjure the very mist that twirled and danced around the group's feet.

As they approached the windmill's entrance, the scratching on the blocks seemed to shift and writhe, casting flickering shadows across the ground like grasping fingers. Old Tom's eyes clouded, and he paused, his gaze lingering on the arcane script as if unraveling some ancient mystery. "This," he muttered, his voice low and heavy, "is the mark of the Architects. A society of sorcerers who once wielded the secrets of this land. They toiled in darkness, crafting the mechanisms that leveraged the balance of the world." His gaze turned to Dave and Elara, and he inclined his head. "Tonight, we seek the one who breached the balance and let the shadows spread."

A keening cry echoed across the ravine, the sound of darkness and longing carried on the wind. The words "We should move quickly" hung unspoken in Old Tom's voice as he grasped the rusty door handle, wrenched the creaking portal open, and led them into the depths of the abandoned windmill. Shafts of silvery light streamed through cracks in the stonework, casting an illusory glow on the worn stone beneath their feet. The air within reeked of abandonment and stale dust, echoing with distant memories, as if whispers seeped from every crumbling brick.

With the chill of the evening gathered around their shoulders, the air trembled with every hesitant breath drawn by those who would dare step further into that place hidden – until silence and doubt came shrouded – before night enveloped their passage.

---

**Date Written:** 2024-11-26 22:00:03

As the creaky door groaned shut behind them, the sudden loss of the flickering moonlight plunged the group into an oppressive darkness. The keening cry still resonated through the air, now muffled by the thick stone walls, but no less unsettling. The sound of scraping and scuttling echoed through the vacant spaces within the windmill's walls, like the whispers of restless spirits. Elara's fingers instinctively danced across the lute's strings once more, weaving a protective melody that faintly illuminated the darkness with an ethereal glow. The notes wove a fragile shield around the group, warding off the oppressive atmosphere that seemed to close in around them.

With the faint light guiding them, Old Tom began to lead the way through the musty darkness, his boots scraping against the worn stone floor. Shafts of silvery light that streamed through the cracks in the stonework cast eerie silhouettes on the walls, making it seem as though unseen figures watched them from the shadows. The air inside the windmill hung heavy with the weight of years of neglect, and the whispers of the past seemed to cling to every surface, reluctant to release their secrets. As they moved deeper into the windmill, the whispers grew louder, an unsettling susurration that threatened to overwhelm the fragile melody of Elara's lute.

The interior of the windmill was a labyrinth of narrow corridors and chambered rooms, each one a gateway to forgotten memories and the remnants of a once-thriving Mechanism. In the heart of the structure, a grand, high-ceilinged chamber beckoned, the walls surrounding a vast, ornate orrery – a celestial map of the land, its brass surfaces tarnished by the passing of time. Old Tom approached the orrery, his eyes narrowing as he examined the positions of the intricately crafted gears and spheres. "This Mechanism once governed the balance of nature within this land," he murmured, his voice laced with awe. "But it has been... altered. A deliberate breach, crafted to unravel the harmony of the world."

As Old Tom's words faded away, the silence within the windmill was broken by a low, menacing chuckle, the sound echoing from the depths of the orrery itself. The group's gazes converged on the mechanism, a sense of foreboding seeping into their hearts as they realized they were not alone in the abandoned windmill.
