"""Audit all enabled clues for detectable bad patterns."""
import yaml, sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open('data/rockbusters.yaml', encoding='utf-8') as f:
    sets = yaml.safe_load(f)

enabled = [s for s in sets if s.get('enabled')]

# Real English names/words that are fine to use in clues
REAL_NAMES = set(['ron', 'bob', 'tom', 'sam', 'jim', 'tim', 'kim', 'don', 'dan', 'jan',
    'ann', 'amy', 'ben', 'ken', 'lee', 'sue', 'joe', 'pat', 'ray', 'jay',
    'will', 'jack', 'mark', 'luke', 'john', 'paul', 'gary', 'neil', 'carl',
    'alan', 'adam', 'ryan', 'sean', 'dean', 'ross', 'bill', 'dave', 'nick',
    'pete', 'mike', 'rick', 'rob', 'rod', 'alf', 'len', 'mel', 'val', 'lyn',
    'liz', 'bev', 'kay', 'may', 'joy', 'ivy', 'eve', 'ada', 'ida', 'ina',
    'emma', 'anna', 'mary', 'jane', 'kate', 'ruth', 'rosa', 'iris', 'ella',
    'vera', 'vera', 'nora', 'dora', 'lora', 'lena', 'tina', 'nina', 'gina',
    'lisa', 'rosa', 'alba', 'alma', 'edna', 'rita', 'babs', 'maud', 'enid',
    'fred', 'frank', 'harry', 'henry', 'barry', 'larry', 'terry', 'perry',
    'jerry', 'kenny', 'donny', 'ronny', 'tommy', 'jimmy', 'billy', 'willy',
    'bobby', 'robby', 'paddy', 'barry', 'carry', 'kerry', 'derry', 'ferry',
    'merry', 'terry', 'berry', 'cherry', 'sherry', 'gerry', 'jerry', 'perry',
    'colin', 'kevin', 'simon', 'peter', 'james', 'david', 'steven', 'martin',
    'gordon', 'harold', 'walter', 'victor', 'alfred', 'george', 'thomas',
    'arthur', 'edward', 'ernest', 'albert', 'robert', 'charles', 'michael',
    'donald', 'dennis', 'philip', 'warren', 'graham', 'trevor', 'stanley',
    'violet', 'evelyn', 'gloria', 'marina', 'sheila', 'sylvia', 'brenda',
    'sandra', 'wendy', 'helen', 'linda', 'janet', 'carol', 'diana', 'elaine',
    'shirley', 'valerie', 'pauline', 'maureen', 'barbara', 'dorothy',
    # actual English words that happen to match answer chunks
    'back', 'band', 'bar', 'barn', 'base', 'bass', 'bath', 'bay', 'bell',
    'bird', 'black', 'blade', 'block', 'blue', 'bold', 'bolt', 'bond', 'bone',
    'book', 'boot', 'bore', 'box', 'brake', 'brave', 'break', 'bright',
    'brow', 'brown', 'buck', 'bull', 'burn', 'bush', 'but', 'call', 'calm',
    'camp', 'can', 'cap', 'car', 'card', 'care', 'case', 'cash', 'cast',
    'cave', 'chain', 'chalk', 'chance', 'change', 'char', 'chase', 'cheap',
    'check', 'chin', 'chip', 'chord', 'clam', 'clap', 'clay', 'clear',
    'clip', 'cloak', 'close', 'club', 'coal', 'coat', 'coil', 'cold',
    'cook', 'cool', 'cope', 'cord', 'corn', 'cost', 'coup', 'crag', 'cram',
    'crane', 'crate', 'cross', 'crow', 'crown', 'cuff', 'cure', 'curl',
    'damp', 'dare', 'dark', 'dart', 'dash', 'daze', 'deal', 'deck', 'deed',
    'deep', 'dell', 'dent', 'dew', 'dice', 'dill', 'dime', 'dip', 'dire',
    'disc', 'dish', 'dock', 'dome', 'door', 'dote', 'drag', 'drain', 'drape',
    'draw', 'dread', 'drift', 'drill', 'drip', 'drive', 'drone', 'drop',
    'drum', 'duck', 'dull', 'dune', 'dust', 'each', 'earl', 'earn', 'ease',
    'east', 'edge', 'else', 'fair', 'fake', 'fall', 'fame', 'fan', 'farm',
    'fast', 'fate', 'fell', 'felt', 'fern', 'fest', 'file', 'film', 'firm',
    'fish', 'fist', 'flag', 'flap', 'flat', 'flaw', 'flea', 'flee', 'flew',
    'flex', 'flip', 'flit', 'flock', 'flow', 'foam', 'fold', 'folk', 'fond',
    'ford', 'fore', 'fork', 'form', 'fort', 'foul', 'four', 'fowl', 'fray',
    'free', 'fret', 'frill', 'froth', 'frown', 'fuel', 'full', 'fume',
    'fund', 'fuse', 'gale', 'gall', 'game', 'gang', 'gash', 'gate', 'gaze',
    'gear', 'gild', 'give', 'glade', 'glare', 'glee', 'glide', 'glow',
    'glue', 'goal', 'gore', 'gown', 'grab', 'grace', 'grade', 'grain',
    'gran', 'grant', 'grasp', 'grate', 'grave', 'gray', 'graze', 'greed',
    'grime', 'grip', 'groan', 'grope', 'grove', 'grow', 'grunt', 'guard',
    'guild', 'gulf', 'gull', 'gulp', 'gust', 'hack', 'hail', 'hair', 'hall',
    'halt', 'hand', 'hang', 'hard', 'harm', 'harp', 'hawk', 'haze', 'heal',
    'heap', 'heat', 'hedge', 'helm', 'hemp', 'herb', 'herd', 'hide', 'high',
    'hike', 'hilt', 'hive', 'hoar', 'hold', 'hole', 'hull', 'hump', 'hunt',
    'hurl', 'idol', 'inch', 'jade', 'jail', 'jest', 'join', 'jump', 'keen',
    'keep', 'kill', 'knot', 'lack', 'lake', 'lame', 'lamp', 'lane', 'lark',
    'lash', 'last', 'lawn', 'lead', 'leaf', 'lean', 'ledge', 'lemon', 'lime',
    'link', 'lint', 'list', 'loft', 'loom', 'loop', 'lore', 'lose', 'loud',
    'lure', 'lurk', 'made', 'mail', 'main', 'make', 'male', 'mall', 'mare',
    'mast', 'meld', 'mend', 'mesh', 'mild', 'mill', 'mind', 'mint', 'mist',
    'mitt', 'mock', 'mode', 'mold', 'mole', 'monk', 'moor', 'mop', 'more',
    'mote', 'moth', 'mow', 'much', 'muck', 'mule', 'mull', 'muse', 'must',
    'nail', 'nape', 'nave', 'neat', 'nest', 'nice', 'nook', 'norm', 'nose',
    'note', 'numb', 'opal', 'orb', 'oven', 'over', 'pace', 'pack', 'page',
    'pail', 'pale', 'palm', 'pane', 'park', 'part', 'pass', 'past', 'pave',
    'peal', 'pear', 'peat', 'peek', 'peel', 'peer', 'pelt', 'perch', 'pick',
    'pike', 'pile', 'pine', 'pipe', 'pith', 'plan', 'plane', 'plant', 'play',
    'plea', 'plot', 'plow', 'plum', 'plume', 'plunge', 'plus', 'poke', 'pole',
    'pond', 'pool', 'pose', 'pour', 'preen', 'prey', 'prig', 'prim', 'prude',
    'puff', 'pull', 'pump', 'pure', 'push', 'rack', 'raid', 'rail', 'rake',
    'ramp', 'rand', 'rang', 'rank', 'rant', 'rare', 'rash', 'rate', 'rave',
    'real', 'reel', 'reef', 'rein', 'rend', 'rent', 'rest', 'rich', 'ride',
    'rift', 'rile', 'rime', 'riot', 'rise', 'risk', 'roam', 'roar', 'rode',
    'role', 'roost', 'rope', 'rose', 'rout', 'rove', 'rude', 'ruin', 'rule',
    'rump', 'rust', 'rut', 'safe', 'sage', 'sail', 'sake', 'sale', 'salt',
    'sand', 'sane', 'scar', 'seam', 'seep', 'self', 'sell', 'shed', 'shim',
    'shin', 'shun', 'shy', 'sick', 'sill', 'silo', 'silt', 'sink', 'site',
    'slab', 'slag', 'slap', 'slat', 'slave', 'slay', 'slim', 'slip', 'slit',
    'slot', 'slug', 'slum', 'slur', 'smash', 'smear', 'smoke', 'snag', 'snare',
    'snob', 'snow', 'snub', 'soak', 'soar', 'sock', 'soft', 'soil', 'sole',
    'some', 'soot', 'sore', 'sort', 'soul', 'span', 'spar', 'spit', 'spoke',
    'spool', 'sport', 'spray', 'spur', 'stab', 'stag', 'stain', 'stake',
    'stale', 'stall', 'stamp', 'stave', 'stem', 'step', 'stern', 'stir',
    'stock', 'stomp', 'stop', 'storm', 'strap', 'straw', 'stray', 'strip',
    'stub', 'stud', 'stun', 'surge', 'swamp', 'swap', 'swath', 'sway', 'swell',
    'swim', 'swipe', 'swoop', 'tale', 'tame', 'tank', 'tape', 'tare', 'tarn',
    'taut', 'teat', 'tell', 'temp', 'tend', 'tent', 'term', 'test', 'text',
    'thaw', 'theft', 'they', 'thin', 'tier', 'tilt', 'tine', 'toll', 'tone',
    'tong', 'tool', 'tops', 'toss', 'tow', 'town', 'track', 'tract', 'trap',
    'tray', 'trim', 'trip', 'trod', 'trot', 'trove', 'trust', 'tuft', 'tune',
    'turf', 'twig', 'type', 'vain', 'vale', 'vane', 'vast', 'veil', 'vein',
    'vent', 'verse', 'vest', 'vow', 'wade', 'wage', 'wail', 'wake', 'wane',
    'ward', 'ware', 'warm', 'warp', 'wart', 'wary', 'wash', 'wave', 'weal',
    'wean', 'weed', 'weir', 'weld', 'west', 'whim', 'whirl', 'wide', 'wild',
    'wilt', 'wimp', 'wipe', 'wire', 'wise', 'wish', 'wisp', 'woe', 'woke',
    'wold', 'wolf', 'wore', 'worn', 'wren', 'writ', 'yell', 'yoke', 'zeal',
    'zinc', 'zone'])

