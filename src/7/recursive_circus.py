def part1(filename):
    with open(filename,'r') as tower:
        tower_dict = {}
        for line in tower.readlines():
            disc = line.strip().split('(')[0].strip()
            weight = int(line.strip().split('(')[1].split(')')[0])
            try:
                carries = line.strip().split('>')[1].replace(' ','').split(',')
            except:
                carries = []
                pass
            tower_dict[disc] = {'weight':weight,'carries':carries}
        #print(tower_dict)
        levels = [[]]
        this_is_true = 1
        for key,value in tower_dict.items():
            if not value['carries']:
                #print(key)
                levels[0].append([key,tower_dict[key]])
        
        level = 1
        while this_is_true:
            levels.insert(level,[])
            prev_level_discs = set([disc[0] for disc in levels[level-1]])
            for disc, attribute in tower_dict.items():
                carries = set(attribute['carries'])
                if prev_level_discs.intersection(carries) != set([]):
                    #print(disc)
                    levels[level].append([disc,attribute])
            if not levels[level]:
                break
            level += 1 

        
        print(levels[level-1])
        return tower_dict,levels

def part2(tower_dict,levels):
    for prev_level,curr_level in zip(levels[:-2],levels[1:]):
        prev_level_discs = set([disc[0] for disc in prev_level])
        curr_level_discs = set([disc[0] for disc in curr_level])
        print(prev_level_discs)
        print(curr_level_discs)



    


part2(*part1('in_test_1.data'))
#part1('in_1.data')
