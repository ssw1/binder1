class Visual(object):

    def __init__(self):
        self.cells = []
        self.rows = None
        self.cols = None

    def imshow(self, board):
        if self.rows is None:
            self.rows = board.env_height
            self.cols = board.env_width
        import matplotlib.pyplot as plt
        y = []
        x = []
        for i in range(self.rows):
            for j in range(self.cols):
                x.append(j)
                y.append(i)
        plt.scatter(x, y, marker="s")
        plt.show()
        return

        import cv2


        im_bgr = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cv2.imshow('Board', im_bgr)
        cv2.waitKey(1)
        return

