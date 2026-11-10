"""
Independent V-Vet symptom extraction dataset.

These cases are separate from the 65 development cases.
Do not add these messages to the extraction prompt.
Expected values represent only explicitly reported, denied,
or uncertain approved signs.
"""

VALIDATION_CASES = [
    {
        "id": "VAL001",
        "message": 'The heifer only nibbles at the hay and leaves most of it behind.',
        "expected": {'reduced_appetite': 'yes'}
    },
    {
        "id": "VAL002",
        "message": 'Since the rain started, the bull has barely gone to the grazing area.',
        "expected": {'reduced_appetite': 'yes'}
    },
    {
        "id": "VAL003",
        "message": 'The mare finishes every portion placed in her manger without hesitation.',
        "expected": {'reduced_appetite': 'no'}
    },
    {
        "id": "VAL004",
        "message": 'Kudya kwake kwakajairika nhasi; hapana chachinja.',
        "expected": {'reduced_appetite': 'no'}
    },
    {
        "id": "VAL005",
        "message": 'The ox is sluggish and does not respond when the others move.',
        "expected": {'weakness': 'yes'}
    },
    {
        "id": "VAL006",
        "message": 'Mombe yacho inoratidzika kuneta, inoramba yakarara.',
        "expected": {'weakness': 'yes'}
    },
    {
        "id": "VAL007",
        "message": 'The steer is lively and keeps running with the herd.',
        "expected": {'weakness': 'no'}
    },
    {
        "id": "VAL008",
        "message": "The farmer noticed a rounded swelling beneath the animal's lower jaw.",
        "expected": {'swelling': 'yes'}
    },
    {
        "id": "VAL009",
        "message": 'Pane bundu pamberi pepfudzi remombe.',
        "expected": {'swelling': 'yes'}
    },
    {
        "id": "VAL010",
        "message": 'Akukho kuqubuka ngaphansi komhlathi wenkomo.',
        "expected": {'swelling': 'no'}
    },
    {
        "id": "VAL011",
        "message": 'A raised lump can be seen on the front of the neck, but its nature is unclear.',
        "expected": {'swelling': 'not_sure'}
    },
    {
        "id": "VAL012",
        "message": "Even while standing in the kraal, the cow's sides are moving unusually quickly.",
        "expected": {'rapid_breathing': 'yes'}
    },
    {
        "id": "VAL013",
        "message": 'Inkomo iphefumula ngamandla ingakagijimi.',
        "expected": {'rapid_breathing': 'yes'}
    },
    {
        "id": "VAL014",
        "message": "When resting quietly, the animal's breathing is steady and unhurried.",
        "expected": {'rapid_breathing': 'no'}
    },
    {
        "id": "VAL015",
        "message": "I'm struggling to tell whether its breathing is faster than normal.",
        "expected": {'rapid_breathing': 'not_sure'}
    },
    {
        "id": "VAL016",
        "message": 'There is a pale, opaque patch covering part of the right eye.',
        "expected": {'cloudy_eye': 'yes'}
    },
    {
        "id": "VAL017",
        "message": 'Iliso lenkomo libonakala limhlophe, alisacaci.',
        "expected": {'cloudy_eye': 'yes'}
    },
    {
        "id": "VAL018",
        "message": 'Both eyes are bright and transparent, with no cloudy film.',
        "expected": {'cloudy_eye': 'no'}
    },
    {
        "id": "VAL019",
        "message": 'The eye looks strange in the sunlight; I cannot tell if it is milky.',
        "expected": {'cloudy_eye': 'not_sure'}
    },
    {
        "id": "VAL020",
        "message": "A bubbly substance is gathering around the animal's nostrils.",
        "expected": {'froth_nose_mouth': 'yes'}
    },
    {
        "id": "VAL021",
        "message": 'Pane furo kubva mumhino dzemombe.',
        "expected": {'froth_nose_mouth': 'yes'}
    },
    {
        "id": "VAL022",
        "message": 'I checked its muzzle and there was no foam or saliva bubbling there.',
        "expected": {'froth_nose_mouth': 'no'}
    },
    {
        "id": "VAL023",
        "message": 'Something white is near its mouth, though I cannot confirm it is froth.',
        "expected": {'froth_nose_mouth': 'not_sure'}
    },
    {
        "id": "VAL024",
        "message": 'The liquid it passes is reddish, almost the shade of rust.',
        "expected": {'red_urine': 'yes'}
    },
    {
        "id": "VAL025",
        "message": 'Umchamo wayo umnyama kakhulu, ufana letiye eliqinileyo.',
        "expected": {'red_urine': 'yes'}
    },
    {
        "id": "VAL026",
        "message": 'Its urine is pale yellow, just as it normally is.',
        "expected": {'red_urine': 'no'}
    },
    {
        "id": "VAL027",
        "message": 'The urine looked unusually dark, but I am unsure of its actual colour.',
        "expected": {'red_urine': 'not_sure'}
    },
    {
        "id": "VAL028",
        "message": 'The cow has remained on the ground and cannot support itself on its legs.',
        "expected": {'unable_to_stand': 'yes'}
    },
    {
        "id": "VAL029",
        "message": 'Inkomo izama ukuphakama kodwa iyawa futhi.',
        "expected": {'unable_to_stand': 'yes'}
    },
    {
        "id": "VAL030",
        "message": 'It rose by itself and is walking around the pen.',
        "expected": {'unable_to_stand': 'no'}
    },
    {
        "id": "VAL031",
        "message": 'It is lying down at the moment, but I have not checked whether it can rise.',
        "expected": {}
    },
    {
        "id": "VAL032",
        "message": 'Small parasites are attached to the skin around the tail and belly.',
        "expected": {'ticks': 'yes'}
    },
    {
        "id": "VAL033",
        "message": 'Kule nkomo imikhaza eminengi emzimbeni wayo.',
        "expected": {'ticks': 'yes'}
    },
    {
        "id": "VAL034",
        "message": 'I searched along the ears and neck and found no ticks.',
        "expected": {'ticks': 'no'}
    },
    {
        "id": "VAL035",
        "message": 'There may be ticks hidden in its coat; I have not looked closely.',
        "expected": {'ticks': 'not_sure'}
    },
    {
        "id": "VAL036",
        "message": 'The cow is weak, but it is still able to rise when called.',
        "expected": {'weakness': 'yes', 'unable_to_stand': 'no'}
    },
    {
        "id": "VAL037",
        "message": 'No foam is visible, although the animal is breathing rapidly at rest.',
        "expected": {'froth_nose_mouth': 'no', 'rapid_breathing': 'yes'}
    },
    {
        "id": "VAL038",
        "message": 'Its eye is clear, but the animal has stopped going to the feed trough.',
        "expected": {'cloudy_eye': 'no', 'reduced_appetite': 'yes'}
    },
    {
        "id": "VAL039",
        "message": 'I cannot confirm the swelling; however, the cow has a rust-coloured urine.',
        "expected": {'swelling': 'not_sure', 'red_urine': 'yes'}
    },
    {
        "id": "VAL040",
        "message": 'The animal is eating as usual and has no ticks around its ears.',
        "expected": {'reduced_appetite': 'no', 'ticks': 'no'}
    },
    {
        "id": "VAL041",
        "message": 'Mombe ine simba, asi pane furo rinobuda mumuromo.',
        "expected": {'weakness': 'no', 'froth_nose_mouth': 'yes'}
    },
    {
        "id": "VAL042",
        "message": "The calf's legs are steady, though its breathing seems unusually quick at rest.",
        "expected": {'unable_to_stand': 'no', 'rapid_breathing': 'yes'}
    },
    {
        "id": "VAL043",
        "message": 'I am unsure about the eye, and I also cannot tell whether the urine is brown.',
        "expected": {'cloudy_eye': 'not_sure', 'red_urine': 'not_sure'}
    },
    {
        "id": "VAL044",
        "message": 'Ayidli njengakuqala, kodwa ayilamandla futhi.',
        "expected": {'reduced_appetite': 'yes', 'weakness': 'yes'}
    },
    {
        "id": "VAL045",
        "message": 'Akulamikhaza engiyibonileyo, kodwa inkomo ilebundu ngaphansi komhlathi.',
        "expected": {'ticks': 'no', 'swelling': 'yes'}
    },
    {
        "id": "VAL046",
        "message": 'The cow has no trouble standing; its appetite is poor and it has ticks.',
        "expected": {'unable_to_stand': 'no', 'reduced_appetite': 'yes', 'ticks': 'yes'}
    },
    {
        "id": "VAL047",
        "message": 'I saw no cloudy appearance in the eyes, and no froth at the nostrils.',
        "expected": {'cloudy_eye': 'no', 'froth_nose_mouth': 'no'}
    },
    {
        "id": "VAL048",
        "message": 'Maybe she is weak, but she is definitely eating less than yesterday.',
        "expected": {'weakness': 'not_sure', 'reduced_appetite': 'yes'}
    },
    {
        "id": "VAL049",
        "message": "The animal's urine may be tea-coloured; its breathing is normal while resting.",
        "expected": {'red_urine': 'not_sure', 'rapid_breathing': 'no'}
    },
    {
        "id": "VAL050",
        "message": 'It has a lump near the shoulder and keeps lying down looking dull.',
        "expected": {'swelling': 'yes', 'weakness': 'yes'}
    },
]
