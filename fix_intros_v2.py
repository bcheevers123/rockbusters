"""
Fix all intros that reference sequence/position (Last set, Final, Three in, etc.).
Updates both batch YAML files and rockbusters.yaml, then regenerates JSON exports.
"""
import yaml
import glob
import sys
from pathlib import Path

ROOT = Path(__file__).parent

NEW_INTROS = {
    'bondbaddiesbusters-003': "Bondbaddiesbusters. Bond villains hiding in the phonetic clues. Say them out loud and something might click. Might not.",
    'biologybusters-003': "Biologybusters. All biology terms hiding in the phonetics. Say them out loud or you'll get nowhere.",
    'riverbusters-003': "Riverbusters. All rivers, all phonetic clues. Say them out loud, close your eyes if it helps, and the answer'll surface eventually like a duck that's been underwater too long.",
    'bookbusters-018': "Bookbusters. Three phonetic literary clues. Say them out loud.",
    'songbusters-020': "Songbusters. Three classic tracks hiding in the sounds. Don't go to pieces now.",
    'mathbusters-003': "Mathbusters. Maths terms hiding in the phonetics. If you've got this far without walking off you deserve something. Though the prize isn't brilliant.",
    'dinosaurbusters-003': "Dinosaurbusters. All long extinct, all hiding in phonetic clues. Say them aloud and see what crawls out.",
    'philosophybusters-003': "Philosophybusters. Three big thinkers hiding in here. The answers are all phonetic. Say them out loud and see if the sounds add up to a philosopher.",
    'currencybusters-003': "Currencybusters. All foreign currency names. None of them are the pound. Say these out loud and see if the money adds up.",
    'tvbusters-020': "TVbusters. Classic British telly, all phonetic. Have a go.",
    'condimentbusters-003': "Condimentbusters. All condiments and sauces. Say these out loud and the answers'll come to you. Hopefully before you give up.",
    'chefbusters-003': "Chefbusters. Celebrity chefs, phonetic clues, and yes, you do have to say the words out loud rather than just staring at them. Off you go then.",
    'pokemonbusters-003': "Pokemonbusters. Three Pokemon lurking in these clues. Have a go.",
    'cartoonbusters-020': "Cartoonbusters. Three phonetic clues, all animated. Say each one out loud.",
    'pubbusters-020': "Pubbusters. Three phonetic pub clues. Off you go.",
    'treebusters-003': "Treebusters. Three more trees hiding in the phonetic clues. If you've got this far you're probably a bit of a nature person.",
    'languagebusters-003': "Languagebusters. Still all languages. Still all phonetic. Say it out loud, that's all you need to do.",
    'countrybusters-020': "Countrybusters. Three countries hiding in the phonetic clues. Say them out loud.",
    'wonderbusters-003': "Wonderbusters. All famous landmarks, all phonetic. Have a go.",
    'anatomybusters-003': "Anatomybusters. More body parts you'd only know if you'd revised properly. Which I hadn't.",
    'superherobusters-003': "Superherobusters. Three superhero names hiding in the phonetic clues. All hiding in the sounds.",
    'spicebusters-003': "Spicebusters. Hard spice names hiding in the phonetic clues. Say each one out loud.",
    'footballbusters-016': "Footballbusters. Three more phonetic legends to find. Say them out loud.",
    'countrybusters-017': "Countrybusters. Countries of the world. Still phonetic, still Rockbusters.",
    'culturebusters-020': "Culturebusters. Famous names from art, science, and culture. Three phonetic clues.",
    'olympicsbusters-003': "Olympicsbusters. Fencing and equestrian and gymnastics all in here somewhere. Say the clues out loud. The Olympic event is hiding in the sounds.",
    'gembusters-003': "Gembusters. Three clues, all gemstones. These are the tricky ones. Say each one aloud a few times. The answer's in there, just being a bit coy about it.",
    'sweetbusters-020': "Sweetbusters. UK sweets hiding in these phonetic clues. Say them out loud.",
    'drugbusters-003': "Drugbusters. Medication names hiding in the phonetic clues. Say these out loud and see if the sounds lead anywhere useful. Might not.",
    'brandbusters-003': "Brandbusters. Global brands hiding in these phonetic clues. Say them out loud.",
    'presidentbusters-003': "Presidentbusters. Leaders of the free world hidden in phonetic clues. Say them out loud, it all makes sense.",
    'artbusters-020': "Artbusters. Three art clues, all phonetic. Say them out loud.",
    'cheesebusters-003': "Cheesebusters. All cheese, all phonetic. Say each one out loud.",
    'disasterbusters-003': "Disasterbusters. Catastrophic events of varying sizes hiding in the sounds. Some of these are harder. Don't overthink it. Just say it out loud. Right.",
    'elementsbusters-003': "Elementsbusters. Some of the heavier elements named after clever people and important places. Say them out loud. That's the whole trick.",
    'extremeweatherbusters-003': "Extremeweatherbusters. Extreme weather, phonetic clues, say them out loud. If you're reading them silently and expecting that to work, it won't. You have been warned.",
    'noughtybusters-018': "Noughtybusters. Cars, beaches, and someone called Dawson. Three clues. Have a go.",
    'bookbusters-020': "Bookbusters. Three phonetic literary clues. Go on then.",
    'actorbusters-020': "Actorbusters. Three phonetic clues, all actors. Say them out loud.",
    'placebusters-020': "Placebusters. UK landmarks hiding in three phonetic clues. Give it a go.",
    'foodbusters-020': "Foodbusters. Three world dishes hiding in the sounds. Say them out loud.",
    'historybusters-019': "Historybusters. Famous people from history in these phonetic clues. Say them out loud.",
    'citybusters-020': "Citybusters. European cities hiding in the phonetic clues. Say them out loud.",
    'drinkbusters-020': "Drinkbusters. Drinks of all kinds hiding in the phonetic clues. Say them out loud.",
    'mixedbusters-020': "Mixedbusters. Three phonetic clues, three different answers. Off you go.",
    'celebbusters-020': "Celebbusters. Three phonetic British legends to find. Say each one out loud.",
    'teambusters-020': "Teambusters. Three football clubs hiding in the sounds. Say each one out loud.",
    'foodbusters-003': "Foodbusters. All international food. Say these out loud and see if the sounds add up.",
    'artbusters-018': "Artbusters. All art, all phonetic. Say each one out loud.",
    'sciencebusters-020': "Sciencebusters. Three science answers hiding in these clues. Say them out loud.",
    'footballbusters-020': "Footballbusters. Three legendary players hiding in the clues. Say them out loud.",
    'tvbusters-019': "TVbusters. British shows hiding in the phonetic clues. Say each one out loud.",
    'animalbusters-020': "Animalbusters. Three animals hiding in the sounds. Say each clue out loud.",
    'brandbusters-020': "Brandbusters. Global brand names hiding in these phonetic clues. Say them out loud.",
    'gamebusters-018': "Gamebusters. Three clues, all gaming. Say them out loud.",
    'snackbusters-020': "Snackbusters. Phonetic snack clues. Say each one out loud.",
    'pubbusters-017': "Pubbusters. Three phonetic pub clues. Say them aloud.",
    'phrasebusters-020': "Phrasebusters. Three common phrases hiding in the sounds. Say them out loud.",
    'historybusters-020': "Historybusters. Famous figures from history, all phonetic. Give it your best shot.",
    'gamebusters-020': "Gamebusters. Three phonetic clues, all gaming. Say them out loud.",
    'noughtybusters-020': "Noughtybusters. Pop culture from the 2000s and 2010s, phonetically disguised. Have a go.",
    'pubbusters-010': "Pubbusters. Three phonetic pub clues. Say them out loud.",
    'nostalgiabusters-020': "Nostalgiabusters. Three phonetic clues about things from the era of dial-up and Woolies. Off you go.",
    'sportbusters-020': "Sportbusters. Three sporting greats hiding in the clues. You know how this works by now.",
    'mixedbusters-010': "Mixedbusters. Same as ever. Say it out loud. That's all.",
    'bandbusters-020': "Bandbusters. British bands and artists hiding in the phonetic clues. Say them out loud.",
    'brandbusters-018': "Brandbusters. All global brands, all phonetic. Say each one out loud.",
    'techbusters-020': "Techbusters. Tech and internet companies hiding in the phonetic clues. Say them out loud.",
    'filmbusters-020': "Filmbusters. Three films hiding in the phonetic clues. See if you can get all three.",
    'filmbusters-040': "Filmbusters. Three clues, all big films. You know these. Go on then.",
    'bandbusters-040': "Bandbusters. Three acts to find. Say each clue out loud.",
    'tvbusters-040': "TVbusters. Three clues, three American shows. Say them out loud.",
    'holidaybusters-018': "Holidaybusters. British holiday destinations abroad. Say each one out loud.",
    'holidaybusters-020': "Holidaybusters. Three clues, all holiday destinations. The prize is what it is.",
    'citybusters-040': "Citybusters. Three more cities hiding in the phonetic clues. Say them out loud.",
    'bandbusters-060': "Bandbusters. Pop groups hiding in the phonetic clues. Say them out loud.",
    'animalbusters-038': "Animalbusters. Sea creatures and birds hiding in the sounds. You know how this works.",
    'animalbusters-040': "Animalbusters. Sea creatures and birds hiding in the phonetic clues. Say each one out loud.",
    'foodbusters-039': "Foodbusters. Three more desserts hiding in the sounds. Say each one out loud.",
    'foodbusters-040': "Foodbusters. Three dessert clues, all phonetic. Good luck.",
    'filmbusters-060': "Filmbusters. British comedy and cult classics hiding in the phonetic clues. Have a crack at it.",
    'sportbusters-040': "Sportbusters. Three phonetic sports names hiding in the clues. Say them out loud.",
    'placebusters-040': "Placebusters. Three phonetic geography clues. Say them out loud.",
    'comediansbusters-019': "Comediansbusters. Three more comedian names hiding in the sounds. Say it out loud. That's all.",
    'comediansbusters-020': "Comediansbusters. Three phonetic comedian clues. Give it a go.",
    'wordbusters-010': "Wordbusters. Three compound word phonetic clues. Off you go.",
    'wordbusters-020': "Wordbusters. Three compound word phonetic clues. Near enough.",
    'fashionbusters-019': "Fashionbusters. Fashion brands hiding in the sounds. Say it out loud.",
    'fashionbusters-020': "Fashionbusters. Three fashion brands hiding in the phonetic clues. Say them out loud.",
    'mediabusters-020': "Mediabusters. Three phonetic British media clues. Give it your best shot.",
    'royalbusters-020': "Royalbusters. Three royals hiding in three silly clues. Go on then.",
    'sciencebusters2-020': "Sciencebusters. Three science answers hiding in these clues. Go on then.",
    'weatherbusters-020': "Weatherbusters. Three weather answers hiding in the sounds. Say them out loud.",
    'crimebusters-020': "Crimebusters. Three phonetic clues, all crime-related. Give it a go.",
    'ukplacesbusters-020': "Ukplacesbusters. Three British places hiding in the sounds. Just say them out loud.",
    'mythbusters-003': "Mythbusters. Legendary figures hiding in the phonetic clues. Say them out loud and listen.",
    'mythbusters-020': "Mythbusters. Three legendary figures hiding in these clues. Say them out loud.",
    'businessbusters-003': "Businessbusters. Famous business people hiding in these phonetic clues. Say them out loud.",
    'businessbusters-018': "Businessbusters. All moguls, all phonetic. Say each clue out loud.",
    'businessbusters-020': "Businessbusters. Three more business moguls hiding in the sounds. Say them out loud.",

    # Penultimate / nearly-there references
    'culturebusters-019': "Culturebusters. Mix of famous people from art, science, culture. Three phonetic clues.",
    'foodbusters-019': "Foodbusters. Three world dishes hiding in the sounds. Say them out loud.",
    'actorbusters-019': "Actorbusters. British acting royalty, all phonetically disguised. Three clues.",
    'phrasebusters-019': "Phrasebusters. Three more phrases hiding in these clues. Say them out loud.",
    'techbusters-019': "Techbusters. All tech brands and companies. You know the game.",
    'sciencebusters-019': "Sciencebusters. Three more science phonetic answers. Say them out loud.",
    'brandbusters-019': "Brandbusters. Three more phonetic brand clues. Say them out loud.",
    'artbusters-019': "Artbusters. Three more art phonetic clues. Say them out loud.",
    'mixedbusters-019': "Mixedbusters. Three phonetic clues. You know the drill.",
    'pubbusters-019': "Pubbusters. Three phonetic pub clues. Say them aloud.",
    'footballbusters-019': "Footballbusters. Three clues, all footballers. Give it a go.",
    'snackbusters-019': "Snackbusters. Crisps and biscuits hiding in these phonetic clues. Have a crack.",
    'animalbusters-019': "Animalbusters. Three more animals hiding in the sounds. Say each one out loud.",
    'sportbusters-019': "Sportbusters. Three more phonetic legends to uncover. Say each clue out loud.",
    'sweetbusters-019': "Sweetbusters. Three more UK sweets hiding in the sounds. Go on then.",
    'countrybusters-019': "Countrybusters. Countries hiding in the phonetic clues. Say each one out loud.",
    'citybusters-019': "Citybusters. Three more European cities hiding in the phonetics. Go on then.",
    'bookbusters-019': "Bookbusters. Three more phonetic literary clues. Say them out loud.",
    'citybusters-039': "Citybusters. Three more big cities hiding in the phonetic clues. Say them out loud.",
    'animalbusters-039': "Animalbusters. Three more sea and sky creatures hiding in the sounds. Say each one out loud.",
    'wordbusters-019': "Wordbusters. Compound words in phonetic clues. Say them out loud.",
    'mythbusters-019': "Mythbusters. Three more legendary figures hiding in the phonetic clues. Say them out loud.",
    'businessbusters-019': "Businessbusters. Three more phonetic business clues. Say them out loud.",

    # Nearly there / nearly done references
    'actorbusters-017': "Actorbusters. Three British actors hidden in the clues. Say each one out loud.",
    'drinkbusters-018': "Drinkbusters. Three drinks hidden in the clues. Go on then.",
    'snackbusters-014': "Snackbusters. All about saying the clue out loud. If you're reading it silently you're doing it wrong.",
    'citybusters-018': "Citybusters. European city, phonetic clue, say it out loud.",
    'teambusters-015': "Teambusters. Say each clue out loud — the team's in the sound of it.",
    'celebbusters-019': "Celebbusters. Three more phonetic British icons. Have a go.",
    'countrybusters-016': "Countrybusters. Three more countries in this one. Say them out loud.",
    'cartoonbusters-018': "Cartoonbusters. Three phonetic clues, all animated. Say them out loud — that's the game.",
    'culturebusters-018': "Culturebusters. Three famous names to crack. All phonetic.",
    'historybusters-018': "Historybusters. Three more famous faces from history. Say each one out loud.",
    'footballbusters-017': "Footballbusters. Three more football phonetics. Say each one out loud.",
    'gamebusters-017': "Gamebusters. Three more phonetic gaming clues. Say them out loud.",
    'bandbusters-018': "Bandbusters. British music phonetic riddles. Say them out loud.",
    'placebusters-017': "Placebusters. UK landmarks and tourist spots, all phonetic. Have a go.",
    'filmbusters-015': "Filmbusters. All classic films, all very famous. Say them out loud.",
    'noughtybusters-019': "Noughtybusters. Soaps, bells, and a motorbike. Say each clue out loud.",
    'sciencebusters-018': "Sciencebusters. Three more from the world of science. Say them out loud.",
    'phrasebusters-018': "Phrasebusters. Still all everyday idioms and phrases. Say them out loud.",
    'holidaybusters-019': "Holidaybusters. Three holiday destinations hiding in these phonetic clues. Stick with it.",
    'sportbusters-017': "Sportbusters. Three clues, three athletes, all phonetic. Give each one a go out loud.",
    'foodbusters-017': "Foodbusters. Three more world dishes. The answer's somewhere in the sounds.",
    'brandbusters-017': "Brandbusters. Three more phonetic brand clues. Say them out loud.",
    'pubbusters-018': "Pubbusters. Three more phonetic clues. Pub names and games. Say them aloud.",
    'phrasebusters-015': "Phrasebusters. Three more well-known phrases hiding in the sounds. Say them out loud.",
    'sweetbusters-018': "Sweetbusters. Still all UK sweets, still phonetic clues. Say them out loud.",
    'techbusters-015': "Techbusters. All tech brands you use every day. Sort of. Say them out loud.",
    'mixedbusters-018': "Mixedbusters. Three phonetic clues. Have a go.",
    'mixedbusters-009': "Mixedbusters. Three clues, all phonetic. Don't overthink it.",
    'techbusters-018': "Techbusters. Tech companies and apps, phonetic clues. Say them out loud.",
    'snackbusters-018': "Snackbusters. Classic snacks, all phonetic. Should be easy enough.",
    'tvbusters-017': "TVbusters. Three phonetic British telly clues. Say them out loud.",
    'animalbusters-018': "Animalbusters. Three more animals hiding in the phonetic clues. Give it one more go.",
    'pubbusters-015': "Pubbusters. Three phonetic clues, all pub names and pub culture. Say them out loud.",
    'gamebusters-019': "Gamebusters. Three clues, gaming theme. Say each one out loud.",
    'teambusters-019': "Teambusters. Three more football clubs hiding in the sounds. Say them out loud.",
    'filmbusters-039': "Filmbusters. Three clues, all films you've probably seen. Or at least heard of.",
    'bandbusters-039': "Bandbusters. Three more phonetic music acts hiding in the clues. Say them out loud.",
    'tvbusters-039': "TVbusters. Three clues, all American shows. Say them out loud.",
    'bookbusters-015': "Bookbusters. Three clues, phonetic, literary. You know how this goes.",
    'bookbusters-017': "Bookbusters. Three more phonetic literary clues. Say them out loud.",
    'holidaybusters-016': "Holidaybusters. All holiday destinations, all phonetic. Say each one out loud.",
    'citybusters-038': "Citybusters. Three more cities hiding in the phonetic clues. Say them out loud.",
    'animalbusters-037': "Animalbusters. Three more sea and sky phonetics. Go on.",
    'filmbusters-059': "Filmbusters. More British films. Some funny, some a bit grim, all worth watching.",
    'sportbusters-037': "Sportbusters. Three phonetic sports names. Say them out loud.",
    'sportbusters-039': "Sportbusters. Three more hiding in the sounds. Say each one out loud.",
    'placebusters-034': "Placebusters. Three more places hiding in these phonetic clues. Say them out loud.",
    'placebusters-037': "Placebusters. Three more phonetic geography clues. Say them out loud.",
    'placebusters-039': "Placebusters. Three phonetic geography clues. Say them out loud.",
    'comediansbusters-017': "Comediansbusters. Three phonetic clues, all comedians. Say them out loud.",
    'wordbusters-016': "Wordbusters. Three more phonetic compound word clues. Say them out loud.",
    'fashionbusters-015': "Fashionbusters. Fashion brands in phonetic form. Say them out loud.",
    'mediabusters-015': "Mediabusters. British media, phonetic clues, silly scenes. Off you go.",
    'mediabusters-018': "Mediabusters. Three more British media names in phonetic disguise. Say them out loud.",
    'royalbusters-017': "Royalbusters. Three royals in three clues. All hidden in sounds, not letters.",
    'royalbusters-019': "Royalbusters. Three more royals hiding in sounds. Say them out loud.",
    'sciencebusters2-018': "Sciencebusters. Three more science answers hidden in these phonetic clues. Say them out loud.",
    'weatherbusters-018': "Weatherbusters. Say these out loud. Sounds like the answer, every time.",
    'artbusters-017': "Artbusters. Three more art clues, all phonetic. Say them out loud.",
    'crimebusters-018': "Crimebusters. Three more phonetic clues. Say them out loud.",
    'mythbusters-017': "Mythbusters. Three more legendary figures. Say the clues out loud.",
    'businessbusters-017': "Businessbusters. Three more clues, all business, all phonetic. Say them aloud.",

    # Keep going / halfway / stick with it / don't give up references
    'gamebusters-011': "Gamebusters. Three phonetic clues, all games. Have a go.",
    'snackbusters-011': "Snackbusters. The theme is still snacks. Say them out loud.",
    'tvbusters-007': "TVbusters. British telly, phonetic clues. You know the drill.",
    'snackbusters-007': "Snackbusters. Say them out loud — it really works.",
    'sportbusters-018': "Sportbusters. All sport, all phonetic, all a bit daft. Say them out loud.",
    'tvbusters-010': "TVbusters. Classic British programmes hiding in the phonetic clues. Say them out loud.",
    'holidaybusters-019': "Holidaybusters. Three holiday destinations hiding in these phonetic clues. Have a go.",
    'foodbusters-010': "Foodbusters. All international grub, all phonetic. Say them out loud.",
    'snackbusters-016': "Snackbusters. More crisps and biscuits hiding in the phonetic clues. Say them out loud.",
    'bandbusters-019': "Bandbusters. Three more phonetic music acts. Say each one out loud.",
    'holidaybusters-010': "Holidaybusters. British holiday destinations, phonetically disguised. Say each one out loud.",
    'sportbusters-029': "Sportbusters. Sports personalities hiding in phonetic scenes. Say them out loud.",
    'wordbusters-012': "Wordbusters. Three more compound word phonetic clues. Say them out loud.",
    'fashionbusters-006': "Fashionbusters. Three fashion clues, all phonetic. You know the drill.",
    'royalbusters-012': "Royalbusters. Three clues, all sounds, all royals. Say them out loud.",
    'weatherbusters-011': "Weatherbusters. All weather, all phonetic. Say them out loud.",

    # Halfway / milestone references
    'bookbusters-010': "Bookbusters. Same rules, phonetic clues, literary theme. Say them out loud.",
    'teambusters-010': "Teambusters. Still all football clubs, still all phonetic. Say them out loud.",
    'citybusters-015': "Citybusters. All European cities, phonetic clues. Off you go.",
    'sweetbusters-015': "Sweetbusters. All UK sweets in these phonetic clues. Say them out loud.",
    'drinkbusters-015': "Drinkbusters. All drinks, phonetic clues. Let's be having you.",
    'countrybusters-010': "Countrybusters. Still countries, still Rockbusters. Three more.",
    'gamebusters-010': "Gamebusters. Three clues, all gaming. Say them out loud.",
    'snackbusters-010': "Snackbusters. Reward yourself with an actual snack after this one.",
    'sportbusters-010': "Sportbusters. All still sport, all still phonetic, all still a bit ridiculous. You know how it works.",
    'sciencebusters-015': "Sciencebusters. Three more phonetic science answers. Say them out loud.",
    'brandbusters-010': "Brandbusters. Three more big brand names hiding in the sounds. Say them out loud.",
    'sweetbusters-010': "Sweetbusters. Three more UK sweets hiding in these clues. Say them out loud.",
    'gamebusters-009': "Gamebusters. Phonetic clues, gaming answers. Say it out loud.",
    'phrasebusters-010': "Phrasebusters. Three more idioms hiding in the sounds. Say them out loud.",
    'footballbusters-010': "Footballbusters. Three clues, three legendary names. Say them out loud.",
    'tvbusters-015': "TVbusters. British telly gold in here, allegedly. Say each one out loud.",
    'sportbusters-030': "Sportbusters. Three more phonetic sports names. See how you get on.",
    'placebusters-030': "Placebusters. Natural wonders and famous landmarks hiding in the sounds. Say them out loud.",
    'comediansbusters-009': "Comediansbusters. Three phonetic riddles, all comedians. You know the drill.",
    'fashionbusters-010': "Fashionbusters. Fashion brands, phonetic clues. You know what to do.",
    'mediabusters-010': "Mediabusters. Three British media names in phonetic disguise. Say them out loud.",
    'mediabusters-011': "Mediabusters. Three more British media phonetics. Off you go.",
    'sciencebusters2-010': "Sciencebusters. Three more science answers hiding in these phonetic clues. Off you go.",
    'weatherbusters-010': "Weatherbusters. Say them out loud. The sounds do the job.",
    'artbusters-010': "Artbusters. Famous art answers hiding in these phonetic clues. Say them out loud.",
    'crimebusters-010': "Crimebusters. Three more phonetic clues. Say them out loud — that's the trick.",
    'mythbusters-010': "Mythbusters. Legendary figures in the answers. Phonetic clues. Say them out loud.",
    'businessbusters-010': "Businessbusters. All moguls, all phonetic. Say them out loud.",

    'filmbusters-058': "Filmbusters. British cult classics hiding in the phonetic clues. You've seen these. Well, you should have.",
    'royalbusters-018': "Royalbusters. All royals, all in the sounds. Say them out loud.",
}


def fix_yaml_file(path):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    changed = 0
    for s in data:
        if s['id'] in NEW_INTROS:
            s['intro'] = NEW_INTROS[s['id']]
            changed += 1
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False,
                      default_flow_style=False, width=2000)
        print(f'  {Path(path).name}: {changed} fixed')
    return changed


total = 0

print('Fixing batch files...')
for batch in sorted(glob.glob(str(ROOT / 'data/batches/*.yaml'))):
    total += fix_yaml_file(batch)

print(f'\nFixing rockbusters.yaml...')
total += fix_yaml_file(ROOT / 'data/rockbusters.yaml')

print(f'\nTotal intros fixed: {total}')

print('\nRegenerating JSON exports...')
sys.path.insert(0, str(ROOT))
import importlib.util
spec = importlib.util.spec_from_file_location('export_json', ROOT / 'scripts/export_json.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print('Done.')