bad_clues = []

for s in enabled:
    for c in s.get('clues', []):
        answer = c.get('answer', '').strip()
        clue = c.get('clue', '').strip()
        ans_lower = answer.lower()
        clue_lower = clue.lower()

        flags = []

        # Pattern 1: em dash still present
        if '—' in clue or '–' in clue:
            flags.append('EM_DASH')

        # Pattern 2: non-word chunk of answer used as a name
        # e.g. 'bloke called Moroc', 'bloke called Adren'
        name_pat = re.compile(
            r'(?:bloke|fella|man|woman|lad|chap|fellow|gentleman|lady|girl|guy|bloke)\s+called\s+([a-z]+)',
            re.IGNORECASE)
        for m in name_pat.finditer(clue):
            name = m.group(1).lower()
            if (len(name) >= 3 and name in ans_lower
                    and name not in REAL_NAMES):
                flags.append(f'FAKE_NAME:{name}')

        # Pattern 3: hyphenated answer breakdown
        for i in range(2, len(ans_lower)-1):
            hyph = ans_lower[:i] + '-' + ans_lower[i:]
            if hyph in clue_lower:
                flags.append(f'HYPHEN:{hyph}')
                break

        # Pattern 4: answer itself (full, 5+ chars) verbatim in clue
        if len(ans_lower) >= 6 and ans_lower in clue_lower:
            flags.append(f'ANSWER_VERBATIM')

        if flags:
            bad_clues.append({
                'id': s['id'],
                'num': c['number'],
                'answer': answer,
                'clue': clue,
                'flags': flags
            })

print(f'Issues found: {len(bad_clues)}')
print()
for b in bad_clues:
    print(f'[{b["id"]}] #{b["num"]} {b["answer"]}')
    print(f'  FLAGS: {b["flags"]}')
    print(f'  CLUE: {b["clue"][:120]}')
    print()

# Save for fixing
with open('scripts/audit_results.json', 'w', encoding='utf-8') as f:
    json.dump(bad_clues, f, ensure_ascii=False, indent=2)
print(f'Saved to scripts/audit_results.json')
