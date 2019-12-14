class Singleton:
    instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance is None or not isinstance(cls.instance, cls):
            cls.instance = cls()
        return cls.instance
