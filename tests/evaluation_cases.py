
EVALUATION_CASES = [
    {
        "id": "EV001",
        "message": "The cow has stopped eating since yesterday.",
        "expected": {
            "reduced_appetite": "yes"
        }
    },
    {
        "id": "EV002",
        "message": "Mombe yacho yakangorara, haina simba.",
        "expected": {
            "weakness": "yes"
        }
    },
    {
        "id": "EV003",
        "message": "I noticed mbandabvu under the cow's jaw.",
        "expected": {
            "swelling": "yes"
        }
    },
    {
        "id": "EV004",
        "message": "The animal is breathing very fast while resting.",
        "expected": {
            "rapid_breathing": "yes"
        }
    },
    {
        "id": "EV005",
        "message": "One eye looks white and milky.",
        "expected": {
            "cloudy_eye": "yes"
        }
    },
    {
        "id": "EV006",
        "message": "There is foam coming out of its mouth.",
        "expected": {
            "froth_nose_mouth": "yes"
        }
    },
    {
        "id": "EV007",
        "message": "The cow's urine looks like strong tea.",
        "expected": {
            "red_urine": "yes"
        }
    },
    {
        "id": "EV008",
        "message": "The animal cannot get up even when we help it.",
        "expected": {
            "unable_to_stand": "yes"
        }
    },
    {
        "id": "EV009",
        "message": "There are many ticks on the animal's body.",
        "expected": {
            "ticks": "yes"
        }
    },
    {
        "id": "EV010",
        "message": "The cow is eating normally and has no swelling.",
        "expected": {
            "reduced_appetite": "no",
            "swelling": "no"
        }
    },
    {
        "id": "EV011",
        "message": "I'm not sure, but maybe the animal's eye is cloudy.",
        "expected": {
            "cloudy_eye": "not_sure"
        }
    },
    {
        "id": "EV012",
        "message": "Mombe iri kudya zvishoma uye ine zvikwekwe.",
        "expected": {
            "reduced_appetite": "yes",
            "ticks": "yes"
        }
    },
    {
        "id": "EV013",
        "message": "The cow is eating well. I haven't noticed any ticks.",
        "expected": {
            "reduced_appetite": "no",
            "ticks": "no"
        }
    },
    {
        "id": "EV014",
        "message": "The cow has mbandabvu, but I don't know whether it is swelling.",
        "expected": {
            "swelling": "not_sure"
        }
    },
    {
        "id": "EV015",
        "message": "The cow is weak and has foam coming from its nose.",
        "expected": {
            "weakness": "yes",
            "froth_nose_mouth": "yes"
        }
    },

    # EV016 - EV060: Expanded evaluation cases

    {"id": "EV016", "message": "The cow is picking at its feed and eating far less than usual.", "expected": {"reduced_appetite": "yes"}},

    {"id": "EV017", "message": "It has not touched its grazing since morning.", "expected": {"reduced_appetite": "yes"}},

    {"id": "EV018", "message": "The animal is eating normally today.", "expected": {"reduced_appetite": "no"}},

    {"id": "EV019", "message": "Its appetite seems fine, but there is a swelling under its jaw.", "expected": {"reduced_appetite": "no", "swelling": "yes"}},

    {"id": "EV020", "message": "The cow has a lump just in front of its shoulder.", "expected": {"swelling": "yes"}},

    {"id": "EV021", "message": "I cannot see any lump under the jaw or near the shoulder.", "expected": {"swelling": "no"}},

    {"id": "EV022", "message": "The animal looks dull and spends most of the day lying down.", "expected": {"weakness": "yes"}},

    {"id": "EV023", "message": "It is active and moving around as usual, not weak.", "expected": {"weakness": "no"}},

    {"id": "EV024", "message": "Mombe haina simba uye yakangorara.", "expected": {"weakness": "yes"}},

    {"id": "EV025", "message": "The cow is breathing rapidly even while resting in the shade.", "expected": {"rapid_breathing": "yes"}},

    {"id": "EV026", "message": "Its breathing is normal when resting.", "expected": {"rapid_breathing": "no"}},

    {"id": "EV027", "message": "The animal is panting after running, but breathes normally at rest.", "expected": {"rapid_breathing": "no"}},

    {"id": "EV028", "message": "One of the cow's eyes has turned grey and cloudy.", "expected": {"cloudy_eye": "yes"}},

    {"id": "EV029", "message": "Both eyes look clear; there is no white or milky appearance.", "expected": {"cloudy_eye": "no"}},

    {"id": "EV030", "message": "There is a white film over the animal's left eye.", "expected": {"cloudy_eye": "yes"}},

    {"id": "EV031", "message": "Foam is dripping from the animal's nose.", "expected": {"froth_nose_mouth": "yes"}},

    {"id": "EV032", "message": "There is no foam around the mouth or nostrils.", "expected": {"froth_nose_mouth": "no"}},

    {"id": "EV033", "message": "I think there may be a little froth coming from its mouth, but I'm not certain.", "expected": {"froth_nose_mouth": "not_sure"}},

    {"id": "EV034", "message": "The urine is dark brown, almost like tea.", "expected": {"red_urine": "yes"}},

    {"id": "EV035", "message": "The cow's urine is yellow and looks normal, not brown or red.", "expected": {"red_urine": "no"}},

    {"id": "EV036", "message": "I cannot tell if the urine is brown or just very dark.", "expected": {"red_urine": "not_sure"}},

    {"id": "EV037", "message": "The cow tries to rise but cannot stand on its legs.", "expected": {"unable_to_stand": "yes"}},

    {"id": "EV038", "message": "It stands and walks without difficulty.", "expected": {"unable_to_stand": "no"}},

    {"id": "EV039", "message": "The animal can get up, but cannot stay standing and keeps collapsing.", "expected": {"unable_to_stand": "yes"}},

    {"id": "EV040", "message": "I'm unsure whether it can stand; it keeps trying and falling back down.", "expected": {"unable_to_stand": "not_sure"}},

    {"id": "EV041", "message": "I found several ticks attached around the cow's ears.", "expected": {"ticks": "yes"}},

    {"id": "EV042", "message": "There are no ticks on its skin or ears.", "expected": {"ticks": "no"}},

    {"id": "EV043", "message": "The cow has ticks, but is eating normally.", "expected": {"ticks": "yes", "reduced_appetite": "no"}},

    {"id": "EV044", "message": "Mombe iri kudya zvishoma, asi haina zvikwekwe.", "expected": {"reduced_appetite": "yes", "ticks": "no"}},

    {"id": "EV045", "message": "Ayidli kahle futhi ilemikhaza.", "expected": {"reduced_appetite": "yes", "ticks": "yes"}},

    {"id": "EV046", "message": "Ayilamandla kodwa iyenelisa ukusukuma.", "expected": {"weakness": "yes", "unable_to_stand": "no"}},

    {"id": "EV047", "message": "The cow has no appetite problem, but I am not sure whether its eye is cloudy.", "expected": {"reduced_appetite": "no", "cloudy_eye": "not_sure"}},

    {"id": "EV048", "message": "I noticed a lump under the jaw, but I am not sure if it is mbandabvu.", "expected": {"swelling": "not_sure"}},

    {"id": "EV049", "message": "The cow is weak, and there are no ticks on it.", "expected": {"weakness": "yes", "ticks": "no"}},

    {"id": "EV050", "message": "The animal has a cloudy eye and is unable to stand.", "expected": {"cloudy_eye": "yes", "unable_to_stand": "yes"}},

    {"id": "EV051", "message": "There is no froth, but the cow cannot get up.", "expected": {"froth_nose_mouth": "no", "unable_to_stand": "yes"}},

    {"id": "EV052", "message": "The cow's urine is tea-coloured, and it is eating normally.", "expected": {"red_urine": "yes", "reduced_appetite": "no"}},

    {"id": "EV053", "message": "It is breathing fast at rest and has a grey eye.", "expected": {"rapid_breathing": "yes", "cloudy_eye": "yes"}},

    {"id": "EV054", "message": "I have not seen foam, and its urine is normal yellow.", "expected": {"froth_nose_mouth": "no", "red_urine": "no"}},

    {"id": "EV055", "message": "Maybe the cow is eating less, but I am certain there are ticks on its body.", "expected": {"reduced_appetite": "not_sure", "ticks": "yes"}},

    {"id": "EV056", "message": "It may be weak, although it is still standing normally.", "expected": {"weakness": "not_sure"}},

    {"id": "EV057", "message": "I don't know if there is swelling, but it is breathing very fast while resting.", "expected": {"swelling": "not_sure", "rapid_breathing": "yes"}},

    {"id": "EV058", "message": "Mombe yacho haichadyi uye haina simba.", "expected": {"reduced_appetite": "yes", "weakness": "yes"}},

    {"id": "EV059", "message": "Inkomo ayidli kahle njalo ilemikhaza.", "expected": {"reduced_appetite": "yes", "ticks": "yes"}},

    {"id": "EV060", "message": "The cow is not breathing fast at rest, has no swelling, and has no ticks.", "expected": {"rapid_breathing": "no", "swelling": "no", "ticks": "no"}},


    # EV061 - EV065: Original V-Vet sample messages

    {
        "id": "EV061",
        "message": "My cow has not been eating since yesterday and she is breathing very fast.",
        "expected": {
            "reduced_appetite": "yes",
            "rapid_breathing": "yes"
        }
    },

    {
        "id": "EV062",
        "message": "There's foam coming from her nose and she can't get up.",
        "expected": {
            "froth_nose_mouth": "yes",
            "unable_to_stand": "yes"
        }
    },

    {
        "id": "EV063",
        "message": "I think the eyes look a bit cloudy but I'm not sure. She has mbandabvu under the ear.",
        "expected": {
            "cloudy_eye": "not_sure",
            "swelling": "yes"
        }
    },

    {
        "id": "EV064",
        "message": "The calf is fine, just lots of ticks on the ears.",
        "expected": {
            "ticks": "yes"
        }
    },

    {
        "id": "EV065",
        "message": "Mombe yangu haisi kudya, and her urine is dark like tea.",
        "expected": {
            "reduced_appetite": "yes",
            "red_urine": "yes"
        }
    }

]
