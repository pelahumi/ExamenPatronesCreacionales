class Base(ABC):
    """
    La interfaz Base declara operaciones para todos los tipos de objetos Base.
    """

    @abstractmethod
    def tipo_base(self) -> str:
        pass

class Ingredientes(ABC):
    """
    La interfaz Ingredientes declara operaciones para todos los tipos de objetos Ingredientes.
    """

    @abstractmethod
    def tipo_ingredientes(self) -> str:
        pass

class Coccion(ABC):
    """
    La interfaz Coccion declara operaciones para todos los tipos de objetos Coccion.
    """

    @abstractmethod
    def tipo_coccion(self) -> str:
        pass

class Presentacion(ABC):
    """
    La interfaz Presentacion declara operaciones para todos los tipos de objetos Presentacion.
    """

    @abstractmethod
    def tipo_presentacion(self) -> str:
        pass

class Maridajes(ABC):
    """
    La interfaz Maridajes declara operaciones para todos los tipos de objetos Maridajes.
    """

    @abstractmethod
    def tipo_maridajes(self) -> str:
        pass

class Extras(ABC):
    """
    La interfaz Extras declara operaciones para todos los tipos de objetos Extras.
    """

    @abstractmethod
    def tipo_extras(self) -> str:
        pass