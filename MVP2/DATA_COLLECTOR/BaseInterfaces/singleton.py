class Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self, *args, **kwargs):
        if self._initialized:
            return

        self.init(*args, **kwargs)

        self._initialized = True

    def init():
        pass
