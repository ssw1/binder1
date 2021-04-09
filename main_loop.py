
from board import Board
from agent import QLearningTable


def update(env, q, max_episodes=100, stop_at_goal=False):
    # Resulted list for the plotting Episodes via Steps
    steps = []

    # Summed costs for all episodes in resulted list
    all_costs = []

    for episode in range(max_episodes):
        print('Episode ', episode, 'of', max_episodes)
        # Initial Observation
        observation = env.reset()

        # Updating number of Steps for each Episode
        i = 0

        # Updating the cost for each episode
        cost = 0

        while True:
            # Refreshing environment
            env.render()

            # RL chooses action based on observation
            action = q.choose_action(str(observation))

            # RL takes an action and get the next observation and reward
            observation_, reward, done = env.step(action)

            # RL learns from this transition and calculating the cost
            cost += q.learn(str(observation), action, reward, str(observation_))

            # Swapping the observations - current and next
            if done:
                print(observation_)
            observation = observation_

            # Calculating number of Steps in the current Episode
            i += 1

            # Break while loop when it is the end of current Episode
            # When agent reached the goal or obstacle
            if done:
                steps += [i]
                all_costs += [cost]
                break

    # Showing the final route
    env.final()

    # Showing the Q-table with values for each action
    q.print_q_table()

    # Plotting the results
    q.plot_results(steps, all_costs)


def run_example(grid=(7, 9), episodes=100, stop_at_goal=False, delay=None, vis=None):
    env = Board(grid, delay, stop_at_goal, vis)
    q = QLearningTable(actions=list(range(env.n_actions)))
    update(env, q, episodes)

