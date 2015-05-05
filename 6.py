class Meta(type):
    _types = []

    def register(self, obj):
        self._types.append(obj)


class Sequence(metaclass=Meta):
    pass


seq = Sequence()
seq.register(int)
