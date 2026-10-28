# Voice guide, version 2 (October 2026)

This replaces the tic budgets in `style-guide.md` as the main rulebook for new chapters and rewrites. Read it before every chapter.

## What went wrong (measured on ch1–310)

A script (`tells.py`) counted the habits a careful reader notices. Sentences average **9–10 words**. A third of all paragraphs are **six words or fewer**. Similes built on "the way a… / the way you…" rose from 1.0 to **2.7 per thousand words**. "He says:" relays rose from 0 to **4 per thousand words** in Book 4. "Telling you first", "that's the rule", "obviously" and "warm" became refrains.

None of these is wrong once. Together they make every chapter sound like the same voice reciting: short, solemn, rhythmic, each scene landing on a quotable line, every character equally wise and gentle. Readers call that "AI voice". Editors would call it **monotone and sermonizing**. Either way it is fixable, line by line.

What still works, and should be kept: the system notifications, the concrete Lingzhou world (dumpling cart, Number Nine bus, the Ossuary, the north wall), Dabao's comedy, the power-system rules, the asking ethic as the story's spine, and the big set pieces.

## The masters we are learning from, and the one lesson from each

- **Anton Chekhov:** one exact, unexpected detail does more than three adjectives. *"Don't tell me the moon is shining; show me the glint of light on broken glass."* Never state the emotion the detail already carries.
- **Ernest Hemingway:** the iceberg. Leave out what the reader can feel. If a character understands something, he does not explain it to the person beside him.
- **Terry Pratchett:** Death can be funny and kind in the same paragraph. Jokes belong *inside* the grief, not after it. People stay petty, hungry and annoyed even at the end of the world.
- **Ursula K. Le Guin:** big ideas in plain words. A moral is acted out by stubborn, specific people, never announced.
- **Raymond Chandler:** a simile has to come from the narrator's own world and be surprising. One good one per scene beats six polite ones.
- **Jin Yong (wuxia):** fights are choreography plus character. Every exchange reveals a temperament, costs something, and ends with someone changed.
- **Cuttlefish That Loves Diving (*Lord of the Mysteries*), the genre benchmark:** rules first, wonder second. Mysteries pay off in order; the protagonist thinks in steps the reader can follow; humor comes from the hero's private commentary.
- **Er Gen / I Eat Tomatoes (cultivation):** a power moment needs a clear before and after, a number, and a witness who reacts.

## The rules

### 1. Rhythm
- Aim for an average sentence of 13–16 words, with real range: a forty-word sentence followed by a four-word one. Never five short sentences in a row unless it is a fight.
- One-line paragraphs: at most about 15% of paragraphs, and only for a genuine beat (a reveal, a blow, a punch line).
- Do not chain clauses with "and… and… and" more than once a chapter.

### 2. Images
- At most one simile per 500 words. It must come from the point-of-view character's life: exams, phone screens, street food, the river, the cemetery, school, bus routes. Ban "the way a person does X when Y" unless it is the best line on the page.
- Prefer the thing itself: not "something very old and warm", but what it does to the room.

### 3. Dialogue
- People interrupt, answer the wrong question, joke when frightened, repeat themselves, lose the thread. Nobody speaks in finished aphorisms more than once a scene.
- Every major voice must be recognizable without a tag:
  - **Yuanshu:** dry, short, deflecting; funnier under pressure; thinks in steps.
  - **Seed:** literal, numerical, curious. It counts and it asks. It does not make speeches about its feelings; when it has one it names it in four words and moves on.
  - **Lingyue:** blunt, competitive, impatient, physical (she hits arms, she eats his food). She does not do tender speeches; tenderness leaks out sideways.
  - **Dabao:** "bro", food, loud loyalty, cries easily, gets things wrong cheerfully.
  - **Xiaoyu:** fast, sarcastic, practical, has the last word.
  - **Su Mingli:** orders. Five words where others use twenty.
  - **Qin Hao:** pedantic, numbers, prickly.
  - **Wanqing:** sharp, dry, a scientist's precision, a mother's ruthlessness.
  - **Old Seven:** soldier's idiom, terse. Relay at most three "He says" lines in a row; otherwise report his words in narration.
- Plain "said". Cut "without the grade" and other repeated tag phrases after their first use per arc.

### 4. The theme
- The asking ethic is the spine. Show it in action and in cost; do not name it. Cut "that's the rule", "I'm telling you first", "asked first", "you can say no" wherever the scene already makes it clear. Keep them only where a character is *using* the rule against someone.
- Not every climax resolves by asking. The guide's older note stands: what happens *after* the answer is where the story grows.
- Let some people say no and stay unconvinced. Let a good choice cost something that is never refunded.

### 5. Scene endings
- At most one quotable closing line per chapter. End other scenes on an action, an object, an interruption, a joke, or a plain fact.
- Do not end a scene with a character "not saying anything" or "looking at something for a long time".

### 6. Texture
- Bodies: hunger, cold tea, sweat, a stiff neck, a phone at 3% battery. Weather. Prices. Smells.
- Each chapter needs at least one laugh, even a small one, and one detail nobody else would have thought of.
- Names and epithets: say "the Collector", not "the oldest thing anyone had ever heard". Epithets once per arc.

### 7. Banned or capped phrases (per chapter)
| Phrase | Cap |
| --- | --- |
| did not say anything / nobody said anything | 1 |
| for a (very) long time | 1 |
| very still / went still | 1 |
| the way (a/an/you/someone/the)… as a simile | 2 |
| Not X. Not Y. openers | 1 |
| very | 6 |
| something | 6 |
| a little | 3 |
| telling you first / told (him) first | 1 |
| that's the rule / obviously | 1 |
| square black capitals | 1 |
| "almost smiled", "face did a thing" | 0 |

Run `python3 EDITORIAL/vcheck.py N` on every chapter before publishing. Dialogue uses plain quotation marks; italics are for emphasis, thoughts and other-language speech only.

## Rewrite procedure (for existing chapters)
1. Reread the chapter and its CANON rows. Every fact, number, name, ability and outcome stays.
2. Rewrite sentence by sentence for rhythm, images, dialogue and texture. Cut sermon lines. Add one laugh and one fresh detail if missing.
3. Keep chapter titles, part markers, system notifications and Stele letters (formats in `style-guide.md`).
4. Length may change by ±15%.
5. Check with `EDITORIAL/vcheck.py`, then publish in batches of about ten chapters with a note in the commit.
