export const meta = {
  name: 'generate-rockbusters',
  description: 'Generate 730 Rockbusters question sets in Karl Pilkington phonetic style',
  phases: [
    { title: 'Generate batches', detail: 'Fan out 37 content agents, each writing 20 sets to batch files' },
    { title: 'Merge and export', detail: 'Concatenate batch files, write rockbusters.yaml, run export_json.py' },
  ],
}

const WIN_ROOT = 'C:\\Users\\BarryCheevers\\OneDrive - Anomali\\Desktop\\Fun\\Rockbusters'
const BASH_ROOT = '/c/Users/BarryCheevers/OneDrive\\ -\\ Anomali/Desktop/Fun/Rockbusters'

const CLUE_INSTRUCTIONS = `
ROCKBUSTERS CLUE-WRITING INSTRUCTIONS

A Rockbuster clue is a PHONETIC RIDDLE. The answer is found by SOUND, not spelling.

CORE RULE: Write clues as bad phonetic riddles where the scene, described out loud, sounds like the answer.

REQUIRED PROCESS FOR EVERY CLUE:
1. Take the answer
2. Split it into a phonetic phrase (what does it SOUND LIKE when spoken aloud?)
3. Check the phrase can be described as a silly little scene
4. Write the clue from the scene, not from the spelling
5. Verify: could someone say the clue out loud and HEAR the answer in the sounds?

GOOD PHONETIC SPLITS AND CLUE EXAMPLES:
- Whitney Houston: wet knee Houston → "That woman's leg joint has got soaking wet, and she's from Texas."
- Jude Bellingham: judge minus g + bell in ham → "The judge has lost the end of his job title, and there's a ringing thing inside some pig meat."
- Peshwari Naan: posh worry nan → "Me gran's panicking because she thinks she's too fancy now."
- Andy Burnham: and he burn ham → "Him over there has set fire to some pig meat. Don't know why."
- The Guardian: the guard Ian → "Ian's got someone watching over him. Keeping him safe and that."
- Benidorm: Ben in dorm → "Ben's gone to kip in the building where students sleep. That's all."
- Stockholm: stock home → "I've got loads of supplies but I'm keeping them all at my house."
- Haribo Starmix: Harry bow, star mix → "Some fella called Harry is doing archery near a space-themed sweet display."
- Rowntree's Randoms: round trees, randoms → "Them circular plants, right, they're a right odd bunch."
- Toxic Waste: toxic waist → "Right, that middle section of your body - it's full of chemicals."
- Rachel Reeves: Ray chill + leaves → "That bloke Ray is freezing, then he clears off."
- Kemi Badenoch: chem-y bad enough → "The scientist's looking at these chemicals going, they'll do."

DO NOT write spelling/letter puzzles. These are BAD:
BAD: "The letter J has attached itself to AWS."
BAD: "Add T to Roy."
BAD: "G is at the front of Greece."
These are mechanical letter puzzles, not Rockbusters. The clue must describe a SCENE.

AVOID using the answer word in the clue:
BAD: "The gums have wine on them." (uses answer word "gums")
GOOD: "That bit in your mouth where the teeth sort of live, it's been on the red and white booze."

EVEN IF THE PHONETIC SPLIT IS SIMPLE (like T + Roy = Troy), still describe it as a scene:
BAD: "T plus Roy."
GOOD: "That lad Roy's got one of those cross-shaped things standing in front of him. Alright?"

TONE: Karl Pilkington voice. Casual, slightly confused, oddly logical. Like someone working it out.
Useful phrases (mix these, don't overuse any one):
"Right..." / "Easy one this." / "That's all." / "Bit weird." / "Sort of works." / "Say it out loud."
"Alright?" / "Don't overthink it." / "Near enough." / "You know what I mean." / "Leave it."

SENTENCE VARIETY - vary all three clues per set:
BAD (all same pattern): "X is doing Y. What's going on there? / A is doing B. What's going on there? / P is doing Q. What's going on there?"
GOOD: Mix of statements, questions, short openers, asides. Each clue should feel different from the others.

OFFICE SAFE: No swearing, no sexual content, no insults to groups, no cruel jokes. Celebrities, food, sport, cities, history all fine.

PICK ANSWERS WITH GOOD PHONETIC SPLITS. If the phonetic split feels weak or forced, choose a different answer from the suggestions.

PRIZE LINES: Daft fake early-2000s prizes. Make each different. Examples:
"Email in. Winner gets a copy of Shrek on DVD and a keyring from a service station."
"Email in. Winner gets an AOL trial disc and a mug from a company that no longer exists."
"Email in. Winner gets a Blockbuster loyalty card and a Now 52 cassette."
"Email in. Winner gets a printed photo from a disposable camera, framed."
"Email in. Winner gets a DVD copy of The Full Monty and some Value biscuits."
"Email in. Winner gets a signed letter from someone off Emmerdale, possibly."
`

