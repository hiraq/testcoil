from abc import ABC, abstractmethod

class BaseRepository(ABC):
    
    _model = None

    def __init__(self, model):
        self._model = model

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def edit(self, id, doc):
        pass

    @abstractmethod
    def delete(self, id, options=None):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findBy(self, options):
        pass
