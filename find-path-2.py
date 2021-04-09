import sys
from visual import Visual
from main_loop import run_example

vis = Visual()

# Commands to be implemented after running this file
if __name__ == "__main__":

    delay = None
    episodes = 55
    grid = (5, 4)
    stop_at_goal = False
    for a in sys.argv[1:]:
        if a == '-h' or a == '--help':
            print('\nusage: python(3) main.py [delay=d][episodes=e][grid=RxC]\n')
            sys.exit()
        if a == '-s' or a == '--stop':
            stop_at_goal = True
            continue
        opt, val = a.split('=')
        if opt == '-d' or opt == '--delay':
            delay = float(val)
        if opt == '-e' or opt == '--episodes':
            episodes = int(val)
        if opt == '-g' or opt == '--grid':
            grid = tuple(map(int, val.split('x')))
    run_example(grid, episodes, vis=vis)