const YAML_EXAMPLE = `
EXACT YAML FORMAT - follow this precisely including quoting rules:

- id: foodbusters-001
  enabled: true
  title: Foodbusters
  topic: British dishes
  difficulty: medium
  office_safe: true
  region_relevance:
    - UK
  intro: "Right, Foodbusters. Rockbusters but it's all British grub."
  prize: "Email in. Winner gets a tin of Quality Street from a petrol station."
  clues:
    - number: 1
      initials: F C
      clue: "Right, that swimming thing's been knocked over, right, and it's landed on some of them crispy shredded things. Bit of a mess."
      answer: Fish and Chips
      aliases:
        - fish and chips
        - fish & chips
      reasoning: "fish (swimming thing, knocked over) and chips (crispy shredded things) = Fish and Chips"
    - number: 2
      initials: S E
      clue: "That Scottish thing, the bloke's wearing a kilt and inside it there's an actual egg. Don't ask."
      answer: Scotch Egg
      aliases:
        - scotch egg
        - scotch eggs
      reasoning: "Scotch (Scottish) + egg = Scotch Egg"
    - number: 3
      initials: B W
      clue: "The shepherd's gone, right, and in his place there's just a fence post. Someone's eaten all the lamb."
      answer: Beef Wellington
      aliases:
        - beef wellington
      reasoning: "beef (not lamb) + Wellington (famous Duke, the boot) = Beef Wellington"

YAML QUOTING RULES (important):
- intro: ALWAYS double-quoted (contains commas/apostrophes)
- prize: ALWAYS double-quoted
- clue: ALWAYS double-quoted
- reasoning: ALWAYS double-quoted
- answer: NOT quoted (plain text)
- aliases: NOT quoted (lowercase, plain text)
- initials: NOT quoted (e.g.: W G or B B or T or J B or F C)
- difficulty: NOT quoted (easy, medium, or hard)
- id: NOT quoted
- enabled: NOT quoted (true)
- office_safe: NOT quoted (true)
- numbers (1, 2, 3): NOT quoted
- If clue text contains a double-quote character, use single quotes to wrap the clue or escape the double-quote with backslash
`

