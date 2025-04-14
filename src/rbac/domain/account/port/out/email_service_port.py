from abc import abstractmethod


class EmailServicePort:
    @abstractmethod
    def send(self, email: str, code: str) -> bool:
        raise NotImplementedError("This method should be overridden by subclasses.")
