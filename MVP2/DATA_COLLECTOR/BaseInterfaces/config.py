class Config():

    @classmethod
    def to_dict(cls):
        attrs = [attr for attr in dir(cls) if not callable(
            getattr(cls, attr)) and not attr.startswith("__")]

        configs = {attr: getattr(cls, attr) for attr in attrs}
        return configs
