# Adding Rockbuster sets

This guide explains how to write new question sets, validate them, and export them to the frontend.

---

## What is a Rockbuster set?

A Rockbuster set is a group of three cryptic-initials clues that share a theme. Each clue gives:

- A set of initials (e.g. `W G`)
- A clue sentence that hints at the answer through wordplay — phonetics, punning, or a cryptic description
- The answer whose initials match

The player reads the clue and tries to guess the answer from the initials. The wordplay is oblique rather than direct: the clue should describe a component of the answer, not state it outright.

---

## YAML schema

All sets live in `data/rockbusters.yaml` as a YAML list. Each entry must conform to the following schema.

### Annotated example

```yaml
- id: sweetbusters-001          # Required. Unique identifier. Use kebab-case, e.g. topic-NNN.
  enabled: true                 # Required. Boolean. Set to false to exclude from rotation without deleting.
  title: Sweetbusters           # Required. Short display title for the set.
  topic: UK sweets              # Required. Category label. Used for filtering and display.
  difficulty: easy              # Optional. One of: easy, medium, hard. Defaults to medium.
  office_safe: true             # Required. Must be boolean true. All sets must pass this check.
  region_relevance:             # Optional list. Tags for content that is regionally specific.
    - UK
  intro: "Right, Sweetbusters. Rockbusters, but UK sweets again."
                                # Optional. Sentence shown above the clues. Can be omitted.
  prize: "Email in. Winner gets The Best of The Corrs on MiniDisc."
                                # Required. Shown below the clues. Use a throwaway novelty prize.
  clues:
    - number: 1                 # Required. Must be 1, 2, or 3. All three must be present.
      initials: W G             # Required. Capital letters, space-separated. Must match the answer.
      clue: "Right, that bit in your mouth where the teeth sort of live, it's been on the red and white booze. What's happened there?"
                                # Required. The clue sentence. See content rules below.
      answer: Wine Gums         # Required. The canonical answer. Title case recommended.
      aliases:                  # Optional list of accepted alternative spellings/forms.
        - wine gums
        - winegums
        - wine gum
      reasoning: "gums (teeth live there) plus wine (red and white booze) = wine gums"
                                # Required. Internal note explaining the wordplay. Not shown to players.
    - number: 2
      initials: J B
      clue: "Little newborns, right, but they're all wobbly. You wouldn't put one in a pram."
      answer: Jelly Babies
      aliases:
        - jelly babies
        - jelly baby
      reasoning: "babies (newborns) plus jelly (wobbly stuff) = jelly babies"
    - number: 3
      initials: L H
      clue: "The organ that pumps blood has gone all romantic and that. Bit soppy."
      answer: Love Hearts
      aliases:
        - love hearts
        - love heart
      reasoning: "hearts (organ that pumps blood) plus love (gone all romantic) = love hearts"
```

### Field reference

| Field | Required | Type | Notes |
|---|---|---|---|
| `id` | Yes | string | Unique across the entire bank. Convention: `topicslug-NNN` |
| `enabled` | Yes | boolean | `true` or `false` — not a string |
| `title` | Yes | string | Short display name |
| `topic` | Yes | string | Category label |
| `difficulty` | No | string | `easy`, `medium`, or `hard`. Defaults to `medium` |
| `office_safe` | Yes | boolean | Must be `true`. All content must be office-safe. |
| `region_relevance` | No | list | Optional tags, e.g. `[UK]`, `[US]`, `[global]` |
| `intro` | No | string | Shown above the clues. Can be omitted. |
| `prize` | Yes | string | Shown with the set. Use a novelty or throwaway prize. |
| `clues[].number` | Yes | int | 1, 2, or 3. Each must appear exactly once. |
| `clues[].initials` | Yes | string | Uppercase, space-separated. Must match first letters of answer words. |
| `clues[].clue` | Yes | string | The clue sentence. |
| `clues[].answer` | Yes | string | The answer. |
| `clues[].aliases` | No | list | Accepted alternative forms. The canonical answer is always accepted. |
| `clues[].reasoning` | Yes | string | Internal explanation of the wordplay. Not shown to players. |

