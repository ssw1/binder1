
class Visual(object):

    def __init__(self):
        self.cells = []
        self.rows = None
        self.cols = None
        self.agent = None

    def imshow(self, board):
        import matplotlib.pyplot as plt
        plt.ion()

        size = 1700

        if self.rows is None:
            self.rows = board.env_height
            self.cols = board.env_width
            self.fig = plt.figure(1)
            self.fig.set_figheight(self.rows)
            self.fig.set_figwidth(self.cols)
            self.fig.patch.set_facecolor('#dddddd')
            self.ax = self.fig.add_subplot(1, 1, 1)
            self.ax.set_facecolor('#dddddd')
            self.fig.patch.set_visible(True) #False)
            self.ax.axis('off')
            y = []
            x = []
            for i in range(self.rows):
                for j in range(self.cols):
                    x.append(j)
                    y.append(i)
            self.ax.scatter(x, y, marker="s", s=size, c='white')
            self.ax.scatter(board.goal[1], board.goal[0], marker="D", s=size//2, c='green')
            for x in board.obstacles:
                self.ax.scatter(x[1], x[0], marker="s", s=size, c='blue')
            assert board.agent is None
            assert self.agent is None
            return

        if board.agent:
            if self.agent is None:
                self.agent = self.ax.scatter([0], [0], marker="o", c='red', s=size)
            else:
                self.agent.set_offsets(list(reversed(board.agent.state)))

        #plt.show()
        plt.pause(.0001)
        return

        import cv2


        im_bgr = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cv2.imshow('Board', im_bgr)
        cv2.waitKey(1)
        return

