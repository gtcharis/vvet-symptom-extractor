
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
]
