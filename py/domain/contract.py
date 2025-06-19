from abc import ABCMeta, abstractmethod, abstractproperty

class Contract():
    __metaclass__=ABCMeta

    @abstractmethod
    def Echo(self, message: str) -> str:
        pass
    