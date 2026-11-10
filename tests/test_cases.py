"""
Independent V-Vet symptom extraction dataset.

These cases are separate from the 65 development cases.
Do not add these messages to the extraction prompt.
Expected values represent only explicitly reported, denied,
or uncertain approved signs.
"""

TEST_CASES = [
    {
        "id": "TEST001",
        "message": 'The dairy cow pushes feed around but consumes very little of it.',
        "expected": {'reduced_appetite': 'yes'}
    },
    {
        "id": "TEST002",
        "message": 'The young bull has ignored its usual morning meal.',
        "expected": {'reduced_appetite': 'yes'}
    },
    {
        "id": "TEST003",
        "message": 'She is feeding eagerly and has cleared the trough.',
        "expected": {'reduced_appetite': 'no'}
    },
    {
        "id": "TEST004",
        "message": 'Akadli kancane namuhla, ushiye ukudla okunengi.',
        "expected": {'reduced_appetite': 'yes'}
    },
    {
        "id": "TEST005",
        "message": 'The animal seems drained and barely reacts to people nearby.',
        "expected": {'weakness': 'yes'}
    },
    {
        "id": "TEST006",
        "message": 'Inkomo ayila mandla, ihlezi phansi isikhathi eside.',
        "expected": {'weakness': 'yes'}
    },
    {
        "id": "TEST007",
        "message": 'The heifer is alert, energetic and behaving normally.',
        "expected": {'weakness': 'no'}
    },
    {
        "id": "TEST008",
        "message": 'A noticeable puffiness has appeared where the neck meets the shoulder.',
        "expected": {'swelling': 'yes'}
    },
    {
        "id": "TEST009",
        "message": 'Ngibone ukuvuvuka ngaphansi kwendlebe yayo.',
        "expected": {'swelling': 'yes'}
    },
    {
        "id": "TEST010",
        "message": 'There is no unusual lump along the jawline or shoulder.',
        "expected": {'swelling': 'no'}
    },
    {
        "id": "TEST011",
        "message": 'I can feel something raised under the skin, but I cannot say if it is a swelling.',
        "expected": {'swelling': 'not_sure'}
    },
    {
        "id": "TEST012",
        "message": 'The animal is taking rapid breaths despite standing quietly.',
        "expected": {'rapid_breathing': 'yes'}
    },
    {
        "id": "TEST013",
        "message": 'Iphefumula masinyane loba iphumule.',
        "expected": {'rapid_breathing': 'yes'}
    },
    {
        "id": "TEST014",
        "message": 'Its chest rises at a normal pace while it lies in the shade.',
        "expected": {'rapid_breathing': 'no'}
    },
    {
        "id": "TEST015",
        "message": "I'm uncertain whether the breathing rate is abnormal when it is resting.",
        "expected": {'rapid_breathing': 'not_sure'}
    },
    {
        "id": "TEST016",
        "message": 'A milky-looking layer has formed over the left eye.',
        "expected": {'cloudy_eye': 'yes'}
    },
    {
        "id": "TEST017",
        "message": 'Iliso lalo seliguquke laba ngathi limpunga.',
        "expected": {'cloudy_eye': 'yes'}
    },
    {
        "id": "TEST018",
        "message": 'I can see the pupil clearly; neither eye looks hazy.',
        "expected": {'cloudy_eye': 'no'}
    },
    {
        "id": "TEST019",
        "message": 'The eye seems pale from where I am standing, but I am not sure.',
        "expected": {'cloudy_eye': 'not_sure'}
    },
    {
        "id": "TEST020",
        "message": 'There are bubbles and froth coming from both nostrils.',
        "expected": {'froth_nose_mouth': 'yes'}
    },
    {
        "id": "TEST021",
        "message": 'Kuphuma amagwebu emlonyeni wayo.',
        "expected": {'froth_nose_mouth': 'yes'}
    },
    {
        "id": "TEST022",
        "message": 'The mouth and nose are clean; I cannot see any foam.',
        "expected": {'froth_nose_mouth': 'no'}
    },
    {
        "id": "TEST023",
        "message": 'I noticed a wet patch on the muzzle, but I do not know if it is froth.',
        "expected": {'froth_nose_mouth': 'not_sure'}
    },
    {
        "id": "TEST024",
        "message": 'The urine left a reddish-brown stain on the ground.',
        "expected": {'red_urine': 'yes'}
    },
    {
        "id": "TEST025",
        "message": 'Umchamo usuphenduke waba nsundu.',
        "expected": {'red_urine': 'yes'}
    },
    {
        "id": "TEST026",
        "message": 'The urine is clear yellow, not reddish or tea-like.',
        "expected": {'red_urine': 'no'}
    },
    {
        "id": "TEST027",
        "message": 'I cannot decide whether the sample is brown or simply concentrated.',
        "expected": {'red_urine': 'not_sure'}
    },
    {
        "id": "TEST028",
        "message": 'It has been down for hours and cannot get onto its feet.',
        "expected": {'unable_to_stand': 'yes'}
    },
    {
        "id": "TEST029",
        "message": 'Ayisavuki, lanxa siyizama ukuyiphakamisa.',
        "expected": {'unable_to_stand': 'yes'}
    },
    {
        "id": "TEST030",
        "message": 'The cow stands firmly and crosses the field without falling.',
        "expected": {'unable_to_stand': 'no'}
    },
    {
        "id": "TEST031",
        "message": 'It is resting on its knees; I have not tried to make it stand.',
        "expected": {}
    },
    {
        "id": "TEST032",
        "message": "Ticks are clustered around the animal's udder and inner thighs.",
        "expected": {'ticks': 'yes'}
    },
    {
        "id": "TEST033",
        "message": 'Ngibone imikhaza eminengi entanyeni lenxeni zayo.',
        "expected": {'ticks': 'yes'}
    },
    {
        "id": "TEST034",
        "message": 'There are no attached ticks after checking the whole body.',
        "expected": {'ticks': 'no'}
    },
    {
        "id": "TEST035",
        "message": 'I suspect there could be ticks, but none have been found yet.',
        "expected": {'ticks': 'not_sure'}
    },
    {
        "id": "TEST036",
        "message": 'The cow has a dull appearance but can get up and walk without help.',
        "expected": {'weakness': 'yes', 'unable_to_stand': 'no'}
    },
    {
        "id": "TEST037",
        "message": 'It is breathing comfortably at rest; however, one eye has become cloudy.',
        "expected": {'rapid_breathing': 'no', 'cloudy_eye': 'yes'}
    },
    {
        "id": "TEST038",
        "message": 'No ticks were found, although the animal has stopped eating properly.',
        "expected": {'ticks': 'no', 'reduced_appetite': 'yes'}
    },
    {
        "id": "TEST039",
        "message": 'The urine is dark like strong tea, but I cannot see any foam around its mouth.',
        "expected": {'red_urine': 'yes', 'froth_nose_mouth': 'no'}
    },
    {
        "id": "TEST040",
        "message": 'Inkomo idla kuhle, kodwa iphefumula masinyane iphumule.',
        "expected": {'reduced_appetite': 'no', 'rapid_breathing': 'yes'}
    },
    {
        "id": "TEST041",
        "message": 'Ayilamandla, kodwa ilamandla okusukuma ihambe.',
        "expected": {'weakness': 'yes', 'unable_to_stand': 'no'}
    },
    {
        "id": "TEST042",
        "message": 'There is no swelling under the neck; the eye may have a grey film.',
        "expected": {'swelling': 'no', 'cloudy_eye': 'not_sure'}
    },
    {
        "id": "TEST043",
        "message": 'She may have lost her appetite, while ticks are clearly visible on her back.',
        "expected": {'reduced_appetite': 'not_sure', 'ticks': 'yes'}
    },
    {
        "id": "TEST044",
        "message": 'The animal is not weak, but it has been unable to rise since dawn.',
        "expected": {'weakness': 'no', 'unable_to_stand': 'yes'}
    },
    {
        "id": "TEST045",
        "message": 'No unusual breathing or cloudy eyes; there is also no lump near the shoulder.',
        "expected": {'rapid_breathing': 'no', 'cloudy_eye': 'no', 'swelling': 'no'}
    },
    {
        "id": "TEST046",
        "message": 'Maybe there is froth at the nose; the cow is otherwise standing normally.',
        "expected": {'froth_nose_mouth': 'not_sure', 'unable_to_stand': 'no'}
    },
    {
        "id": "TEST047",
        "message": 'The cow has a swollen-looking area below its ear and is passing red urine.',
        "expected": {'swelling': 'yes', 'red_urine': 'yes'}
    },
    {
        "id": "TEST048",
        "message": 'I am not sure if it is weak, but I saw several ticks on its neck.',
        "expected": {'weakness': 'not_sure', 'ticks': 'yes'}
    },
    {
        "id": "TEST049",
        "message": 'The animal is eating well, breathing normally, and has no visible ticks.',
        "expected": {'reduced_appetite': 'no', 'rapid_breathing': 'no', 'ticks': 'no'}
    },
    {
        "id": "TEST050",
        "message": 'The cow has stopped grazing, and I can see a cloudy patch in one eye.',
        "expected": {'reduced_appetite': 'yes', 'cloudy_eye': 'yes'}
    },
]