---

## Content quality rules

**Initials must match the answer.** The initials field must be the first letter of each word in the answer, uppercased and space-separated. `Wine Gums` = `W G`. `Paris` = `P`.

**The clue must not contain the answer word.** Do not use the answer or any direct synonym in the clue text. The wordplay should describe components of the answer indirectly.

**Phonetic and cryptic style.** The clue works by describing the answer's meaning (or phonetic sound) in a roundabout way. A good clue describes what the answer IS or DOES, not what it is called. For example: "the organ that pumps blood" = heart; "gone all romantic" = love.

**Three clues per set.** Exactly three clues are required. Numbers must be 1, 2, and 3.

**Aliases cover common variants.** If the answer has a plural, a one-word variant, or a common misspelling, list them as aliases. The normalisation step removes punctuation and lowercases answers, so `wine gums` and `Wine Gums` are treated as the same.

**Prize lines are light-hearted.** The prize should be a joke — something deliberately low-value or obsolete (a cassette, a MiniDisc, a novelty item). Do not use real prizes.

**`office_safe` must be `true`.** Do not add content that is adult, politically charged, or offensive.

**`reasoning` is mandatory.** It documents the intended wordplay so future editors can understand and maintain the set. It is never shown to players.

---

## Validation rules

`load_bank` enforces the following on load:

- The YAML file is a list.
- Each entry has a unique `id`.
- `title`, `topic`, `prize` are non-empty strings.
- `office_safe` is boolean `true`.
- `enabled` is a boolean.
- `clues` is a list of exactly 3 entries.
- Clue numbers are 1, 2, and 3, each appearing exactly once.
- Each clue has non-empty `initials`, `clue`, `answer`, and `reasoning`.

If any rule fails, `ContentBankError` is raised with a message identifying the offending set and field.

---

## How to run validation

Run this from the project root to validate the entire bank:

```bash
python -c "from api.content_bank import load_bank; load_bank('data/rockbusters.yaml'); print('Bank OK')"
```

If validation passes, you will see `Bank OK`. If it fails, the error message will identify the set and field that caused the problem.

---

## How to export after adding sets

After editing `data/rockbusters.yaml`, regenerate the JSON files served by the frontend:

```bash
python scripts/export_json.py
```

This writes:
- `docs/data/rockbusters.json` — clues only (no answers)
- `docs/data/rockbusters-answers.json` — answers, aliases, and reasoning

Commit both JSON files alongside the YAML change. The frontend reads directly from these files.

---

## Reaching 730 sets

The daily rotation picks one set per day. 730 sets covers approximately two years without repeating.

Sets can be added in bulk — just append YAML list entries to `data/rockbusters.yaml`. There is no limit on how many entries the file contains.

### Suggested topic categories

| Category | Examples |
|---|---|
| UK sweets | Jelly Babies, Wine Gums, Drumstick, Sherbet Dip |
| European cities | Paris, Rome, Berlin, Lisbon, Vienna |
| World foods | Falafel, Croissant, Sushi, Baklava, Paella |
| Films | Grease, Titanic, Jaws, Alien |
| UK TV shows | Fawlty Towers, Peaky Blinders, The Bill |
| Music artists | Blondie, Radiohead, Oasis, Portishead |
| Sports and games | Snooker, Cricket, Darts, Chess |
| Geography | Mountain ranges, rivers, countries, capitals |
| Science and nature | Elements, planets, animals, plants |
| Occupations | Baker, Surgeon, Librarian, Mechanic |
| Animals | Flamingo, Armadillo, Axolotl, Wombat |
| Fictional characters | Any well-known character whose name works as initials |

A single themed batch (e.g. 30 European cities) adds about a month of content. Topics can be revisited with different sets — the `id` must be unique, but the `topic` field can repeat.
