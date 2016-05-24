import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_life(board, update, n, plot=False):
    n_steps = 20
    if plot:
        fig = plt.figure()
        im = plt.imshow(board, interpolation='nearest')
        plt.title("The Game of Life")
        plt.axis('off')

        def update_im(dt, im):
            update(board, n)
            im.set_data(board)
            return im,
            
        anim = FuncAnimation(fig, update_im, frames=n_steps, fargs=(im,),
            init_func=lambda: None, interval=50, blit=False, repeat=False)
        plt.show()

    else:
        for t in range(n_steps):
            update(board, n)