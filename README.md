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

**Date Written:** 2024-10-29 18:37:32

As the sun rose over the rolling hills of the Dragon Coast, a worn leather wagon rattled and creaked its way along the dusty road to Bluestone. Among its passengers was Dave the Paladin, a young and ambitious warrior-monk clad in the simple, yet practical, attire of his order. With his gleaming steel-plated armor, longsword, and the symbol of his faith – a silver holy symbol of Selûne, the Moonmaiden – emblazoned on his chest, Dave cut an imposing figure amidst the peasant travelers. Yet, despite his martial bearing, a palpable sense of restlessness hung about him, like a traveler eager to shake off the tedium of months spent within the cloistered walls of his monastery.

Dave's thoughts were consumed by the whispered tales of adventure and bravery that had long circulated among the brothers of his order. Tales of valiant heroes, of treacherous quests, and of the world beyond the monastery's walls had stirred something deep within him. It was this insatiable hunger for excitement and purpose that had driven him to bid farewell to the familiar, if unfulfilling, routines of his monastic life and set out into the wider world. Bluestone, a humble but bustling town on the northwestern coast of Faerûn, was to be his starting point – a stepping stone into the great unknown.

As the wagon creaked and groaned over a particularly rutted stretch of road, a lanky, freckled youth with a handful of straw-stuffed luggage and a stringy-looking packmule caught Dave's eye. "Hey there! Mind if I slide on in? The missus has a heap of baskets on this side," the youth called out, motioning toward a corner of the wagon, where a stocky countrywoman guarded a veritable forest of woven reed containers. "They're for the market – finest freshwater clams this side of the Coast Way," she explained in a gruff, no-nonsense voice.

Dave motioned graciously for the youth to join him, and they introduced themselves as Eli and his mother, Elara – a long-time seller of fresh seafood in Bluestone. "We've made the trip from Greenhaven these six years now," Elara explained, "though the tales of orcs and bandits along the roads don't make me sleep easy of late." As they spoke, the wagon inched closer to its destination – and the promise of adventure hovered tantalizingly within reach, like the first wisps of morning fog lifting to reveal the unsuspected wonders of the day to come.

---

**Date Written:** 2024-10-29 18:38:25

The air was alive with the sweet scent of wildflowers and the earthy aroma of damp soil as the wagon rounded a bend, affording a breathtaking view of Bluestone in the distance. Nestled between the windswept dunes and the sun-kissed waters of the Dragon's Teeth bay, the town seemed to shimmer and dance in the morning light, its weather-beaten buildings and sail-crowded harbor blending into a tapestry of color and life. A sturdy stone lighthouse stood sentinel over the town's seaside promenade, its watchfires still smoldering from the previous night's vigil.

As the wagon drew closer, the faint sounds of market-day commerce – hawkers calling their wares, haggling merchants, and the constant clucking of poultry – mingled with the creaking of the wagon's wooden frame, drawing Dave's senses into a world of cacophonous delight. He felt his excitement building, like a drumbeat quickening its tempo, and his thoughts began to turn to the many possibilities this bustling town might offer – adventure, danger, or fortune. He knew, deep within, that this place was but the starting point on a grand journey that would see him facing his share of trials and tribulations, all in the name of service to his faith and his unyielding pursuit of justice.

As the wagon approached the town gate, its attendant watchmen cast a practiced eye over the passenger manifest, scrutinizing the new faces in their midst. A dour-faced veteran of the town watch, a portly sergeant named Marcellus with a gruff tone to match, approached the wagon, scanning each passenger with a practiced gaze. His eyes narrowed in inspection as they landed upon the armor-clad paladin, and a half-step closer, he inquired gruffly, "Mind showin' yer credentials, friend? Can't be too careful with all these... incidents 'round the Coast of late." The other riders, Elara in particular, cast inquisitive glances at Dave, sizing up his potential to attract unwanted attention.

The conversation hung, like the uncertain pause between musical phrases, as Dave sought to demonstrate his peaceful intentions while convincingly establishing his, and thus his fellow passengers', legitimacy in the face of curious scrutiny. What manner of resolve would he muster in this time-honored ritual of convincing the vigilant gate sergeant of his integrity, faith unshakeable, and pure heart burning with purpose, only time could tell.

---

**Date Written:** 2024-10-29 18:38:30