const BATCHES = [
  { num: 1,  prefix: 'sweetbusters',     start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: 'UK sweets and confectionery', suggest: 'Maltesers, Smarties, Curly Wurly, Fruit Pastilles, Skittles, Bounty, Kit Kat, Flake, Lion Bar, Crunchie, Dime Bar, Wispa, Toblerone, Aero, Milkybar, Double Decker, Rhubarb and Custard, Cola Bottles, Parma Violets, Refreshers, Starburst, Sherbet Fountain, Gobstopper, Humbugs, Polos, Black Jacks, Fruit Salad, Chewits, Pear Drops, Aniseed Balls, Liquorice Allsorts, Fudge, Caramel, Toffee, Space Dust, Flying Saucers, Candy Necklace, Jelly Worms, Fizzy Belts, Foam Shrimps' },
  { num: 2,  prefix: 'citybusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US', 'Europe'], theme: 'European cities', suggest: 'Barcelona, Madrid, Vienna, Berlin, Amsterdam, Brussels, Prague, Budapest, Warsaw, Athens, Lisbon, Copenhagen, Stockholm, Oslo, Helsinki, Dublin, Edinburgh, Cardiff, Lyon, Milan, Naples, Porto, Seville, Venice, Florence, Nice, Bruges, Dubrovnik, Reykjavik, Tallinn, Riga, Vilnius, Bern, Zurich, Geneva, Antwerp, Rotterdam, Marseille, Bratislava' },
  { num: 3,  prefix: 'filmbusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'classic films from the 1970s through 1990s', suggest: 'Jaws, Rocky, Alien, Psycho, Titanic, Gladiator, Braveheart, Goodfellas, Fargo, Forrest Gump, Pulp Fiction, Toy Story, Home Alone, Die Hard, Terminator, Ghostbusters, Jurassic Park, Speed, Rain Man, Misery, Basic Instinct, Hook, The Mask, Robocop, Beetlejuice, Grease' },
  { num: 4,  prefix: 'filmbusters',      start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'modern films from 2000 onwards', suggest: 'Inception, Shrek, Elf, Mean Girls, Finding Nemo, Frozen, Avatar, Interstellar, The Revenant, Deadpool, Black Panther, Coco, Parasite, Joker, Dune, Oppenheimer, Barbie, Saltburn, Poor Things, Wonka, Mamma Mia, Paddington, Rocketman, Bohemian Rhapsody, Yesterday, Belfast, Spencer' },
  { num: 5,  prefix: 'bandbusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'classic British bands and solo artists', suggest: 'The Beatles, Rolling Stones, Led Zeppelin, Pink Floyd, David Bowie, The Clash, Oasis, Blur, Radiohead, The Prodigy, Amy Winehouse, Adele, Ed Sheeran, Coldplay, Arctic Monkeys, The Kinks, The Smiths, Pulp, Supergrass, Elastica, Portishead, Massive Attack, The Cure, The Jam, Depeche Mode, Primal Scream, Suede, Gene' },
  { num: 6,  prefix: 'bandbusters',      start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'international music acts from USA and beyond', suggest: 'Nirvana, Eminem, Beyonce, Lady Gaga, Taylor Swift, Rihanna, Kanye West, Jay Z, Drake, Kendrick Lamar, ABBA, Madonna, Michael Jackson, Bruce Springsteen, Fleetwood Mac, Eagles, AC DC, Metallica, Daft Punk, Guns N Roses, Blink 182, Green Day, Red Hot Chili Peppers, Pearl Jam, Soundgarden' },
  { num: 7,  prefix: 'footballbusters',  start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'famous footballers British and international', suggest: 'David Beckham, Wayne Rooney, Steven Gerrard, Frank Lampard, Michael Owen, Gary Lineker, Alan Shearer, Paul Scholes, Ryan Giggs, Peter Schmeichel, Thierry Henry, Zinedine Zidane, Ronaldinho, Pele, Diego Maradona, Lionel Messi, Cristiano Ronaldo, Marcus Rashford, Harry Kane, Bukayo Saka, Jamie Vardy, Dele Alli' },
  { num: 8,  prefix: 'tvbusters',        start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'classic and modern UK TV shows', suggest: 'Eastenders, Coronation Street, Emmerdale, Hollyoaks, Only Fools and Horses, Blackadder, Fawlty Towers, Dads Army, The Office, Peaky Blinders, Downton Abbey, Doctor Who, Sherlock, Broadchurch, Line of Duty, Fleabag, Derry Girls, The IT Crowd, Top Gear, Trigger Happy TV, Spaced, Green Wing, Hustle, Wire in the Blood' },
  { num: 9,  prefix: 'tvbusters',        start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'popular US TV shows', suggest: 'Friends, The Simpsons, Seinfeld, Breaking Bad, The Wire, Game of Thrones, The Sopranos, Lost, Desperate Housewives, Greys Anatomy, House, NCIS, CSI, Suits, Succession, Stranger Things, Yellowstone, Ozark, The Americans, Homeland, Frasier, Cheers, Will and Grace, Sex and the City, How I Met Your Mother' },
  { num: 10, prefix: 'foodbusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'British dishes and classic UK food', suggest: 'Fish and Chips, Chicken Tikka Masala, Beef Wellington, Yorkshire Pudding, Scotch Egg, Shepherds Pie, Bangers and Mash, Toad in the Hole, Spotted Dick, Sticky Toffee Pudding, Jam Roly Poly, Bread and Butter Pudding, Macaroni Cheese, Cottage Pie, Cauliflower Cheese, Bubble and Squeak, Welsh Rarebit, Pot Noodle, Cornish Pasty, Ploughmans Lunch' },
  { num: 11, prefix: 'animalbusters',    start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'land animals from around the world', suggest: 'Hippopotamus, Rhinoceros, Chimpanzee, Crocodile, Kangaroo, Cheetah, Flamingo, Penguin, Giraffe, Porcupine, Armadillo, Chameleon, Platypus, Narwhal, Capybara, Wolverine, Aardvark, Pangolin, Tasmanian Devil, Meerkat, Warthog, Hyena, Meerkat, Manatee' },
  { num: 12, prefix: 'countrybusters',   start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'countries of the world', suggest: 'Portugal, Romania, Slovakia, Slovenia, Bulgaria, Lithuania, Estonia, Latvia, Moldova, Montenegro, Albania, Bosnia, Croatia, Serbia, Iceland, Norway, Denmark, Finland, Switzerland, Cambodia, Bolivia, Ecuador, Paraguay, Uruguay, Madagascar, Mozambique, Zimbabwe, Zambia' },
  { num: 13, prefix: 'sportbusters',     start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'famous sports personalities UK and beyond', suggest: 'Roger Federer, Tiger Woods, Usain Bolt, Muhammad Ali, Mike Tyson, Serena Williams, Andy Murray, Mo Farah, Paula Radcliffe, Jessica Ennis, Kelly Holmes, Linford Christie, Daley Thompson, Steve Redgrave, Carl Lewis, Denise Lewis, Michael Johnson, Haile Gebrselassie, Derek Redmond, Jonathan Edwards' },
  { num: 14, prefix: 'politicbusters',   start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'UK politicians past and present', suggest: 'Boris Johnson, Theresa May, David Cameron, Gordon Brown, Tony Blair, John Major, Margaret Thatcher, Harold Wilson, Jim Callaghan, Ted Heath, Alistair Darling, Peter Mandelson, Jack Straw, Robin Cook, Michael Heseltine, Norman Tebbit, Alastair Campbell, Geoffrey Howe, Michael Howard, William Hague, Keir Starmer, Ed Miliband' },
  { num: 15, prefix: 'actorbusters',     start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'British film and TV actors', suggest: 'Hugh Grant, Colin Firth, Judi Dench, Helen Mirren, Emma Thompson, Kate Winslet, Benedict Cumberbatch, Tom Hardy, Daniel Craig, Keira Knightley, Michael Caine, Sean Connery, Roger Moore, Peter Sellers, Alec Guinness, Maggie Smith, Ian McKellen, Anthony Hopkins, Richard Burton, Peter OToole, Ralph Fiennes, Gary Oldman' },
  { num: 16, prefix: 'bookbusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'books authors and literary characters', suggest: 'Harry Potter, Hermione Granger, Ron Weasley, Albus Dumbledore, Voldemort, Severus Snape, Sherlock Holmes, Doctor Watson, Bilbo Baggins, Frodo Baggins, Gandalf, Elizabeth Bennet, Mr Darcy, Heathcliff, Jane Eyre, Oliver Twist, Fagin, Ebenezer Scrooge, Long John Silver, Captain Hook, Robinson Crusoe' },
  { num: 17, prefix: 'holidaybusters',   start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: 'British holiday destinations abroad', suggest: 'Majorca, Menorca, Ibiza, Tenerife, Lanzarote, Gran Canaria, Corfu, Crete, Rhodes, Cyprus, Malta, Tunisia, Turkey, Morocco, Egypt, Barbados, Jamaica, Cuba, Bali, Thailand, Benidorm, Marbella, Algarve, Tuscany, Amalfi, Fuerteventura, Magaluf' },
  { num: 18, prefix: 'drinkbusters',     start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: 'drinks beers wines spirits and soft drinks', suggest: 'Guinness, Stella Artois, Kronenbourg, Fosters, Carling, Carlsberg, Tennents, San Miguel, Peroni, Heineken, Budweiser, Corona, Becks, Strongbow, Kopparberg, Baileys, Prosecco, Aperol Spritz, Pimms, Shandy Bass, Tizer, Vimto, Dandelion and Burdock, Lucozade, Ribena, Irn Bru' },
  { num: 19, prefix: 'citybusters',      start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US', 'Global'], theme: 'major cities outside Europe', suggest: 'Istanbul, Cairo, Dubai, Mumbai, Bangkok, Singapore, Tokyo, Seoul, Beijing, Shanghai, Hong Kong, Sydney, Melbourne, Toronto, New York, Los Angeles, Chicago, Miami, Las Vegas, San Francisco, Mexico City, Buenos Aires, Rio de Janeiro, Cape Town, Johannesburg, Nairobi' },
  { num: 20, prefix: 'teambusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'football clubs and sports teams', suggest: 'Manchester United, Manchester City, Arsenal, Chelsea, Liverpool, Tottenham Hotspur, Newcastle United, Everton, Aston Villa, Leeds United, West Ham, Leicester City, Southampton, Brighton, Crystal Palace, Norwich City, Burnley, Sheffield United, Wolverhampton Wanderers, Brentford, Nottingham Forest, Middlesbrough' },
  { num: 21, prefix: 'placebusters',     start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: 'UK places landmarks and tourist attractions', suggest: 'Stonehenge, Big Ben, Tower Bridge, Buckingham Palace, Windsor Castle, Hadrians Wall, Lake District, Peak District, Yorkshire Dales, Dartmoor, Snowdonia, Ben Nevis, Loch Ness, Giants Causeway, Blackpool Tower, Wembley Stadium, Lords Cricket Ground, Glastonbury, Alton Towers, Legoland Windsor, The Eden Project, Durham Cathedral' },
  { num: 22, prefix: 'techbusters',      start: 1,  count: 20, difficulty: 'easy',   region: ['UK', 'US'], theme: 'technology brands products and internet companies', suggest: 'Google, Amazon, Microsoft, Apple, Facebook, Twitter, Instagram, TikTok, YouTube, Netflix, Spotify, Uber, Airbnb, LinkedIn, Snapchat, WhatsApp, Zoom, Slack, Dropbox, PayPal, Wikipedia, Reddit, Twitch, Discord, Pinterest, Ebay, Etsy, Deliveroo' },
  { num: 23, prefix: 'nostalgiabusters', start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: '1980s and 1990s nostalgia gadgets tech and pop culture', suggest: 'Tamagotchi, Game Boy, Walkman, VHS, Teletext, Ceefax, MiniDisc, Floppy Disk, Dial Up Internet, AOL, ICQ, Netscape, Napster, Friends Reunited, Bebo, MySpace, Kazaa, Encarta, Sega Mega Drive, Super Nintendo, Woolworths, Blockbuster Video, HMV, Woolies, Now Thats What I Call Music' },
  { num: 24, prefix: 'noughtybusters',   start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: '2000s and 2010s pop culture and reality TV', suggest: 'Big Brother, Pop Idol, X Factor, Britains Got Talent, The Apprentice, Masterchef, Come Dine With Me, Gogglebox, Made in Chelsea, TOWIE, Geordie Shore, Jersey Shore, Pimp My Ride, The OC, Dawsons Creek, Hollyoaks, Byker Grove, Grange Hill, Saved by the Bell, Laguna Beach, MySpace, Bebo' },
  { num: 25, prefix: 'cartoonbusters',   start: 1,  count: 20, difficulty: 'easy',   region: ['UK', 'US'], theme: 'animated films and classic cartoons', suggest: 'The Lion King, Aladdin, Beauty and the Beast, The Little Mermaid, Cinderella, Snow White, Bambi, Dumbo, Pinocchio, Mulan, Tarzan, Hercules, Lilo and Stitch, The Emperor s New Groove, The Incredibles, WALL E, Up, Inside Out, Moana, Ratatouille, Monsters Inc, A Bugs Life, Finding Nemo, Shrek' },
  { num: 26, prefix: 'snackbusters',     start: 1,  count: 20, difficulty: 'easy',   region: ['UK'], theme: 'crisps snacks biscuits and fast food', suggest: 'Pringles, Wotsits, Quavers, Hula Hoops, Skips, Monster Munch, Discos, Doritos, Kettle Chips, McCoys, Frazzles, Nik Naks, Twiglets, Jaffa Cakes, Club Biscuit, Penguin, Bourbon, Custard Cream, Garibaldi, Jammy Dodger, Rich Tea, Hobnob, Digestive, Ginger Nut, Caramel Wafer' },
  { num: 27, prefix: 'celebbusters',     start: 1,  count: 20, difficulty: 'medium', region: ['UK'], theme: 'classic British celebrities and entertainers', suggest: 'Rod Stewart, Robbie Williams, Elton John, Tom Jones, Cliff Richard, Paul McCartney, Mick Jagger, Keith Richards, Eric Clapton, Ozzy Osbourne, Jimmy Page, Roger Daltrey, Pete Townshend, Robert Plant, Brian May, Freddie Mercury, John Lennon, George Harrison, Ringo Starr, Noel Gallagher, Liam Gallagher' },
  { num: 28, prefix: 'songbusters',      start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'iconic pop songs and classic albums', suggest: 'Bohemian Rhapsody, Stairway to Heaven, Hotel California, Smells Like Teen Spirit, Purple Rain, Like a Virgin, Thriller, Billie Jean, Man in the Mirror, Don t Stop Me Now, We Are the Champions, Radio Ga Ga, I Want to Break Free, Yesterday, Hey Jude, Let It Be, Come Together, Something, Eleanor Rigby, Penny Lane' },
  { num: 29, prefix: 'historybusters',   start: 1,  count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'historical figures from ancient to modern', suggest: 'Julius Caesar, Napoleon Bonaparte, Alexander the Great, Cleopatra, Christopher Columbus, Galileo Galilei, Isaac Newton, Charles Darwin, Albert Einstein, Winston Churchill, Adolf Hitler, Joseph Stalin, Genghis Khan, Attila the Hun, Richard the Lionheart, Henry VIII, Elizabeth I, Mary Queen of Scots, Oliver Cromwell, William the Conqueror' },
  { num: 30, prefix: 'bandbusters',      start: 41, count: 20, difficulty: 'easy',   region: ['UK'], theme: 'pop groups boybands and girl groups', suggest: 'Take That, Boyzone, Westlife, Backstreet Boys, New Kids on the Block, N Sync, Spice Girls, Sugababes, Girls Aloud, All Saints, Atomic Kitten, B Witched, S Club 7, Blue, Hear Say, Liberty X, One Direction, Little Mix, The Wanted, Five, East 17, Let Loose' },
  { num: 31, prefix: 'animalbusters',    start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US', 'Global'], theme: 'sea creatures and birds', suggest: 'Bottlenose Dolphin, Blue Whale, Great White Shark, Hammerhead Shark, Manta Ray, Sea Horse, Octopus, Squid, Jellyfish, Lobster, Crab, Oyster, Puffin, Albatross, Pelican, Peacock, Toucan, Kingfisher, Hummingbird, Parrot, Macaw, Flamingo, Pelican, Gannet, Cormorant' },
  { num: 32, prefix: 'foodbusters',      start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'puddings desserts and sweet dishes', suggest: 'Sticky Toffee Pudding, Eton Mess, Pavlova, Profiteroles, Chocolate Fondant, Tiramisu, Creme Brulee, Rice Pudding, Jam Roly Poly, Treacle Tart, Rhubarb Crumble, Apple Pie, Bread Pudding, Summer Pudding, Trifle, Cheesecake, Banoffee Pie, Key Lime Pie, Lemon Meringue Pie, Black Forest Gateau' },
  { num: 33, prefix: 'filmbusters',      start: 41, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'British comedy films and cult classics', suggest: 'Shaun of the Dead, Hot Fuzz, The Worlds End, Monty Python and the Holy Grail, Life of Brian, Withnail and I, Four Weddings and a Funeral, Notting Hill, About a Boy, Love Actually, Bridget Jones s Diary, Bend It Like Beckham, Billy Elliot, Calendar Girls, Brassed Off, The Full Monty, East Is East, Trainspotting, Lock Stock and Two Smoking Barrels, Snatch' },
  { num: 34, prefix: 'sportbusters',     start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US'], theme: 'tennis players golfers boxers and other sports personalities', suggest: 'Boris Becker, Steffi Graf, Pete Sampras, Andre Agassi, John McEnroe, Jimmy Connors, Bjorn Borg, Tiger Woods, Nick Faldo, Colin Montgomerie, Sandy Lyle, Seve Ballesteros, Muhammad Ali, Joe Frazier, George Foreman, Evander Holyfield, Floyd Mayweather, Lennox Lewis, Frank Bruno, Amir Khan' },
  { num: 35, prefix: 'placebusters',     start: 21, count: 20, difficulty: 'medium', region: ['UK', 'US', 'Global'], theme: 'world geography rivers mountains and natural wonders', suggest: 'Niagara Falls, Grand Canyon, Great Barrier Reef, Amazon River, Sahara Desert, Mount Everest, Victoria Falls, Great Wall of China, Machu Picchu, Angkor Wat, Taj Mahal, Eiffel Tower, Colosseum, Acropolis, Sydney Opera House, Statue of Liberty, Golden Gate Bridge, Empire State Building, Burj Khalifa, Mount Kilimanjaro' },
  { num: 36, prefix: 'culturebusters',   start: 1,  count: 20, difficulty: 'hard',   region: ['UK', 'US'], theme: 'scientists artists royals and cultural figures', suggest: 'Isaac Newton, Stephen Hawking, Marie Curie, Charles Darwin, Nikola Tesla, Leonardo da Vinci, Michelangelo, Rembrandt, Pablo Picasso, Vincent van Gogh, Salvador Dali, Andy Warhol, Queen Elizabeth II, Prince Charles, Prince William, Princess Diana, Kate Middleton, Meghan Markle, Prince Harry, Prince Philip' },
  { num: 37, prefix: 'mixedbusters',     start: 1,  count: 10, difficulty: 'medium', region: ['UK', 'US'], theme: 'mixed bonus sets - creative phonetic wordplay on any topic not yet covered', suggest: 'everyday phrases, compound words, idioms, place names, brand names, anything with a strong phonetic split - be creative' },
]

const pad3 = n => String(n).padStart(3, '0')

phase('Generate batches')

const genResults = await parallel(BATCHES.map(b => () => {
  const ids = Array.from({length: b.count}, (_, i) => b.prefix + '-' + pad3(b.start + i))
  const regionStr = b.region.join(', ')
  const batchFile = WIN_ROOT + '\\data\\batches\\batch-' + pad3(b.num) + '.yaml'

  const prompt = `You are generating content for the Rockbusters workplace quiz game. Your job is to generate exactly ${b.count} quiz sets.

THEME: ${b.theme}
DIFFICULTY: ${b.difficulty}
REGION RELEVANCE: ${regionStr}

IDs TO USE (in this exact order - use each one exactly as written):
${ids.join('\n')}

SUGGESTED ANSWERS (pick ones with good phonetic splits - change any that won't work):
${b.suggest}

${CLUE_INSTRUCTIONS}

${YAML_EXAMPLE}

YOUR TASK:
Generate exactly ${b.count} complete Rockbusters sets following the YAML format above.

Requirements:
- Use the IDs provided above, in order
- Each set has exactly 3 clues
- The title field should reflect the theme (e.g. "Sweetbusters", "Filmbusters", "Bandbusters")
- Vary the intro lines - not all should start with "Right,"
- Use a different prize line for each set
- Within each set, vary the 3 clues in structure and endings
- The reasoning field must show the phonetic split clearly (like "wet knee + Houston = Whitney Houston")
- Choose answers where the phonetic split genuinely works when spoken aloud
- If a suggested answer has a weak phonetic split, choose a different one

Write all ${b.count} sets as valid YAML to this file:
${batchFile}

The file must contain ONLY valid YAML (starting with "- id: ${ids[0]}"), with no text before or after.
After writing, output exactly: DONE: batch ${b.num} (${b.count} sets written)`

  return agent(prompt, { label: 'batch-' + b.num + ':' + b.theme.slice(0, 30), phase: 'Generate batches' })
}))

log('All ' + BATCHES.length + ' content batches complete. Starting merge.')

phase('Merge and export')

const totalSets = BATCHES.reduce((sum, b) => sum + b.count, 0)

const mergePrompt = `You need to merge ${BATCHES.length} YAML batch files into one rockbusters.yaml and run the export script.

The project is at: ${WIN_ROOT}

STEP 1: Concatenate all batch files using Bash. Run this command:
cat ${BASH_ROOT}/data/batches/batch-*.yaml > ${BASH_ROOT}/data/rockbusters.yaml

If that fails (e.g. path issues), alternatively use Python:
python -c "
import os, glob
root = r'${WIN_ROOT}'
files = sorted(glob.glob(os.path.join(root, 'data', 'batches', 'batch-*.yaml')))
with open(os.path.join(root, 'data', 'rockbusters.yaml'), 'w', encoding='utf-8') as out:
    for f in files:
        with open(f, encoding='utf-8') as inp:
            content = inp.read().strip()
            out.write(content)
            out.write('\\n\\n')
print(f'Merged {len(files)} files')
"

STEP 2: Run the export script to generate the JSON files for the frontend:
cd "${WIN_ROOT.replace(/\\/g, '/')}" && python scripts/export_json.py
or equivalently:
cd "${BASH_ROOT}" && python scripts/export_json.py

STEP 3: Check the output - it should say "Exported ${totalSets} sets" (or close to it).

STEP 4: Report the result - how many sets were exported, and confirm the files exist:
- data/rockbusters.yaml
- docs/data/rockbusters.json
- docs/data/rockbusters-answers.json

If there are any YAML parsing errors, report which batch file caused the issue so it can be fixed.`

await agent(mergePrompt, { label: 'merge-and-export', phase: 'Merge and export' })

log('Rockbusters content generation complete!')
