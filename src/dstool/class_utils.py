def singleton(cls: type):
    def __new__singleton(cls: type, *args, **kwargs):
        if not hasattr(cls, '__singleton'):
            cls.__singleton = object.__new__(cls)
        return cls.__singleton
    cls.__new__ = __new__singleton
    return cls