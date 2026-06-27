from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAgent(ABC):
    """
    Abstract Base Class for all specialized agents in the system.
    Ensures a consistent interface for the Orchestrator.
    """

    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}

    @abstractmethod
    async def run(self, input_data: Any) -> Any:
        """
        The core execution method for the agent.
        
        Args:
            input_data: A structured object (usually a Pydantic model) 
                        containing the necessary data for the agent.

        Returns:
            A structured object (Pydantic model) containing the agent's 
            findings or results.
            
        Raises:
            NotImplementedError: If the subclass does not implement this method.
            Exception: For errors during agent execution.
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}'>"
