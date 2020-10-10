from abc import abstractmethod, ABCMeta


class Vehicle(metaclass=ABCMeta):

    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def kill_engine(self) -> None:
        pass

    @abstractmethod
    def drive(self) -> None:
        pass

    @abstractmethod
    def open_door(self) -> None:
        pass

    @abstractmethod
    def turn(self, direction) -> None:
        pass