As Dave's hand instinctively rose to the engraved silver medallion hanging around his neck, a symbol of his unwavering allegiance to the Order of the Radiant Dawn, a gentle influx of sunlight highlighted the fine lines and delicate filigree that adorned the pendant. His eyes locked onto Sergeant Marcellus's, conveying a sense of sincerity and diligence honed from years of devotion to his faith. In a clear, measured tone, Dave declared, "Greetings, Sergeant. I am Dave, a paladin of the Order of the Radiant Dawn. I come to Bluestone on a mission of peace, with the intention of providing aid to those in need and dispelling the shadows that seek to encroach upon this fair town."

He retrieved a fold of parchment, sealed with the Order's emblem in crimson wax, from a hidden compartment within his armor. The document, penned by the Order's Chancellor herself, attested to Dave's status and mission, carried all the weight of his organization's authority, further underscoring the legitimacy of his claim. Elara's curious gaze also encompassed the parchment as Dave unfolded it, her angular features tilting with interest. The air appeared to thicken momentarily as the watchman scrutinized the seal, weighing the weight of the endorsement and his own seasoned judgment against the perceived risks presented by a battle-hardened paladin.

Sergeant Marcellus deliberated in a state of quiet contemplation, a flicker of intense scrutiny dancing within the depths of his otherwise stony visage, before finally breaking the silence with an economical nod. "Welcome, Paladin Dave. You and your companions may pass. Mind you keep a weather eye on the goings-on around town. Rumors've been circulating... certain unwholesome occurrences disturbing the peace. If you should happen to run into trouble, don't hesitate to reach out to the watch. We'll be keeping an eye out for you." A quiet sigh accompanied the passing of his gaze over the wagon's occupants once more, leaving them to continue onward into the vibrant melee that awaited in Bluestone.

Once the wagon had passed beneath the raised portcullis, the sounds of market-day commerce swelled around them in a joyous surge. The sweet fragrance of exotic spices and freshly baked bread, mingling with the sounds of hammering on metal and clashing steel from the local smithies and armorers, surrounded the wagon as they threaded their way deeper into Bluestone. Vendors selling an assortment of treasures, trinkets, and seemingly vital necessities of oceanic provenance flanked their progress, competing for the attention of passersby and out-of-town merchant travelers in an incessant flurry of motion, eye-catching spectacles, and melodic cajoling.

---

**Date Written:** 2024-10-29 18:38:35

As the wagon navigated through the bustling streets, the cacophony of sounds and vibrant colors enveloped Dave and his companions, creating a sensory overload that was both exhilarating and overwhelming. The warm sunlight danced across the town, casting long shadows behind the colorful stalls and illuminating the dusty cobblestones. Elara's gaze darted from one vendor to the next, her eyes sparkling with curiosity as she took in the kaleidoscope of sights and sounds. She fingered the hilt of her sword, a habitual gesture that betrayed a lingering unease, even as a hint of excitement played on her lips.

To their left, a harried-looking vendor touted his wares, a rainbow of seashells arranged artfully on a velvet-draped board. The vendor's cries of "Crabs, shells, and curios from the farthest reaches!" mingled with the chatter of a nearby performer, a juggler whose whirling clubs created a blur of motion as he effortlessly kept a half-dozen different objects aloft. Further on, the pungent aroma of fresh fish wafted from a food stall, entwining itself with the sweet scent of sugar and spices from a nearby bakery. A cluster of passersby gathered around the baker's stall, sampling her wares and laughing as she traded banter with the juggler.

Dave guided the wagon with a gentle touch, navigating the crowded streets with a practiced ease. His eyes never strayed far from the bustling throng, his paladin's instincts honed to detect even the slightest whisper of unrest or deceit. As they made their way deeper into the heart of Bluestone, the architecture shifted from rough-hewn commercial structures to more refined, ornate dwellings, replete with intricate carvings and coats of arms that told the story of a rich and storied history. The air was alive with the pulse of the town, a fascinating tapestry of sound, color, and scent that seemed to grow more complex, and alluring, with every passing moment.

Ahead, the rooftop of a stately structure dominated the skyline, gleaming a weathered gold in the sunlight. The Bluestone Manor, seat of the town's wealthy patron family, loomed over the surrounding landscape like a gently weathered behemoth. Rumors had circulated among the townspeople about the strange occurrences and mysterious phenomena reported within the manor's hallowed halls, the strange disappearances and inexplicable occurrences said to plague the halls that seemed to defy the understanding of even the wisest scholars. The tales hung in the air like the persistent scent of salt and seaweed, piquing the interest of both the townsfolk and the visitors, as the mysterious allures of the ancient structure seemingly called out like a siren's song, drawing in all who would pause to listen.

---

**Date Written:** 2024-10-29 20:00:04

