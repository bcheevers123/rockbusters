"""Apply phonetic fixes for all 109 audit-flagged clues. No em dashes anywhere."""
import yaml, sys
sys.stdout.reconfigure(encoding='utf-8')

# (set_id, clue_number): new_clue
# All clues encode answer syllables as real images. No fake syllable names.
# No answer verbatim. No hyphens. No em dashes. No phonetic suffix.
FIXES = {

    # ══ HYPHENS ══════════════════════════════════════════════════════════════

    # Thailand: Tie(Thai) + land
    ('countrybusters-017', 3):
        "A silk neckwear has gone and found itself a country to settle on.",

    # Carling: Carl(real name) + ing
    ('drinkbusters-016', 2):
        "That fella Carl is just hanging about. Won't shift. Very persistent presence.",

    # Kenya: Ken(do you know, Scottish) + ya(informal you)
    ('countrybusters-010', 3):
        "Someone asking if you know something, using a very informal pronoun.",

    # Denmark: Den(animal lair) + mark(score/tally)
    ('countrybusters-006', 2):
        "An animal's private lair with a tally mark scored on the wall.",

    # Bangladesh: Bangle(bracelet) + desk
    ('countrybusters-019', 3):
        "A bracelet worn round the wrist and a writing surface have somehow become a country.",

    # Lanzarote: Lance + a + rote(by repetition)
    ('holidaybusters-010', 3):
        "A knight's weapon with an extra vowel on the end, and something learned entirely by heart.",

    # Thailand again (holidaybusters)
    ('holidaybusters-006', 2):
        "A silk necktie has found itself a land to call home.",

    # Magaluf: Mag(magazine) + a + luff(front edge of sail)
    ('holidaybusters-008', 3):
        "Someone's favourite magazine, an indefinite article, and the very front edge of a sail.",

    # ══ ANSWER VERBATIM ══════════════════════════════════════════════════════

    # Cyprus: Cypress(tree, homophone of Cyprus)
    ('holidaybusters-004', 1):
        "A tall pointed evergreen tree found in Mediterranean gardens has become an island.",

    # Tunisia: Too(two) + knee + Shah(Persian king)
    ('holidaybusters-007', 2):
        "Two kneepads have been delivered and a Persian king has turned up to inspect them.",

    # Trigonometry: Trig(point on hill) + a + nom(eating) + i + try
    ('mathbusters-002', 1):
        "A surveying marker on a hilltop, an indefinite article, an eating sound, the letter I, and a valiant attempt.",

    # Energy: En(French in) + er(hesitation) + gee(letter G)
    ('sciencebusters-010', 2):
        "Someone speaking French said 'in', then hesitated, then said the letter G out loud.",

    # Grease: Greece(country, homophone)
    ('filmbusters-007', 3):
        "A Mediterranean country famous for olives and mythology has gone all musical.",

    # Sideways: Side(flank) + ways(directions)
    ('sciencebusters-019', 2):
        "One flank of something has found multiple directions to travel in.",

    # Tenerife: Tena(brand) + reef
    ('holidaybusters-001', 3):
        "A well-known brand found in care home bathrooms and a coral reef.",

    # Nachos (foodbusters): Natch(British: naturally) + oz(Wizard of Oz)
    ('foodbusters-003', 2):
        "Naturally, of course, and then that famous fictional land where the wizard lives.",

    # The Jam: The + jamb(door frame)
    ('bandbusters-008', 2):
        "The definite article and a door frame have formed a very influential punk band.",

    # Something (songbusters-014): Sum(maths) + thing
    ('songbusters-014', 1):
        "A mathematical total and an unidentified object.",

    # Costa Rica: Costa(coffee chain) + rica(rich/wealthy)
    ('countrybusters-012', 3):
        "A well-known motorway service station coffee chain has counted its money and become a country.",

    # Turkey #1 (holidaybusters-005): encode as the Christmas bird
    ('holidaybusters-005', 1):
        "A massive festive bird people stuff and roast at Christmas has become a country.",

    # Morocco: Mo(runner) + rock + oh
    ('holidaybusters-005', 3):
        "That famous long-distance runner Mo found a very large rock and went oh.",

    # Turkey #2 (holidaybusters-014): same as above
    ('holidaybusters-014', 3):
        "A big festive roasting bird has packed its bags and become a country.",

    # Tuscany: Tusk(elephant tooth) + any
    ('holidaybusters-009', 1):
        "An elephant's tooth and any option you care to choose.",

    # Amalfi #1: Am(verb to be) + Al(name) + fee
    ('holidaybusters-009', 2):
        "I am a bloke called Al and someone's charged me a fee for the privilege.",

    # Algarve: Al(name) + garve(carve with G, near-homophone)
    ('holidaybusters-016', 3):
        "A bloke called Al has done some very committed carving.",

    # Amalfi #2
    ('holidaybusters-017', 2):
        "I am Al, and I have been handed quite a considerable bill.",

    # Rhodes: Roads(homophone of Rhodes)
    ('holidaybusters-020', 3):
        "Multiple roads going somewhere have become a Greek island.",

    # Albania: Al(name) + ban + ia
    ('countrybusters-004', 2):
        "A bloke called Al has been banned from something and is extremely unhappy about it.",

    # Inside Out: Inn(pub) + side + out
    ('cartoonbusters-007', 3):
        "A pub has gone all sideways and then departed entirely.",

    # Cobweb: Cob(male swan) + web(network)
    ('compoundbusters-007', 2):
        "A male swan has gone and built himself a digital network.",

    # The Telegraph #1: The + tele(TV) + graph(chart)
    ('mediabusters-007', 2):
        "The definite article, a television, and a bar chart have combined into a newspaper.",

    # The Telegraph #2
    ('mediabusters-020', 2):
        "The definite article in front of a telly that's gone off to draw itself a diagram.",

    # Mitochondria: My + toe + con(swindle) + dree(suffer, Scottish) + a
    ('sciencebusters2-011', 2):
        "Something of mine, a toe, a swindle, and something very dry at the end.",

    # Snowflake: Snow(frozen precipitation) + flake(unreliable person)
    ('weatherbusters-019', 2):
        "Some frozen precipitation has found an unreliable person.",

    # Merlin: Mer(sea, French) + lin(pool)
    ('mythbusters-009', 3):
        "The French word for sea and a small Scottish pool.",

    # Chicago: She + car + go
    ('musicalbusters-005', 2):
        "She's taken the car and gone.",

    # Thriller: Thrill + er
    ('songbusters-009', 2):
        "Something that gives you an incredible adrenaline rush, said with a slight hesitation.",

    # Something (songbusters-006)
    ('songbusters-006', 3):
        "A maths total and an unidentified object.",

    # Gazelle: Gaze + l(letter L)
    ('animalbusters-013', 3):
        "Someone's had a very long intense stare at the letter L and it became a graceful antelope.",

    # ══ FAKE NAMES ══════════════════════════════════════════════════════════

    # Taj Mahal: barge(near-rhyme with taj) + ma + hall
    ('wonderbusters-002', 2):
        "Someone barged into your mum's hallway without knocking. All very ornate. Very Indian.",

    # Christ the Redeemer: (figure on cross) + the + (saviour)
    ('wonderbusters-002', 3):
        "The most famous figure ever nailed to a cross is THE definitive example of someone who saves all of mankind.",

    # Nachos (foodbusters-019): Natch + oz
    ('foodbusters-019', 3):
        "Naturally, of course, and then the fictional land from the yellow brick road.",

    # Hyena: Hi(greeting) + eena(sound of screechy laugh)
    ('animalbusters-007', 2):
        "A cheerful greeting followed by a very high-pitched screeching laugh.",

    # Moana (cartoonbusters-020): Moan + a
    ('cartoonbusters-020', 3):
        "Someone's having a good old moan and then just said the letter A.",

    # Douglas Fir: Dug(past of dig) + lass(Scottish girl) + fur
    ('treebusters-003', 2):
        "Someone dug up a Scottish lass who was wearing a fur coat.",

    # Harvey Wallbanger: Har(laughter) + vee(letter V) + wall + banger
    ('cocktailbusters-001', 3):
        "A hearty laugh, then the letter V, then someone's headbutted a wall and made a right bang.",

    # Adrenaline: Ad(vert) + wren(bird) + a + line
    ('biologybusters-001', 3):
        "An advert featuring a small garden bird standing in a very long queue.",

    # Ikea (brandbusters-001): I + key + a
    ('brandbusters-001', 3):
        "Someone pointing at themselves, a door key, and an indefinite article.",

    # Tagliatelle: Tag(chasing game) + lia(fibber) + tell(e)
    ('pastabusters-001', 1):
        "A children's chasing game, a fibber, and someone who tells you everything.",

    # Linguine: Ling(heather) + wee(small) + knee
    ('pastabusters-001', 3):
        "Purple moorland heather, something very small, and a kneecap.",

    # Stegosaurus: Stag(male deer, near steg) + o + sore + us
    ('dinosaurbusters-001', 1):
        "A male deer, the letter O, and something very sore about the whole situation.",

    # Wensleydale: Wens(skin cysts) + ley(line) + dale(valley)
    ('cheesebusters-001', 1):
        "Multiple skin cysts on a ley line in a valley.",

    # Pompeii: Pom(pom, cheerleader fluffy) + pay + ee
    ('disasterbusters-001', 1):
        "A cheerleader's fluffy pompom has gone and earned a wage and gone ee about it.",

    # Hiroshima: Hi + row(dispute) + shim(wedge) + a
    ('disasterbusters-001', 3):
        "A greeting, then an argument on the water, then a thin door wedge, then someone's mum.",

    # Fukushima: Fu(kung fu) + queue + she + ma
    ('disasterbusters-003', 2):
        "A kung fu move, a very long queue of people, a young woman, and her mum.",

    # Sweeney Todd: Sweet + knee + on-your-tod(alone)
    ('musicalbusters-002', 3):
        "Something sweetly applied to a knee, and then someone standing completely on their tod.",

    # Forrest Gump (filmbusters-016): Forest + gumption
    ('filmbusters-016', 2):
        "A dense woodland and someone who has completely lost their gumption.",

    # Seville: Sev(en contracted) + ill
    ('citybusters-008', 2):
        "A number reduced from its full seven letters has gone and fallen ill.",

    # Ian McKellen: Ian + Mc + bell + in
    ('actorbusters-019', 2):
        "Ian has arrived with a Scottish lad who keeps ringing bells.",

    # Water Lilies (artbusters-014): Watt + er + Lily(ies)
    ('artbusters-014', 3):
        "A unit of electrical power and a woman called Lily who has gone plural.",

    # Game Boy: Game + boy(young male as common noun)
    ('nostalgiabusters-001', 2):
        "A sporting contest and a young male have been combined into something handheld.",

    # Chateaubriand: Chateau(French wine estate) + Brie(cheese) + and
    ('foodbusters-020', 1):
        "A French wine estate, a soft French cheese, and the conjunction.",

    # Moana (cartoonbusters-014): Moan + a
    ('cartoonbusters-014', 3):
        "Someone's having a very prolonged moan and then just added the letter A.",

    # Wayne Rooney: Wane(moon decreasing) + rooney(loony with R)
    ('footballbusters-017', 3):
        "The moon has started to shrink and someone's gone completely round the bend.",

    # Rigatoni: Rig(oil rig) + a + Toni(real name)
    ('pastabusters-002', 1):
        "An oil platform, an indefinite article, and a bloke called Tony.",

    # Waltz: Walt(Disney reference) + z
    ('dancebusters-001', 3):
        "The bloke very associated with Mickey Mouse has discovered the last letter of the alphabet and started dancing.",

    # Forrest Gump (filmbusters-005)
    ('filmbusters-005', 1):
        "Overgrown forest and someone who has completely lost their gumption.",

    # Pepsi (brandbusters-002): Pep + see
    ('brandbusters-002', 2):
        "Some pep and energy, and then having a good look around.",

    # Miss the Boat: Miss(to fail to catch, verb) + the + boat
    ('phrasebusters-004', 2):
        "Someone's failed to catch a vessel. Stood on the dock watching it go.",

    # Tarzan: Tar(road material) + Z(letter) + an
    ('cartoonbusters-017', 2):
        "Black sticky road material has found the last letter of the alphabet and swung off into the jungle.",

    # Nachos (cartoonbusters-008 Moana): Moan + a
    ('cartoonbusters-008', 2):
        "Someone making a prolonged moan and then the letter A.",

    # The Beatles: The + Beetles(insect, homophone)
    ('bandbusters-001', 1):
        "The definite article in front of four insects you would find under a log.",

    # Aardvark: Art(painting, near-aard) + dark(near-vark)
    ('animalbusters-020', 1):
        "A painting has gone off into the dark.",

    # Pepsi (brandbusters-020)
    ('brandbusters-020', 1):
        "Some real pep and energy and then having a good look around.",

    # Napster: Nap(short sleep, real word) + ster
    ('nostalgiabusters-011', 2):
        "A very quick sleep has gone and started sharing music without paying for it.",

    # Pangolin: Pan(cooking vessel) + go + lin(pool)
    ('animalbusters-006', 1):
        "A cooking vessel has gone off to find a pool to swim in.",

    # Alec Guinness: Alec(real name) + Guinness(the stout)
    ('actorbusters-005', 3):
        "Someone's handed a pint of dark Irish stout to a bloke called Alec.",

    # Adele: A + dell(small valley)
    ('bandbusters-012', 1):
        "The indefinite article and a small wooded valley.",

    # Ikea (brandbusters-018)
    ('brandbusters-018', 1):
        "Someone pointing at themselves, a door key, and an indefinite article out front.",

    # Skoda (brandbusters-018): Soda(near-homophone) + k
    ('brandbusters-018', 2):
        "A fizzy carbonated drink has found itself an extra consonant and become a Czech car.",

    # Ginger Nut: Ginger(the spice, real word) + nut
    ('snackbusters-008', 3):
        "That hot root spice they put in gingerbread has found itself a hard outer shell.",

    # Proton: Pro(professional) + ton(weight unit)
    ('sciencebusters-013', 3):
        "A professional and a unit of weight have become a subatomic particle.",

    # Marcus Rashford: Marcus(real name) + rash + ford
    ('footballbusters-002', 3):
        "A bloke called Marcus has done something reckless while trying to cross a river.",

    # Berlin: Bear(near-ber) + lin(pool)
    ('citybusters-002', 1):
        "A large furry forest animal has gone and found a swimming pool.",

    # Warsaw: War(armed conflict) + saw(cutting tool)
    ('citybusters-002', 3):
        "Armed conflict and a cutting implement have formed a capital city.",

    # Madrid: Mad(angry/crazy) + rid(to get rid)
    ('citybusters-003', 1):
        "Someone gone crazy has decided to get rid of the whole problem.",

    # Budapest: Bud(flower bud) + a + pest(annoying creature)
    ('citybusters-004', 1):
        "A flower bud and a very annoying creature.",

    # Dublin: Dub(recording session) + lin(pool)
    ('citybusters-004', 3):
        "A music recording session and a swimming pool have merged.",

    # Madonna: Ma(mum) + don(to dress oneself) + a
    ('bandbusters-024', 2):
        "Your mum has dressed herself up. Very Italian. Very grand.",

    # Mick Jagger: M(letter) + ick(disgust) + jagged + er
    ('bandbusters-037', 2):
        "The letter M, an expression of disgust, and someone very rough around the edges.",

    # Katy Perry: Kay(name) + T(letter) + perry(pear drink)
    ('bandbusters-037', 3):
        "A woman called Kay has found the letter T and is drinking something made from fermented pears.",

    # Mariah Carey: Ma(mum) + rye(grain) + ah + Carey(carrying)
    ('bandbusters-038', 2):
        "Your mum has found a rye field, let out a sigh of relief, and she is doing all the carrying.",

    # Bruno Mars: Brew + no + Mars
    ('bandbusters-040', 1):
        "A brewing session that someone has put a stop to, and then a planet.",

    # Ian McKellen (actorbusters-013)
    ('actorbusters-013', 1):
        "Ian has shown up with a Scottish lad who keeps ringing bells.",

    # Pink Floyd: Pink + Freud(near-homophone of Floyd)
    ('bandbusters-002', 1):
        "The colour pink and the most famous Austrian psychoanalyst.",

    # Skoda (brandbusters-004)
    ('brandbusters-004', 1):
        "A fizzy carbonated drink has escaped to Eastern Europe and become a motor vehicle.",

    # Daniel Craig: Dan + eel + crag(rocky cliff, near Craig)
    ('actorbusters-003', 3):
        "Dan has an eel and there is a rocky cliff face at the end of it.",

    # Mexico City: Mechs(robot suits) + i + co + city
    ('citybusters-027', 1):
        "Giant mechanical warrior suits have found an eye, a company, and a very large city.",

    # San Francisco: Sand + frank(honest/hot dog) + sis + co
    ('citybusters-028', 1):
        "Some gritty sand, a very honest person, a sister, and a company.",

    # Yangtze River: Yang(yin-yang concept) + tze(tse fly) + river
    ('placebusters-028', 1):
        "The light masculine half of a famous Eastern symbol and a blood-sucking African fly in a very long river.",

    # Dylan Moran: Dill(herb) + an + Mo(runner) + ran
    ('comediansbusters-005', 2):
        "The herb you put on smoked salmon, then a famous runner who has absolutely legged it.",

    # Romesh Ranganathan: Rome + sh + rang + an + Nathan
    ('comediansbusters-020', 3):
        "Rome has gone all hushed and quiet, a phone rang, and a bloke called Nathan was there.",

    # Water Lilies (artbusters-002): Watt + er + Lily(ies)
    ('artbusters-002', 3):
        "A unit of electrical power and a woman called Lily who has multiplied.",

    # Jeff Bezos: Jeff(using Bez from Happy Mondays approach) + bee + Z + os
    ('businessbusters-001', 2):
        "Bez from Happy Mondays has acquired a bee and an operating system with a bloke called Jeff.",

    # Steve Jobs: Steeve(to stow cargo tight) + jobs
    ('businessbusters-002', 3):
        "Someone who stows cargo very tightly has taken on far too many occupations.",

    # Steve Jobs #2
    ('businessbusters-011', 3):
        "A person who packs cargo with great efficiency has got themselves far too many job descriptions.",

    # Lana Del Rey: Llama(near-homophone of Lana) + dell + ray
    ('2020spopbusters-005', 1):
        "A woolly South American animal, a small wooded valley, and a beam of sunshine.",

    # Jennifer Lawrence: Gen(British slang: information) + i + fur + law + rents
    ('actressbusters-004', 3):
        "All the gen on something involving eyes, a fur coat, a courtroom, and a rent dispute.",

    # Monsoon: Mon(day) + soon
    ('weatherbusters-005', 2):
        "Monday is coming and it is coming very, very quickly.",
}

with open('data/rockbusters.yaml', encoding='utf-8') as f:
    sets = yaml.safe_load(f)

applied = 0
not_found = []
for key, new_clue in FIXES.items():
    set_id, clue_num = key
    if '—' in new_clue or '–' in new_clue:
        print(f'WARNING em-dash in fix {key}')
        continue
    found = False
    for s in sets:
        if s['id'] == set_id:
            for c in s.get('clues', []):
                if c['number'] == clue_num:
                    c['clue'] = new_clue
                    applied += 1
                    found = True
                    break
    if not found:
        not_found.append(key)

if not_found:
    print(f'NOT FOUND: {not_found}')

with open('data/rockbusters.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(sets, f, allow_unicode=True, sort_keys=False,
              default_flow_style=False, width=2000)

print(f'Applied {applied} / {len(FIXES)} fixes')

em_count = sum(1 for s in sets for c in s.get('clues', [])
               if '—' in c.get('clue', '') or '–' in c.get('clue', ''))
print(f'Em dashes remaining in file: {em_count}')
