import scipy.io

from src.box import Box


class Annotation:
    def __init__(self, path):
        self._boxes = []
        self._path = path
        self._load_data()

    def _load_data(self):
        data = scipy.io.loadmat(self._path)
        # god knows why it needs a [0]
        file_data = data["boxes"][0]

        for i in range(len(file_data)):
            current_data = file_data[i]
            self._boxes.append(Box(current_data["a"], current_data["b"], current_data["c"], current_data["d"]))

    def __str__(self):
        result = ""

        for box in self._boxes:
            result += str(box) + "\n"

        return result

    @property
    def boxes(self):
        return self._boxes