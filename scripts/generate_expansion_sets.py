"""Generate expansion sets for existing Rockbusters categories."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent

EXPANSION_SETS = [
    # ── Superherobusters +12 (004-015) ────────────────────────────────────────
    {"id": "superherobusters-004", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. More capes and powers. All phonetic.", "prize": "Email in. Winner gets a utility belt with nothing useful in it.",
     "clues": [
         {"number": 1, "initials": "S M", "clue": "A small creepy creature — gone all heroic and started climbing up buildings.", "answer": "Spider-Man", "aliases": ["spider-man", "spiderman"], "reasoning": "Spider (arachnid) + Man = Spider-Man"},
         {"number": 2, "initials": "B", "clue": "A small flying mammal — gone all brooding and started dressing in black in a cave.", "answer": "Batman", "aliases": ["batman"], "reasoning": "Bat (flying mammal) + man = Batman"},
         {"number": 3, "initials": "S", "clue": "A man of exceptional strength — gone all flying and started wearing his pants on the outside.", "answer": "Superman", "aliases": ["superman"], "reasoning": "Super (exceptional) + man = Superman"},
     ]},
    {"id": "superherobusters-005", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more heroes. Say them out loud.", "prize": "Email in. Winner gets a sidekick who asks too many questions.",
     "clues": [
         {"number": 1, "initials": "I M", "clue": "A metal pressing tool — gone all billionaire and started flying around in a suit.", "answer": "Iron Man", "aliases": ["iron man", "ironman"], "reasoning": "Iron (metal/pressing tool) + Man = Iron Man"},
         {"number": 2, "initials": "W W", "clue": "A world of amazement — gone all warrior and started throwing a golden lasso at people.", "answer": "Wonder Woman", "aliases": ["wonder woman"], "reasoning": "Wonder (amazement) + Woman = Wonder Woman"},
         {"number": 3, "initials": "T", "clue": "A loud noise from the sky — gone all Norse and started swinging a hammer.", "answer": "Thor", "aliases": ["thor"], "reasoning": "Thor (Norse god of thunder) = Thor"},
     ]},
    {"id": "superherobusters-006", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more. All capes and tights.", "prize": "Email in. Winner gets a superpower that only works in very specific circumstances.",
     "clues": [
         {"number": 1, "initials": "C A", "clue": "A large sailing vessel — gone all patriotic and started throwing a circular shield.", "answer": "Captain America", "aliases": ["captain america"], "reasoning": "Captain (rank) + America = Captain America"},
         {"number": 2, "initials": "B P", "clue": "A dark feline — gone all African royalty and started defending Wakanda.", "answer": "Black Panther", "aliases": ["black panther"], "reasoning": "Black (the colour) + Panther (a big cat) = Black Panther"},
         {"number": 3, "initials": "D S", "clue": "A medical doctor — gone all mystical and started bending time and space.", "answer": "Doctor Strange", "aliases": ["doctor strange"], "reasoning": "Doctor (medical title) + Strange (odd/peculiar) = Doctor Strange"},
     ]},
    {"id": "superherobusters-007", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more heroes.", "prize": "Email in. Winner gets an origin story nobody asked for.",
     "clues": [
         {"number": 1, "initials": "T F", "clue": "A bolt of electricity — gone all red and started running very fast.", "answer": "The Flash", "aliases": ["the flash", "flash"], "reasoning": "The + Flash (lightning bolt) = The Flash"},
         {"number": 2, "initials": "A M", "clue": "A tiny insect — gone all tiny and started shrinking to solve crimes.", "answer": "Ant-Man", "aliases": ["ant-man", "antman"], "reasoning": "Ant (an insect) + Man = Ant-Man"},
         {"number": 3, "initials": "B W", "clue": "A dark colour — gone all spy-like and started fighting without any superpowers.", "answer": "Black Widow", "aliases": ["black widow"], "reasoning": "Black (a colour) + Widow (a woman whose husband has died) = Black Widow"},
     ]},
    {"id": "superherobusters-008", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. More Marvel and DC. All phonetic.", "prize": "Email in. Winner gets a nemesis who keeps escaping.",
     "clues": [
         {"number": 1, "initials": "W", "clue": "An animal with very sharp claws — gone all metal-boned and started fighting everyone.", "answer": "Wolverine", "aliases": ["wolverine"], "reasoning": "Wolverine (an animal with sharp claws/retractable metal claws) = Wolverine"},
         {"number": 2, "initials": "D", "clue": "A bloke who's already shuffled off — gone all fourth wall breaking and red-suited.", "answer": "Deadpool", "aliases": ["deadpool"], "reasoning": "Dead + Pool (a body of water) = Deadpool"},
         {"number": 3, "initials": "S W", "clue": "A female relative of a witch — gone all reality-bending and started doing hex magic.", "answer": "Scarlet Witch", "aliases": ["scarlet witch"], "reasoning": "Scarlet (a red colour) + Witch = Scarlet Witch"},
     ]},
    {"id": "superherobusters-009", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three villains and heroes.", "prize": "Email in. Winner gets a lair with inadequate heating.",
     "clues": [
         {"number": 1, "initials": "T J", "clue": "A court jester — gone all unhinged and started causing chaos in Gotham.", "answer": "The Joker", "aliases": ["the joker", "joker"], "reasoning": "The + Joker (a jester/the Batman villain) = The Joker"},
         {"number": 2, "initials": "L L", "clue": "A very rich bloke — gone bald and started battling a man in a cape from a tall building.", "answer": "Lex Luthor", "aliases": ["lex luthor"], "reasoning": "Lex (a name) + Luthor (a name) = Lex Luthor"},
         {"number": 3, "initials": "T", "clue": "A giant purple bloke — very determined to halve everything. Has an infinity glove.", "answer": "Thanos", "aliases": ["thanos"], "reasoning": "Thanos (Greek deity of death) = Thanos"},
     ]},
    {"id": "superherobusters-010", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. More heroes.", "prize": "Email in. Winner gets a cape that gets caught in doors.",
     "clues": [
         {"number": 1, "initials": "H Q", "clue": "A female jester — gone all lovesick and started causing mayhem with a mallet.", "answer": "Harley Quinn", "aliases": ["harley quinn"], "reasoning": "Harley (a name/motorbike) + Quinn (a name, like a jester/harlequin) = Harley Quinn"},
         {"number": 2, "initials": "A", "clue": "A man of the sea — gone all fishy and started talking to marine life.", "answer": "Aquaman", "aliases": ["aquaman"], "reasoning": "Aqua (water) + man = Aquaman"},
         {"number": 3, "initials": "M", "clue": "A bloke called Max who's got metal bones and can control other metals.", "answer": "Magneto", "aliases": ["magneto"], "reasoning": "Magneto (magnetic force) = Magneto"},
     ]},
    {"id": "superherobusters-011", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more from the comics.", "prize": "Email in. Winner gets a secret identity nobody believes.",
     "clues": [
         {"number": 1, "initials": "C W", "clue": "A female feline burglar — gone all leather-suited and started robbing Gotham.", "answer": "Catwoman", "aliases": ["catwoman"], "reasoning": "Cat (feline) + woman = Catwoman"},
         {"number": 2, "initials": "S G", "clue": "A female version of a bloke who flies around in a cape — also flies around in a cape.", "answer": "Supergirl", "aliases": ["supergirl"], "reasoning": "Super (exceptional) + girl = Supergirl"},
         {"number": 3, "initials": "G L", "clue": "A ring on a finger — gone all heroic and started flying through space in green.", "answer": "Green Lantern", "aliases": ["green lantern"], "reasoning": "Green (a colour) + Lantern (a lamp) = Green Lantern"},
     ]},
    {"id": "superherobusters-012", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more.", "prize": "Email in. Winner gets a villain who escapes every episode.",
     "clues": [
         {"number": 1, "initials": "P X", "clue": "A teacher — gone all bald and telepathic and started running a school for unusual teenagers.", "answer": "Professor X", "aliases": ["professor x"], "reasoning": "Professor (academic title) + X = Professor X"},
         {"number": 2, "initials": "C", "clue": "A large tropical bird — gone all dark and started firing arrows from rooftops.", "answer": "Cyclops", "aliases": ["cyclops"], "reasoning": "Cyclops (one-eyed creature/X-Men character) = Cyclops"},
         {"number": 3, "initials": "S", "clue": "A tempest — gone all female and started controlling the weather in a white wig.", "answer": "Storm", "aliases": ["storm"], "reasoning": "Storm (weather phenomenon) = Storm"},
     ]},
    {"id": "superherobusters-013", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Nearly at the end of the capes.", "prize": "Email in. Winner gets an arch-enemy they didn't ask for.",
     "clues": [
         {"number": 1, "initials": "R", "clue": "A male Robin — gone all tights-wearing and started helping a man in a bat costume.", "answer": "Robin", "aliases": ["robin"], "reasoning": "Robin (a bird/Batman's sidekick) = Robin"},
         {"number": 2, "initials": "N", "clue": "Something that happens at night — gone all gymnastics and started swinging between buildings.", "answer": "Nightwing", "aliases": ["nightwing"], "reasoning": "Night + Wing (a bird's limb) = Nightwing"},
         {"number": 3, "initials": "L", "clue": "A mischievous Norse god — gone all trickster and started causing problems for his brother.", "answer": "Loki", "aliases": ["loki"], "reasoning": "Loki (Norse trickster god) = Loki"},
     ]},
    {"id": "superherobusters-014", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. More heroes.", "prize": "Email in. Winner gets a sequel nobody expected.",
     "clues": [
         {"number": 1, "initials": "B G", "clue": "A female version of a nocturnal flying mammal — gone all heroic and started fighting in Gotham.", "answer": "Batgirl", "aliases": ["batgirl"], "reasoning": "Bat (flying mammal) + girl = Batgirl"},
         {"number": 2, "initials": "V", "clue": "A synthetic humanoid — gone all complicated feelings and started living in a suburb.", "answer": "Vision", "aliases": ["vision"], "reasoning": "Vision (sight/perception) = Vision"},
         {"number": 3, "initials": "H", "clue": "A big green bloke who's very angry — smashes things when he gets upset.", "answer": "Hulk", "aliases": ["hulk"], "reasoning": "Hulk (a large mass/the Marvel character) = Hulk"},
     ]},
    {"id": "superherobusters-015", "enabled": True, "title": "Superherobusters", "topic": "superheroes and comic book characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Superherobusters. Three more to finish off the set.", "prize": "Email in. Winner gets a radioactive bite and mild superpowers.",
     "clues": [
         {"number": 1, "initials": "H", "clue": "An arrow — gone all feathered and started firing other arrows with great precision.", "answer": "Hawkeye", "aliases": ["hawkeye"], "reasoning": "Hawk (a bird of prey) + Eye = Hawkeye"},
         {"number": 2, "initials": "P", "clue": "A bird with a large beak — gone all villainous and started waddling around Gotham.", "answer": "Penguin", "aliases": ["penguin"], "reasoning": "Penguin (the bird/Batman villain) = Penguin"},
         {"number": 3, "initials": "T F", "clue": "A double-sided coin — gone all split personality and started terrorising Gotham.", "answer": "Two-Face", "aliases": ["two-face", "two face"], "reasoning": "Two + Face = Two-Face"},
     ]},
    # ── TV Busters +10 (011-020, existing disabled ones → use new IDs 041-050) ─
    {"id": "tvbusters-041", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more shows. All phonetic.", "prize": "Email in. Winner gets a remote control with a sticky button.",
     "clues": [
         {"number": 1, "initials": "F", "clue": "A group of people who are very close — live near each other in New York and sit on a sofa.", "answer": "Friends", "aliases": ["friends"], "reasoning": "Friends (companions/the TV show) = Friends"},
         {"number": 2, "initials": "S", "clue": "A bloke called Jerry who finds everything in life mildly irritating — makes a show about it.", "answer": "Seinfeld", "aliases": ["seinfeld"], "reasoning": "Seinfeld (Jerry Seinfeld's surname) = Seinfeld"},
         {"number": 3, "initials": "T O", "clue": "A place where you do your paperwork — gone all awkward and started filming everyone.", "answer": "The Office", "aliases": ["the office"], "reasoning": "The + Office (workplace) = The Office"},
     ]},
    {"id": "tvbusters-042", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more classics.", "prize": "Email in. Winner gets a boxset with a scratched disc four.",
     "clues": [
         {"number": 1, "initials": "M M", "clue": "A bloke in a suit — gone all advertising and started drinking at his desk in the 1960s.", "answer": "Mad Men", "aliases": ["mad men"], "reasoning": "Mad (crazy) + Men = Mad Men"},
         {"number": 2, "initials": "C Y E", "clue": "A bloke called Larry who is perpetually annoyed by the smallest things.", "answer": "Curb Your Enthusiasm", "aliases": ["curb your enthusiasm"], "reasoning": "Curb + Your + Enthusiasm = Curb Your Enthusiasm"},
         {"number": 3, "initials": "S", "clue": "A state of shame — gone all British and started depicting a Manchester family in crisis.", "answer": "Shameless", "aliases": ["shameless"], "reasoning": "Shameless (without shame) = Shameless"},
     ]},
    {"id": "tvbusters-043", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more shows.", "prize": "Email in. Winner gets a spoiler from someone who's already seen it.",
     "clues": [
         {"number": 1, "initials": "O Z", "clue": "A wonderful place — gone all criminal and started showing what happens when drug money piles up.", "answer": "Ozark", "aliases": ["ozark"], "reasoning": "Ozark (the Ozarks region/the TV show) = Ozark"},
         {"number": 2, "initials": "T B B", "clue": "A group of young men — gone all chemistry teacher and started making methamphetamine.", "answer": "The Boys", "aliases": ["the boys"], "reasoning": "The + Boys = The Boys"},
         {"number": 3, "initials": "S", "clue": "A number of people dressed in matching green outfits playing brutal games for money.", "answer": "Suits", "aliases": ["suits"], "reasoning": "Suits (formal outfits/the TV show) = Suits"},
     ]},
    {"id": "tvbusters-044", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more telly shows.", "prize": "Email in. Winner gets a cliffhanger that never gets resolved.",
     "clues": [
         {"number": 1, "initials": "T S", "clue": "A cartoon family — yellow, live in Springfield, dad works at a nuclear plant.", "answer": "The Simpsons", "aliases": ["the simpsons"], "reasoning": "The + Simpsons (the animated family) = The Simpsons"},
         {"number": 2, "initials": "S", "clue": "A very unusual town — alien things keep happening there and two brothers investigate.", "answer": "Spaced", "aliases": ["spaced"], "reasoning": "Spaced (the British sitcom) = Spaced"},
         {"number": 3, "initials": "T X F", "clue": "That definite article, followed by an unknown quantity, followed by a bunch of filed documents.", "answer": "The X Files", "aliases": ["the x files", "the x-files"], "reasoning": "The + X (unknown) + Files = The X Files"},
     ]},
    {"id": "tvbusters-045", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more. All phonetic.", "prize": "Email in. Winner gets a cancelled show brought back nobody wanted.",
     "clues": [
         {"number": 1, "initials": "P B", "clue": "A place for keeping criminals — someone's trying to get out of it using a tattoo of the building.", "answer": "Prison Break", "aliases": ["prison break"], "reasoning": "Prison (where criminals are kept) + Break (to escape) = Prison Break"},
         {"number": 2, "initials": "B B", "clue": "A chemistry teacher who's not very well — decides to make drugs in a campervan.", "answer": "Breaking Bad", "aliases": ["breaking bad"], "reasoning": "Breaking (going wrong) + Bad = Breaking Bad"},
         {"number": 3, "initials": "G O T", "clue": "A competitive event for sitting on a metal chair with pointy bits.", "answer": "Game of Thrones", "aliases": ["game of thrones"], "reasoning": "Game + of + Thrones (seats of power) = Game of Thrones"},
     ]},
    {"id": "tvbusters-046", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more.", "prize": "Email in. Winner gets a TV licence reminder and a biscuit.",
     "clues": [
         {"number": 1, "initials": "T S", "clue": "A group of criminals in Birmingham who keep birds' beaks sewn into their caps.", "answer": "The Sopranos", "aliases": ["the sopranos"], "reasoning": "The + Sopranos (a singing range/the mob family) = The Sopranos"},
         {"number": 2, "initials": "T W", "clue": "That thing you do when you connect cables together — gone all gritty and started documenting Baltimore crime.", "answer": "The Wire", "aliases": ["the wire"], "reasoning": "The + Wire (a cable/to wire a room) = The Wire"},
         {"number": 3, "initials": "S", "clue": "A set of steps going up — gone all supernatural and started showing what happens after someone dies.", "answer": "Succession", "aliases": ["succession"], "reasoning": "Succession (sequence/the HBO show) = Succession"},
     ]},
    {"id": "tvbusters-047", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more shows.", "prize": "Email in. Winner gets a streaming service they didn't sign up for.",
     "clues": [
         {"number": 1, "initials": "F", "clue": "A bloke from Seattle who is very good at listening to people's problems on the radio.", "answer": "Frasier", "aliases": ["frasier"], "reasoning": "Frasier (the character's surname) = Frasier"},
         {"number": 2, "initials": "S", "clue": "That investigator with a pipe and a dressing gown — very clever, lives in Baker Street.", "answer": "Sherlock", "aliases": ["sherlock"], "reasoning": "Sherlock (Holmes) = Sherlock"},
         {"number": 3, "initials": "D W", "clue": "A medical man who travels through time in a telephone box — been going since the 1960s.", "answer": "Doctor Who", "aliases": ["doctor who"], "reasoning": "Doctor (medical title) + Who (questioning pronoun) = Doctor Who"},
     ]},
    {"id": "tvbusters-048", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more. All from the telly.", "prize": "Email in. Winner gets a repeat and an episode they've already seen.",
     "clues": [
         {"number": 1, "initials": "T C", "clue": "A big expensive hat — gone all royal and started depicting the Queen's life in great detail.", "answer": "The Crown", "aliases": ["the crown"], "reasoning": "The + Crown (royal headwear) = The Crown"},
         {"number": 2, "initials": "D A", "clue": "Going down in rank — gone all Edwardian and started involving a lot of dinner parties.", "answer": "Downton Abbey", "aliases": ["downton abbey"], "reasoning": "Downton (a place name) + Abbey (a monastery/church) = Downton Abbey"},
         {"number": 3, "initials": "L O D", "clue": "A queue — gone all police procedural and started investigating corruption.", "answer": "Line of Duty", "aliases": ["line of duty"], "reasoning": "Line + of + Duty = Line of Duty"},
     ]},
    {"id": "tvbusters-049", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more.", "prize": "Email in. Winner gets an episode guide nobody asked for.",
     "clues": [
         {"number": 1, "initials": "P B", "clue": "A set of sharp spines on a mountain range — gone all Birmingham and started making razor blades.", "answer": "Peaky Blinders", "aliases": ["peaky blinders"], "reasoning": "Peaky (peaks/pointed) + Blinders (blinkers/the cap gang) = Peaky Blinders"},
         {"number": 2, "initials": "F", "clue": "A small insect that jumps — gone all Irish and started involving priests on a small island.", "answer": "Fleabag", "aliases": ["fleabag"], "reasoning": "Flea (a small jumping insect) + bag = Fleabag"},
         {"number": 3, "initials": "G A S", "clue": "A bloke called Gavin — gone all Welsh and started being very fond of his girlfriend.", "answer": "Gavin and Stacey", "aliases": ["gavin and stacey"], "reasoning": "Gavin + and + Stacey = Gavin and Stacey"},
     ]},
    {"id": "tvbusters-050", "enabled": True, "title": "TV Busters", "topic": "classic and modern TV shows", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "TV Busters. Three more to finish.", "prize": "Email in. Winner gets the last episode of something they've been watching for years.",
     "clues": [
         {"number": 1, "initials": "T I C", "clue": "A definite article, followed by two letters, followed by a group of people who fix computers.", "answer": "The IT Crowd", "aliases": ["the it crowd"], "reasoning": "The + IT (information technology) + Crowd = The IT Crowd"},
         {"number": 2, "initials": "B", "clue": "A colour — gone all historical and started satirising British history from the Middle Ages.", "answer": "Blackadder", "aliases": ["blackadder"], "reasoning": "Black (colour) + adder (a snake) = Blackadder"},
         {"number": 3, "initials": "D G", "clue": "A group of young women from Northern Ireland — very funny, very Catholic, very 1990s.", "answer": "Derry Girls", "aliases": ["derry girls"], "reasoning": "Derry (city in Northern Ireland) + Girls = Derry Girls"},
     ]},
    # ── Film Busters +10 (061-070) ─────────────────────────────────────────────
    {"id": "filmbusters-061", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more classic films. All phonetic.", "prize": "Email in. Winner gets a cinema ticket for a film that started ten minutes ago.",
     "clues": [
         {"number": 1, "initials": "T D K", "clue": "The saddest hour of the day — gone all heroic and started fighting a man in face paint.", "answer": "The Dark Knight", "aliases": ["the dark knight"], "reasoning": "The + Dark (absence of light) + Knight (armoured warrior) = The Dark Knight"},
         {"number": 2, "initials": "T G", "clue": "A bloke who is the best at everything and has an offer you can't refuse.", "answer": "The Godfather", "aliases": ["the godfather"], "reasoning": "The + Godfather (a religious sponsor/mafia boss) = The Godfather"},
         {"number": 3, "initials": "B T F", "clue": "Returning to a time before now — gone all DeLorean and started involving a scientist.", "answer": "Back to the Future", "aliases": ["back to the future"], "reasoning": "Back + to + the + Future (time ahead) = Back to the Future"},
     ]},
    {"id": "filmbusters-062", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more films.", "prize": "Email in. Winner gets a DVD with a scratch right through act two.",
     "clues": [
         {"number": 1, "initials": "E T", "clue": "Someone who doesn't live on this planet — gone all friendly and started eating sweets with a boy.", "answer": "E.T.", "aliases": ["e.t.", "et", "e t"], "reasoning": "E.T. (extra-terrestrial) = E.T."},
         {"number": 2, "initials": "R O T L A", "clue": "A search for a missing chest — involves a man with a whip and a terrible fear of snakes.", "answer": "Raiders of the Lost Ark", "aliases": ["raiders of the lost ark"], "reasoning": "Raiders + of + the + Lost + Ark = Raiders of the Lost Ark"},
         {"number": 3, "initials": "S W", "clue": "Conflict among the galaxies — a bloke in a black helmet keeps breathing heavily.", "answer": "Star Wars", "aliases": ["star wars"], "reasoning": "Star (a celestial body) + Wars (conflicts) = Star Wars"},
     ]},
    {"id": "filmbusters-063", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more classics.", "prize": "Email in. Winner gets a sequel that's worse than the original.",
     "clues": [
         {"number": 1, "initials": "G", "clue": "A man in ancient Rome — gone all fighting and started entertaining crowds in an arena.", "answer": "Gladiator", "aliases": ["gladiator"], "reasoning": "Gladiator (Roman fighter/arena combatant) = Gladiator"},
         {"number": 2, "initials": "T M", "clue": "A computer programme — gone all leather and started offering red or blue pills.", "answer": "The Matrix", "aliases": ["the matrix"], "reasoning": "The + Matrix (a grid/virtual reality) = The Matrix"},
         {"number": 3, "initials": "S L", "clue": "A list — gone all historical and started saving lives during the Second World War.", "answer": "Schindler's List", "aliases": ["schindler's list", "schindlers list"], "reasoning": "Schindler's + List (a written catalogue) = Schindler's List"},
     ]},
    {"id": "filmbusters-064", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more. All phonetic.", "prize": "Email in. Winner gets a film poster that doesn't fit any standard frame.",
     "clues": [
         {"number": 1, "initials": "C R", "clue": "A gambling establishment — gone all James Bond and started featuring a very good card game.", "answer": "Casino Royale", "aliases": ["casino royale"], "reasoning": "Casino (gambling house) + Royale (royal/the Bond film) = Casino Royale"},
         {"number": 2, "initials": "S", "clue": "A clear blue sky — gone all spy-like and started featuring a bloke called Silva.", "answer": "Skyfall", "aliases": ["skyfall"], "reasoning": "Sky (overhead space) + Fall (to drop) = Skyfall"},
         {"number": 3, "initials": "B R", "clue": "A sharp cutting tool — gone all futuristic and started hunting artificial people.", "answer": "Blade Runner", "aliases": ["blade runner"], "reasoning": "Blade (a sharp edge) + Runner (one who runs) = Blade Runner"},
     ]},
    {"id": "filmbusters-065", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more films.", "prize": "Email in. Winner gets a limited release in three cinemas nobody can reach.",
     "clues": [
         {"number": 1, "initials": "T", "clue": "A large wooden horse — gone all Greek and started containing soldiers inside it.", "answer": "Troy", "aliases": ["troy"], "reasoning": "Troy (ancient city/Brad Pitt film) = Troy"},
         {"number": 2, "initials": "B R", "clue": "A man with a very large shield — gone all ancient Greek and started kicking people into pits.", "answer": "300", "aliases": ["300", "three hundred"], "reasoning": "300 (Spartans at Thermopylae) = 300"},
         {"number": 3, "initials": "N T D", "clue": "Something that happens after midnight — gone all animated and started involving a man called Jack.", "answer": "Nightmare Before Christmas", "aliases": ["nightmare before christmas", "the nightmare before christmas"], "reasoning": "Nightmare + Before + Christmas = Nightmare Before Christmas"},
     ]},
    {"id": "filmbusters-066", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more. All from the big screen.", "prize": "Email in. Winner gets a medium popcorn that costs as much as a mortgage payment.",
     "clues": [
         {"number": 1, "initials": "T L K", "clue": "A very important male lion — gone all musical and started worrying about his place in the food chain.", "answer": "The Lion King", "aliases": ["the lion king"], "reasoning": "The + Lion (large feline) + King (ruler) = The Lion King"},
         {"number": 2, "initials": "E", "clue": "A film about a strange creature being raised by a family — very tall, very kind, makes you cry.", "answer": "Encanto", "aliases": ["encanto"], "reasoning": "Encanto (Spanish for enchanted/the Disney film) = Encanto"},
         {"number": 3, "initials": "I O", "clue": "Something happening inside the skull — gone all colourful and started fighting about feelings.", "answer": "Inside Out", "aliases": ["inside out"], "reasoning": "Inside + Out = Inside Out"},
     ]},
    {"id": "filmbusters-067", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more classics.", "prize": "Email in. Winner gets a free cinema hot dog they'll regret.",
     "clues": [
         {"number": 1, "initials": "T G B", "clue": "How good something is — gone all spaghetti western and started involving three armed men.", "answer": "The Good the Bad and the Ugly", "aliases": ["the good the bad and the ugly"], "reasoning": "The + Good + the + Bad + and + the + Ugly = The Good the Bad and the Ugly"},
         {"number": 2, "initials": "N T D", "clue": "A timetable for something that hasn't happened yet — gone all Keanu Reeves and started on a bus.", "answer": "Speed", "aliases": ["speed"], "reasoning": "Speed (fast movement/the film) = Speed"},
         {"number": 3, "initials": "A", "clue": "An extraterrestrial being — gone all purple and started collecting gems to wipe out half of everything.", "answer": "Avengers", "aliases": ["avengers", "avengers endgame", "avengers infinity war"], "reasoning": "Avengers (those who avenge) = Avengers"},
     ]},
    {"id": "filmbusters-068", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more. All phonetic.", "prize": "Email in. Winner gets a limited edition blu-ray with no special features.",
     "clues": [
         {"number": 1, "initials": "S", "clue": "A bloke in a top hat who lives in a stripy tower and makes chocolate.", "answer": "Wonka", "aliases": ["wonka"], "reasoning": "Wonka (Willy Wonka) = Wonka"},
         {"number": 2, "initials": "R", "clue": "A rat — gone all French and started cooking in a five-star restaurant in Paris.", "answer": "Ratatouille", "aliases": ["ratatouille"], "reasoning": "Ratatouille (a French vegetable dish/the film) = Ratatouille"},
         {"number": 3, "initials": "B", "clue": "A large bear from Peru — gone all British and started making marmalade sandwiches.", "answer": "Paddington", "aliases": ["paddington", "paddington 2"], "reasoning": "Paddington (the bear/the London station) = Paddington"},
     ]},
    {"id": "filmbusters-069", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more films.", "prize": "Email in. Winner gets a director's cut that's forty minutes too long.",
     "clues": [
         {"number": 1, "initials": "F F", "clue": "A quick walker — gone all Southern American and started running across the country with a box of chocolates.", "answer": "Forrest Gump", "aliases": ["forrest gump"], "reasoning": "Forrest (a name/a forest) + Gump (a name) = Forrest Gump"},
         {"number": 2, "initials": "G", "clue": "Phantom-catching equipment — gone all paranormal and started busting things in New York.", "answer": "Ghostbusters", "aliases": ["ghostbusters"], "reasoning": "Ghost (spirit) + busters (those who bust) = Ghostbusters"},
         {"number": 3, "initials": "J P", "clue": "A large extinct creature — gone all theme park and started eating visitors.", "answer": "Jurassic Park", "aliases": ["jurassic park"], "reasoning": "Jurassic (prehistoric era) + Park (an outdoor recreation area) = Jurassic Park"},
     ]},
    {"id": "filmbusters-070", "enabled": True, "title": "Film Busters", "topic": "classic and modern films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Film Busters. Three more to finish.", "prize": "Email in. Winner gets a film adaptation of a book they loved that ruins everything.",
     "clues": [
         {"number": 1, "initials": "T F M", "clue": "That full nude version of a town — gone all Sheffield and started organising a strip show for charity.", "answer": "The Full Monty", "aliases": ["the full monty"], "reasoning": "The + Full + Monty (the whole thing/the Sheffield film) = The Full Monty"},
         {"number": 2, "initials": "T", "clue": "Heroin addiction in Edinburgh — a bloke chooses life, then doesn't, then does again.", "answer": "Trainspotting", "aliases": ["trainspotting"], "reasoning": "Train (railway vehicle) + spotting (observing) = Trainspotting"},
         {"number": 3, "initials": "F W A A F", "clue": "Four occasions when people get married — one occasion when someone dies.", "answer": "Four Weddings and a Funeral", "aliases": ["four weddings and a funeral"], "reasoning": "Four + Weddings + and + a + Funeral = Four Weddings and a Funeral"},
     ]},
    # ── Cartoon Busters +10 (021-030) ─────────────────────────────────────────
    {"id": "cartoonbusters-021", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. More animated films. All phonetic.", "prize": "Email in. Winner gets a plush toy of a character from a film they haven't seen.",
     "clues": [
         {"number": 1, "initials": "B", "clue": "A young female who is very brave — goes off into the Scottish highlands and causes a lot of trouble.", "answer": "Brave", "aliases": ["brave"], "reasoning": "Brave (courageous/the Pixar film) = Brave"},
         {"number": 2, "initials": "T", "clue": "A long-haired girl in a tower — goes out, causes chaos, and eventually gets a haircut.", "answer": "Tangled", "aliases": ["tangled"], "reasoning": "Tangled (knotted/the Rapunzel film) = Tangled"},
         {"number": 3, "initials": "E", "clue": "A film in Spanish — a family with magical powers lives in a house that's also magical.", "answer": "Encanto", "aliases": ["encanto"], "reasoning": "Encanto (enchanted in Spanish) = Encanto"},
     ]},
    {"id": "cartoonbusters-022", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more animated films.", "prize": "Email in. Winner gets a colouring book of a film nobody remembers.",
     "clues": [
         {"number": 1, "initials": "O", "clue": "Something happening in a vehicle moving forward — gone all Pixar and started involving emotions as characters.", "answer": "Onward", "aliases": ["onward"], "reasoning": "Onward (moving forward/the Pixar film) = Onward"},
         {"number": 2, "initials": "S", "clue": "A state of being — gone all jazz and started following a music teacher into the afterlife.", "answer": "Soul", "aliases": ["soul"], "reasoning": "Soul (spirit/the Pixar film) = Soul"},
         {"number": 3, "initials": "T R", "clue": "A young female panda — gone all red and started embarrassing her mother.", "answer": "Turning Red", "aliases": ["turning red"], "reasoning": "Turning + Red = Turning Red"},
     ]},
    {"id": "cartoonbusters-023", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more cartoons.", "prize": "Email in. Winner gets a sequel to a film that didn't need one.",
     "clues": [
         {"number": 1, "initials": "D M", "clue": "A bloke who is very bad — gone all minion-shaped and started trying to steal the moon.", "answer": "Despicable Me", "aliases": ["despicable me"], "reasoning": "Despicable (contemptible) + Me = Despicable Me"},
         {"number": 2, "initials": "K F P", "clue": "A large black and white bear — gone all martial arts and started kicking things impressively.", "answer": "Kung Fu Panda", "aliases": ["kung fu panda"], "reasoning": "Kung Fu (martial art) + Panda (the bear) = Kung Fu Panda"},
         {"number": 3, "initials": "H T T Y D", "clue": "A guide for taming a fire-breathing creature — a boy manages it despite everyone's advice.", "answer": "How to Train Your Dragon", "aliases": ["how to train your dragon"], "reasoning": "How + to + Train + Your + Dragon = How to Train Your Dragon"},
     ]},
    {"id": "cartoonbusters-024", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. More animated classics.", "prize": "Email in. Winner gets a sing-along version nobody asked for.",
     "clues": [
         {"number": 1, "initials": "T S 2", "clue": "Children's playthings — gone all cinematic and started having adventures without the boy.", "answer": "Toy Story 2", "aliases": ["toy story 2"], "reasoning": "Toy + Story + 2 = Toy Story 2"},
         {"number": 2, "initials": "T S 3", "clue": "Children's playthings — gone all emotional and started going to university.", "answer": "Toy Story 3", "aliases": ["toy story 3"], "reasoning": "Toy + Story + 3 = Toy Story 3"},
         {"number": 3, "initials": "M", "clue": "A large island with dancing lemurs — a lion, a hippo, a giraffe, and a zebra visit.", "answer": "Madagascar", "aliases": ["madagascar"], "reasoning": "Madagascar (the island/the animated film) = Madagascar"},
     ]},
    {"id": "cartoonbusters-025", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more animated films.", "prize": "Email in. Winner gets a Blu-ray with a bonus disc that's just the trailer.",
     "clues": [
         {"number": 1, "initials": "S", "clue": "Music — gone all competitive and started featuring animated creatures singing their hearts out.", "answer": "Sing", "aliases": ["sing"], "reasoning": "Sing (to make music vocally/the film) = Sing"},
         {"number": 2, "initials": "T", "clue": "Small colourful creatures with big hair — gone all musical and started trying to be happy.", "answer": "Trolls", "aliases": ["trolls"], "reasoning": "Trolls (mythological creatures/the film) = Trolls"},
         {"number": 3, "initials": "B B", "clue": "An infant — gone all suited and started managing a corporation of babies.", "answer": "Boss Baby", "aliases": ["boss baby"], "reasoning": "Boss (in charge) + Baby (infant) = Boss Baby"},
     ]},
    {"id": "cartoonbusters-026", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more cartoons.", "prize": "Email in. Winner gets an animated short before the main feature.",
     "clues": [
         {"number": 1, "initials": "T I 2", "clue": "A group of exceptional people — gone all retired and started fighting again.", "answer": "The Incredibles 2", "aliases": ["the incredibles 2", "incredibles 2"], "reasoning": "The + Incredibles + 2 = The Incredibles 2"},
         {"number": 2, "initials": "R", "clue": "A place for cooking in a French kitchen — gone all rat-shaped and started making gourmet food.", "answer": "Ratatouille", "aliases": ["ratatouille"], "reasoning": "Ratatouille (French dish/Pixar film) = Ratatouille"},
         {"number": 3, "initials": "L", "clue": "A small battery-powered toy — gone all space age and started having an identity crisis.", "answer": "Lightyear", "aliases": ["lightyear"], "reasoning": "Light (not heavy/the toy) + year = Lightyear"},
     ]},
    {"id": "cartoonbusters-027", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more animated films. All phonetic.", "prize": "Email in. Winner gets a cinema loyalty card for a cinema that's closed.",
     "clues": [
         {"number": 1, "initials": "W W", "clue": "A small cylindrical robot — gone all lonely and started collecting rubbish on an abandoned Earth.", "answer": "WALL-E", "aliases": ["wall-e", "walle", "wall e"], "reasoning": "WALL-E (Waste Allocation Load Lifter Earth-class) = WALL-E"},
         {"number": 2, "initials": "U", "clue": "A direction — gone all Pixar and involved a house flying away on balloons.", "answer": "Up", "aliases": ["up"], "reasoning": "Up (a direction/the Pixar film) = Up"},
         {"number": 3, "initials": "M I", "clue": "A company that frightens people for a living — turns out the monsters are scared too.", "answer": "Monsters Inc", "aliases": ["monsters inc", "monsters inc."], "reasoning": "Monsters (scary creatures) + Inc (incorporated) = Monsters Inc"},
     ]},
    {"id": "cartoonbusters-028", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three more.", "prize": "Email in. Winner gets a signed cel from a film that was done on computers.",
     "clues": [
         {"number": 1, "initials": "T L M", "clue": "A young female fish — gone all curious about the surface world and started collecting forks.", "answer": "The Little Mermaid", "aliases": ["the little mermaid"], "reasoning": "The + Little + Mermaid (half-fish creature) = The Little Mermaid"},
         {"number": 2, "initials": "T E N G", "clue": "A royal who is also very silly — loses his kingdom through his own stupidity.", "answer": "The Emperor's New Groove", "aliases": ["the emperor's new groove", "the emperors new groove"], "reasoning": "The + Emperor's + New + Groove = The Emperor's New Groove"},
         {"number": 3, "initials": "L A S", "clue": "Two small Hawaiian people — one of them is an alien and causes nothing but trouble.", "answer": "Lilo and Stitch", "aliases": ["lilo and stitch"], "reasoning": "Lilo (an inflatable mattress/a name) + and + Stitch = Lilo and Stitch"},
     ]},
    {"id": "cartoonbusters-029", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Almost done with the animations.", "prize": "Email in. Winner gets a 3D glasses headache and a stiff neck.",
     "clues": [
         {"number": 1, "initials": "H", "clue": "A Greek demigod — gone all muscles and started having adventures while a gospel choir narrates.", "answer": "Hercules", "aliases": ["hercules"], "reasoning": "Hercules (the Greek hero) = Hercules"},
         {"number": 2, "initials": "M", "clue": "A Chinese soldier's daughter — pretends to be a man to save her father from war.", "answer": "Mulan", "aliases": ["mulan"], "reasoning": "Mulan (the Chinese heroine) = Mulan"},
         {"number": 3, "initials": "T", "clue": "A man raised by apes in the jungle — very good at swinging between trees.", "answer": "Tarzan", "aliases": ["tarzan"], "reasoning": "Tarzan (the jungle man) = Tarzan"},
     ]},
    {"id": "cartoonbusters-030", "enabled": True, "title": "Cartoon Busters", "topic": "animated films", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Cartoon Busters. Three final animations.", "prize": "Email in. Winner gets the animatic and absolutely nothing else.",
     "clues": [
         {"number": 1, "initials": "R A T D", "clue": "A young island girl — goes off to sea and has to find a demigod to save everyone.", "answer": "Moana", "aliases": ["moana"], "reasoning": "Moana (the Polynesian heroine) = Moana"},
         {"number": 2, "initials": "P", "clue": "A wooden puppet — really wants to be a real boy and tells lies with a growing nose.", "answer": "Pinocchio", "aliases": ["pinocchio"], "reasoning": "Pinocchio (the puppet/the Disney film) = Pinocchio"},
         {"number": 3, "initials": "B A T B", "clue": "A very beautiful female — falls for a large hairy creature that turns out to be a prince.", "answer": "Beauty and the Beast", "aliases": ["beauty and the beast"], "reasoning": "Beauty + and + the + Beast = Beauty and the Beast"},
     ]},
    # ── History Busters +10 (021-030) ─────────────────────────────────────────
    {"id": "historybusters-021", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. More famous figures from history. All phonetic.", "prize": "Email in. Winner gets a Wikipedia page that needs citations.",
     "clues": [
         {"number": 1, "initials": "N M", "clue": "A bloke called Nelson — went to prison, came out, and changed an entire country for the better.", "answer": "Nelson Mandela", "aliases": ["nelson mandela"], "reasoning": "Nelson (a name) + Mandela (a name) = Nelson Mandela"},
         {"number": 2, "initials": "A L", "clue": "A very tall honest bloke from America — had a hat, a beard, and freed a lot of people.", "answer": "Abraham Lincoln", "aliases": ["abraham lincoln"], "reasoning": "Abraham (a name) + Lincoln (a city/a car) = Abraham Lincoln"},
         {"number": 3, "initials": "G W", "clue": "A bloke who chopped down a cherry tree — became the first president of a very large country.", "answer": "George Washington", "aliases": ["george washington"], "reasoning": "George (a name) + Washington (a place/a name) = George Washington"},
     ]},
    {"id": "historybusters-022", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK"],
     "intro": "History Busters. Three more from the history books.", "prize": "Email in. Winner gets a dated encyclopaedia and a smug expression.",
     "clues": [
         {"number": 1, "initials": "Q V", "clue": "A female ruler — gone all diamond jubilee and started wearing black for forty years.", "answer": "Queen Victoria", "aliases": ["queen victoria"], "reasoning": "Queen (female ruler) + Victoria (a name) = Queen Victoria"},
         {"number": 2, "initials": "F N", "clue": "A lamp — gone all nursing and started improving hospital conditions during a war.", "answer": "Florence Nightingale", "aliases": ["florence nightingale"], "reasoning": "Florence (a city/a name) + Nightingale (a bird that sings at night) = Florence Nightingale"},
         {"number": 3, "initials": "C D", "clue": "A bloke who writes things down — gone all Victorian and started inventing street urchins.", "answer": "Charles Dickens", "aliases": ["charles dickens"], "reasoning": "Charles (a name) + Dickens (a name) = Charles Dickens"},
     ]},
    {"id": "historybusters-023", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. Three more great figures.", "prize": "Email in. Winner gets a history lesson they didn't ask for.",
     "clues": [
         {"number": 1, "initials": "M P", "clue": "A Venetian traveller — went all the way to China and wrote a very long book about it.", "answer": "Marco Polo", "aliases": ["marco polo"], "reasoning": "Marco (a name) + Polo (a sport/a name) = Marco Polo"},
         {"number": 2, "initials": "L D V", "clue": "A bloke who painted a woman smiling mysteriously and also designed flying machines that didn't work.", "answer": "Leonardo da Vinci", "aliases": ["leonardo da vinci"], "reasoning": "Leonardo (a name) + da + Vinci (from Vinci) = Leonardo da Vinci"},
         {"number": 3, "initials": "G G", "clue": "A bloke who looked through a tube at the sky and got in trouble for saying the Earth goes round the Sun.", "answer": "Galileo Galilei", "aliases": ["galileo galilei", "galileo"], "reasoning": "Galileo + Galilei = Galileo Galilei"},
     ]},
    {"id": "historybusters-024", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. More historical figures.", "prize": "Email in. Winner gets a bronze plaque with the wrong dates on it.",
     "clues": [
         {"number": 1, "initials": "J C", "clue": "Crossing a piece of water — gone all Roman and started stabbing his friends in the senate.", "answer": "Julius Caesar", "aliases": ["julius caesar"], "reasoning": "Julius (a name) + Caesar (a name/Roman emperor) = Julius Caesar"},
         {"number": 2, "initials": "C", "clue": "An Egyptian queen — had a nose that supposedly changed the course of history.", "answer": "Cleopatra", "aliases": ["cleopatra"], "reasoning": "Cleopatra (the Egyptian queen) = Cleopatra"},
         {"number": 3, "initials": "A T H", "clue": "A warrior on horseback — went all nomadic and started conquering most of Europe and Asia.", "answer": "Attila the Hun", "aliases": ["attila the hun"], "reasoning": "Attila (a name) + the + Hun (a nomadic people) = Attila the Hun"},
     ]},
    {"id": "historybusters-025", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. Three more. All from the textbooks.", "prize": "Email in. Winner gets a footnote in a book nobody reads.",
     "clues": [
         {"number": 1, "initials": "N B", "clue": "A short French bloke — went all general and started invading things. Very keen on hats.", "answer": "Napoleon Bonaparte", "aliases": ["napoleon bonaparte"], "reasoning": "Napoleon (a name) + Bonaparte (a name) = Napoleon Bonaparte"},
         {"number": 2, "initials": "G K", "clue": "A bloke on horseback — went all Mongolian and conquered most of the known world.", "answer": "Genghis Khan", "aliases": ["genghis khan"], "reasoning": "Genghis (a name) + Khan (a title/leader) = Genghis Khan"},
         {"number": 3, "initials": "A T G", "clue": "A bloke called Alex — went all Greek and started conquering everything from Egypt to India.", "answer": "Alexander the Great", "aliases": ["alexander the great"], "reasoning": "Alexander + the + Great = Alexander the Great"},
     ]},
    {"id": "historybusters-026", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK"],
     "intro": "History Busters. More British history.", "prize": "Email in. Winner gets a commemorative mug with a chip in it.",
     "clues": [
         {"number": 1, "initials": "H V I I I", "clue": "A Tudor monarch — had six wives and kept losing patience with them. Very fond of his dinner.", "answer": "Henry VIII", "aliases": ["henry viii", "henry the eighth"], "reasoning": "Henry (a name) + VIII (the eighth) = Henry VIII"},
         {"number": 2, "initials": "E I", "clue": "A female monarch — went all Tudor and started defeating the Spanish Armada.", "answer": "Elizabeth I", "aliases": ["elizabeth i", "elizabeth the first"], "reasoning": "Elizabeth (a name) + I (the first) = Elizabeth I"},
         {"number": 3, "initials": "W T C", "clue": "A French duke who sailed across to England and won a very important battle.", "answer": "William the Conqueror", "aliases": ["william the conqueror"], "reasoning": "William + the + Conqueror = William the Conqueror"},
     ]},
    {"id": "historybusters-027", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. Three more. All famous names.", "prize": "Email in. Winner gets a history podcast that's eighty hours long.",
     "clues": [
         {"number": 1, "initials": "C C", "clue": "A navigator — went all sailing and accidentally discovered somewhere he wasn't looking for.", "answer": "Christopher Columbus", "aliases": ["christopher columbus"], "reasoning": "Christopher (a name) + Columbus (a name/a city) = Christopher Columbus"},
         {"number": 2, "initials": "O C", "clue": "A bloke from Ireland — went all Puritan and started chopping off the king's head.", "answer": "Oliver Cromwell", "aliases": ["oliver cromwell"], "reasoning": "Oliver (a name) + Cromwell (a name) = Oliver Cromwell"},
         {"number": 3, "initials": "M Q O S", "clue": "A Scottish female monarch — things didn't end well. Very tragic.", "answer": "Mary Queen of Scots", "aliases": ["mary queen of scots"], "reasoning": "Mary + Queen + of + Scots = Mary Queen of Scots"},
     ]},
    {"id": "historybusters-028", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. Three more historical names.", "prize": "Email in. Winner gets a primary school project about the Romans.",
     "clues": [
         {"number": 1, "initials": "J S", "clue": "A Soviet leader — went all steely and started running a very large cold country.", "answer": "Joseph Stalin", "aliases": ["joseph stalin"], "reasoning": "Joseph (a name) + Stalin (steel in Russian) = Joseph Stalin"},
         {"number": 2, "initials": "A H", "clue": "A failed Austrian artist — went all dictator and caused the worst war in history.", "answer": "Adolf Hitler", "aliases": ["adolf hitler"], "reasoning": "Adolf (a name) + Hitler (a name) = Adolf Hitler"},
         {"number": 3, "initials": "A E", "clue": "A very clever bloke — had wild hair, worked out that energy equals mass times the speed of light squared.", "answer": "Albert Einstein", "aliases": ["albert einstein"], "reasoning": "Albert (a name) + Einstein (a name) = Albert Einstein"},
     ]},
    {"id": "historybusters-029", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK"],
     "intro": "History Busters. Three more. All from history.", "prize": "Email in. Winner gets a bronze age artefact and no context.",
     "clues": [
         {"number": 1, "initials": "R T L H", "clue": "A crusading king — went all lion-hearted and spent most of his reign abroad.", "answer": "Richard the Lionheart", "aliases": ["richard the lionheart"], "reasoning": "Richard + the + Lionheart (brave as a lion) = Richard the Lionheart"},
         {"number": 2, "initials": "I N", "clue": "An apple fell on his head — went all gravity and started explaining why things fall down.", "answer": "Isaac Newton", "aliases": ["isaac newton"], "reasoning": "Isaac (a name) + Newton (a name/unit of force) = Isaac Newton"},
         {"number": 3, "initials": "C D", "clue": "A bloke on a boat — went to the Galapagos and came back saying everything was related to everything else.", "answer": "Charles Darwin", "aliases": ["charles darwin"], "reasoning": "Charles (a name) + Darwin (a name/city in Australia) = Charles Darwin"},
     ]},
    {"id": "historybusters-030", "enabled": True, "title": "History Busters", "topic": "famous historical figures", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "History Busters. Three final historical figures.", "prize": "Email in. Winner gets a history GCSE they didn't revise for.",
     "clues": [
         {"number": 1, "initials": "W C", "clue": "A statesman who gave speeches during the war — very good with words, very fond of cigars.", "answer": "Winston Churchill", "aliases": ["winston churchill"], "reasoning": "Winston (a name) + Churchill (church + hill) = Winston Churchill"},
         {"number": 2, "initials": "G G", "clue": "An Italian bloke — went all astronomy and looked at the sky until the church told him to stop.", "answer": "Galileo Galilei", "aliases": ["galileo galilei", "galileo"], "reasoning": "Galileo + Galilei = Galileo Galilei"},
         {"number": 3, "initials": "A T H", "clue": "A fierce horseman — went all nomadic and terrorised Europe until he ran out of places to conquer.", "answer": "Attila the Hun", "aliases": ["attila the hun"], "reasoning": "Attila + the + Hun = Attila the Hun"},
     ]},
    # ── Holiday Busters +10 (021-030) ─────────────────────────────────────────
    {"id": "holidaybusters-021", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. More destinations. All phonetic.", "prize": "Email in. Winner gets a suitcase with a broken wheel.",
     "clues": [
         {"number": 1, "initials": "S", "clue": "A group of Greek islands — very beautiful, very blue, very expensive since someone did a travel piece on them.", "answer": "Santorini", "aliases": ["santorini"], "reasoning": "Santorini (Greek island) = Santorini"},
         {"number": 2, "initials": "M", "clue": "A series of small sandy islands in the Indian Ocean — very turquoise, very expensive, very remote.", "answer": "Maldives", "aliases": ["maldives", "the maldives"], "reasoning": "Maldives (the island nation) = Maldives"},
         {"number": 3, "initials": "C", "clue": "A region of Mexico with very white beaches — popular with people who want to drink cocktails on sand.", "answer": "Cancun", "aliases": ["cancun"], "reasoning": "Cancun (Mexican resort city) = Cancun"},
     ]},
    {"id": "holidaybusters-022", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more destinations.", "prize": "Email in. Winner gets a hotel room that smells of other people.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A Thai island — very popular, very busy, full of people who thought it would be quiet.", "answer": "Phuket", "aliases": ["phuket"], "reasoning": "Phuket (Thai island) = Phuket"},
         {"number": 2, "initials": "M", "clue": "A Greek island — very fashionable, very white, windmills everywhere.", "answer": "Mykonos", "aliases": ["mykonos"], "reasoning": "Mykonos (Greek island) = Mykonos"},
         {"number": 3, "initials": "B B", "clue": "A French Polynesian island — so beautiful it barely seems real. Very good for honeymoons.", "answer": "Bora Bora", "aliases": ["bora bora"], "reasoning": "Bora + Bora = Bora Bora"},
     ]},
    {"id": "holidaybusters-023", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three UK destinations.", "prize": "Email in. Winner gets a weekend in a caravan with intermittent rain.",
     "clues": [
         {"number": 1, "initials": "C", "clue": "The most south-westerly bit of England — beautiful coast, cream teas, very long drive to get there.", "answer": "Cornwall", "aliases": ["cornwall"], "reasoning": "Cornwall (the UK county) = Cornwall"},
         {"number": 2, "initials": "L D", "clue": "A region in the north of England — lots of lakes, lots of poets, lots of drizzle.", "answer": "Lake District", "aliases": ["lake district", "the lake district"], "reasoning": "Lake + District = Lake District"},
         {"number": 3, "initials": "S H", "clue": "The northern part of Scotland — mountains, lochs, midges, and tourists in waterproofs.", "answer": "Scottish Highlands", "aliases": ["scottish highlands", "the highlands"], "reasoning": "Scottish + Highlands = Scottish Highlands"},
     ]},
    {"id": "holidaybusters-024", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. More UK and European destinations.", "prize": "Email in. Winner gets a tourist information leaflet from 2003.",
     "clues": [
         {"number": 1, "initials": "D", "clue": "A place in the south of England — famous for white cliffs and looking at France.", "answer": "Devon", "aliases": ["devon"], "reasoning": "Devon (the UK county) = Devon"},
         {"number": 2, "initials": "D", "clue": "A coastal county famous for its coast and being a bit smug about it.", "answer": "Dorset", "aliases": ["dorset"], "reasoning": "Dorset (the UK county) = Dorset"},
         {"number": 3, "initials": "N F", "clue": "A forested area in southern England — deer, ponies, and people on bicycles.", "answer": "New Forest", "aliases": ["new forest", "the new forest"], "reasoning": "New + Forest = New Forest"},
     ]},
    {"id": "holidaybusters-025", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more destinations.", "prize": "Email in. Winner gets a passport that expired six months ago.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A long thin country in South America — next to the sea, very mountainous.", "answer": "Peru", "aliases": ["peru"], "reasoning": "Peru (South American country) = Peru"},
         {"number": 2, "initials": "C R", "clue": "A Central American country — very green, lots of wildlife, people go there to look at things.", "answer": "Costa Rica", "aliases": ["costa rica"], "reasoning": "Costa (coast in Spanish) + Rica (rich) = Costa Rica"},
         {"number": 3, "initials": "T", "clue": "A Southeast Asian country — very cheap, very hot, beautiful temples everywhere.", "answer": "Thailand", "aliases": ["thailand"], "reasoning": "Thailand (the country) = Thailand"},
     ]},
    {"id": "holidaybusters-026", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more. All destinations.", "prize": "Email in. Winner gets a delayed flight and a voucher for the airport Wetherspoons.",
     "clues": [
         {"number": 1, "initials": "N", "clue": "A county in the east of England — very flat, very wide skies, lots of broads.", "answer": "Norfolk", "aliases": ["norfolk"], "reasoning": "Norfolk (the UK county) = Norfolk"},
         {"number": 2, "initials": "P D", "clue": "A hilly region in the Midlands — popular with walkers who like to look at things from heights.", "answer": "Peak District", "aliases": ["peak district", "the peak district"], "reasoning": "Peak + District = Peak District"},
         {"number": 3, "initials": "Y", "clue": "A large county in the north of England — very proud of itself and its puddings.", "answer": "Yorkshire", "aliases": ["yorkshire"], "reasoning": "Yorkshire (the UK county) = Yorkshire"},
     ]},
    {"id": "holidaybusters-027", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more holiday spots.", "prize": "Email in. Winner gets a travel plug adapter for the wrong country.",
     "clues": [
         {"number": 1, "initials": "D", "clue": "A Croatian city on the coast — very old walls, very popular with people who like Game of Thrones.", "answer": "Dubrovnik", "aliases": ["dubrovnik"], "reasoning": "Dubrovnik (Croatian city) = Dubrovnik"},
         {"number": 2, "initials": "P", "clue": "A Portuguese city full of people drinking port and going up hills on trams.", "answer": "Porto", "aliases": ["porto"], "reasoning": "Porto (Portuguese city) = Porto"},
         {"number": 3, "initials": "P", "clue": "A coastal town on the French Riviera — very glamorous, very warm, very full of yachts.", "answer": "Positano", "aliases": ["positano"], "reasoning": "Positano (Italian coastal town) = Positano"},
     ]},
    {"id": "holidaybusters-028", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more destinations.", "prize": "Email in. Winner gets a travel insurance claim that takes eighteen months.",
     "clues": [
         {"number": 1, "initials": "B", "clue": "An Indonesian island — very spiritual, very beautiful, rice paddies everywhere.", "answer": "Bali", "aliases": ["bali"], "reasoning": "Bali (Indonesian island) = Bali"},
         {"number": 2, "initials": "J", "clue": "A Caribbean island — reggae music, Blue Mountains, beaches everywhere.", "answer": "Jamaica", "aliases": ["jamaica"], "reasoning": "Jamaica (Caribbean island) = Jamaica"},
         {"number": 3, "initials": "B", "clue": "A Caribbean island — cricket mad, very colonial, very beautiful.", "answer": "Barbados", "aliases": ["barbados"], "reasoning": "Barbados (Caribbean island) = Barbados"},
     ]},
    {"id": "holidaybusters-029", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three more destinations.", "prize": "Email in. Winner gets a souvenir that breaks on the way home.",
     "clues": [
         {"number": 1, "initials": "C", "clue": "A large island in the Mediterranean — very Greek, very mountainous, very popular.", "answer": "Crete", "aliases": ["crete"], "reasoning": "Crete (Greek island) = Crete"},
         {"number": 2, "initials": "C", "clue": "A small island in the Mediterranean — British for a very long time, very hot.", "answer": "Cyprus", "aliases": ["cyprus"], "reasoning": "Cyprus (Mediterranean island) = Cyprus"},
         {"number": 3, "initials": "M", "clue": "A small island nation in the middle of the Mediterranean — Knights Hospitaller, very old buildings.", "answer": "Malta", "aliases": ["malta"], "reasoning": "Malta (the island nation) = Malta"},
     ]},
    {"id": "holidaybusters-030", "enabled": True, "title": "Holiday Busters", "topic": "holiday destinations", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Holiday Busters. Three final destinations.", "prize": "Email in. Winner gets the middle seat on a long-haul flight.",
     "clues": [
         {"number": 1, "initials": "I", "clue": "A Spanish island — famous for nightclubs, sunburn, and people who should know better.", "answer": "Ibiza", "aliases": ["ibiza"], "reasoning": "Ibiza (Spanish party island) = Ibiza"},
         {"number": 2, "initials": "T", "clue": "A long thin island off the coast of Spain — Alcudia, Palma, loads of British tourists.", "answer": "Tenerife", "aliases": ["tenerife"], "reasoning": "Tenerife (Canary Island) = Tenerife"},
         {"number": 3, "initials": "G C", "clue": "A Spanish island — sand dunes, beaches, and people reading crime novels.", "answer": "Gran Canaria", "aliases": ["gran canaria"], "reasoning": "Gran (great in Spanish) + Canaria (from Canaries) = Gran Canaria"},
     ]},
    # ── Game Busters +10 (021-030) ─────────────────────────────────────────────
    {"id": "gamebusters-021", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. More games. All phonetic.", "prize": "Email in. Winner gets a controller with a sticky thumbstick.",
     "clues": [
         {"number": 1, "initials": "T L O U", "clue": "A zombie apocalypse — someone's trying to get a young girl from one side of America to the other.", "answer": "The Last of Us", "aliases": ["the last of us"], "reasoning": "The + Last + of + Us = The Last of Us"},
         {"number": 2, "initials": "G O W", "clue": "A deity of fighting — going around killing other gods and getting very angry about things.", "answer": "God of War", "aliases": ["god of war"], "reasoning": "God (a deity) + of + War (conflict) = God of War"},
         {"number": 3, "initials": "R D R", "clue": "A cowboy on a horse — going around the Wild West doing morally questionable things.", "answer": "Red Dead Redemption", "aliases": ["red dead redemption"], "reasoning": "Red + Dead + Redemption = Red Dead Redemption"},
     ]},
    {"id": "gamebusters-022", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more games.", "prize": "Email in. Winner gets a game that requires a day-one patch.",
     "clues": [
         {"number": 1, "initials": "A C", "clue": "A murderer in a hood — going around historical cities stabbing people from great heights.", "answer": "Assassin's Creed", "aliases": ["assassin's creed", "assassins creed"], "reasoning": "Assassin's (belonging to an assassin) + Creed (a set of beliefs) = Assassin's Creed"},
         {"number": 2, "initials": "T S", "clue": "A pretend family — you build their house, control their lives, and generally make things miserable.", "answer": "The Sims", "aliases": ["the sims"], "reasoning": "The + Sims (simulations/the game) = The Sims"},
         {"number": 3, "initials": "C C", "clue": "Sweets on a phone screen — matching coloured things in rows. Extremely addictive.", "answer": "Candy Crush", "aliases": ["candy crush"], "reasoning": "Candy (sweets) + Crush (to crush/match) = Candy Crush"},
     ]},
    {"id": "gamebusters-023", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more. All phonetic.", "prize": "Email in. Winner gets a gaming chair that broke after two weeks.",
     "clues": [
         {"number": 1, "initials": "A B", "clue": "Creatures that are very cross — being launched from a catapult at structures built by pigs.", "answer": "Angry Birds", "aliases": ["angry birds"], "reasoning": "Angry (cross/annoyed) + Birds = Angry Birds"},
         {"number": 2, "initials": "A U", "clue": "People on a spaceship — some of them are saboteurs, you have to figure out which ones.", "answer": "Among Us", "aliases": ["among us"], "reasoning": "Among (in the middle of) + Us = Among Us"},
         {"number": 3, "initials": "O", "clue": "A shooting game — go around with other players, build things, and fall out of a flying bus.", "answer": "Overwatch", "aliases": ["overwatch"], "reasoning": "Overwatch (to watch over/the game) = Overwatch"},
     ]},
    {"id": "gamebusters-024", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more games.", "prize": "Email in. Winner gets a save file from level 47 of a game they've never played.",
     "clues": [
         {"number": 1, "initials": "W", "clue": "A five-letter word guessing game — everyone plays it at breakfast and argues about it.", "answer": "Wordle", "aliases": ["wordle"], "reasoning": "Wordle (word + -le suffix, the daily word game) = Wordle"},
         {"number": 2, "initials": "R", "clue": "A large platform used for creative construction — millions of people playing in a blocky world.", "answer": "Roblox", "aliases": ["roblox"], "reasoning": "Roblox (Rob + blocks/the game) = Roblox"},
         {"number": 3, "initials": "L O L", "clue": "A competitive online arena — five players fight five others with fictional characters.", "answer": "League of Legends", "aliases": ["league of legends"], "reasoning": "League + of + Legends = League of Legends"},
     ]},
    {"id": "gamebusters-025", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more. All from gaming.", "prize": "Email in. Winner gets a loot box with nothing good in it.",
     "clues": [
         {"number": 1, "initials": "C 2", "clue": "A futuristic city — gone all dystopian and a bloke with implants drives around causing chaos.", "answer": "Cyberpunk 2077", "aliases": ["cyberpunk 2077", "cyberpunk"], "reasoning": "Cyberpunk + 2077 = Cyberpunk 2077"},
         {"number": 2, "initials": "H", "clue": "A ring — gone all military and started involving a group of soldiers in green armour fighting aliens.", "answer": "Halo", "aliases": ["halo"], "reasoning": "Halo (a ring of light/the game) = Halo"},
         {"number": 3, "initials": "P", "clue": "An underground walkway for pipes — gone all physics-based and started involving a woman called Chell.", "answer": "Portal", "aliases": ["portal"], "reasoning": "Portal (a doorway/the game) = Portal"},
     ]},
    {"id": "gamebusters-026", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more games.", "prize": "Email in. Winner gets a gaming headset that only picks up everyone else's breathing.",
     "clues": [
         {"number": 1, "initials": "R E", "clue": "A large old house — gone all zombies and started requiring a lot of puzzle solving.", "answer": "Resident Evil", "aliases": ["resident evil"], "reasoning": "Resident (one who lives somewhere) + Evil = Resident Evil"},
         {"number": 2, "initials": "M K", "clue": "A combat game — very violent, everyone does finishing moves nobody should describe.", "answer": "Mortal Kombat", "aliases": ["mortal kombat"], "reasoning": "Mortal (capable of dying) + Kombat (combat) = Mortal Kombat"},
         {"number": 3, "initials": "S F", "clue": "A fighting competition on a road — people in colourful outfits punch each other.", "answer": "Street Fighter", "aliases": ["street fighter"], "reasoning": "Street + Fighter = Street Fighter"},
     ]},
    {"id": "gamebusters-027", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more. All gaming classics.", "prize": "Email in. Winner gets a game over screen and no continue option.",
     "clues": [
         {"number": 1, "initials": "S T H", "clue": "A blue creature — goes very fast, collects rings, hates a fat scientist with a moustache.", "answer": "Sonic the Hedgehog", "aliases": ["sonic the hedgehog", "sonic"], "reasoning": "Sonic (sound/fast) + the + Hedgehog = Sonic the Hedgehog"},
         {"number": 2, "initials": "T R", "clue": "A female archaeologist — goes into old tombs and shoots things.", "answer": "Tomb Raider", "aliases": ["tomb raider"], "reasoning": "Tomb (burial chamber) + Raider (one who raids) = Tomb Raider"},
         {"number": 3, "initials": "Z", "clue": "An elf in a green tunic — goes around collecting triangles and saving a princess.", "answer": "Zelda", "aliases": ["zelda", "the legend of zelda"], "reasoning": "Zelda (the princess/the game series) = Zelda"},
     ]},
    {"id": "gamebusters-028", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more games.", "prize": "Email in. Winner gets a character skin that makes them look worse.",
     "clues": [
         {"number": 1, "initials": "M", "clue": "A property board game — involves buying streets, building hotels, and ruining relationships.", "answer": "Monopoly", "aliases": ["monopoly"], "reasoning": "Monopoly (exclusive control/the board game) = Monopoly"},
         {"number": 2, "initials": "S", "clue": "A word game — seven tiles, a board, a dictionary argument, and a family row.", "answer": "Scrabble", "aliases": ["scrabble"], "reasoning": "Scrabble (to scramble/the word game) = Scrabble"},
         {"number": 3, "initials": "T P", "clue": "A quiz game in a pie shape — a wedge for every category, complete arguments over geography.", "answer": "Trivial Pursuit", "aliases": ["trivial pursuit"], "reasoning": "Trivial (insignificant) + Pursuit (a chase) = Trivial Pursuit"},
     ]},
    {"id": "gamebusters-029", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three more.", "prize": "Email in. Winner gets a battle pass that expires before they can use it.",
     "clues": [
         {"number": 1, "initials": "F", "clue": "A survival game — drop onto a large island, find weapons, be the last one standing.", "answer": "Fortnite", "aliases": ["fortnite"], "reasoning": "Fortnite (two weeks/the game) = Fortnite"},
         {"number": 2, "initials": "M", "clue": "A blocky world — dig, build, craft, survive the night when everything comes to kill you.", "answer": "Minecraft", "aliases": ["minecraft"], "reasoning": "Mine (to dig) + craft (to make) = Minecraft"},
         {"number": 3, "initials": "G T A", "clue": "A car-themed crime game — go around a city causing chaos and avoiding police.", "answer": "Grand Theft Auto", "aliases": ["grand theft auto", "gta"], "reasoning": "Grand (large/serious) + Theft + Auto = Grand Theft Auto"},
     ]},
    {"id": "gamebusters-030", "enabled": True, "title": "Game Busters", "topic": "video games and board games", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Game Busters. Three final games.", "prize": "Email in. Winner gets an achievement nobody will ever see.",
     "clues": [
         {"number": 1, "initials": "D K", "clue": "A large ape — throws barrels at a little man trying to climb up to rescue someone.", "answer": "Donkey Kong", "aliases": ["donkey kong"], "reasoning": "Donkey (a stubborn animal) + Kong (a large ape) = Donkey Kong"},
         {"number": 2, "initials": "P M", "clue": "A circular yellow creature — eats dots, avoids ghosts, been doing it since 1980.", "answer": "Pac-Man", "aliases": ["pac-man", "pacman"], "reasoning": "Pac (from 'paku-paku', Japanese for chomping) + Man = Pac-Man"},
         {"number": 3, "initials": "C O D", "clue": "A military fish — gone all first-person shooter and started having very serious conversations over headsets.", "answer": "Call of Duty", "aliases": ["call of duty"], "reasoning": "Call + of + Duty (obligation) = Call of Duty"},
     ]},
    # ── Food Busters +10 (041-050) ─────────────────────────────────────────────
    {"id": "foodbusters-041", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Food Busters. More dishes. All phonetic.", "prize": "Email in. Winner gets a takeaway that arrives an hour late.",
     "clues": [
         {"number": 1, "initials": "F E", "clue": "A full morning meal — bacon, eggs, sausage, beans, everything. Very British. Very excessive.", "answer": "Full English", "aliases": ["full english", "full english breakfast"], "reasoning": "Full (complete) + English (from England) = Full English"},
         {"number": 2, "initials": "T I T H", "clue": "Sausages — submerged inside a Yorkshire pudding. Very British.", "answer": "Toad in the Hole", "aliases": ["toad in the hole"], "reasoning": "Toad + in + the + Hole = Toad in the Hole"},
         {"number": 3, "initials": "B A M", "clue": "Cylindrical meat products — accompanied by mashed potato. Very comforting.", "answer": "Bangers and Mash", "aliases": ["bangers and mash"], "reasoning": "Bangers (sausages) + and + Mash (mashed potato) = Bangers and Mash"},
     ]},
    {"id": "foodbusters-042", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Food Busters. Three more dishes.", "prize": "Email in. Winner gets a restaurant booking for the wrong day.",
     "clues": [
         {"number": 1, "initials": "C P", "clue": "A pastry shaped like a half-moon — filled with meat and vegetables, from the far south-west of England.", "answer": "Cornish Pasty", "aliases": ["cornish pasty"], "reasoning": "Cornish (from Cornwall) + Pasty (a pastry parcel) = Cornish Pasty"},
         {"number": 2, "initials": "S E", "clue": "A hard-boiled egg — wrapped in sausage meat and breadcrumbs. Very picnic.", "answer": "Scotch Egg", "aliases": ["scotch egg"], "reasoning": "Scotch (Scottish/a method of preparation) + Egg = Scotch Egg"},
         {"number": 3, "initials": "H", "clue": "A Scottish dish — made from a sheep's insides, with oatmeal, onion. Served on Burns Night.", "answer": "Haggis", "aliases": ["haggis"], "reasoning": "Haggis (the Scottish dish) = Haggis"},
     ]},
    {"id": "foodbusters-043", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Food Busters. Three more foods.", "prize": "Email in. Winner gets a michelin star for something they made in a microwave.",
     "clues": [
         {"number": 1, "initials": "Y P", "clue": "A large puffed-up pudding — goes with a Sunday roast, falls flat if you open the oven too early.", "answer": "Yorkshire Pudding", "aliases": ["yorkshire pudding"], "reasoning": "Yorkshire (county in England) + Pudding = Yorkshire Pudding"},
         {"number": 2, "initials": "W R", "clue": "A toasted cheese dish — from Wales, nothing to do with actual rabbits.", "answer": "Welsh Rarebit", "aliases": ["welsh rarebit"], "reasoning": "Welsh (from Wales) + Rarebit (a corruption of rabbit) = Welsh Rarebit"},
         {"number": 3, "initials": "B P", "clue": "A dark processed pig product — eaten in full breakfast, some people refuse to discuss it.", "answer": "Black Pudding", "aliases": ["black pudding"], "reasoning": "Black + Pudding (a type of sausage) = Black Pudding"},
     ]},
    {"id": "foodbusters-044", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more international dishes.", "prize": "Email in. Winner gets a trip to a restaurant that's stopped doing that dish.",
     "clues": [
         {"number": 1, "initials": "G", "clue": "Small Japanese parcels of filling — fried or steamed, always delicious.", "answer": "Gyoza", "aliases": ["gyoza"], "reasoning": "Gyoza (Japanese dumplings) = Gyoza"},
         {"number": 2, "initials": "B", "clue": "A Middle Eastern pastry — layers of filo, honey, and nuts. Very sweet, very sticky.", "answer": "Baklava", "aliases": ["baklava"], "reasoning": "Baklava (Middle Eastern pastry) = Baklava"},
         {"number": 3, "initials": "S R", "clue": "A bread roll — gone all Vietnamese and started containing pork, pickles, and coriander.", "answer": "Spring Roll", "aliases": ["spring roll"], "reasoning": "Spring + Roll (a type of food) = Spring Roll"},
     ]},
    {"id": "foodbusters-045", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more. All phonetic.", "prize": "Email in. Winner gets a portion of something they can't identify.",
     "clues": [
         {"number": 1, "initials": "S", "clue": "A small Indian triangle — filled with potato and peas, deep fried. Excellent.", "answer": "Samosa", "aliases": ["samosa"], "reasoning": "Samosa (the Indian snack) = Samosa"},
         {"number": 2, "initials": "P", "clue": "An Indian fritter — vegetables in batter, deep fried. Excellent with chutney.", "answer": "Pakora", "aliases": ["pakora"], "reasoning": "Pakora (the Indian snack) = Pakora"},
         {"number": 3, "initials": "D", "clue": "Small parcels of dough filled with things — Chinese, steamed or fried, eaten with chopsticks.", "answer": "Dumplings", "aliases": ["dumplings", "dumpling"], "reasoning": "Dumplings (filled dough parcels) = Dumplings"},
     ]},
    {"id": "foodbusters-046", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more dishes.", "prize": "Email in. Winner gets a food delivery with the wrong order.",
     "clues": [
         {"number": 1, "initials": "S B", "clue": "A Japanese dish — raw fish on rice, beautiful presentation, someone spent years training for this.", "answer": "Sushi", "aliases": ["sushi"], "reasoning": "Sushi (Japanese rice and fish dish) = Sushi"},
         {"number": 2, "initials": "R", "clue": "A Japanese noodle dish — in a very rich broth, lots of toppings, became very fashionable.", "answer": "Ramen", "aliases": ["ramen"], "reasoning": "Ramen (Japanese noodle soup) = Ramen"},
         {"number": 3, "initials": "P T", "clue": "A Thai noodle dish — stir fried, with peanuts, bean sprouts, and a lime wedge.", "answer": "Pad Thai", "aliases": ["pad thai"], "reasoning": "Pad (Thai for stir-fried) + Thai = Pad Thai"},
     ]},
    {"id": "foodbusters-047", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more.", "prize": "Email in. Winner gets a cookbook they'll never open.",
     "clues": [
         {"number": 1, "initials": "N", "clue": "Tortilla chips with cheese and toppings — found at Mexican restaurants and the cinema.", "answer": "Nachos", "aliases": ["nachos"], "reasoning": "Nachos (the Mexican snack) = Nachos"},
         {"number": 2, "initials": "E", "clue": "A wrap — filled with spicy meat, rice and beans, Mexican in origin.", "answer": "Enchilada", "aliases": ["enchilada"], "reasoning": "Enchilada (the Mexican dish) = Enchilada"},
         {"number": 3, "initials": "B", "clue": "A large flour wrap — filled with everything, rolled up, eaten with hands.", "answer": "Burrito", "aliases": ["burrito"], "reasoning": "Burrito (the Mexican wrap) = Burrito"},
     ]},
    {"id": "foodbusters-048", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more dishes. All phonetic.", "prize": "Email in. Winner gets a portion of leftovers from the day before.",
     "clues": [
         {"number": 1, "initials": "P A", "clue": "A Spanish rice dish — cooked in a big flat pan with seafood or chicken, very yellow.", "answer": "Paella", "aliases": ["paella"], "reasoning": "Paella (the Spanish rice dish) = Paella"},
         {"number": 2, "initials": "M", "clue": "A Greek baked dish — layers of meat, aubergine, and a white sauce on top.", "answer": "Moussaka", "aliases": ["moussaka"], "reasoning": "Moussaka (the Greek dish) = Moussaka"},
         {"number": 3, "initials": "G", "clue": "A central European stew — beef, paprika, very hearty, from Hungary.", "answer": "Goulash", "aliases": ["goulash"], "reasoning": "Goulash (the Hungarian stew) = Goulash"},
     ]},
    {"id": "foodbusters-049", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three more.", "prize": "Email in. Winner gets a meal deal that expired yesterday.",
     "clues": [
         {"number": 1, "initials": "T T", "clue": "A dark sticky sweet — baked in a pastry case, found in Victorian cookbooks.", "answer": "Treacle Tart", "aliases": ["treacle tart"], "reasoning": "Treacle (dark syrup) + Tart (a pastry) = Treacle Tart"},
         {"number": 2, "initials": "S T P", "clue": "A dark sticky sponge — with a toffee sauce poured over, very indulgent.", "answer": "Sticky Toffee Pudding", "aliases": ["sticky toffee pudding"], "reasoning": "Sticky + Toffee + Pudding = Sticky Toffee Pudding"},
         {"number": 3, "initials": "R P", "clue": "Grains cooked in milk — sweet, comforting, either loved or hated by people who had it at school.", "answer": "Rice Pudding", "aliases": ["rice pudding"], "reasoning": "Rice + Pudding = Rice Pudding"},
     ]},
    {"id": "foodbusters-050", "enabled": True, "title": "Food Busters", "topic": "world foods and dishes", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Food Busters. Three final dishes.", "prize": "Email in. Winner gets a very small portion of something very expensive.",
     "clues": [
         {"number": 1, "initials": "C T M", "clue": "A British-Indian classic — chicken in a creamy tomato sauce. Apparently Britain's favourite dish.", "answer": "Chicken Tikka Masala", "aliases": ["chicken tikka masala"], "reasoning": "Chicken + Tikka + Masala = Chicken Tikka Masala"},
         {"number": 2, "initials": "F A C", "clue": "A deep fried fish — sitting next to some chips. British institution.", "answer": "Fish and Chips", "aliases": ["fish and chips"], "reasoning": "Fish + and + Chips = Fish and Chips"},
         {"number": 3, "initials": "E M", "clue": "A messy British dessert — smashed meringue with cream and fruit. Very polite chaos.", "answer": "Eton Mess", "aliases": ["eton mess"], "reasoning": "Eton (the school) + Mess (disorder) = Eton Mess"},
     ]},
    # ── Myth Busters +10 (011-020) ─────────────────────────────────────────────
    {"id": "mythbusters-011", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. More mythological figures. All phonetic.", "prize": "Email in. Winner gets a golden fleece that's actually polyester.",
     "clues": [
         {"number": 1, "initials": "A", "clue": "A Greek warrior with one weak spot — very good at fighting, terrible at keeping his heel out of trouble.", "answer": "Achilles", "aliases": ["achilles"], "reasoning": "Achilles (the Greek hero) = Achilles"},
         {"number": 2, "initials": "O", "clue": "A Greek wanderer — spent ten years trying to get home from a war. Very distracted.", "answer": "Odysseus", "aliases": ["odysseus"], "reasoning": "Odysseus (the Greek hero/Ulysses) = Odysseus"},
         {"number": 3, "initials": "J", "clue": "A Greek hero — went off on a boat with a crew to find a very shiny sheep.", "answer": "Jason", "aliases": ["jason"], "reasoning": "Jason (the Greek hero of the Argonauts) = Jason"},
     ]},
    {"id": "mythbusters-012", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more legends.", "prize": "Email in. Winner gets a labyrinth with no map and no exit sign.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A woman — opened a box she was told not to open. Released all the world's troubles. Classic.", "answer": "Pandora", "aliases": ["pandora"], "reasoning": "Pandora (the Greek myth/Pandora's Box) = Pandora"},
         {"number": 2, "initials": "I", "clue": "A young man who flew on wings made of wax — went too high, came down very fast.", "answer": "Icarus", "aliases": ["icarus"], "reasoning": "Icarus (the Greek myth of flight) = Icarus"},
         {"number": 3, "initials": "N", "clue": "A very attractive young man — fell in love with his own reflection in a pond. Couldn't leave.", "answer": "Narcissus", "aliases": ["narcissus"], "reasoning": "Narcissus (the Greek myth/origin of narcissism) = Narcissus"},
     ]},
    {"id": "mythbusters-013", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more mythological characters.", "prize": "Email in. Winner gets a prophecy that's open to interpretation.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A hero — sliced off a snake-haired woman's head and used it to turn people to stone.", "answer": "Perseus", "aliases": ["perseus"], "reasoning": "Perseus (Greek hero who slew Medusa) = Perseus"},
         {"number": 2, "initials": "T", "clue": "An Athenian hero — killed a half-man half-bull in a maze. Very brave.", "answer": "Theseus", "aliases": ["theseus"], "reasoning": "Theseus (killed the Minotaur) = Theseus"},
         {"number": 3, "initials": "O", "clue": "A musician — went down into the underworld to get his wife back. Looked back. Shouldn't have.", "answer": "Orpheus", "aliases": ["orpheus"], "reasoning": "Orpheus (the musician who descended to Hades) = Orpheus"},
     ]},
    {"id": "mythbusters-014", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more. All mythological.", "prize": "Email in. Winner gets an oracle that's deliberately vague.",
     "clues": [
         {"number": 1, "initials": "A", "clue": "A Greek goddess — born from sea foam. Very beautiful, in charge of love.", "answer": "Aphrodite", "aliases": ["aphrodite"], "reasoning": "Aphrodite (Greek goddess of love) = Aphrodite"},
         {"number": 2, "initials": "A", "clue": "A Greek goddess — born from her father's head. In charge of wisdom and warfare.", "answer": "Athena", "aliases": ["athena"], "reasoning": "Athena (Greek goddess of wisdom) = Athena"},
         {"number": 3, "initials": "A", "clue": "A Greek god — twin of Artemis. In charge of the sun, music, and poetry.", "answer": "Apollo", "aliases": ["apollo"], "reasoning": "Apollo (Greek god of the sun) = Apollo"},
     ]},
    {"id": "mythbusters-015", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more mythological figures.", "prize": "Email in. Winner gets an epic poem about their commute.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A winged horse — white, flies, very majestic, born from Medusa's blood.", "answer": "Pegasus", "aliases": ["pegasus"], "reasoning": "Pegasus (the winged horse) = Pegasus"},
         {"number": 2, "initials": "P", "clue": "A Greek goddess — went to live in the underworld for six months of the year. That's why we have winter.", "answer": "Persephone", "aliases": ["persephone"], "reasoning": "Persephone (goddess of spring/queen of underworld) = Persephone"},
         {"number": 3, "initials": "P", "clue": "A Greek god — in charge of the sea. Very temperamental. Has a trident.", "answer": "Poseidon", "aliases": ["poseidon"], "reasoning": "Poseidon (Greek god of the sea) = Poseidon"},
     ]},
    {"id": "mythbusters-016", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. More legends.", "prize": "Email in. Winner gets a curse that only activates in mild inconvenience.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A Greek Titan — stole fire from the gods and gave it to humans. Gods were not pleased.", "answer": "Prometheus", "aliases": ["prometheus"], "reasoning": "Prometheus (stole fire from the gods) = Prometheus"},
         {"number": 2, "initials": "H", "clue": "A Greek god — forge master to the gods. Lame, not beautiful, but made the best weapons.", "answer": "Hephaestus", "aliases": ["hephaestus"], "reasoning": "Hephaestus (Greek god of fire/forge) = Hephaestus"},
         {"number": 3, "initials": "D", "clue": "A Greek god — in charge of wine and partying. Very popular at festivals.", "answer": "Dionysus", "aliases": ["dionysus"], "reasoning": "Dionysus (Greek god of wine) = Dionysus"},
     ]},
    {"id": "mythbusters-017", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more figures.", "prize": "Email in. Winner gets a myth that turns out to be historically accurate.",
     "clues": [
         {"number": 1, "initials": "H", "clue": "A Greek goddess — in charge of the hearth and home. Very important, rarely mentioned.", "answer": "Hera", "aliases": ["hera"], "reasoning": "Hera (queen of the Greek gods) = Hera"},
         {"number": 2, "initials": "A", "clue": "A Greek god — twin of Apollo. In charge of hunting and the moon. Has a bow and arrow.", "answer": "Artemis", "aliases": ["artemis"], "reasoning": "Artemis (Greek goddess of the hunt) = Artemis"},
         {"number": 3, "initials": "A", "clue": "A Greek god — in charge of war. Very aggressive. Not well-liked even by his own parents.", "answer": "Ares", "aliases": ["ares"], "reasoning": "Ares (Greek god of war) = Ares"},
     ]},
    {"id": "mythbusters-018", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three more mythological names.", "prize": "Email in. Winner gets a quest with no clear objective.",
     "clues": [
         {"number": 1, "initials": "H", "clue": "A Greek god — in charge of the dead. Lives underground. Very serious about it.", "answer": "Hades", "aliases": ["hades"], "reasoning": "Hades (Greek god of the underworld) = Hades"},
         {"number": 2, "initials": "D", "clue": "A Greek goddess — in charge of grain and the harvest. Mother of Persephone.", "answer": "Demeter", "aliases": ["demeter"], "reasoning": "Demeter (Greek goddess of harvest) = Demeter"},
         {"number": 3, "initials": "H", "clue": "A Greek hero — given twelve impossible tasks. Completed them all. Very strong.", "answer": "Heracles", "aliases": ["heracles", "hercules"], "reasoning": "Heracles (Greek name for Hercules) = Heracles"},
     ]},
    {"id": "mythbusters-019", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Almost at the end of the myths.", "prize": "Email in. Winner gets a mythological creature they can't prove exists.",
     "clues": [
         {"number": 1, "initials": "K A", "clue": "A British king — had a round table, a magic sword, and a wizard who aged backwards.", "answer": "King Arthur", "aliases": ["king arthur"], "reasoning": "King + Arthur = King Arthur"},
         {"number": 2, "initials": "M", "clue": "A wise old wizard — advised a king, possibly aged backwards, lived in Britain long ago.", "answer": "Merlin", "aliases": ["merlin"], "reasoning": "Merlin (the wizard of Arthurian legend) = Merlin"},
         {"number": 3, "initials": "G", "clue": "A lady associated with a round table and a king — wife who caused a lot of trouble.", "answer": "Guinevere", "aliases": ["guinevere"], "reasoning": "Guinevere (Queen of Camelot) = Guinevere"},
     ]},
    {"id": "mythbusters-020", "enabled": True, "title": "Myth Busters", "topic": "mythology and legends", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Myth Busters. Three final mythological figures.", "prize": "Email in. Winner gets a legend that nobody can verify.",
     "clues": [
         {"number": 1, "initials": "R H", "clue": "A man in green — steals from the rich, gives to the poor. Lives in a forest.", "answer": "Robin Hood", "aliases": ["robin hood"], "reasoning": "Robin (a bird/a name) + Hood (a type of headwear) = Robin Hood"},
         {"number": 2, "initials": "M M", "clue": "A lady associated with Robin Hood — very capable, often overlooked.", "answer": "Maid Marian", "aliases": ["maid marian"], "reasoning": "Maid (a young woman) + Marian (a name) = Maid Marian"},
         {"number": 3, "initials": "L", "clue": "A knight — very loyal, very brave, very in love with the king's wife. Complicated.", "answer": "Lancelot", "aliases": ["lancelot"], "reasoning": "Lancelot (Arthurian knight) = Lancelot"},
     ]},
    # ── Disaster Busters +2 (004-005) ─────────────────────────────────────────
    {"id": "disasterbusters-004", "enabled": True, "title": "Disaster Busters", "topic": "famous disasters and catastrophes", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Disaster Busters. More famous disasters. All phonetic.", "prize": "Email in. Winner gets a disaster plan with several key sections missing.",
     "clues": [
         {"number": 1, "initials": "H K", "clue": "A tropical storm with a woman's name — went all American and flooded a very famous city.", "answer": "Hurricane Katrina", "aliases": ["hurricane katrina"], "reasoning": "Hurricane (a tropical storm) + Katrina (a name) = Hurricane Katrina"},
         {"number": 2, "initials": "G F O L", "clue": "A very large fire — happened in London in 1666. Destroyed most of the city.", "answer": "Great Fire of London", "aliases": ["great fire of london"], "reasoning": "Great + Fire + of + London = Great Fire of London"},
         {"number": 3, "initials": "S F E", "clue": "A city in California — shook violently and fell down in 1906. Very dramatic.", "answer": "San Francisco Earthquake", "aliases": ["san francisco earthquake"], "reasoning": "San Francisco + Earthquake = San Francisco Earthquake"},
     ]},
    {"id": "disasterbusters-005", "enabled": True, "title": "Disaster Busters", "topic": "famous disasters and catastrophes", "difficulty": "medium", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Disaster Busters. Three final disasters.", "prize": "Email in. Winner gets a hard hat and a very concerned look.",
     "clues": [
         {"number": 1, "initials": "B D", "clue": "A chemical plant — leaked poison gas in India in 1984. One of the worst industrial accidents.", "answer": "Bhopal Disaster", "aliases": ["bhopal disaster", "bhopal"], "reasoning": "Bhopal (the Indian city) + Disaster = Bhopal Disaster"},
         {"number": 2, "initials": "B D", "clue": "A very dark Tuesday — the financial markets went all panicky in 1929 and everything went wrong.", "answer": "Black Death", "aliases": ["black death"], "reasoning": "Black + Death = Black Death"},
         {"number": 3, "initials": "M S H", "clue": "A volcano — erupted dramatically in Washington state in 1980. Blew its top off.", "answer": "Mount St Helens", "aliases": ["mount st helens", "mount saint helens"], "reasoning": "Mount + St + Helens = Mount St Helens"},
     ]},
    # ── Musical Busters +2 (004-005) ──────────────────────────────────────────
    {"id": "musicalbusters-004", "enabled": True, "title": "Musical Busters", "topic": "famous stage musicals", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Musical Busters. More stage shows. All phonetic.", "prize": "Email in. Winner gets a seat in the gods with a restricted view.",
     "clues": [
         {"number": 1, "initials": "O", "clue": "A boy who asks for more — goes to London, falls in with criminals. Very catchy songs.", "answer": "Oliver!", "aliases": ["oliver", "oliver!"], "reasoning": "Oliver! (the Dickens musical) = Oliver!"},
         {"number": 2, "initials": "T P O T O", "clue": "A masked man who lives beneath an opera house — not very happy about it.", "answer": "The Phantom of the Opera", "aliases": ["the phantom of the opera", "phantom of the opera"], "reasoning": "The + Phantom + of + the + Opera = The Phantom of the Opera"},
         {"number": 3, "initials": "W S S", "clue": "Two rival gangs in New York — dancing and fighting in equal measure. Very dramatic.", "answer": "West Side Story", "aliases": ["west side story"], "reasoning": "West + Side + Story = West Side Story"},
     ]},
    {"id": "musicalbusters-005", "enabled": True, "title": "Musical Busters", "topic": "famous stage musicals", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Musical Busters. Three final shows. All phonetic.", "prize": "Email in. Winner gets a programme that costs twelve pounds and tells you nothing.",
     "clues": [
         {"number": 1, "initials": "G", "clue": "A very popular American school musical — leather jackets, fast cars, summer romance.", "answer": "Grease", "aliases": ["grease"], "reasoning": "Grease (the musical) = Grease"},
         {"number": 2, "initials": "C", "clue": "A jazz-themed show about murder in 1920s Chicago — all razzle dazzle.", "answer": "Chicago", "aliases": ["chicago"], "reasoning": "Chicago (the city/the musical) = Chicago"},
         {"number": 3, "initials": "R", "clue": "A show about bohemians in New York — living for today, singing about seasons.", "answer": "Rent", "aliases": ["rent"], "reasoning": "Rent (the musical) = Rent"},
     ]},
    # ── Wonder Busters +2 (004-005) ────────────────────────────────────────────
    {"id": "wonderbusters-004", "enabled": True, "title": "Wonder Busters", "topic": "wonders of the world", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Wonder Busters. Two more wonders.", "prize": "Email in. Winner gets a fridge magnet that doesn't stick.",
     "clues": [
         {"number": 1, "initials": "E T", "clue": "A metal tower — went all Parisian and became the most recognisable thing in France.", "answer": "Eiffel Tower", "aliases": ["eiffel tower"], "reasoning": "Eiffel (the engineer) + Tower = Eiffel Tower"},
         {"number": 2, "initials": "S O H", "clue": "A building shaped like sails — went all Australian and started hosting opera.", "answer": "Sydney Opera House", "aliases": ["sydney opera house"], "reasoning": "Sydney + Opera + House = Sydney Opera House"},
         {"number": 3, "initials": "G C", "clue": "A very large crack in the ground — in Arizona, millions of years old, very photogenic.", "answer": "Grand Canyon", "aliases": ["grand canyon"], "reasoning": "Grand (large/impressive) + Canyon = Grand Canyon"},
     ]},
    {"id": "wonderbusters-005", "enabled": True, "title": "Wonder Busters", "topic": "wonders of the world", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Wonder Busters. Three final wonders.", "prize": "Email in. Winner gets a wonder that's currently under renovation.",
     "clues": [
         {"number": 1, "initials": "G G B", "clue": "A reddish-orange bridge — went all San Franciscan and became very famous for being very foggy.", "answer": "Golden Gate Bridge", "aliases": ["golden gate bridge"], "reasoning": "Golden + Gate + Bridge = Golden Gate Bridge"},
         {"number": 2, "initials": "N F", "clue": "A large amount of water going over a ledge — on the border of America and Canada. Very loud.", "answer": "Niagara Falls", "aliases": ["niagara falls"], "reasoning": "Niagara (a name) + Falls (water dropping) = Niagara Falls"},
         {"number": 3, "initials": "B K", "clue": "A very tall building in Dubai — went all glass-and-steel and became the tallest thing in the world.", "answer": "Burj Khalifa", "aliases": ["burj khalifa"], "reasoning": "Burj (tower in Arabic) + Khalifa (a name) = Burj Khalifa"},
     ]},
    # ── Pokemon Busters +2 (004-005) ──────────────────────────────────────────
    {"id": "pokemonbusters-004", "enabled": True, "title": "Pokemon Busters", "topic": "Pokemon characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Pokemon Busters. More Pokemon. Say them out loud.", "prize": "Email in. Winner gets a holographic card that's not rare anymore.",
     "clues": [
         {"number": 1, "initials": "C", "clue": "A small orange lizard — has a flame on its tail. Goes all fire and starts breathing it.", "answer": "Charmander", "aliases": ["charmander"], "reasoning": "Char (to burn) + mander = Charmander"},
         {"number": 2, "initials": "E", "clue": "A small fox-like creature — can evolve into almost anything. Very popular.", "answer": "Eevee", "aliases": ["eevee"], "reasoning": "Eevee (the evolution Pokemon) = Eevee"},
         {"number": 3, "initials": "J", "clue": "A pink round creature — sings a lullaby that puts everyone to sleep. Annoying.", "answer": "Jigglypuff", "aliases": ["jigglypuff"], "reasoning": "Jiggly (wobbly) + puff (a ball of air) = Jigglypuff"},
     ]},
    {"id": "pokemonbusters-005", "enabled": True, "title": "Pokemon Busters", "topic": "Pokemon characters", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK", "US"],
     "intro": "Pokemon Busters. Three final Pokemon.", "prize": "Email in. Winner gets a Pokemon that refuses to evolve.",
     "clues": [
         {"number": 1, "initials": "P", "clue": "A yellow duck — always looks confused. Has a perpetual headache.", "answer": "Psyduck", "aliases": ["psyduck"], "reasoning": "Psy (psychic) + duck = Psyduck"},
         {"number": 2, "initials": "M", "clue": "A useless fish — can barely swim, flops about. Evolves into something terrifying.", "answer": "Magikarp", "aliases": ["magikarp"], "reasoning": "Magic + carp (a fish) = Magikarp"},
         {"number": 3, "initials": "D", "clue": "A large dragon-like creature — orange, very powerful, very hard to control.", "answer": "Dragonite", "aliases": ["dragonite"], "reasoning": "Dragon + ite = Dragonite"},
     ]},
    # ── Comedians Busters +2 (021-022) ────────────────────────────────────────
    {"id": "comediansbusters-021", "enabled": True, "title": "Comedians Busters", "topic": "UK comedians", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Comedians Busters. Two more comedians. All phonetic.", "prize": "Email in. Winner gets a heckle and an awkward silence.",
     "clues": [
         {"number": 1, "initials": "A C", "clue": "A camp bloke from Essex — very loud, very funny, talks about his life in detail.", "answer": "Alan Carr", "aliases": ["alan carr"], "reasoning": "Alan (a name) + Carr (a name) = Alan Carr"},
         {"number": 2, "initials": "F S", "clue": "A bloke from Birmingham — observational, very dry, been going since the 1980s.", "answer": "Frank Skinner", "aliases": ["frank skinner"], "reasoning": "Frank (a name) + Skinner (a name) = Frank Skinner"},
         {"number": 3, "initials": "J B", "clue": "A large female comedian — very deadpan, very dry, has been on every panel show.", "answer": "Jo Brand", "aliases": ["jo brand"], "reasoning": "Jo (a name) + Brand (a trademark) = Jo Brand"},
     ]},
    {"id": "comediansbusters-022", "enabled": True, "title": "Comedians Busters", "topic": "UK comedians", "difficulty": "easy", "office_safe": True, "region_relevance": ["UK"],
     "intro": "Comedians Busters. Three final comedians.", "prize": "Email in. Winner gets a five-minute slot at an open mic night.",
     "clues": [
         {"number": 1, "initials": "B C", "clue": "A Scottish bloke — very big, very hairy, been making people laugh since before most of us were born.", "answer": "Billy Connolly", "aliases": ["billy connolly"], "reasoning": "Billy (a name) + Connolly (a name) = Billy Connolly"},
         {"number": 2, "initials": "K B", "clue": "A Scottish comedian — observational, very likeable, talks about being Scottish a lot.", "answer": "Kevin Bridges", "aliases": ["kevin bridges"], "reasoning": "Kevin (a name) + Bridges (a name) = Kevin Bridges"},
         {"number": 3, "initials": "R H", "clue": "A bloke called Russell — had a chat show, got in trouble, very quick-witted.", "answer": "Russell Howard", "aliases": ["russell howard"], "reasoning": "Russell (a name) + Howard (a name) = Russell Howard"},
     ]},
]


def write_expansion_sets():
    batches_dir = ROOT / "data" / "batches"
    existing = sorted(batches_dir.glob("batch-*.yaml"))
    last_num = int(existing[-1].stem.split("-")[1]) if existing else 0

    batch_num = last_num
    for i in range(0, len(EXPANSION_SETS), 3):
        batch_num += 1
        chunk = EXPANSION_SETS[i:i+3]
        batch_path = batches_dir / f"batch-{batch_num:03d}.yaml"
        with open(batch_path, "w", encoding="utf-8") as f:
            yaml.dump(chunk, f, allow_unicode=True, sort_keys=False,
                      default_flow_style=False, width=2000)
        print(f"Wrote {batch_path.name}: {[s['id'] for s in chunk]}")

    main_yaml = ROOT / "data" / "rockbusters.yaml"
    with open(main_yaml, encoding="utf-8") as f:
        existing_data = yaml.safe_load(f)
    existing_ids = {s["id"] for s in existing_data}
    new_sets = [s for s in EXPANSION_SETS if s["id"] not in existing_ids]
    existing_data.extend(new_sets)
    with open(main_yaml, "w", encoding="utf-8") as f:
        yaml.dump(existing_data, f, allow_unicode=True, sort_keys=False,
                  default_flow_style=False, width=2000)
    print(f"Added {len(new_sets)} sets to rockbusters.yaml")
    return len(new_sets)


if __name__ == "__main__":
    n = write_expansion_sets()
    print(f"Done: {n} expansion sets written")