As the wagon neared the imposing Bluestone Manor, the atmosphere around it seemed to grow heavier, as if the air itself was weighed down by the secrets and mysteries that lay within its ancient walls. The sound of hammering on metal drifted from the nearby blacksmith, mingling with the distant crash of waves against the shore and the murmur of hushed conversations among the townspeople. Elara's gaze lingered on the manor, her eyes narrowing as if trying to pierce the veil of intrigue that shrouded it.

Dave guided the wagon past the bustling town square, where a statue of the town's benefactor, a long-forgotten sea captain, stood proudly atop a weathered pedestal. The pedestal was adorned with the same coat of arms that adorned the manor's walls, and Dave couldn't help but feel a sense of pride in the town's resilience and history. As they passed by the square, a hooded figure slipped out of the shadows, their eyes lingering on the group before disappearing into the crowded streets once more. The paladin's instincts prickled at the sudden movement, but his gaze returned to the road ahead, unsure if the figure had been a threat or merely a curious onlooker.

As the wagon's wheels rattled over the cobblestones, the sounds and smells of the town gave way to a sense of quiet anticipation. The promise of an evening's rest and perhaps a more leisurely exploration of Bluestone's secrets tantalized the travelers. Before them, the Bluestone Manor's imposing façade beckoned, like a sea-worn behemoth slumbering in the heart of the town. As they drew closer to the manor's main gate, the sound of a solitary horn drifted out into the air, announcing the arrival of the wagon and its weary occupants. The great wooden gates creaked open, revealing a glimpse of manicured gardens and polished silverware within. Elara's hand on the hilt of her sword betrayed a lingering unease, even as the promises of a warm fire and fine dining seemed to allay her concerns.

A dignified steward, resplendent in a tailored coat, emerged to greet the wagon. His name was Renolds, a tall and slender man with piercing blue eyes that seemed to hold the secret histories of a dozen lifetimes. "Welcome, travelers," he said, with a bow as calculated as a royal courtier's. "I trust your journey to Bluestone was a pleasant one. Please, after you." With a gesture that conveyed both precision and kindness, Renolds ushered the group through the gates, and into the intricate world of the Bluestone Manor. As they passed through the gates, Elara's unease seemed to step aside, and for a moment, the allure of the ancient manor took center stage, inviting the group to surrender to its timeless charm and enchanted halls.

---

**Date Written:** 2024-10-29 21:00:05

As they stepped through the gates, the scents of blooming flowers and freshly polished leather enveloped them, momentarily quelling the lingering unease in their minds. The soft chime of tiny wind bells, delicately hung among the manicured hedges, added a soothing melody to the evening air. Elara's gaze drifted upwards, tracing the façade of the manor as it stretched towards the sky, its walls bearing the faint scars of centuries past, where forgotten family crests and legends of the sea mingled with the stonework. The windows, like the dark, still pools of a forest lake, offered fleeting glimpses into the hearts of the rooms within, where the flicker of candelabras cast warm, inviting shadows on the walls.

Renolds led them along a meandering path, lined with lantern-lit sculptures of the sea creatures said to be the friends of the long-forgotten sea captain. Each carefully crafted sculpture seemed to embody the essence of its oceanic counterpart, and the fine details that adorned them seemed to speak to an artistry so precise, so heartfelt, that one could almost hear the siren song of the sea within the gentle rustling of the leaves nearby. The air around them was heavy with the anticipation of fine dining and warm firesides, as they made their way deeper into the heart of Bluestone Manor.

Their arrival at the manor's doorstep was met with the soft clinking of a servant, swiftly and discreetly opening the heavy, ornate door, allowing the group to spill into the warm glow of the grand foyer. Columns, adorned with intricate frescoes of sea battles and myths of old, stood watch over the newcomers, exuding the quiet serenity of a monastic library. As they entered the foyer, a figure stepped out of the nearby library, their eyes catching the attention of the travelers. Lady Harcourt, the enigmatic owner of Bluestone Manor, stood poised before them, her very presence reminiscent of an autumn morning on a mist-shrouded coast – mysterious, delicate, and altogether captivating. Her eyes, like two glints of frost in a moonlit window, sparkled with curiosity as she took in the weary companions.

With a calm, elegant smile, she stepped forward, offering Elara her hand. "Welcome, Elara, and friends. You've arrived just in time for dinner. Tonight, we dine on the celebrated lobster of Bluestone, expertly prepared by our chef, Maître Lapierre." Lady Harcourt's voice had the gentle cadence of a lullaby, mixing the promise of fine food, wine, and warm conversation, under a spell that was impossible to resist. As Elara's hand touched Lady Harcourt's, a tingling spark of curiosity flared to life, igniting within the paladin a profound curiosity – one that the tranquil atmosphere and ancient walls of Bluestone Manor seemed to tempt her to surrender to.

