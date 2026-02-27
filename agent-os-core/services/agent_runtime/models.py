from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class AgentTask:
    task_id: str
    step: str
    goal: str
    payload: Optional[Dict[str, Any]] = None
    retry_count: int = 0
    