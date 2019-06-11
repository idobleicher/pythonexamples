class Base:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

    def test(self):
        print("Base.")


class PluginA(Base):
    def test(self):
        super().test()
        print("Plugin A.")


class PluginB(Base):
    def test(self):
        super().test()
        print("Plugin B.")


PluginA().test()
# Base.
# Plugin A.

PluginB().test()
# Base.
 # Plugin B.

print(Base.plugins)
# [__main__.PluginA, __main__.PluginB]
