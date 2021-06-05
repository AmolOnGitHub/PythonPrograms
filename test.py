from itertools import combinations

enchants = ["Mending", "Unbreaking", "Fire Aspect", "Looting", "Knockback II", "Sweeping Edge", "Sharpness", "Smite", "Bane of Arthropods"]
banned = ["Sharpness", "Smite", "Bane of Arthropods"]
enchantComb = list(combinations(enchants, 3))
i = 0
while i < len(enchantComb):
    count = 0
    comb = enchantComb[i]
    for ban in banned:
        count += comb.count(ban)
    
    if count >= 2:
        enchantComb.remove(comb)
    else: i += 1

