from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Input = TypeVar('Input')
Output = TypeVar('Output')


class UseCase(Generic[Input, Output], ABC):
    @abstractmethod
    async def execute(self, input_data: Input) -> Output:
        pass
