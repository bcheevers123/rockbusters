"""Generate new Rockbusters sets for review categories."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent

NEW_SETS = [
    # ── 2020s TV ──────────────────────────────────────────────────────────────
    {
        "id": "2020stvbusters-001", "enabled": True, "title": "2020s TV Busters",
        "topic": "hit TV shows from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Right, 2020s TV Busters. All shows from the last few years. Say the clues out loud.",
        "prize": "Email in. Winner gets a Netflix password that probably doesn't work anymore.",
        "clues": [
            {"number": 1, "initials": "S G", "clue": "That bloke who squeezes things for a living — runs a little stall. Rhymes with fluid game.", "answer": "Squid Game", "aliases": ["squid game"], "reasoning": "squid (sea creature) + game (competition) = Squid Game"},
            {"number": 2, "initials": "S", "clue": "When you take over from someone else at work and follow them up the stairs, that's what you've done to their job.", "answer": "Succession", "aliases": ["succession"], "reasoning": "suc-cess-ion sounds like succession = Succession"},
            {"number": 3, "initials": "T L", "clue": "A cup of that hot brown stuff you drink, but it's gone all relaxed and put its feet up.", "answer": "Ted Lasso", "aliases": ["ted lasso"], "reasoning": "Ted (a name) + lasso (a rope) = Ted Lasso"},
        ]
    },
    {
        "id": "2020stvbusters-002", "enabled": True, "title": "2020s TV Busters",
        "topic": "hit TV shows from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "More telly from the 2020s. Three clues, all phonetic. Have a go.",
        "prize": "Email in. Winner gets a binge-watch hangover and a cold cup of tea.",
        "clues": [
            {"number": 1, "initials": "W L", "clue": "That woman over there has gone all pale and porcelain. Standing on a small wall.", "answer": "White Lotus", "aliases": ["white lotus"], "reasoning": "white (pale) + lotus (a flower/wall) = White Lotus"},
            {"number": 2, "initials": "B", "clue": "A small bridge, but it's been given a fancy title and thinks it's better than the others.", "answer": "Bridgerton", "aliases": ["bridgerton"], "reasoning": "bridge + -erton (suffix) = Bridgerton"},
            {"number": 3, "initials": "E", "clue": "That Greek goddess of the dawn has gone a bit dizzy and started spinning round.", "answer": "Euphoria", "aliases": ["euphoria"], "reasoning": "eu-phor-ia sounds like euphoria = Euphoria"},
        ]
    },
    {
        "id": "2020stvbusters-003", "enabled": True, "title": "2020s TV Busters",
        "topic": "hit TV shows from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s TV. Three more. All phonetic, all from the last few years.",
        "prize": "Email in. Winner gets a streaming subscription to a service that got cancelled.",
        "clues": [
            {"number": 1, "initials": "H O T D", "clue": "A place where you sleep — made entirely of fire-breathing lizards. Bit of a fire hazard.", "answer": "House of the Dragon", "aliases": ["house of the dragon"], "reasoning": "house (accommodation) + of + the + dragon (fire lizard) = House of the Dragon"},
            {"number": 2, "initials": "S", "clue": "That bloke's gone a bit serious and cut himself off from the rest of the office. Bit aloof.", "answer": "Severance", "aliases": ["severance"], "reasoning": "sever-ance = Severance"},
            {"number": 3, "initials": "T B", "clue": "A grizzly animal that works in a kitchen. Very intense about its sandwiches.", "answer": "The Bear", "aliases": ["the bear"], "reasoning": "the + bear (large animal) = The Bear"},
        ]
    },
    {
        "id": "2020stvbusters-004", "enabled": True, "title": "2020s TV Busters",
        "topic": "hit TV shows from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "2020s telly. Three more shows you've probably been watching instead of going outside.",
        "prize": "Email in. Winner gets a TV remote with a sticky button.",
        "clues": [
            {"number": 1, "initials": "T T", "clue": "Those people who try to catch you out — bunch of them, aren't trustworthy. Keep betraying each other.", "answer": "The Traitors", "aliases": ["the traitors"], "reasoning": "the + traitors (people who betray) = The Traitors"},
            {"number": 2, "initials": "W", "clue": "That day in the middle of the week has gone a bit spooky and started wearing all black.", "answer": "Wednesday", "aliases": ["wednesday"], "reasoning": "Wednesday (middle of the week, also Addams Family character) = Wednesday"},
            {"number": 3, "initials": "T L O U", "clue": "That definite article, followed by a word for the end of something, then the word for a female sheep.", "answer": "The Last of Us", "aliases": ["the last of us"], "reasoning": "the + last (final) + of + us (ewe/us) = The Last of Us"},
        ]
    },
    {
        "id": "2020stvbusters-005", "enabled": True, "title": "2020s TV Busters",
        "topic": "hit TV shows from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s TV. Three shows everyone's been banging on about.",
        "prize": "Email in. Winner gets a DVD box set of something nobody watches anymore.",
        "clues": [
            {"number": 1, "initials": "B", "clue": "Two bits of steak, sat next to each other. Just hanging about. Not doing much.", "answer": "Beef", "aliases": ["beef"], "reasoning": "beef (a type of meat/also a grudge) = Beef"},
            {"number": 2, "initials": "H", "clue": "That thing that keeps your chest warm — gone all romantic and started holding hands with someone.", "answer": "Heartstopper", "aliases": ["heartstopper"], "reasoning": "heart + stopper = Heartstopper"},
            {"number": 3, "initials": "A E", "clue": "That primary school in America — all the teachers are basically just winging it.", "answer": "Abbott Elementary", "aliases": ["abbott elementary"], "reasoning": "Abbott (a name) + Elementary (primary school level) = Abbott Elementary"},
        ]
    },
    # ── 2020s Pop ─────────────────────────────────────────────────────────────
    {
        "id": "2020spopbusters-001", "enabled": True, "title": "2020s Pop Busters",
        "topic": "pop artists from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s Pop Busters. All big music acts from recent years. Say it out loud.",
        "prize": "Email in. Winner gets a Spotify playlist with one good song and forty filler tracks.",
        "clues": [
            {"number": 1, "initials": "H S", "clue": "A bloke's hair, but it's gone all fashionable and started wearing a feather boa.", "answer": "Harry Styles", "aliases": ["harry styles"], "reasoning": "Harry (a name) + Styles (fashion choices) = Harry Styles"},
            {"number": 2, "initials": "D L", "clue": "That locked entrance to a place — it's gone all musical and started dancing about.", "answer": "Dua Lipa", "aliases": ["dua lipa"], "reasoning": "Dua (a name) + Lipa (lip-a) = Dua Lipa"},
            {"number": 3, "initials": "B E", "clue": "A small invoice, but it's gone all mysterious and started whispering into microphones.", "answer": "Billie Eilish", "aliases": ["billie eilish"], "reasoning": "Billie (a name) + Eilish (eel-ish) = Billie Eilish"},
        ]
    },
    {
        "id": "2020spopbusters-002", "enabled": True, "title": "2020s Pop Busters",
        "topic": "pop artists from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "More 2020s pop acts. Big names, all phonetic.",
        "prize": "Email in. Winner gets a signed photo of someone they've never heard of.",
        "clues": [
            {"number": 1, "initials": "O R", "clue": "A green oil from Spanish trees, but it's from the other side of the world and writes sad songs.", "answer": "Olivia Rodrigo", "aliases": ["olivia rodrigo"], "reasoning": "Olivia (olive-ia) + Rodrigo (rod-ree-go) = Olivia Rodrigo"},
            {"number": 2, "initials": "S", "clue": "That thing you stir a drink with — gone all fierce and started making grime tracks.", "answer": "Stormzy", "aliases": ["stormzy"], "reasoning": "storm-zy = Stormzy"},
            {"number": 3, "initials": "L C", "clue": "A bloke from Scotland who sounds like he's been crying into his own songs for years.", "answer": "Lewis Capaldi", "aliases": ["lewis capaldi"], "reasoning": "Lewis (a name) + Capaldi (ca-pal-di) = Lewis Capaldi"},
        ]
    },
    {
        "id": "2020spopbusters-003", "enabled": True, "title": "2020s Pop Busters",
        "topic": "pop artists from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s pop. Three more big acts from recent years.",
        "prize": "Email in. Winner gets a pair of earphones with only one side working.",
        "clues": [
            {"number": 1, "initials": "B B", "clue": "A bad rabbit — mischievous little thing. Won't stop making music about it.", "answer": "Bad Bunny", "aliases": ["bad bunny"], "reasoning": "bad (naughty) + bunny (rabbit) = Bad Bunny"},
            {"number": 2, "initials": "P M", "clue": "A bloke delivering letters who's gone a bit melancholy and started rapping about it.", "answer": "Post Malone", "aliases": ["post malone"], "reasoning": "post (mail) + Malone (a name) = Post Malone"},
            {"number": 3, "initials": "L", "clue": "A city in Italy, but it's gone big and started belting out pop songs.", "answer": "Lizzo", "aliases": ["lizzo"], "reasoning": "Lizzo (liz-zo) = Lizzo"},
        ]
    },
    {
        "id": "2020spopbusters-004", "enabled": True, "title": "2020s Pop Busters",
        "topic": "pop artists from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s pop artists. Three more. All phonetic.",
        "prize": "Email in. Winner gets a music festival wristband from 2019 that's gone mouldy.",
        "clues": [
            {"number": 1, "initials": "D C", "clue": "That female dog from Japan — gone all colourful and started releasing bangers.", "answer": "Doja Cat", "aliases": ["doja cat"], "reasoning": "Doja (doe-ja) + Cat (feline) = Doja Cat"},
            {"number": 2, "initials": "W L", "clue": "A damp piece of wood that's got all wobbly and started playing indie music.", "answer": "Wet Leg", "aliases": ["wet leg"], "reasoning": "wet (damp) + leg (limb) = Wet Leg"},
            {"number": 3, "initials": "S F", "clue": "A bloke from Newcastle who gets emotional about his surroundings and writes songs about them.", "answer": "Sam Fender", "aliases": ["sam fender"], "reasoning": "Sam (a name) + Fender (a guitar brand/car part) = Sam Fender"},
        ]
    },
    {
        "id": "2020spopbusters-005", "enabled": True, "title": "2020s Pop Busters",
        "topic": "pop artists from the 2020s", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "2020s pop. Three more artists who've been all over the charts.",
        "prize": "Email in. Winner gets a vinyl record of something nobody asked for.",
        "clues": [
            {"number": 1, "initials": "L D R", "clue": "A woman called Lana who lives by a river and writes very long, sad songs about it.", "answer": "Lana Del Rey", "aliases": ["lana del rey"], "reasoning": "Lana (a name) + Del Rey (of the king) = Lana Del Rey"},
            {"number": 2, "initials": "T W", "clue": "That seven days — gone all moody and started making R&B records.", "answer": "The Weeknd", "aliases": ["the weeknd"], "reasoning": "the + weeknd (weekend) = The Weeknd"},
            {"number": 3, "initials": "I S", "clue": "Frozen water, but it's got a bit spicy and started doing drill music.", "answer": "Ice Spice", "aliases": ["ice spice"], "reasoning": "ice (frozen water) + spice (seasoning) = Ice Spice"},
        ]
    },
    # ── Reality TV ────────────────────────────────────────────────────────────
    {
        "id": "realitytvbusters-001", "enabled": True, "title": "Reality TV Busters",
        "topic": "reality TV shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Reality TV Busters. All shows where real people embarrass themselves on telly. Say the clues out loud.",
        "prize": "Email in. Winner gets a rejection letter from a reality TV casting director.",
        "clues": [
            {"number": 1, "initials": "L I", "clue": "A piece of land surrounded by water — gone all romantic and started pairing people up.", "answer": "Love Island", "aliases": ["love island"], "reasoning": "love + island (land surrounded by water) = Love Island"},
            {"number": 2, "initials": "S C D", "clue": "Doing something tightly, in a formal way — gone all glittery and started waltzing.", "answer": "Strictly Come Dancing", "aliases": ["strictly come dancing"], "reasoning": "strictly (in a strict manner) + come + dancing = Strictly Come Dancing"},
            {"number": 3, "initials": "T G B B O", "clue": "That large cooking competition — everyone's very polite about it despite the stress.", "answer": "The Great British Bake Off", "aliases": ["the great british bake off", "great british bake off", "bake off"], "reasoning": "The + Great + British + Bake + Off = The Great British Bake Off"},
        ]
    },
    {
        "id": "realitytvbusters-002", "enabled": True, "title": "Reality TV Busters",
        "topic": "reality TV shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "More reality telly. Three phonetic clues, all unscripted chaos.",
        "prize": "Email in. Winner gets a fake tan and a bruised ego.",
        "clues": [
            {"number": 1, "initials": "I A C", "clue": "That statement of existence, followed by a royal, then a big cold country full of moose.", "answer": "I'm a Celebrity", "aliases": ["im a celebrity", "i'm a celebrity get me out of here"], "reasoning": "I'm + a + Celebrity = I'm a Celebrity"},
            {"number": 2, "initials": "T A", "clue": "That bloke in charge of everything has given someone a task and is watching them fail at it.", "answer": "The Apprentice", "aliases": ["the apprentice"], "reasoning": "the + apprentice (trainee) = The Apprentice"},
            {"number": 3, "initials": "B B", "clue": "A large sibling — watching everyone inside a house and judging their every move.", "answer": "Big Brother", "aliases": ["big brother"], "reasoning": "big + brother (male sibling) = Big Brother"},
        ]
    },
    {
        "id": "realitytvbusters-003", "enabled": True, "title": "Reality TV Busters",
        "topic": "reality TV shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Reality TV. Three more shows where ordinary people lose the plot on camera.",
        "prize": "Email in. Winner gets a NDA and a taxi home.",
        "clues": [
            {"number": 1, "initials": "T T", "clue": "A group of people who can't be trusted — all scheming away in a castle somewhere.", "answer": "The Traitors", "aliases": ["the traitors"], "reasoning": "the + traitors = The Traitors"},
            {"number": 2, "initials": "G", "clue": "People sitting on a sofa watching telly and commenting on it — which is basically what everyone does anyway.", "answer": "Gogglebox", "aliases": ["gogglebox"], "reasoning": "goggle (stare) + box (TV) = Gogglebox"},
            {"number": 3, "initials": "M A F S", "clue": "Two strangers saying those two big words in a church to someone they've never met before.", "answer": "Married at First Sight", "aliases": ["married at first sight"], "reasoning": "married + at + first + sight = Married at First Sight"},
        ]
    },
    {
        "id": "realitytvbusters-004", "enabled": True, "title": "Reality TV Busters",
        "topic": "reality TV shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Reality TV Busters. Three more shows. All phonetic.",
        "prize": "Email in. Winner gets fifteen minutes of fame and a very short Wikipedia page.",
        "clues": [
            {"number": 1, "initials": "F D", "clue": "That number one, followed by the things you go on before you decide if you like someone.", "answer": "First Dates", "aliases": ["first dates"], "reasoning": "first + dates = First Dates"},
            {"number": 2, "initials": "T C", "clue": "That definite article, followed by a geometric shape with all equal sides. People inside it talking to cameras.", "answer": "The Circle", "aliases": ["the circle"], "reasoning": "the + circle (geometric shape) = The Circle"},
            {"number": 3, "initials": "R A T W", "clue": "Moving at speed across the whole planet — but doing it on a shoestring budget.", "answer": "Race Across the World", "aliases": ["race across the world"], "reasoning": "race + across + the + world = Race Across the World"},
        ]
    },
    {
        "id": "realitytvbusters-005", "enabled": True, "title": "Reality TV Busters",
        "topic": "reality TV shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Reality TV. Three more. Say the clues out loud and you'll get there.",
        "prize": "Email in. Winner gets a selfie stick and zero followers.",
        "clues": [
            {"number": 1, "initials": "C B B", "clue": "Famous people, but they're siblings — all crammed in a house together being watched.", "answer": "Celebrity Big Brother", "aliases": ["celebrity big brother"], "reasoning": "celebrity + big + brother = Celebrity Big Brother"},
            {"number": 2, "initials": "H", "clue": "A group of people being chased across the country by professionals trying to find them.", "answer": "Hunted", "aliases": ["hunted"], "reasoning": "hunted (being tracked down) = Hunted"},
            {"number": 3, "initials": "S", "clue": "People on an island trying to outlast each other — voting each other off one by one.", "answer": "Survivor", "aliases": ["survivor"], "reasoning": "survivor (one who survives) = Survivor"},
        ]
    },
    # ── Prime Ministers ───────────────────────────────────────────────────────
    {
        "id": "primeministersbusters-001", "enabled": True, "title": "Prime Ministers Busters",
        "topic": "UK Prime Ministers", "difficulty": "medium", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Prime Ministers Busters. All UK PMs, full names. Say the clues out loud.",
        "prize": "Email in. Winner gets a resignation letter and a chauffeur-driven car going the wrong way.",
        "clues": [
            {"number": 1, "initials": "M T", "clue": "A female relative of mine — she's a bit metalworking, likes to fix things made of iron.", "answer": "Margaret Thatcher", "aliases": ["margaret thatcher"], "reasoning": "Margaret (a name) + Thatcher (someone who thatches roofs) = Margaret Thatcher"},
            {"number": 2, "initials": "T B", "clue": "A tiny piece of something — very small, like an insect's leg. Very enthusiastic about it though.", "answer": "Tony Blair", "aliases": ["tony blair"], "reasoning": "Tony (a name) + Blair (sounds like 'blare' or a Scottish place) = Tony Blair"},
            {"number": 3, "initials": "J M", "clue": "A bloke called John who's gone all big and important and is working in a quarry now.", "answer": "John Major", "aliases": ["john major"], "reasoning": "John (a name) + Major (army rank/important) = John Major"},
        ]
    },
    {
        "id": "primeministersbusters-002", "enabled": True, "title": "Prime Ministers Busters",
        "topic": "UK Prime Ministers", "difficulty": "medium", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "More UK Prime Ministers. Three more full names, all phonetic.",
        "prize": "Email in. Winner gets a safe seat in a constituency they've never visited.",
        "clues": [
            {"number": 1, "initials": "G B", "clue": "A bloke called Gordon whose skin has turned a sort of golden colour. Bit shiny about it.", "answer": "Gordon Brown", "aliases": ["gordon brown"], "reasoning": "Gordon (a name) + Brown (the colour) = Gordon Brown"},
            {"number": 2, "initials": "D C", "clue": "A bloke called Dave who's gone all photogenic and started shooting things with a lens.", "answer": "David Cameron", "aliases": ["david cameron"], "reasoning": "David (a name) + Cameron (sounds like camera) = David Cameron"},
            {"number": 3, "initials": "T M", "clue": "That month in spring — gone female and taken charge of the whole country.", "answer": "Theresa May", "aliases": ["theresa may"], "reasoning": "Theresa (a name) + May (the month) = Theresa May"},
        ]
    },
    {
        "id": "primeministersbusters-003", "enabled": True, "title": "Prime Ministers Busters",
        "topic": "UK Prime Ministers", "difficulty": "medium", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Prime Ministers Busters. More full names, all phonetic.",
        "prize": "Email in. Winner gets a press conference no one shows up to.",
        "clues": [
            {"number": 1, "initials": "B J", "clue": "A bloke called Boris who makes you laugh but you're not sure why. Bit of a joker.", "answer": "Boris Johnson", "aliases": ["boris johnson"], "reasoning": "Boris (a name) + Johnson (a surname) = Boris Johnson"},
            {"number": 2, "initials": "L T", "clue": "A female relative — gone all transparent and started falling through things.", "answer": "Liz Truss", "aliases": ["liz truss"], "reasoning": "Liz (a name) + Truss (a structural support) = Liz Truss"},
            {"number": 3, "initials": "R S", "clue": "That bloke with very rich parents — he's rolling in it, isn't he. Very well off.", "answer": "Rishi Sunak", "aliases": ["rishi sunak"], "reasoning": "Rishi (a name) + Sunak (soo-nak) = Rishi Sunak"},
        ]
    },
    {
        "id": "primeministersbusters-004", "enabled": True, "title": "Prime Ministers Busters",
        "topic": "UK Prime Ministers", "difficulty": "medium", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Prime Ministers Busters. Older ones now. Full names, all phonetic.",
        "prize": "Email in. Winner gets a black door with a number on it.",
        "clues": [
            {"number": 1, "initials": "H W", "clue": "A bloke called Harold who's gone off to get some water from a well. Very determined about it.", "answer": "Harold Wilson", "aliases": ["harold wilson"], "reasoning": "Harold (a name) + Wilson (son of Will) = Harold Wilson"},
            {"number": 2, "initials": "E H", "clue": "A patch of open land covered in purple flowers — it's gone all grand and put on a suit.", "answer": "Edward Heath", "aliases": ["edward heath"], "reasoning": "Edward (a name) + Heath (open land with heather) = Edward Heath"},
            {"number": 3, "initials": "W C", "clue": "A person who wins things — goes into small rooms and comes out victorious.", "answer": "Winston Churchill", "aliases": ["winston churchill"], "reasoning": "Winston (a name) + Churchill (church + hill) = Winston Churchill"},
        ]
    },
    {
        "id": "primeministersbusters-005", "enabled": True, "title": "Prime Ministers Busters",
        "topic": "UK Prime Ministers", "difficulty": "medium", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Prime Ministers Busters. Three more from the history books.",
        "prize": "Email in. Winner gets a memoirs book nobody's read past chapter two.",
        "clues": [
            {"number": 1, "initials": "C A", "clue": "A bloke from the church — gone all political and started nationalising things left, right, and centre.", "answer": "Clement Attlee", "aliases": ["clement attlee"], "reasoning": "Clement (a church title/name) + Attlee (at-lee) = Clement Attlee"},
            {"number": 2, "initials": "H M", "clue": "A bloke called Harold who's gone all grand and started living in a big house on a hill.", "answer": "Harold Macmillan", "aliases": ["harold macmillan"], "reasoning": "Harold (a name) + Macmillan (mac + millan) = Harold Macmillan"},
            {"number": 3, "initials": "J C", "clue": "A bloke called James who's very calm about everything. Very tranquil. Not a care in the world.", "answer": "James Callaghan", "aliases": ["james callaghan"], "reasoning": "James (a name) + Callaghan (calla-han) = James Callaghan"},
        ]
    },
    # ── Landmarks ─────────────────────────────────────────────────────────────
    {
        "id": "landmarkbusters-001", "enabled": True, "title": "Landmark Busters",
        "topic": "famous UK landmarks", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Landmark Busters. All famous UK landmarks. Say the clues out loud.",
        "prize": "Email in. Winner gets a fridge magnet of somewhere they've never been.",
        "clues": [
            {"number": 1, "initials": "B B", "clue": "A large male pig — gone all tall and started telling everyone what time it is.", "answer": "Big Ben", "aliases": ["big ben"], "reasoning": "Big (large) + Ben (a name) = Big Ben"},
            {"number": 2, "initials": "B P", "clue": "A large container for water — gone all royal and got a long driveway.", "answer": "Buckingham Palace", "aliases": ["buckingham palace"], "reasoning": "Buckingham (a place) + Palace (grand residence) = Buckingham Palace"},
            {"number": 3, "initials": "T O L", "clue": "That tall structure — gone all old and started locking people inside it.", "answer": "Tower of London", "aliases": ["tower of london"], "reasoning": "Tower (tall structure) + of + London = Tower of London"},
        ]
    },
    {
        "id": "landmarkbusters-002", "enabled": True, "title": "Landmark Busters",
        "topic": "famous UK landmarks", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Landmark Busters. Three more famous UK landmarks.",
        "prize": "Email in. Winner gets a laminated tourist map from 1987.",
        "clues": [
            {"number": 1, "initials": "S", "clue": "Large rocks arranged in a circle on a plain. Been there for ages. Nobody knows why.", "answer": "Stonehenge", "aliases": ["stonehenge"], "reasoning": "stone + henge (prehistoric monument type) = Stonehenge"},
            {"number": 2, "initials": "A O T N", "clue": "A heavenly body — gone all pointy and landed in the north of England.", "answer": "Angel of the North", "aliases": ["angel of the north"], "reasoning": "Angel (heavenly being) + of + the + North = Angel of the North"},
            {"number": 3, "initials": "W C", "clue": "A place where the wind blows through a gap — gone all regal and started wearing a crown.", "answer": "Windsor Castle", "aliases": ["windsor castle"], "reasoning": "Windsor (winds + or) + Castle (fortification) = Windsor Castle"},
        ]
    },
    {
        "id": "landmarkbusters-003", "enabled": True, "title": "Landmark Busters",
        "topic": "famous UK landmarks", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Landmark Busters. Three more. All phonetic, all famous.",
        "prize": "Email in. Winner gets a guided tour of a car park that used to be something interesting.",
        "clues": [
            {"number": 1, "initials": "H W", "clue": "A wall built by a bloke called Adrian — keeps the cold out and the Romans in.", "answer": "Hadrian's Wall", "aliases": ["hadrians wall", "hadrian's wall"], "reasoning": "Hadrian's (the emperor) + Wall = Hadrian's Wall"},
            {"number": 2, "initials": "T S", "clue": "That definite article, followed by something very pointed and glass-covered in London.", "answer": "The Shard", "aliases": ["the shard"], "reasoning": "The + Shard (a sharp fragment/glass building) = The Shard"},
            {"number": 3, "initials": "T S", "clue": "A large open area in London — lions on columns, pigeons everywhere, tourists gawping.", "answer": "Trafalgar Square", "aliases": ["trafalgar square"], "reasoning": "Trafalgar (famous battle) + Square (open public space) = Trafalgar Square"},
        ]
    },
    # ── Horror films ──────────────────────────────────────────────────────────
    {
        "id": "horrorbusters-001", "enabled": True, "title": "Horror Busters",
        "topic": "famous horror films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Horror Busters. All famous horror films. Say the clues out loud if you dare.",
        "prize": "Email in. Winner gets a torch that runs out of batteries at the worst moment.",
        "clues": [
            {"number": 1, "initials": "T S", "clue": "That bloke who's been polishing floors all winter — gone a bit peculiar and started chasing his family.", "answer": "The Shining", "aliases": ["the shining"], "reasoning": "the + shining (polishing/glowing) = The Shining"},
            {"number": 2, "initials": "H", "clue": "A spooky event that happens on the night before November — gone all masked and stabby.", "answer": "Halloween", "aliases": ["halloween"], "reasoning": "Halloween (Oct 31st holiday) = Halloween"},
            {"number": 3, "initials": "P", "clue": "A bloke who works with brains for a living — gone a bit eccentric and started running a motel.", "answer": "Psycho", "aliases": ["psycho"], "reasoning": "Psycho (psychiatry/crazy) = Psycho"},
        ]
    },
    {
        "id": "horrorbusters-002", "enabled": True, "title": "Horror Busters",
        "topic": "famous horror films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Horror Busters. Three more classics. All phonetic.",
        "prize": "Email in. Winner gets a babysitting job they can't get out of.",
        "clues": [
            {"number": 1, "initials": "A", "clue": "Something from outer space — not friendly. Very tall, drools a lot. In space, nobody can hear it.", "answer": "Alien", "aliases": ["alien"], "reasoning": "Alien (extraterrestrial creature) = Alien"},
            {"number": 2, "initials": "J", "clue": "A very large fish — lurking in shallow water near the beach. Put people off swimming for decades.", "answer": "Jaws", "aliases": ["jaws"], "reasoning": "Jaws (the mouth of a large shark) = Jaws"},
            {"number": 3, "initials": "S", "clue": "A loud, high-pitched sound coming from someone in a white mask — been doing it since 1996.", "answer": "Scream", "aliases": ["scream"], "reasoning": "Scream (a loud shriek) = Scream"},
        ]
    },
    {
        "id": "horrorbusters-003", "enabled": True, "title": "Horror Busters",
        "topic": "famous horror films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Horror Busters. Three more scary ones.",
        "prize": "Email in. Winner gets a nightlight and a very thin duvet.",
        "clues": [
            {"number": 1, "initials": "T E", "clue": "That church bloke — gone all possessed and started spinning his head round.", "answer": "The Exorcist", "aliases": ["the exorcist"], "reasoning": "the + exorcist (one who performs exorcisms) = The Exorcist"},
            {"number": 2, "initials": "I", "clue": "A personal pronoun — gone all red and started floating in the drains.", "answer": "It", "aliases": ["it"], "reasoning": "It (pronoun/the clown) = It"},
            {"number": 3, "initials": "G O", "clue": "That colour you use to leave somewhere — gone all racial and started uncovering hidden fears.", "answer": "Get Out", "aliases": ["get out"], "reasoning": "Get + Out (leave/escape) = Get Out"},
        ]
    },
    {
        "id": "horrorbusters-004", "enabled": True, "title": "Horror Busters",
        "topic": "famous horror films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Horror Busters. More scary films. All phonetic.",
        "prize": "Email in. Winner gets a creaky floorboard and an unidentified noise downstairs.",
        "clues": [
            {"number": 1, "initials": "H", "clue": "Going to live somewhere that is inherited from someone — gone all dark and started flickering the lights.", "answer": "Hereditary", "aliases": ["hereditary"], "reasoning": "hereditary (passed down through family) = Hereditary"},
            {"number": 2, "initials": "A Q P", "clue": "A very silent spot — no noise whatsoever. Best not make a sound or something very bad happens.", "answer": "A Quiet Place", "aliases": ["a quiet place"], "reasoning": "A + Quiet (silent) + Place (location) = A Quiet Place"},
            {"number": 3, "initials": "C", "clue": "A young woman covered in something red at a school dance — not happy about it.", "answer": "Carrie", "aliases": ["carrie"], "reasoning": "Carrie (a name, also to carry) = Carrie"},
        ]
    },
    {
        "id": "horrorbusters-005", "enabled": True, "title": "Horror Busters",
        "topic": "famous horror films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Horror Busters. Three more. Say them out loud and something might get you.",
        "prize": "Email in. Winner gets a door that won't lock properly.",
        "clues": [
            {"number": 1, "initials": "M", "clue": "A sunny Swedish festival — everyone's wearing flowers and smiling. Something is very wrong.", "answer": "Midsommar", "aliases": ["midsommar"], "reasoning": "Midsommar (midsummer in Swedish) = Midsommar"},
            {"number": 2, "initials": "T C", "clue": "People consulting a bloke in an overalls about plumbing — turns out it's all connected to something evil.", "answer": "The Conjuring", "aliases": ["the conjuring"], "reasoning": "the + conjuring (summoning/magic) = The Conjuring"},
            {"number": 3, "initials": "U", "clue": "A pronoun for people together — gone all paranoid and started running from their other selves.", "answer": "Us", "aliases": ["us"], "reasoning": "Us (we/the group) = Us"},
        ]
    },
    # ── Christmas Films ───────────────────────────────────────────────────────
    {
        "id": "christmasfilmbusters-001", "enabled": True, "title": "Christmas Film Busters",
        "topic": "classic Christmas films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Christmas Film Busters. All festive classics. Say the clues out loud.",
        "prize": "Email in. Winner gets a selection box with all the good ones already eaten.",
        "clues": [
            {"number": 1, "initials": "H A", "clue": "A house — gone all solitary and started booby-trapping itself for burglars.", "answer": "Home Alone", "aliases": ["home alone"], "reasoning": "home (house) + alone (by itself) = Home Alone"},
            {"number": 2, "initials": "E", "clue": "A Christmas fairy — gone a bit tall and started working in a sweet shop in New York.", "answer": "Elf", "aliases": ["elf"], "reasoning": "Elf (a Christmas sprite) = Elf"},
            {"number": 3, "initials": "D H", "clue": "A bloke who dies — gone all heroic inside a tall building at Christmas. Very festive.", "answer": "Die Hard", "aliases": ["die hard"], "reasoning": "Die (to die) + Hard (difficult) = Die Hard"},
        ]
    },
    {
        "id": "christmasfilmbusters-002", "enabled": True, "title": "Christmas Film Busters",
        "topic": "classic Christmas films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Christmas films. Three more classics. All phonetic.",
        "prize": "Email in. Winner gets a Christmas card from someone they can't quite place.",
        "clues": [
            {"number": 1, "initials": "L A", "clue": "Something you feel for someone — gone all romantic and started happening around an airport.", "answer": "Love Actually", "aliases": ["love actually"], "reasoning": "love + actually = Love Actually"},
            {"number": 2, "initials": "T H", "clue": "A break from work — gone all snowy and involved two women swapping houses.", "answer": "The Holiday", "aliases": ["the holiday"], "reasoning": "the + holiday (a break) = The Holiday"},
            {"number": 3, "initials": "T P E", "clue": "That public transport for cold, icy regions — gone all magical and started heading to the North Pole.", "answer": "The Polar Express", "aliases": ["the polar express", "polar express"], "reasoning": "the + Polar (arctic) + Express (fast train) = The Polar Express"},
        ]
    },
    {
        "id": "christmasfilmbusters-003", "enabled": True, "title": "Christmas Film Busters",
        "topic": "classic Christmas films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Christmas films. Three more. Say them out loud.",
        "prize": "Email in. Winner gets a tangerine and a coin at the bottom of a stocking.",
        "clues": [
            {"number": 1, "initials": "A C C", "clue": "That miserly bloke being visited by three transparent people who show him what a rotter he's been.", "answer": "A Christmas Carol", "aliases": ["a christmas carol"], "reasoning": "A + Christmas + Carol (festive song) = A Christmas Carol"},
            {"number": 2, "initials": "I A W L", "clue": "That thing said when something exists — gone all wonderful and started involving an angel earning wings.", "answer": "It's a Wonderful Life", "aliases": ["its a wonderful life", "it's a wonderful life"], "reasoning": "It's + a + Wonderful + Life = It's a Wonderful Life"},
            {"number": 3, "initials": "K", "clue": "A small ship — gone all animated and started delivering presents to children.", "answer": "Klaus", "aliases": ["klaus"], "reasoning": "Klaus (Santa Klaus) = Klaus"},
        ]
    },
    {
        "id": "christmasfilmbusters-004", "enabled": True, "title": "Christmas Film Busters",
        "topic": "classic Christmas films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Christmas films. Three more festive classics.",
        "prize": "Email in. Winner gets a pair of novelty socks they'll never wear.",
        "clues": [
            {"number": 1, "initials": "A C", "clue": "A festive song — going by boat, past all the presents under the tree.", "answer": "Arthur Christmas", "aliases": ["arthur christmas"], "reasoning": "Arthur (a name) + Christmas = Arthur Christmas"},
            {"number": 2, "initials": "T S", "clue": "That thing in a room where it's very cold and everyone's wearing jumpers. Frosty atmosphere.", "answer": "The Snowman", "aliases": ["the snowman"], "reasoning": "the + snowman (figure made of snow) = The Snowman"},
            {"number": 3, "initials": "W C", "clue": "A colour that's gone all festive and started singing carols in black and white.", "answer": "White Christmas", "aliases": ["white christmas"], "reasoning": "white (the colour) + Christmas = White Christmas"},
        ]
    },
    {
        "id": "christmasfilmbusters-005", "enabled": True, "title": "Christmas Film Busters",
        "topic": "classic Christmas films", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Christmas films. Three more for the festive season.",
        "prize": "Email in. Winner gets a festive jumper from a charity shop.",
        "clues": [
            {"number": 1, "initials": "S C T M", "clue": "That jolly big bloke in red — gone all Hollywood and started explaining how he does it all in one night.", "answer": "Santa Claus the Movie", "aliases": ["santa claus the movie", "santa claus"], "reasoning": "Santa + Claus + the + Movie = Santa Claus the Movie"},
            {"number": 2, "initials": "H I", "clue": "A place where aircraft land — but it's warm and everyone keeps singing.", "answer": "Holiday Inn", "aliases": ["holiday inn"], "reasoning": "Holiday (festive break) + Inn (a place to stay) = Holiday Inn"},
            {"number": 3, "initials": "J F", "clue": "A month of the year — gone all icy and started singing in a scarf.", "answer": "Jack Frost", "aliases": ["jack frost"], "reasoning": "Jack (a name) + Frost (frozen condensation) = Jack Frost"},
        ]
    },
    # ── Actress Busters ───────────────────────────────────────────────────────
    {
        "id": "actressbusters-001", "enabled": True, "title": "Actress Busters",
        "topic": "modern actresses", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Actress Busters. All modern actresses. Say the clues out loud.",
        "prize": "Email in. Winner gets a supporting role in something they'll never watch.",
        "clues": [
            {"number": 1, "initials": "M R", "clue": "A large female deer — gone all glamorous and started producing films about dolls.", "answer": "Margot Robbie", "aliases": ["margot robbie"], "reasoning": "Margot (a name) + Robbie (a name) = Margot Robbie"},
            {"number": 2, "initials": "F P", "clue": "A small, rounded cushion — gone all fierce and started appearing in Marvel films.", "answer": "Florence Pugh", "aliases": ["florence pugh"], "reasoning": "Florence (a city/name) + Pugh (a name, sounds like 'pew') = Florence Pugh"},
            {"number": 3, "initials": "Z", "clue": "A small piece of energy — gone all tall and started taking over Spider-Man films.", "answer": "Zendaya", "aliases": ["zendaya"], "reasoning": "Zen (calm/energy) + daya = Zendaya"},
        ]
    },
    {
        "id": "actressbusters-002", "enabled": True, "title": "Actress Busters",
        "topic": "modern actresses", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Actress Busters. Three more modern actresses.",
        "prize": "Email in. Winner gets a walk-on part and no speaking lines.",
        "clues": [
            {"number": 1, "initials": "E S", "clue": "A rock — gone all precious and started winning Oscars left, right, and centre.", "answer": "Emma Stone", "aliases": ["emma stone"], "reasoning": "Emma (a name) + Stone (a rock) = Emma Stone"},
            {"number": 2, "initials": "S R", "clue": "That Irish female sheep — gone all serious and started making very good films.", "answer": "Saoirse Ronan", "aliases": ["saoirse ronan"], "reasoning": "Saoirse (an Irish name, sounds like Sur-sha) + Ronan (a name) = Saoirse Ronan"},
            {"number": 3, "initials": "A T J", "clue": "Any female deer — gone all otherworldly and started playing chess in a period drama.", "answer": "Anya Taylor-Joy", "aliases": ["anya taylor-joy", "anya taylor joy"], "reasoning": "Anya (a name) + Taylor (one who tailors) + Joy (happiness) = Anya Taylor-Joy"},
        ]
    },
    {
        "id": "actressbusters-003", "enabled": True, "title": "Actress Busters",
        "topic": "modern actresses", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Actress Busters. Three more. All phonetic.",
        "prize": "Email in. Winner gets a BAFTA they have to give back by Monday.",
        "clues": [
            {"number": 1, "initials": "A D A", "clue": "A small channel for water — gone all mysterious and started appearing in Bond films.", "answer": "Ana de Armas", "aliases": ["ana de armas"], "reasoning": "Ana (a name) + de + Armas (of arms/weapons in Spanish) = Ana de Armas"},
            {"number": 2, "initials": "C M", "clue": "A female relative — gone all proper and started appearing in serious British dramas.", "answer": "Carey Mulligan", "aliases": ["carey mulligan"], "reasoning": "Carey (a name) + Mulligan (a do-over in golf) = Carey Mulligan"},
            {"number": 3, "initials": "D R", "clue": "A puzzle — gone all galactic and started wielding a lightsabre.", "answer": "Daisy Ridley", "aliases": ["daisy ridley"], "reasoning": "Daisy (a flower) + Ridley (a name) = Daisy Ridley"},
        ]
    },
    {
        "id": "actressbusters-004", "enabled": True, "title": "Actress Busters",
        "topic": "modern actresses", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Actress Busters. Three more modern actresses.",
        "prize": "Email in. Winner gets a table read they weren't invited to.",
        "clues": [
            {"number": 1, "initials": "V D", "clue": "A musical instrument with strings — gone all powerful and started giving speeches.", "answer": "Viola Davis", "aliases": ["viola davis"], "reasoning": "Viola (a string instrument) + Davis (a name) = Viola Davis"},
            {"number": 2, "initials": "L N", "clue": "A small wolf pup — gone all Kenyan and started winning Oscars.", "answer": "Lupita Nyong'o", "aliases": ["lupita nyongo", "lupita nyong'o"], "reasoning": "Lupita (a name, lupa = wolf) + Nyong'o (a name) = Lupita Nyong'o"},
            {"number": 3, "initials": "J L", "clue": "A bloke called Jen — gone all enthusiastic about films involving districts and hunger.", "answer": "Jennifer Lawrence", "aliases": ["jennifer lawrence"], "reasoning": "Jennifer (a name) + Lawrence (a name) = Jennifer Lawrence"},
        ]
    },
    {
        "id": "actressbusters-005", "enabled": True, "title": "Actress Busters",
        "topic": "modern actresses", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Actress Busters. Three final modern actresses.",
        "prize": "Email in. Winner gets a director's cut nobody asked for.",
        "clues": [
            {"number": 1, "initials": "C B", "clue": "A white cliff — gone all elegant and started winning every award going.", "answer": "Cate Blanchett", "aliases": ["cate blanchett"], "reasoning": "Cate (a name, sounds like Kate) + Blanchett (blanc = white) = Cate Blanchett"},
            {"number": 2, "initials": "M Y", "clue": "An Asian year — gone all martial and started kicking things impressively.", "answer": "Michelle Yeoh", "aliases": ["michelle yeoh"], "reasoning": "Michelle (a name) + Yeoh (a name) = Michelle Yeoh"},
            {"number": 3, "initials": "S S", "clue": "A female pig that swims — gone all Hollywood and started starring in very popular series.", "answer": "Sydney Sweeney", "aliases": ["sydney sweeney"], "reasoning": "Sydney (a city/name) + Sweeney (a name, sounds like sweeny) = Sydney Sweeney"},
        ]
    },
    # ── Game Show Busters ─────────────────────────────────────────────────────
    {
        "id": "gameshowbusters-001", "enabled": True, "title": "Game Show Busters",
        "topic": "famous TV game shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Game Show Busters. All famous TV game shows. Say the clues out loud.",
        "prize": "Email in. Winner gets a cheque for the right amount but made out to the wrong person.",
        "clues": [
            {"number": 1, "initials": "W W T B A M", "clue": "A bloke asking if he could possibly become very wealthy — had some help from a friend on the phone.", "answer": "Who Wants to be a Millionaire", "aliases": ["who wants to be a millionaire"], "reasoning": "Who + Wants + to + be + a + Millionaire = Who Wants to be a Millionaire"},
            {"number": 2, "initials": "T C", "clue": "That person who runs after you in a race — gone all brainy and started sitting behind a desk.", "answer": "The Chase", "aliases": ["the chase"], "reasoning": "the + chase (pursuit) = The Chase"},
            {"number": 3, "initials": "P", "clue": "Something that serves no purpose whatsoever — gone all intellectual and won a quiz.", "answer": "Pointless", "aliases": ["pointless"], "reasoning": "pointless (serving no purpose) = Pointless"},
        ]
    },
    {
        "id": "gameshowbusters-002", "enabled": True, "title": "Game Show Busters",
        "topic": "famous TV game shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Game Show Busters. Three more famous TV quizzes.",
        "prize": "Email in. Winner gets a lifetime supply of incorrect final answers.",
        "clues": [
            {"number": 1, "initials": "D O N D", "clue": "That thing you do when you make an agreement — someone's telling you not to do it. Peculiar request.", "answer": "Deal or No Deal", "aliases": ["deal or no deal"], "reasoning": "Deal + or + No + Deal = Deal or No Deal"},
            {"number": 2, "initials": "C", "clue": "A clock going backwards — people shouting letters at a screen on a weekday afternoon.", "answer": "Countdown", "aliases": ["countdown"], "reasoning": "countdown (counting down from a number) = Countdown"},
            {"number": 3, "initials": "T W L", "clue": "That thing you can't do when you're strong — gone all Anne Robinson and started being nasty.", "answer": "The Weakest Link", "aliases": ["the weakest link"], "reasoning": "the + weakest + link (a chain component) = The Weakest Link"},
        ]
    },
    {
        "id": "gameshowbusters-003", "enabled": True, "title": "Game Show Busters",
        "topic": "famous TV game shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Game Show Busters. Three more. All phonetic.",
        "prize": "Email in. Winner gets a consolation prize that's worse than nothing.",
        "clues": [
            {"number": 1, "initials": "C", "clue": "A word you shout when you've caught someone doing something — gone all Saturday teatime.", "answer": "Catchphrase", "aliases": ["catchphrase"], "reasoning": "catch + phrase = Catchphrase"},
            {"number": 2, "initials": "B", "clue": "A large round target — someone's throwing sharp things at it in a pub. Now it's a game show.", "answer": "Bullseye", "aliases": ["bullseye"], "reasoning": "bull's + eye (centre of a target) = Bullseye"},
            {"number": 3, "initials": "B B", "clue": "Something that's empty on the inside — gone all television and started rhyming things.", "answer": "Blankety Blank", "aliases": ["blankety blank"], "reasoning": "blankety + blank (empty space) = Blankety Blank"},
        ]
    },
    {
        "id": "gameshowbusters-004", "enabled": True, "title": "Game Show Busters",
        "topic": "famous TV game shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Game Show Busters. Three more classics.",
        "prize": "Email in. Winner gets a bonus question nobody can answer.",
        "clues": [
            {"number": 1, "initials": "T P I R", "clue": "The cost of a tin of beans — someone's guessing it without going over. Very tense.", "answer": "The Price is Right", "aliases": ["the price is right"], "reasoning": "the + price + is + right = The Price is Right"},
            {"number": 2, "initials": "B", "clue": "A place where you stop moving vehicles — gone all educational and started asking general knowledge questions.", "answer": "Blockbusters", "aliases": ["blockbusters"], "reasoning": "block (obstruction) + busters = Blockbusters"},
            {"number": 3, "initials": "P Y C R", "clue": "A suggestion that you gamble with flat pieces of paper — someone's doing it on a Saturday evening.", "answer": "Play Your Cards Right", "aliases": ["play your cards right"], "reasoning": "play + your + cards + right = Play Your Cards Right"},
        ]
    },
    {
        "id": "gameshowbusters-005", "enabled": True, "title": "Game Show Busters",
        "topic": "famous TV game shows", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Game Show Busters. Three more. All from the telly.",
        "prize": "Email in. Winner gets a parting gift and a handshake from the host.",
        "clues": [
            {"number": 1, "initials": "F T O", "clue": "Fifteen people — one of them is slowly getting removed from the room.", "answer": "Fifteen to One", "aliases": ["fifteen to one"], "reasoning": "fifteen + to + one = Fifteen to One"},
            {"number": 2, "initials": "3-2-1", "clue": "A countdown, going backwards from a small number. Someone in a robot costume is involved.", "answer": "3-2-1", "aliases": ["3-2-1", "three two one"], "reasoning": "3-2-1 (countdown) = 3-2-1"},
            {"number": 3, "initials": "B F H", "clue": "A large rotund bloke who has a very complete answer to every question. Very satisfied with it.", "answer": "Bob's Full House", "aliases": ["bobs full house", "bob's full house"], "reasoning": "Bob's + Full + House = Bob's Full House"},
        ]
    },
    # ── Castle Busters ────────────────────────────────────────────────────────
    {
        "id": "castlebusters-001", "enabled": True, "title": "Castle Busters",
        "topic": "famous UK castles", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Castle Busters. All famous UK castles. Say the clues out loud.",
        "prize": "Email in. Winner gets a portcullis that sticks.",
        "clues": [
            {"number": 1, "initials": "W C", "clue": "A place where the wind comes through a gap — gone all regal and put on a crown.", "answer": "Windsor Castle", "aliases": ["windsor castle"], "reasoning": "Windsor (winds-or) + Castle = Windsor Castle"},
            {"number": 2, "initials": "E C", "clue": "A city in Scotland full of festivals — it's got a massive fort on top of a volcanic rock.", "answer": "Edinburgh Castle", "aliases": ["edinburgh castle"], "reasoning": "Edinburgh (Scottish capital) + Castle = Edinburgh Castle"},
            {"number": 3, "initials": "L C", "clue": "A city in Yorkshire with a complicated football club — it's got a medieval fortress nearby.", "answer": "Leeds Castle", "aliases": ["leeds castle"], "reasoning": "Leeds (a city) + Castle = Leeds Castle"},
        ]
    },
    {
        "id": "castlebusters-002", "enabled": True, "title": "Castle Busters",
        "topic": "famous UK castles", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Castle Busters. Three more famous castles.",
        "prize": "Email in. Winner gets a drawbridge that won't lower.",
        "clues": [
            {"number": 1, "initials": "W C", "clue": "A place associated with conflict — gone all medieval and started charging tourists to visit.", "answer": "Warwick Castle", "aliases": ["warwick castle"], "reasoning": "Warwick (a town) + Castle = Warwick Castle"},
            {"number": 2, "initials": "B C", "clue": "A long stick used for hitting things — gone all Scottish and sat on a clifftop.", "answer": "Bamburgh Castle", "aliases": ["bamburgh castle"], "reasoning": "Bamburgh (a village in Northumberland) + Castle = Bamburgh Castle"},
            {"number": 3, "initials": "C C", "clue": "A Welsh word meaning fortress — gone all UNESCO and started attracting tourists.", "answer": "Caernarfon Castle", "aliases": ["caernarfon castle"], "reasoning": "Caernarfon (a Welsh town) + Castle = Caernarfon Castle"},
        ]
    },
    {
        "id": "castlebusters-003", "enabled": True, "title": "Castle Busters",
        "topic": "famous UK castles", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK"],
        "intro": "Castle Busters. Three more. All phonetic.",
        "prize": "Email in. Winner gets a turret with a very cold draught.",
        "clues": [
            {"number": 1, "initials": "B C", "clue": "A Scottish estate where a very famous family goes on holiday — tartan everywhere.", "answer": "Balmoral Castle", "aliases": ["balmoral castle"], "reasoning": "Balmoral (Scottish royal residence) + Castle = Balmoral Castle"},
            {"number": 2, "initials": "S C", "clue": "Something that's stopped moving — gone all Scottish and started overlooking a city.", "answer": "Stirling Castle", "aliases": ["stirling castle"], "reasoning": "Stirling (a Scottish city) + Castle = Stirling Castle"},
            {"number": 3, "initials": "D C", "clue": "That white stuff on a cliff face — gone all historical and started staring at France.", "answer": "Dover Castle", "aliases": ["dover castle"], "reasoning": "Dover (white cliffs) + Castle = Dover Castle"},
        ]
    },
    # ── Number Two Busters ────────────────────────────────────────────────────
    {
        "id": "numbertwobusters-001", "enabled": True, "title": "Number Two Busters",
        "topic": "things always known as second best", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Number Two Busters. All things that came second. Say the clues out loud.",
        "prize": "Email in. Winner gets a silver medal and nobody's attention.",
        "clues": [
            {"number": 1, "initials": "P", "clue": "A fizzy drink — not the one everyone prefers, but it keeps trying. Blind tests and everything.", "answer": "Pepsi", "aliases": ["pepsi"], "reasoning": "Pepsi (the second cola) = Pepsi"},
            {"number": 2, "initials": "B K", "clue": "A place where burgers are prepared — not the most famous one, but the flame-grilled one.", "answer": "Burger King", "aliases": ["burger king"], "reasoning": "Burger (a meat patty) + King (royalty) = Burger King"},
            {"number": 3, "initials": "A", "clue": "A car rental company — they try harder because they know they're not top of the pile.", "answer": "Avis", "aliases": ["avis"], "reasoning": "Avis (the car rental company, famous for 'We Try Harder') = Avis"},
        ]
    },
    {
        "id": "numbertwobusters-002", "enabled": True, "title": "Number Two Busters",
        "topic": "things always known as second best", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Number Two Busters. More runners-up. All phonetic.",
        "prize": "Email in. Winner gets a consolation prize and a very small podium.",
        "clues": [
            {"number": 1, "initials": "B", "clue": "A search engine — not the one everyone uses. Comes pre-installed on things and gets quietly removed.", "answer": "Bing", "aliases": ["bing"], "reasoning": "Bing (Microsoft's search engine, second to Google) = Bing"},
            {"number": 2, "initials": "Y", "clue": "A cowboy sound — but it's a website. Used to be a big deal. Still alive, just about.", "answer": "Yahoo", "aliases": ["yahoo"], "reasoning": "Yahoo (exclamation/search engine) = Yahoo"},
            {"number": 3, "initials": "B", "clue": "A small dark fruit from a bush — gone all mobile and started making phones with tiny keyboards.", "answer": "Blackberry", "aliases": ["blackberry"], "reasoning": "Blackberry (the fruit/the phone brand) = Blackberry"},
        ]
    },
    {
        "id": "numbertwobusters-003", "enabled": True, "title": "Number Two Busters",
        "topic": "things always known as second best", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Number Two Busters. Three more also-rans.",
        "prize": "Email in. Winner gets an honourable mention nobody will remember.",
        "clues": [
            {"number": 1, "initials": "B", "clue": "The video format that lost the war — now nobody can play it even if they wanted to.", "answer": "Betamax", "aliases": ["betamax", "beta max"], "reasoning": "Beta (the format) + max (maximum) = Betamax"},
            {"number": 2, "initials": "M", "clue": "A website where everyone used to be friends with a bloke called Tom. Gone quiet now.", "answer": "MySpace", "aliases": ["myspace"], "reasoning": "My + Space = MySpace"},
            {"number": 3, "initials": "A J", "clue": "A digital butler — you could ask it things, but Google came along and answered faster.", "answer": "Ask Jeeves", "aliases": ["ask jeeves", "askjeeves"], "reasoning": "Ask (to ask a question) + Jeeves (the famous butler) = Ask Jeeves"},
        ]
    },
    # ── Internet Slang Busters ────────────────────────────────────────────────
    {
        "id": "internetslangbusters-001", "enabled": True, "title": "Internet Slang Busters",
        "topic": "internet slang and online culture", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Internet Slang Busters. All modern online words and phrases. Say them out loud.",
        "prize": "Email in. Winner gets a verified tick and zero followers.",
        "clues": [
            {"number": 1, "initials": "G O A T", "clue": "A farmyard animal — gone all internet and decided it's the best there's ever been.", "answer": "GOAT", "aliases": ["goat"], "reasoning": "GOAT (Greatest Of All Time) = GOAT"},
            {"number": 2, "initials": "F O M O", "clue": "That feeling when everyone else is out having fun and you're at home knowing about it.", "answer": "FOMO", "aliases": ["fomo"], "reasoning": "FOMO (Fear Of Missing Out) = FOMO"},
            {"number": 3, "initials": "G V", "clue": "Something spreading very fast across the internet — not a disease, but behaves like one.", "answer": "Going Viral", "aliases": ["going viral"], "reasoning": "going + viral (spreading like a virus) = Going Viral"},
        ]
    },
    {
        "id": "internetslangbusters-002", "enabled": True, "title": "Internet Slang Busters",
        "topic": "internet slang and online culture", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Internet Slang Busters. Three more. All phonetic.",
        "prize": "Email in. Winner gets a notification they can't turn off.",
        "clues": [
            {"number": 1, "initials": "G", "clue": "When someone disappears from your life without warning — just stops replying. Vanished.", "answer": "Ghosting", "aliases": ["ghosting"], "reasoning": "ghosting (disappearing like a ghost) = Ghosting"},
            {"number": 2, "initials": "C B", "clue": "Something that gets you to look at it under false pretences — a misleading title on the internet.", "answer": "Clickbait", "aliases": ["clickbait"], "reasoning": "click + bait (lure) = Clickbait"},
            {"number": 3, "initials": "S", "clue": "A photograph of yourself, taken by yourself, on a stick or just an outstretched arm.", "answer": "Selfie", "aliases": ["selfie"], "reasoning": "selfie (self-photograph) = Selfie"},
        ]
    },
    {
        "id": "internetslangbusters-003", "enabled": True, "title": "Internet Slang Busters",
        "topic": "internet slang and online culture", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "Internet Slang Busters. Three final ones.",
        "prize": "Email in. Winner gets a DM that says 'hey'.",
        "clues": [
            {"number": 1, "initials": "T", "clue": "Something that's very popular right now — going up and up on the charts with no explanation.", "answer": "Trending", "aliases": ["trending"], "reasoning": "trending (becoming popular) = Trending"},
            {"number": 2, "initials": "H", "clue": "A symbol that turns a word into a category — the pound sign went all social media.", "answer": "Hashtag", "aliases": ["hashtag"], "reasoning": "hash (the # symbol) + tag = Hashtag"},
            {"number": 3, "initials": "T", "clue": "A person hiding behind a screen being horrible to strangers — not the kind that lives under bridges.", "answer": "Trolling", "aliases": ["trolling"], "reasoning": "trolling (harassing online, from troll) = Trolling"},
        ]
    },
    # ── YouTuber Busters ──────────────────────────────────────────────────────
    {
        "id": "youtuberbusters-001", "enabled": True, "title": "YouTuber Busters",
        "topic": "famous YouTubers", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "YouTuber Busters. All famous YouTubers. Say the clues out loud.",
        "prize": "Email in. Winner gets a subscribe button and zero new subscribers.",
        "clues": [
            {"number": 1, "initials": "M B", "clue": "A large carnivorous creature — gone all generous and started giving things away to random strangers.", "answer": "MrBeast", "aliases": ["mrbeast", "mr beast"], "reasoning": "Mr (a title) + Beast (large animal) = MrBeast"},
            {"number": 2, "initials": "K", "clue": "A British boxer — gone all gaming and started making music. Won't leave the internet alone.", "answer": "KSI", "aliases": ["ksi"], "reasoning": "KSI (Knowledge, Strength, Integrity — YouTuber name) = KSI"},
            {"number": 3, "initials": "Z", "clue": "A young woman — gone all beauty tutorial and taken over the internet in the early 2010s.", "answer": "Zoella", "aliases": ["zoella"], "reasoning": "Zoella (Zoe + -ella suffix) = Zoella"},
        ]
    },
    {
        "id": "youtuberbusters-002", "enabled": True, "title": "YouTuber Busters",
        "topic": "famous YouTubers", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "YouTuber Busters. Three more internet famous people.",
        "prize": "Email in. Winner gets a ring light and a total lack of content ideas.",
        "clues": [
            {"number": 1, "initials": "P", "clue": "A bloke from Sweden who plays games on camera and shouts at them. Very popular about it.", "answer": "PewDiePie", "aliases": ["pewdiepie"], "reasoning": "Pew (a church bench) + Die (to die) + Pie (pastry) = PewDiePie"},
            {"number": 2, "initials": "L P", "clue": "A man called Logan who jumped into things and filmed it. Caused quite a stir.", "answer": "Logan Paul", "aliases": ["logan paul"], "reasoning": "Logan (a name) + Paul (a name) = Logan Paul"},
            {"number": 3, "initials": "D P", "clue": "Blokes doing brilliant things — gone all sporty and started throwing balls through hoops very impressively.", "answer": "Dude Perfect", "aliases": ["dude perfect"], "reasoning": "Dude (a casual term for a man) + Perfect (flawless) = Dude Perfect"},
        ]
    },
    {
        "id": "youtuberbusters-003", "enabled": True, "title": "YouTuber Busters",
        "topic": "famous YouTubers", "difficulty": "easy", "office_safe": True,
        "region_relevance": ["UK", "US"],
        "intro": "YouTuber Busters. Three final ones.",
        "prize": "Email in. Winner gets one viral video and fifteen years of diminishing returns.",
        "clues": [
            {"number": 1, "initials": "C N", "clue": "A bloke with a camera and a van — drove around America filming things and made everyone jealous.", "answer": "Casey Neistat", "aliases": ["casey neistat"], "reasoning": "Casey (a name) + Neistat (a name) = Casey Neistat"},
            {"number": 2, "initials": "E C", "clue": "A young woman called Emma who drinks coffee and vlogs about doing very ordinary things.", "answer": "Emma Chamberlain", "aliases": ["emma chamberlain"], "reasoning": "Emma (a name) + Chamberlain (a name) = Emma Chamberlain"},
            {"number": 3, "initials": "D D", "clue": "A bloke called David who filmed his friends doing things and everyone found it brilliant for a while.", "answer": "David Dobrik", "aliases": ["david dobrik"], "reasoning": "David (a name) + Dobrik (a name) = David Dobrik"},
        ]
    },
]

def write_sets():
    # Find existing highest batch number
    batches_dir = ROOT / "data" / "batches"
    existing = sorted(batches_dir.glob("batch-*.yaml"))
    last_num = int(existing[-1].stem.split("-")[1]) if existing else 0

    # Write 3 sets per batch file
    batch_num = last_num
    for i in range(0, len(NEW_SETS), 3):
        batch_num += 1
        chunk = NEW_SETS[i:i+3]
        batch_path = batches_dir / f"batch-{batch_num:03d}.yaml"
        with open(batch_path, "w", encoding="utf-8") as f:
            yaml.dump(chunk, f, allow_unicode=True, sort_keys=False,
                      default_flow_style=False, width=2000)
        print(f"Wrote {batch_path.name}: {[s['id'] for s in chunk]}")

    # Append to main yaml
    main_yaml = ROOT / "data" / "rockbusters.yaml"
    with open(main_yaml, encoding="utf-8") as f:
        existing_data = yaml.safe_load(f)
    existing_ids = {s["id"] for s in existing_data}
    new_sets_to_add = [s for s in NEW_SETS if s["id"] not in existing_ids]
    existing_data.extend(new_sets_to_add)
    with open(main_yaml, "w", encoding="utf-8") as f:
        yaml.dump(existing_data, f, allow_unicode=True, sort_keys=False,
                  default_flow_style=False, width=2000)
    print(f"Added {len(new_sets_to_add)} sets to rockbusters.yaml")
    return len(new_sets_to_add)

if __name__ == "__main__":
    n = write_sets()
    print(f"Done: {n} new sets written")
