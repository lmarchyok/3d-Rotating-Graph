import matplotlib.pyplot as plt


def main():
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    for c, z in zip(['r', 'g'], [1, 0]):

        xs = [1, 2, 3, 4]

        if c == 'r':
            ys = [1.9, 2.508, 3.363, 4.799]
        elif c == 'g':
            ys = [0.75, 1.216, 1.29, 2.092]
        else:
            ys = None

        ax.bar(xs, ys, zs=z, zdir='y', color=c, alpha=0.99)

    ax.set_yticklabels([None, "Control", None, None, None, None, "Heat Stress"])
    ax.set_xlabel('Dnj-13 Samples')
    ax.set_ylabel('Treatment Groups')
    ax.set_zlabel('2^(-ddCt)')
    ax.set_title('Gene Expression under Heat Stress')

    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)


if __name__ == "__main__":
    main()
