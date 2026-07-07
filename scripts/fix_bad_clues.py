"""Fix clues that spell out the answer (hyphenated or fake-syllable-names)."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Each entry: (set_id, clue_number, new_clue_text)
FIXES = [
    # ── countrybusters-015 (user's examples) ──────────────────────────────────
    ("countrybusters-015", 1,
     "That famous runner — Mo, everyone calls him — has found a massive legendary bird and gone oh. Mo. Roc. Oh."),
    ("countrybusters-015", 2,
     "Someone's hurt both their kneecaps — both of them at once — and let out a big disappointed sigh. Too. Knee. Sha."),
    ("countrybusters-015", 3,
     "Your mate Al has got himself all the kit. Every bit of equipment you could want. Al. Gear. Yeah."),

    # ── countrybusters-018 ─────────────────────────────────────────────────────
    ("countrybusters-018", 1,
     "Your mum's gone all legal. Very firm on the law, she is — and she's saying I to everything. Ma. Law. I."),
    ("countrybusters-018", 2,
     "Someone's saying no to everything on my behalf, then a bee stings them and they go ooh about it. Nah. Me. Bee. Ah."),
    ("countrybusters-018", 3,
     "That wandering woman — always off somewhere — but she always puts the letter R at the front of her name. On everything. R. Wanda."),

    # ── countrybusters-020 ─────────────────────────────────────────────────────
    ("countrybusters-020", 3,
     "Your mum's gone completely flat out — just lying there — and there's a small island next to her. Ma. Lay. Sia."),

    # ── countrybusters-016 ─────────────────────────────────────────────────────
    ("countrybusters-016", 2,
     "The whole alphabet, and then buying something for a bloke called Jan for Christmas. A to Z and buy Jan a present."),

    # ── countrybusters-014 ─────────────────────────────────────────────────────
    ("countrybusters-014", 1,
     "The letter E has gone sulphurous — all rotten eggs and that — and then it's ordered itself a nice pastry. E. Thio. Pia."),
    ("countrybusters-014", 2,
     "Someone's been on the sunbed, gone all bronzed, and now there's a bloke called Zan standing next to them with a vowel."),

    # ── countrybusters-017 ─────────────────────────────────────────────────────
    ("countrybusters-017", 1,
     "That silk thing men wear round their collar — the proper neckwear — has gone tropical and found itself a country to sit on."),

    # ── countrybusters-010 ─────────────────────────────────────────────────────
    ("countrybusters-010", 1,
     "That practical bloke with the flat cap — always asking if you're capable — right. Can ya? Ken wants to know."),

    # ── countrybusters-006 ─────────────────────────────────────────────────────
    ("countrybusters-006", 3,
     "An animal's private space — proper underground lair — and there's a notch on the wall. Someone's been keeping score in there."),

    # ── countrybusters-005 ─────────────────────────────────────────────────────
    ("countrybusters-005", 2,
     "A very attentive waiter — formal, silver salver, the works — who makes a slightly odd sound at the end of each sentence."),

    # ── countrybusters-011 ─────────────────────────────────────────────────────
    ("countrybusters-011", 1,
     "That ceramic vessel your great-nan used to keep under the bed. Gone all golden and warm. You know the one."),

    # ── countrybusters-013 ─────────────────────────────────────────────────────
    ("countrybusters-013", 1,
     "Someone's had a really frustrating moment — made that noise — and then a very thin woman appeared. Infuriating combination."),

    # ── countrybusters-019 ─────────────────────────────────────────────────────
    ("countrybusters-019", 2,
     "A very loud door slam — proper bang — and then the flattest, most tuneless sound imaginable after it. Desh."),

    # ── holidaybusters-004 ─────────────────────────────────────────────────────
    ("holidaybusters-004", 3,
     "A sharp point on a fence — barbed wire type of arrangement — and there's two of them. A barb and dos of them."),

    # ── holidaybusters-006 ─────────────────────────────────────────────────────
    ("holidaybusters-006", 1,
     "That silk thing blokes wear round their collar — the proper formal neckwear — it's gone and found itself a country."),

    # ── holidaybusters-008 ─────────────────────────────────────────────────────
    ("holidaybusters-008", 1,
     "The Spanish word for sea — they say mar, the Spanish — and a beautiful woman's gone and sat down next to it. Very scenic."),
    ("holidaybusters-008", 2,
     "A very large group of enthusiastic followers who've gone on holiday and things haven't gone well for any of them."),

    # ── holidaybusters-010 ─────────────────────────────────────────────────────
    ("holidaybusters-010", 2,
     "A javelin — properly thrown, good technique — and someone doing repetitive learning. The javelin is very committed to its revision."),

    # ── holidaybusters-016 ─────────────────────────────────────────────────────
    ("holidaybusters-016", 1,
     "The Spanish word for sea and a beautiful woman. They've found each other. Very nice for both of them."),

    # ── drinkbusters-016 ──────────────────────────────────────────────────────
    ("drinkbusters-016", 3,
     "A vehicle — four wheels, engine, the works — that's gone all purple and heathery up north. The car's gone native."),

    # ── primeministersbusters-001 ─────────────────────────────────────────────
    ("primeministersbusters-001", 2,
     "A musical note that won't stop blaring at everyone. Very loud tone, very insistent. Just keeps going about things."),
    ("primeministersbusters-001", 3,
     "A lavatory has climbed through the military ranks. Started at the bottom, worked its way up. It's a major now. The toilet's a major."),

    # ── primeministersbusters-002 ─────────────────────────────────────────────
    ("primeministersbusters-002", 1,
     "A very famous gin brand has gone all muddy. Left out in the rain, hasn't it. Proper brown now, the gin is."),
    ("primeministersbusters-002", 2,
     "Someone's left the recording equipment running — the camera's still on — and a large grey heron has walked into shot."),

    # ── primeministersbusters-003 ─────────────────────────────────────────────
    ("primeministersbusters-003", 1,
     "A very large wild pig — big hairy boar, really getting on everyone's nerves — has had a son who works in sanitation. The son's got silly hair."),
    ("primeministersbusters-003", 3,
     "Someone absolutely loaded — rolling in it, minted — having a small snack. Very well-heeled nibble."),

    # ── primeministersbusters-004 ─────────────────────────────────────────────
    ("primeministersbusters-004", 1,
     "Something very old and very hairy — been around for ages — and it's got Will's son standing next to it. Belongs to Will's lad, that."),

    # ── primeministersbusters-005 ─────────────────────────────────────────────
    ("primeministersbusters-005", 2,
     "A very old hairy thing has put on a Scottish raincoat and gone to work at a flour mill. Very committed to the milling."),
    ("primeministersbusters-005", 3,
     "A very holy bloke who keeps ringing back. Every time you put the phone down, there he is again. Won't stop calling."),

    # ── historybusters-021 ────────────────────────────────────────────────────
    ("historybusters-021", 1,
     "That arm hold they do in wrestling — someone's neck in the crook of your arm — gone all South African and started fighting for justice."),
    ("historybusters-021", 2,
     "A magic trick involving a pig and someone's very impressed — then there's a long straight road that's also a city. Abra. Ham. Lin-coln."),
    ("historybusters-021", 3,
     "A saint who kills dragons has got an absolutely enormous pile of laundry to get through. Tons of it. Washing. Ton."),

    # ── historybusters-025 ────────────────────────────────────────────────────
    ("historybusters-025", 3,
     "A law — a proper legal decree — has joined forces with something, gone even further, and declared itself the greatest."),

    # ── tvbusters-049 ─────────────────────────────────────────────────────────
    ("tvbusters-049", 3,
     "A wooden hammer making a formal decision in a law court, and then someone who's decided to stay and have a look at everything."),

    # ── comediansbusters-022 ──────────────────────────────────────────────────
    ("comediansbusters-022", 3,
     "A noise in dry leaves — very quiet rustling — and then a hospital wing that someone's got very excited about. Very wards-based excitement."),

    # ── landmarkbusters-003 ──────────────────────────────────────────────────
    ("landmarkbusters-003", 3,
     "Something that was owned — a thing that was had — and a bloke called Rian's involved. What Rian had. He built a wall."),

    # ── actressbusters-004 ───────────────────────────────────────────────────
    ("actressbusters-004", 1,
     "The law's been applied very strictly to someone's rental situation — a young woman called Jenny's taken full advantage of it."),

    # ── youtuberbusters-002 ──────────────────────────────────────────────────
    ("youtuberbusters-002", 2,
     "A rocking stone — one of those massive ones that wobbles when you push it — and then a saint who kept getting things in the wrong order."),

    # ── youtuberbusters-003 ──────────────────────────────────────────────────
    ("youtuberbusters-003", 1,
     "A room has gone completely horizontal — just lying there flat out — and it's making coffee and talking about its feelings."),
    ("youtuberbusters-003", 3,
     "Someone's informed on a haystack. Really grassed it up. The haystack is absolutely furious about it."),

    # ── 2020spopbusters-005 ──────────────────────────────────────────────────
    ("2020spopbusters-005", 3,
     "A beam of sunshine — proper ray of light — has gone all Spanish and decided it's royalty. Very sad about the whole thing."),
]


def apply_fixes():
    main_yaml = ROOT / "data" / "rockbusters.yaml"
    with open(main_yaml, encoding="utf-8") as f:
        sets = yaml.safe_load(f)

    # Index sets by id
    by_id = {s["id"]: s for s in sets}

    applied = 0
    for set_id, clue_num, new_clue in FIXES:
        if set_id not in by_id:
            print(f"  MISS (no set): {set_id}")
            continue
        s = by_id[set_id]
        found = False
        for clue in s.get("clues", []):
            if clue["number"] == clue_num:
                old = clue["clue"]
                clue["clue"] = new_clue
                print(f"  FIXED [{set_id} #{clue_num}] {clue.get('answer','')}")
                print(f"    OLD: {old[:80]}")
                print(f"    NEW: {new_clue[:80]}")
                applied += 1
                found = True
                break
        if not found:
            print(f"  MISS (no clue #{clue_num}): {set_id}")

    with open(main_yaml, "w", encoding="utf-8") as f:
        yaml.dump(sets, f, allow_unicode=True, sort_keys=False,
                  default_flow_style=False, width=2000)

    print(f"\nApplied {applied} fixes to rockbusters.yaml")
    return applied


if __name__ == "__main__":
    apply_fixes()
