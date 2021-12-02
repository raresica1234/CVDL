import matplotlib.pyplot as plt
from data_loading import DataGenerator
from src.annotation import Annotation
from src.box import Box


def box_to_plot_points(box: Box):
    return [box.a.y, box.b.y, box.c.y, box.d.y, box.a.y], [box.a.x, box.b.x, box.c.x, box.d.x, box.a.x]


if __name__ == '__main__':
    train_generator = DataGenerator("res/", 32, (400, 400, 3), 37)
    # technically those two are useless.
    # label_names = train_generator.class_names
    # assert len(label_names) == 6
    batch_x, batch_y = train_generator[0]

    fig, axes = plt.subplots(nrows=1, ncols=6, figsize=[16, 9])
    for i in range(len(axes)):
        # axes[i].set_title(label_names[batch_y[i]])
        axes[i].imshow(batch_x[i])
        annotation = batch_y[i]
        for box in annotation.boxes:
            axes[i].plot(*box_to_plot_points(box), "g*:")

            # line1 = plt.Line2D(box.a.as_tuple(), box.b.as_tuple(), lw=1.5)
            # line2 = plt.Line2D(box.b.as_tuple(), box.c.as_tuple(), lw=1.5)
            # line3 = plt.Line2D(box.c.as_tuple(), box.d.as_tuple(), lw=1.5)
            # line4 = plt.Line2D(box.d.as_tuple(), box.a.as_tuple(), lw=1.5)
            #
            # print(dir(axes[i]))
            # axes[i].gca().add_line(line1)
            # axes[i].gca().add_line(line2)
            # axes[i].gca().add_line(line3)
            # axes[i].gca().add_line(line4)

    plt.show()
