from dataclasses import dataclass, MISSING 


@dataclass
class TaskConfig:
    max_steps: int=10
    supports_continuous_actions:  bool=True
    supports_discrete_actions: bool=True
    env_name: str = "anfuelpriceenv" # Assign the function to the module
    
    
    
    
    
    
    
     # Replace with the actual name of your environment

