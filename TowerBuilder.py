from Tower import Tower


class TowerBuilder(object):
    def __init__(self):
        self.button = Tower(image='tower1.png')

    def new_TowerButton(self):
        return self.button

    def clear(self):
        self.button = Tower(image='tower1.png')

    def set_property(self, attribute, value):
        if attribute == 'image':
            self.button.set_image(value)
        elif attribute == 'range':
            self.button.set_range(int(value))