---

**Date Written:** 2024-10-29 22:00:04

As Elara's hand met Lady Harcourt's, the gentle warmth of the foyer seemed to envelop her, weaving a subtle spell of tranquility that soothed her travel-worn senses. The scent of old books and the faint hint of saltwater wafted from the lady's skin, transporting Elara to a forgotten cove on a summer's day, where the sound of waves gently lapping against the shore seemed to echo through her mind. Lady Harcourt's eyes, those frosty glints in a moonlit window, sparkled with a knowing warmth as she drew Elara closer, their hands clasped in a gentle hold. "I see you are weary from your journey," she said, her voice a soothing melody that seemed to wash away the fatigue of the road. "Renolds, kindly see our guests to their quarters. Maître Lapierre has outdone himself this evening. We dine in an hour."

With a measured bow, Renolds gestured for the travelers to follow him, leading them through a maze of corridors adorned with cobweb-shrouded oil paintings, their subjects shadowy figures from a bygone era. As they traversed the manor's depths, the silence between them was punctuated only by the soft ticking of distant clocks and the faint scent of flowers that trailed in Lady Harcourt's wake, her very essence now seeming to permeate the entire manor. It was as if she had awakened a deep sense of enchantment within Bluestone's walls, coaxing the forgotten tales of the sea captain's exploits and the whispers of ancient myths into a world both captivating and tangible.

At the door to her chambers, Elara paused for a moment, casting a glance over her shoulder. In the fading light of the corridor, the long, flowing silhouette of Lady Harcourt still lingered, an ethereal shadow that seemed to be etched into the very fabric of the manor itself. And then, in a whisper of sound, the lady vanished into the darkness of the corridor, leaving Elara with an unmistakable sense of tantalizing anticipation, her curiosity ignited like a flame set alight by the light of a thousand burning candles.

As Elara turned to enter her rooms, the soft glow of candlelight spilled from within, casting a welcoming radiance across the floorboards, like an untold secret shared between old friends. But even in the peaceful reprieve offered by these quarters, Elara's mind could not shake the feeling that the borders of reality were being tenderly pushed – and stretched – as the timeless heartbeat of Bluestone Manor, with all its myths and legends, whispered an invitation into the night, urging her onward, on a journey to unravel the many mysteries that the coming days would bring.

---

**Date Written:** 2024-10-29 23:00:04

As Elara entered her chambers, she was enveloped by the soft candlelight that danced across the walls, casting a warm, golden glow over the intricately carved four-poster bed and the plush velvet armchair positioned in front of a crackling fire. A delicate lace shawl, its intricate threads sparkling in the firelight, lay elegantly draped across the back of the chair, imbuing the space with a sense of understated elegance. A small, ornate clock perched upon a nearby inlaid dresser, its gentle ticking echoing through the room as the scent of sandalwood wafted through the air, infusing the space with an unmistakable sense of reverence.

To her left, a towering triple-paned window beckoned Elara closer, its frosty glass gleaming with a gentle luminescence that seemed to emanate from within. As she approached the glass, she discovered a tiny silver ledge adorned with small, translucent figurines of delicate boats, gleaming like silver crescent moons. Each figure depicted an image of a lone sailor, sternly set against the weight of an unseen sea, etched with an unyielding resolve as the vast unknown stretched out before them. And Elara was immediately transfixed by their steadfast quietude – as if these small sailors held within them a world of collective wisdom that whispered mystically at the edge of her thoughts.

Just then, Renolds discreetly re-entered the room with a quiet bow, carefully laying out a delectable selection of sparkling gowns and wraps across the bed, reminding Elara of the upcoming dinner party and the need for haste if she wished to prepare herself for the company of the manor's guests. As Elara turned from the frozen windowpane, the night's darkness – full of whispers, secrets, and ancient watchfulness – yielded a disquieting impression, an unshakeable intuition that each hour, like the figures on the small glass boats, held within them a heavy load of unexplored destinies – mysteries no amount of candlelit hospitality could alter or camouflage – and that the moon hanging high in the oncoming twilight cast long shadows of which her very presence within Bluestone House had altered, ever so slightly, and irrevocably, a delicate pattern of interwoven lives and hidden paths that were, in truth, far from being hers – yet within which her sole being stood bound to unravel their deeply embedded enigma, revealing, finally, whether the truth behind this sea captain's house was a haven – or its most carefully locked room.

