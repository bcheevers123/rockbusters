import yaml

with open(r'data/rockbusters.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Map of id -> new intro (Karl Pilkington, theme-only, no sequence reference, max 2 sentences)
new_intros = {
    # footballbusters
    'footballbusters-019': "Footballbusters. Famous players, phonetic clues. Give it a go.",
    'footballbusters-020': "Footballbusters. Three legends hiding in the sounds. See if you can get them.",
    'footballbusters-016': "Footballbusters. Famous names from the world of football. Say the clues out loud.",
    'footballbusters-010': "Footballbusters. Legendary players, all hiding in the phonetics. Have a go.",
    'footballbusters-017': "Footballbusters. Three footballing legends to find. Say each one out loud.",

    # historybusters
    'historybusters-018': "Historybusters. All famous faces from history. Say the clues out loud and you'll hear them.",
    'historybusters-020': "Historybusters. Famous people from the history books, all phonetic. Give it your best shot.",
    'historybusters-010': "Historybusters. Three more names from the past. Could be ancient, could be more recent.",
    'historybusters-019': "Historybusters. Big names from history, all wrapped up phonetically. Have a go.",

    # gamebusters
    'gamebusters-020': "Gamebusters. All games, video games, board games, the lot. Say each clue out loud.",
    'gamebusters-019': "Gamebusters. Gaming answers hiding in the sounds. Say it out loud, not in your head.",
    'gamebusters-010': "Gamebusters. Three clues, all gaming. Could be old, could be new. Off you go.",
    'gamebusters-017': "Gamebusters. Gaming clues done phonetically. You know the routine by now.",
    'gamebusters-009': "Gamebusters. Phonetic clues, gaming answers. Say each one out loud.",
    'gamebusters-011': "Gamebusters. Three games hiding in the sounds. Give it a go.",

    # citybusters
    'citybusters-018': "Citybusters. European cities hiding in the phonetic clues. Say them out loud.",
    'citybusters-020': "Citybusters. Three European cities, all phonetically disguised. Off you go.",
    'citybusters-015': "Citybusters. All European cities, all phonetic riddles. Have a crack.",

    # phrasebusters
    'phrasebusters-005': "Phrasebusters. All common English phrases and idioms. The phrase is hiding in the sounds.",
    'phrasebusters-016': "Phrasebusters. Everyday idioms and expressions, phonetically disguised. Off you go.",
    'phrasebusters-018': "Phrasebusters. Common phrases hiding in the clues. Say them out loud.",
    'phrasebusters-010': "Phrasebusters. Three idioms, all hiding in the phonetic clues. Have a think.",
    'phrasebusters-009': "Phrasebusters. Everyday phrases wrapped up in phonetic clues. Say each one out loud.",
    'phrasebusters-015': "Phrasebusters. Well-known expressions, all phonetically scrambled. You'll hear them if you say them.",
    'phrasebusters-020': "Phrasebusters. Three common phrases to find. The sounds are doing all the work.",
    'phrasebusters-019': "Phrasebusters. Everyday phrases and idioms, all phonetically disguised. Off you go.",

    # animalbusters
    'animalbusters-019': "Animalbusters. Land animals hiding in these phonetic clues. Say each one out loud.",
    'animalbusters-018': "Animalbusters. All land creatures, all phonetically disguised. Have a go.",
    'animalbusters-010': "Animalbusters. Animals from around the world, all wrapped up phonetically.",
    'animalbusters-020': "Animalbusters. Three land animals to find. The sounds will tell you what they are.",

    # biologybusters
    'biologybusters-003': "Biologybusters. More biology terms hiding in the sounds. Say the clues out loud or you'll get nowhere.",

    # placebusters
    'placebusters-010': "Placebusters. All famous UK landmarks and tourist spots. Say them out loud.",
    'placebusters-017': "Placebusters. UK landmarks and tourist attractions, all phonetically hidden. Off you go.",
    'placebusters-015': "Placebusters. Famous UK spots phonetically disguised. Say each clue out loud.",
    'placebusters-008': "Placebusters. UK landmarks and famous places. The name is hiding in the sounds.",
    'placebusters-005': "Placebusters. Famous UK spots and landmarks. Say the clues out loud and you'll hear where they are.",
    'placebusters-020': "Placebusters. Three UK landmarks to find. It's all in the sounds, not the spelling.",

    # mixedbusters
    'mixedbusters-019': "Mixedbusters. Three phonetic clues, the lot of them. Work it out by sound.",
    'mixedbusters-006': "Mixedbusters. All sorts, all phonetic. Could be anything. Say each one out loud.",
    'mixedbusters-018': "Mixedbusters. Three phonetic clues, three different answers. Have a go.",
    'mixedbusters-014': "Mixedbusters. All sorts in here. Say them out loud, that's all there is to it.",
    'mixedbusters-010': "Mixedbusters. Three phonetic clues. Don't overthink it, say it out loud.",
    'mixedbusters-009': "Mixedbusters. Phonetic clues, mixed bag of answers. Say each one and you'll get there.",

    # pubbusters
    'pubbusters-006': "Pubbusters. All British pub names and pub culture. Say the clues out loud.",
    'pubbusters-015': "Pubbusters. Pub names and pub games hiding in these phonetic clues. Have a go.",
    'pubbusters-011': "Pubbusters. Phonetic clues, all pub-themed. Say them out loud.",
    'pubbusters-019': "Pubbusters. Three phonetic clues, all about pubs. Say them aloud.",
    'pubbusters-010': "Pubbusters. British pub culture in phonetic form. Say each one out loud.",
    'pubbusters-018': "Pubbusters. Pub names and pub games, all phonetically scrambled. Have a crack.",

    # holidaybusters
    'holidaybusters-019': "Holidaybusters. British holiday destinations abroad, all hiding in the phonetics. Have a go.",

    # tvbusters
    'tvbusters-017': "TVbusters. Classic British telly programmes, all phonetically disguised. Give it a go.",
    'tvbusters-015': "TVbusters. British programmes hiding in the clues. Say each one out loud.",
    'tvbusters-007': "TVbusters. British telly, phonetic clues. Say them out loud, that's the whole trick.",
    'tvbusters-010': "TVbusters. Classic British programmes, all phonetically scrambled. Off you go.",
    'tvbusters-012': "TVbusters. More British programmes in phonetic disguise. Have a crack.",
    'tvbusters-018': "TVbusters. British telly hiding in the sounds. Say the clues out loud.",
    'tvbusters-020': "TVbusters. Classic British telly, all phonetic. Make it count.",
    'tvbusters-014': "TVbusters. British programmes phonetically wrapped up. You're either very good at this or you've been guessing.",

    # foodbusters
    'foodbusters-020': "Foodbusters. World dishes hiding in the phonetic clues. Say them out loud and you'll get there.",
    'foodbusters-015': "Foodbusters. All world food, all phonetic. Say these out loud.",
    'foodbusters-017': "Foodbusters. Dishes from around the world, all phonetically disguised. Have a go.",
    'foodbusters-019': "Foodbusters. World cuisine hiding in the clues. Say each one out loud.",
    'foodbusters-010': "Foodbusters. All international grub, all phonetic. You'll know these when you hear them.",

    # artbusters
    'artbusters-019': "Artbusters. Famous artworks and artists hiding in these phonetic clues. Have a go.",
    'artbusters-016': "Artbusters. Art answers, phonetic clues. Say them out loud.",
    'artbusters-020': "Artbusters. Famous names and works from the art world, all phonetically scrambled.",

    # bookbusters
    'bookbusters-010': "Bookbusters. Literary phonetic clues. Books, authors, characters, say them out loud.",
    'bookbusters-020': "Bookbusters. Three literary phonetic clues. Books and authors hiding in the sounds.",

    # comediansbusters
    'comediansbusters-006': "Comediansbusters. Stand-up comedians hiding in these phonetic clues. Say each one aloud.",
    'comediansbusters-010': "Comediansbusters. Three more phonetic comedian clues. The name's in the sounds.",

    # crimebusters
    'crimebusters-019': "Crimebusters. Famous criminals and crime cases, phonetically hidden. Say each clue out loud.",

    # culturebusters
    'culturebusters-018': "Culturebusters. Scientists, artists, royals, famous people phonetically disguised. Have a go.",
    'culturebusters-020': "Culturebusters. Famous names from art, science, and culture. Three phonetic clues.",
    'culturebusters-019': "Culturebusters. Mix of famous people, scientists, artists, royals. All phonetic.",
    'culturebusters-015': "Culturebusters. Artists and cultural figures hiding in the phonetic clues. Have a go.",
    'culturebusters-010': "Culturebusters. Famous scientists, artists, and royals, all phonetically wrapped up.",
    'culturebusters-007': "Culturebusters. Well-known cultural figures hiding in these clues. Say them out loud.",

    # filmbusters
    'filmbusters-015': "Filmbusters. Classic films from the big decades. All very famous, all phonetic.",

    # drugbusters
    'drugbusters-003': "Drugbusters. Medication names hiding in the phonetic clues. Say them out loud and see if the sounds lead anywhere useful.",

    # sportbusters
    'sportbusters-010': "Sportbusters. Famous sports personalities, all wrapped up phonetically. Say each one out loud.",
    'sportbusters-020': "Sportbusters. Three sporting legends to find. All phonetic, all a bit ridiculous.",
    'sportbusters-019': "Sportbusters. Famous athletes from across the sporting world. Say each phonetic clue out loud.",
    'sportbusters-009': "Sportbusters. Famous faces from sport, all hidden in silly sentences. Say them out loud.",
    'sportbusters-017': "Sportbusters. Three phonetic clues, three athletes. Give each one a go.",

    # disasterbusters
    'disasterbusters-003': "Disasterbusters. More catastrophic events hiding in the sounds. Say each clue out loud.",

    # drinkbusters
    'drinkbusters-020': "Drinkbusters. Drinks of all kinds hiding in the phonetic clues. Say them out loud.",
    'drinkbusters-015': "Drinkbusters. All drinks, beers, wines, spirits, whatever. Phonetic clues, say them aloud.",
    'drinkbusters-010': "Drinkbusters. Three drinks hiding in the sounds. Could be anything from a pint to a cocktail.",
    'drinkbusters-018': "Drinkbusters. Drinks hiding in the phonetic clues. Say them out loud.",
    'drinkbusters-019': "Drinkbusters. Three drinks to find. The sounds will tell you what they are.",

    # celebbusters
    'celebbusters-019': "Celebbusters. Classic British icons, all phonetically disguised. Have a go.",

    # spicebusters
    'spicebusters-003': "Spicebusters. Spice names hiding in the phonetic clues. Say each one out loud.",

    # snackbusters
    'snackbusters-007': "Snackbusters. All crisps, biscuits, and things you'd eat from a packet. Say them out loud.",
    'snackbusters-008': "Snackbusters. All snacks, all phonetic. Say them out loud, it really does work.",
    'snackbusters-019': "Snackbusters. Crisps and biscuits hiding in the phonetic clues. Have a crack.",
    'snackbusters-018': "Snackbusters. Classic snacks phonetically disguised. Should be easy enough.",
    'snackbusters-010': "Snackbusters. Snacks and crisps hiding in the sounds. Reward yourself with an actual one after.",
    'snackbusters-014': "Snackbusters. It's all about saying the clue out loud. If you're reading it silently you're doing it wrong.",
    'snackbusters-011': "Snackbusters. All snacks and crisps, all phonetic. Say each one out loud.",
    'snackbusters-009': "Snackbusters. Every answer is something you'd eat from a packet. Or a box.",
    'snackbusters-020': "Snackbusters. Final selection of phonetic snack clues. Go on then.",
    'snackbusters-004': "Snackbusters. Still all snacks and crisps. Say each one out loud if you're stuck.",

    # teambusters
    'teambusters-018': "Teambusters. Football clubs hiding in these phonetic clues. Say each one out loud.",
    'teambusters-010': "Teambusters. Still all football clubs, still all phonetic. Off you go.",
    'teambusters-015': "Teambusters. Say each clue out loud, the team's in the sound of it.",
    'teambusters-020': "Teambusters. Three football clubs to find. The names are in the sounds.",
    'teambusters-019': "Teambusters. Football clubs phonetically disguised. Say each one out loud.",

    # techbusters
    'techbusters-019': "Techbusters. Tech brands and internet companies hiding in the clues. Say them out loud.",
    'techbusters-020': "Techbusters. Tech and internet companies, all phonetically scrambled. Finish strong.",
    'techbusters-015': "Techbusters. Tech brands you probably use every day. All phonetic, say them out loud.",
    'techbusters-010': "Techbusters. Still all tech and internet companies. Say them out loud, don't overthink it.",
    'techbusters-018': "Techbusters. Tech companies and apps, phonetically disguised. Say each one out loud.",

    # brandbusters
    'brandbusters-010': "Brandbusters. Big brand names hiding in the sounds. You'll know them when you hear them.",
    'brandbusters-016': "Brandbusters. Three more brand names phonetically scrambled. Off you go.",
    'brandbusters-017': "Brandbusters. Phonetic brand clues. The name's somewhere in the sounds.",
    'brandbusters-019': "Brandbusters. Three phonetic brand clues. Well-known names, all of them.",
    'brandbusters-020': "Brandbusters. Global brand names in phonetic disguise. Say them out loud.",

    # countrybusters
    'countrybusters-015': "Countrybusters. Countries of the world, all phonetically disguised. Off you go.",
    'countrybusters-016': "Countrybusters. Three more countries hiding in the sounds. Have a go.",
    'countrybusters-004': "Countrybusters. Countries of the world, Rockbusters format. Say each one out loud.",
    'countrybusters-020': "Countrybusters. Three countries to find. The names are in the sounds.",
    'countrybusters-010': "Countrybusters. Still countries, still phonetic. Three more to crack.",
    'countrybusters-019': "Countrybusters. Countries hiding in the phonetic clues. Say each one out loud.",
    'countrybusters-014': "Countrybusters. Countries of the world, phonetically wrapped up. Have a crack.",

    # bandbusters
    'bandbusters-020': "Bandbusters. Classic British music hiding in these phonetic clues. Off you go.",
    'bandbusters-018': "Bandbusters. British bands and artists, phonetically disguised. Say them out loud.",

    # sciencebusters
    'sciencebusters-009': "Sciencebusters. Science and nature answers hiding in the phonetics. Have a go.",
    'sciencebusters-010': "Sciencebusters. Three more from science and nature. Say them out loud.",
    'sciencebusters-019': "Sciencebusters. Three more from the natural and scientific world. All phonetic.",
    'sciencebusters-005': "Sciencebusters. Science and nature answers, all phonetically wrapped up. Off you go.",
    'sciencebusters-018': "Sciencebusters. Three more from the world of science. Say the clues out loud.",
    'sciencebusters-015': "Sciencebusters. Science and nature phonetic clues. You'll hear the answer if you say it out loud.",

    # sweetbusters
    'sweetbusters-010': "Sweetbusters. UK sweets and confectionery hiding in phonetic clues. Say them out loud.",
    'sweetbusters-020': "Sweetbusters. Three UK sweets to find. The names are all in the sounds.",
    'sweetbusters-019': "Sweetbusters. UK confectionery hiding in these phonetic clues. Go on then.",
    'sweetbusters-009': "Sweetbusters. All UK confectionery, all phonetic. Say each clue out loud.",
    'sweetbusters-018': "Sweetbusters. UK sweets phonetically disguised. Say them out loud.",
    'sweetbusters-015': "Sweetbusters. British sweets hiding in these phonetic clues. Have a go.",

    # actorbusters
    'actorbusters-017': "Actorbusters. British actors hiding in the phonetic clues. Say each one out loud.",
    'actorbusters-019': "Actorbusters. British film and TV actors, all phonetically wrapped up. Have a go.",

    # cartoonbusters
    'cartoonbusters-018': "Cartoonbusters. Animated films and classic cartoons hiding in the sounds. Say them out loud.",
    'cartoonbusters-020': "Cartoonbusters. Three animated answers to find. Say each clue out loud.",

    # noughtybusters
    'noughtybusters-019': "Noughtybusters. Reality TV and pop culture from the 2000s and 2010s, phonetically disguised. Have a go.",

    # ukgeographybusters
    'ukgeographybusters-020': "Ukplacesbusters. Three British places hiding in the sounds. Say each one out loud and you'll get there.",

    # songbusters
    'songbusters-020': "Songbusters. Three classic tracks to find. The song titles are hiding in the sounds.",
}

# Apply fixes
fixed_count = 0
for s in data:
    sid = s['id']
    if sid in new_intros:
        s['intro'] = new_intros[sid]
        fixed_count += 1

print(f'Fixed {fixed_count} intros')

# Write back
with open(r'data/rockbusters.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False, width=2000)

print('Done.')
