def gossip_evaluator():
    while True:
        print ('Who told the gossip? ')
        name = input()
        if name == 'F':
            print ('subtract the drama anda maybe there is something true.')
        elif name == 'M':
            print ('certainly lie.')
        elif name=='Mari':
            print ('obviously true.')
        else:
            print ('evaluate other factor')

gossip_evaluator()
