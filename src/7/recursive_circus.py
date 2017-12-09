def part1(filename):
    with open(filename,'r') as tower:
        tower_dict = {}
        for line in tower.readlines():
            disc = line.strip().split('(')[0]
            weight = int(line.strip().split('(')[1].split(')')[0])
            try:
                carries = line.strip().split('>')[1].replace(' ','').split(',')
            except:
                carries = []
                pass
            tower_dict[disc] = {'weight':weight,'carries':carries}

        levels = [[]]
        level = 0
        this_is_true = 1
        while this_is_true:
            levels.insert(0,[])
            to_delete = []
            for key,value in tower_dict.items():
                print(value)
                if not value['carries']:
                    levels[0].append({key:tower_dict[key]})
                    to_delete.append(key)
                     
            #for key in to_delete:
            #    del tower_dict[key]
            #if not tower_dict:
            #    break
            


part1('in_test_1.data')
