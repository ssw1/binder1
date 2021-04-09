class Visual(object):
    @staticmethod
    def imshow(im):
        import cv2
        im_bgr = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cv2.imshow('Board', im_bgr)
        cv2.waitKey(1)
        return

