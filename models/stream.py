class Stream:

    def __init__(self, name=None, **kwargs):
        super(Stream, self).__init__(**kwargs)
        self.name = name

    def hello(self):
        return f'Hi {self.name}'

    @staticmethod
    def world():
        return f'Hello World'
