from collections import defaultdict

possible_sources = dict()
ingreadient_cnt = defaultdict(int)
known_sources = set()
all_ingr      = set()


def rm_if_found_source(allerg):
    if len(possible_sources[allerg]) == 1:
        for allerg2 in possible_sources:
            if allerg2 != allerg:
                possible_sources[allerg2].difference_update(possible_sources[allerg])



for food in open("input"):
    ingreadients, allergiens = food.strip().split(" (contains ")
    ingreadients = set(ingreadients.split(" "))
    ingreadients.difference_update(known_sources)

    allergiens = allergiens[:-1].split(", ")
    all_ingr.update(ingreadients)

    for allerg in allergiens:
        if allerg in possible_sources: # and len(possible_sources[allerg]) > 1:
            possible_sources[allerg].intersection_update(ingreadients)
        else:
            possible_sources[allerg] = set(ingreadients)
        
        rm_if_found_source(allerg)


    for ingr in ingreadients:
        ingreadient_cnt[ingr] +=1

known_sources.update(*possible_sources.values())
sources = all_ingr.difference(known_sources)

print(possible_sources)
print("Part 1", sum(ingreadient_cnt[s]  for s in sources))
print("Part 2", ",".join(map(lambda item: item[1].pop(),sorted(possible_sources.items(), key=lambda item:item[0]))))
