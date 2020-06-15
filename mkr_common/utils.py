class Choices:
    def __init__(self, choices):
        self.vals = choices
        for k, v in self.vals.items():
            setattr(self, k, v['value'])

    @property
    def choices(self):
        return [(v['value'], v['desc']) for k, v in self.vals.items()]

    @property
    def key_vals(self):
        return {k: v['value'] for k, v in self.vals.items()}
