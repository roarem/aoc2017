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

        levels = []
        this_is_true = 1
        while this_is_true:
            for key,value in tower_dict.items():
                print(key,value)
            


part1('in_test_1.data')