At length, breaking this spell, Elara responded to Renolds by saying with some sense of effort, "Thank you. Which gown should I choose to dine in this evening?" Renolds offered, "May I suggest, my lady, this one – made of lightweight French silk – the lady shipwrecked upon moon, all to which echoes one within full sight of moored ships gently fastening toward that coast."

---

**Date Written:** 2024-10-30 00:00:04

As Elara's gaze followed Renolds' discreet gesture, it fell upon a breathtaking gown of the finest French silk, its lustrous sheen glimmering in the soft candlelight like the moon's silver glow on a midsummer night. The exquisite fabric was woven with a delicate pattern of small, moonlit boats gently drifting upon a sea of shimmering ivory, and the intricate design seemed to shimmer and dance with every movement of the candle flames. Elara felt an inexplicable connection to the gown, as if the silken threads held within them the whispers of the small sailors on the silver ledge, beckoning her toward the unfathomable depths of the sea captain's mansion.

With a quiet nod, Elara accepted Renolds' suggestion, and the devoted servant swiftly set about assisting her mistress into the gown, carefully adjusting the delicate straps and embroidered hem. As the silk folds enveloped her figure, Elara felt an uncanny sense of transformation, as if she had slipped into a role that had been waiting for her all along – a part that would soon draw her into the mysterious world of Bluestone House and the whispers that came with it. The gentle caress of the silk against her skin, the soft lapping of the moon boats against her feet, and the echoing susurrus of the frosty night beyond the windows – all of these subtle sensations combined to evoke an intuition that this night, above all others, would be a moment when the fragile balance of Bluestone's closely guarded secrets would begin to shift and unravel, beckoning her toward an unseen destiny that was intertwined with the delicate glass sailors and their unresolved mysteries.

With the gown securely in place, Renolds paused to hand Elara a delicate white rose, which she carefully pinned into her hair, allowing the sweet, heady scent to mingle with the lingering aroma of sandalwood and the distant tang of the frosty night air. A quiet knock on the chamber door broke the spell, announcing the arrival of Lady Olivia, Bluestone's enigmatic mistress, who had come to escort Elara to the dinner party. As Elara turned toward the door, she was met with the faintest hint of a mysterious glance, exchanged between Renolds and Lady Olivia, a fleeting exchange that left her with an unshakeable sense that she was stepping into a world where every smile concealed a hidden purpose and every friendly greeting hid an unknown intention.

---

**Date Written:** 2024-10-30 01:00:04

As Lady Olivia glided into the room, her eyes locked onto Elara, sparkling with a subtle intensity that bordered on a challenge, her long, slender fingers extending a beautifully crafted ivory fan adorned with a delicate etching of a seahorse, its body curling around the scalloped edges of the fan like a symbol of protection. "You look enchanting, dear Elara," Lady Olivia said, her voice dripping with honey, as she shifted the ivory fan to reveal a glint of pearl that cascaded down the center spine like a delicate waterfall, "though I suppose the gown was meant to be the star of the evening, not its wearer." With a soft smile, Lady Olivia extended her elbow to escort Elara to the grand ballroom below, the whisper of silk rustling as the rich velvet drapes parted to reveal a chandelier-lit staircase that seemed to thrust skyward like a glittering crystal shard.

As they descended into the grand ballroom, the opulent setting unfolded like a tapestry of intrigue and mystery, the guests weaving an undercurrent of secrets and unspoken conflicts, each one carefully concealed behind a mask of cordiality and refinement. The room was a tapestry of gemstones, gold-thread embroidery, and delicate champagne glasses, each reflecting a glimmer of light that danced in harmony with the lilt of waltzing couples. Amidst the whirl of ballgown silhouettes, the rustle of black tails and the refined whispers of conversation, Elara spotted the faint figure of Captain Blackwood standing alone by the French doors, a solitary silhouette that commanded her attention like a ghostly siren on a stormy night, its presence imbuing her with an overwhelming sense of destiny and imminent resolution.

With the ball already in full swing, the evening had claimed its rhythm, and as Elara surrendered herself to the orchestral waltz that swelled through the room like an oceanic tide, her heart pounding in sympathy, she began to lose herself in the motion of the music, letting the silken folds of her gown stir around her in languid waves as if the moon boats themselves had borne her aloft into the soaring spaces of Bluestone House. Yet, even as her senses ebbed and flowed with the gentle beat, her gaze stealthily sought out Captain Blackwood's solitary figure, an irresistible pull that refused to be shaken – an unseen thread binding them across the sea of unknown secrets that promised to erupt into revelation, as the moon dipped toward its zenith in the frosty night beyond the windows, standing vigil over the fates that were gathering within the shadowy corridors of Bluestone House.
