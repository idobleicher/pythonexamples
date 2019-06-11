from enum import Enum , auto

#An __init_subclass__ hook that initializes all subclasses of a given class.
#upon class creation, a __set_name__ hook is called on all the attribute (descriptors) defined in the class, and


class RepositoryType(Enum):
    HG = auto()
    GIT = auto()
    SVN = auto()
    PERFORCE = auto()



class Repository():
    _registry = {t: {} for t in RepositoryType}

    @property
    def registry(self):
        return self._registry


    def __init_subclass__(cls, scm_type=None, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if scm_type is not None:
            cls._registry[scm_type][name] = cls



class MainHgRepository(Repository, scm_type=RepositoryType.HG, name='main'):
    pass

class GenericGitRepository(Repository, scm_type=RepositoryType.GIT):
    pass


mainHgRepository = MainHgRepository()

regist = mainHgRepository.registry
print(regist)