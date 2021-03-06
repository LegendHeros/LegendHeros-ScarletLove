from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################
chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26
comp_less_than = -1;
comp_greater_than = 1;

skins = [

("man", 0,
"man_body", "man_calf_l", "m_handL", "male_head",
[(20, 0, 0.700000, -0.600000, "Chin Size"),
(260, 0, -0.600000, 1.400000, "Chin Shape"),
(10, 0, -0.500000, 0.900000, "Chin Forward"),
(240, 0, 0.900000, -0.800000, "Jaw Width"),
(210, 0, -0.500000, 1.000000, "Jaw Position"),
(250, 0, 0.800000, -1.000000, "Mouth-Nose Distance"),
(200, 0, -0.300000, 1.000000, "Mouth Width"),
(50, 0, -1.500000, 1.000000, "Cheeks"),
(60, 0, -0.400000, 1.350000, "Nose Height"),
(70, 0, -0.600000, 0.700000, "Nose Width"),
(80, 0, 1.000000, -0.100000, "Nose Size"),
(270, 0, -0.500000, 1.000000, "Nose Shape"),
(90, 0, -0.200000, 1.400000, "Nose Bridge"),
(100, 0, -0.300000, 1.500000, "Cheek Bones"),
(150, 0, -0.200000, 3.000000, "Eye Width"),
(110, 0, 1.500000, -0.900000, "Eye to Eye Dist"),
(120, 0, 1.900000, -1.000000, "Eye Shape"),
(130, 0, -0.500000, 1.100000, "Eye Depth"),
(140, 0, 1.000000, -1.200000, "Eyelids"),
(160, 0, 1.300000, -0.200000, "Eyebrow Position"),
(170, 0, -0.100000, 1.900000, "Eyebrow Height"),
(220, 0, -0.100000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.100000, 1.600000, "Eyebrow Shape"),
(230, 0, 1.200000, -0.700000, "Temple Width"),
(30, 0, -0.600000, 0.900000, "Face Depth"),
(40, 0, 0.900000, -0.600000, "Face Ratio"),
(190, 0, 0.000000, 0.950000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
[("manface_young_2", 0xffcbe0e0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
("manface_midage", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
("manface_young", 0xffd0e0e0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_young_3", 0xffdceded, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
("manface_7", 0xffc0c8c8, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_midage_2", 0xfde4c8d8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_rugged", 0xffb0aab5, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_african", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
],
[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
"skel_human", 1.000000,
psys_game_blood, psys_game_blood_2, 
[[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, temple_width)],
[0.300000, comp_less_than, (1.000000, face_width), (1.000000, temple_width)],
[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, face_depth)],
[0.300000, comp_less_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[1.700000, comp_greater_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[-0.700000, comp_less_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[0.700000, comp_greater_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[2.700000, comp_greater_than, (1.000000, chin_size), (1.000000, mouth_nose_distance), (1.000000, nose_height), (-1.000000, face_width)]
]
),

("woman", skf_use_morph_key_10,
"woman_body", "woman_calf_l", "f_handL", "female_head",
[(230, 0, 0.800000, -1.000000, "Chin Size"),
(220, 0, -1.000000, 1.000000, "Chin Shape"),
(10, 0, -1.200000, 1.000000, "Chin Forward"),
(20, 0, -0.600000, 1.200000, "Jaw Width"),
(40, 0, -0.700000, 1.000000, "Jaw Position"),
(270, 0, 0.900000, -0.900000, "Mouth-Nose Distance"),
(30, 0, -0.500000, 1.000000, "Mouth Width"),
(50, 0, -0.500000, 1.000000, "Cheeks"),
(60, 0, -0.500000, 1.000000, "Nose Height"),
(70, 0, -0.500000, 1.100000, "Nose Width"),
(80, 0, 1.500000, -0.300000, "Nose Size"),
(240, 0, -1.000000, 0.800000, "Nose Shape"),
(90, 0, 0.000000, 1.100000, "Nose Bridge"),
(100, 0, -0.500000, 1.500000, "Cheek Bones"),
(150, 0, -0.400000, 1.000000, "Eye Width"),
(110, 0, 1.000000, 0.000000, "Eye to Eye Dist"),
(120, 0, -0.200000, 1.000000, "Eye Shape"),
(130, 0, -0.100000, 1.600000, "Eye Depth"),
(140, 0, -0.200000, 1.000000, "Eyelids"),
(160, 0, -0.200000, 1.200000, "Eyebrow Position"),
(170, 0, -0.200000, 0.700000, "Eyebrow Height"),
(250, 0, -0.400000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.500000, 1.200000, "Eyebrow Shape"),
(260, 0, 1.000000, -0.700000, "Temple Width"),
(200, 0, -0.500000, 1.000000, "Face Depth"),
(210, 0, -0.500000, 0.900000, "Face Ratio"),
(190, 0, -0.400000, 0.800000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s"],
[],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
[],
[("womanface_young", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_b", 0xffdfdfdf, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_a", 0xffe8dfe5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_brown", 0xffaf9f7e, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
("womanface_african", 0xff808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
("womanface_midage", 0xffe5eaf0, ["hair_black", "hair_brunette", "hair_red", "hair_white"], [0xffffcded, 0xffbbcded, 0xff99eebb]),
],
[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
"skel_human", 0.900000,
psys_game_blood, psys_game_blood_2, 
[]
),

("undead", 0,
"undead_body", "undead_calf_l", "undead_handL", "undead_head",
[],
["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
[("undeadface", 0xffffffff, ["hair_blonde", "hair_red", "hair_brunette"], []),
],
[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit")],
"skel_human", 1.000000,
psys_game_blood, psys_game_blood_2, 
[]
),

("woman2", skf_use_morph_key_10,
"woman_body", "woman_calf_l", "f_handL", "corprus_female_head",
[(40, 0, -1.000000, 0.000000, "Chin Size"),
(30, 0, 0.000000, 1.000000, "Chin Shape"),
(10, 0, 0.000000, 1.000000, "Chin Forward"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0"],
[],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
[],
[("womanface_b_gaolu", 0xffdfdfdf, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_c_gaolu", 0xffe8dfe5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_young_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_brown_gaolu", 0xffaf9f7e, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
("womanface_caucas_gaolu", 0xff808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
("womanface_african_gaolu", 0xff808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
],
[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
"skel_human", 0.950000,
psys_game_blood, psys_game_blood_2, 
[]
),

("female_china", skf_use_morph_key_10,
"woman_body", "woman_calf_l", "f_handL", "female_head_china",
[(230, 0, 0.800000, -1.000000, "Chin Size"),
(220, 0, -1.000000, 1.000000, "Chin Shape"),
(10, 0, -1.200000, 1.000000, "Chin Forward"),
(20, 0, -0.600000, 1.200000, "Jaw Width"),
(40, 0, -0.700000, 1.000000, "Jaw Position"),
(270, 0, 0.900000, -0.900000, "Mouth-Nose Distance"),
(30, 0, -0.500000, 1.000000, "Mouth Width"),
(50, 0, -0.500000, 1.000000, "Cheeks"),
(60, 0, -0.500000, 1.000000, "Nose Height"),
(70, 0, -0.500000, 1.100000, "Nose Width"),
(80, 0, 1.500000, -0.300000, "Nose Size"),
(240, 0, -1.000000, 0.800000, "Nose Shape"),
(90, 0, 0.000000, 1.100000, "Nose Bridge"),
(100, 0, -0.500000, 1.500000, "Cheek Bones"),
(150, 0, -0.400000, 1.000000, "Eye Width"),
(110, 0, 1.000000, 0.000000, "Eye to Eye Dist"),
(120, 0, -0.200000, 1.000000, "Eye Shape"),
(130, 0, -0.100000, 1.600000, "Eye Depth"),
(140, 0, -0.200000, 1.000000, "Eyelids"),
(160, 0, -0.200000, 1.200000, "Eyebrow Position"),
(170, 0, -0.200000, 0.700000, "Eyebrow Height"),
(250, 0, -0.400000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.500000, 1.200000, "Eyebrow Shape"),
(260, 0, 1.000000, -0.700000, "Temple Width"),
(200, 0, -0.500000, 1.000000, "Face Depth"),
(210, 0, -0.500000, 0.900000, "Face Ratio"),
(190, 0, -0.400000, 0.800000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["woman_hair_long_01", "woman_hair_long_02", "woman_hair_y11", "woman_hair_y12", "woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0"],
[],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white", "woman_hair_p"],
[],
[("womanface_young_sg", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_b_sg", 0xffdfdfdf, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_a_sg", 0xffe8dfe5, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_brown_sg", 0xffaf9f7e, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_african_sg", 0xff808080, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
],
[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell"), (voice_victory, "snd_woman_vectory")],
"skel_human", 0.950000,
psys_game_blood, psys_game_blood_2, 
[]
),

("jurenzu", 0,
"man_body", "man_calf_l", "m_handL", "male_head",
[(20, 0, 0.700000, -0.600000, "Chin Size"),
(260, 0, -0.600000, 1.400000, "Chin Shape"),
(10, 0, -0.500000, 0.900000, "Chin Forward"),
(240, 0, 0.900000, -0.800000, "Jaw Width"),
(210, 0, -0.500000, 1.000000, "Jaw Position"),
(250, 0, 0.800000, -1.000000, "Mouth-Nose Distance"),
(200, 0, -0.300000, 1.000000, "Mouth Width"),
(50, 0, -1.500000, 1.000000, "Cheeks"),
(60, 0, -0.400000, 1.350000, "Nose Height"),
(70, 0, -0.600000, 0.700000, "Nose Width"),
(80, 0, 1.000000, -0.100000, "Nose Size"),
(270, 0, -0.500000, 1.000000, "Nose Shape"),
(90, 0, -0.200000, 1.400000, "Nose Bridge"),
(100, 0, -0.300000, 1.500000, "Cheek Bones"),
(150, 0, -0.200000, 3.000000, "Eye Width"),
(110, 0, 1.500000, -0.900000, "Eye to Eye Dist"),
(120, 0, 1.900000, -1.000000, "Eye Shape"),
(130, 0, -0.500000, 1.100000, "Eye Depth"),
(140, 0, 1.000000, -1.200000, "Eyelids"),
(160, 0, 1.300000, -0.200000, "Eyebrow Position"),
(170, 0, -0.100000, 1.900000, "Eyebrow Height"),
(220, 0, -0.100000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.100000, 1.600000, "Eyebrow Shape"),
(230, 0, 1.200000, -0.700000, "Temple Width"),
(30, 0, -0.600000, 0.900000, "Face Depth"),
(40, 0, 0.900000, -0.600000, "Face Ratio"),
(190, 0, 0.000000, 0.950000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
[("manface_young_2", 0xffcbe0e0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
("manface_midage", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
("manface_young", 0xffd0e0e0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_young_3", 0xffdceded, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
("manface_7", 0xffc0c8c8, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_midage_2", 0xfde4c8d8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_rugged", 0xffb0aab5, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_african", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
],
[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
"skel_human", 1.150000,
psys_game_blood, psys_game_blood_2, 
[[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, temple_width)],
[0.300000, comp_less_than, (1.000000, face_width), (1.000000, temple_width)],
[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, face_depth)],
[0.300000, comp_less_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[1.700000, comp_greater_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[-0.700000, comp_less_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[0.700000, comp_greater_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[2.700000, comp_greater_than, (1.000000, chin_size), (1.000000, mouth_nose_distance), (1.000000, nose_height), (-1.000000, face_width)]
]
),

("airenzu", 0,
"man_body", "man_calf_l", "m_handL", "male_head",
[(20, 0, 0.700000, -0.600000, "Chin Size"),
(260, 0, -0.600000, 1.400000, "Chin Shape"),
(10, 0, -0.500000, 0.900000, "Chin Forward"),
(240, 0, 0.900000, -0.800000, "Jaw Width"),
(210, 0, -0.500000, 1.000000, "Jaw Position"),
(250, 0, 0.800000, -1.000000, "Mouth-Nose Distance"),
(200, 0, -0.300000, 1.000000, "Mouth Width"),
(50, 0, -1.500000, 1.000000, "Cheeks"),
(60, 0, -0.400000, 1.350000, "Nose Height"),
(70, 0, -0.600000, 0.700000, "Nose Width"),
(80, 0, 1.000000, -0.100000, "Nose Size"),
(270, 0, -0.500000, 1.000000, "Nose Shape"),
(90, 0, -0.200000, 1.400000, "Nose Bridge"),
(100, 0, -0.300000, 1.500000, "Cheek Bones"),
(150, 0, -0.200000, 3.000000, "Eye Width"),
(110, 0, 1.500000, -0.900000, "Eye to Eye Dist"),
(120, 0, 1.900000, -1.000000, "Eye Shape"),
(130, 0, -0.500000, 1.100000, "Eye Depth"),
(140, 0, 1.000000, -1.200000, "Eyelids"),
(160, 0, 1.300000, -0.200000, "Eyebrow Position"),
(170, 0, -0.100000, 1.900000, "Eyebrow Height"),
(220, 0, -0.100000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.100000, 1.600000, "Eyebrow Shape"),
(230, 0, 1.200000, -0.700000, "Temple Width"),
(30, 0, -0.600000, 0.900000, "Face Depth"),
(40, 0, 0.900000, -0.600000, "Face Ratio"),
(190, 0, 0.000000, 0.950000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4"],
["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
[("manface_young_2", 0xffcbe0e0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
("manface_midage", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
("manface_young", 0xffd0e0e0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_young_3", 0xffdceded, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
("manface_7", 0xffc0c8c8, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_midage_2", 0xfde4c8d8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("manface_rugged", 0xffb0aab5, ["hair_blonde"], [0xff171313, 0xff007080c]),
("manface_african", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
],
[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
"skel_human", 0.900000,
psys_game_blood, psys_game_blood_2, 
[[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, temple_width)],
[0.300000, comp_less_than, (1.000000, face_width), (1.000000, temple_width)],
[1.700000, comp_greater_than, (1.000000, face_width), (1.000000, face_depth)],
[0.300000, comp_less_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[1.700000, comp_greater_than, (1.000000, eyebrow_height), (1.000000, eyebrow_position)],
[-0.700000, comp_less_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[0.700000, comp_greater_than, (1.000000, nose_size), (-1.000000, nose_shape)],
[2.700000, comp_greater_than, (1.000000, chin_size), (1.000000, mouth_nose_distance), (1.000000, nose_height), (-1.000000, face_width)]
]
),

("jurennv", skf_use_morph_key_10,
"woman_body", "woman_calf_l", "f_handL", "female_head",
[(230, 0, 0.800000, -1.000000, "Chin Size"),
(220, 0, -1.000000, 1.000000, "Chin Shape"),
(10, 0, -1.200000, 1.000000, "Chin Forward"),
(20, 0, -0.600000, 1.200000, "Jaw Width"),
(40, 0, -0.700000, 1.000000, "Jaw Position"),
(270, 0, 0.900000, -0.900000, "Mouth-Nose Distance"),
(30, 0, -0.500000, 1.000000, "Mouth Width"),
(50, 0, -0.500000, 1.000000, "Cheeks"),
(60, 0, -0.500000, 1.000000, "Nose Height"),
(70, 0, -0.500000, 1.100000, "Nose Width"),
(80, 0, 1.500000, -0.300000, "Nose Size"),
(240, 0, -1.000000, 0.800000, "Nose Shape"),
(90, 0, 0.000000, 1.100000, "Nose Bridge"),
(100, 0, -0.500000, 1.500000, "Cheek Bones"),
(150, 0, -0.400000, 1.000000, "Eye Width"),
(110, 0, 1.000000, 0.000000, "Eye to Eye Dist"),
(120, 0, -0.200000, 1.000000, "Eye Shape"),
(130, 0, -0.100000, 1.600000, "Eye Depth"),
(140, 0, -0.200000, 1.000000, "Eyelids"),
(160, 0, -0.200000, 1.200000, "Eyebrow Position"),
(170, 0, -0.200000, 0.700000, "Eyebrow Height"),
(250, 0, -0.400000, 0.900000, "Eyebrow Depth"),
(180, 0, -1.500000, 1.200000, "Eyebrow Shape"),
(260, 0, 1.000000, -0.700000, "Temple Width"),
(200, 0, -0.500000, 1.000000, "Face Depth"),
(210, 0, -0.500000, 0.900000, "Face Ratio"),
(190, 0, -0.400000, 0.800000, "Face Width"),
(280, 0, 0.000000, 1.000000, "Post-Edit"),
],
["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s"],
[],
["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
[],
[("womanface_young", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
("womanface_b", 0xffdfdfdf, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_a", 0xffe8dfe5, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
("womanface_brown", 0xffaf9f7e, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
("womanface_african", 0xff808080, ["hair_blonde"], [0xff120808, 0xff007080c]),
],
[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
"skel_human", 1.050000,
psys_game_blood, psys_game_blood_2, 
[]
),


]