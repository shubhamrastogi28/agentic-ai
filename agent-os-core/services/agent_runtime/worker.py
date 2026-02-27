from services.agent_runtime.models import AgentTask
import time

class AgentWorker:
    def process(self, task: AgentTask) -> dict:
        """
        Process exactly ONE step of an agent task.
        The worker is stateless
        """
        print(f"[AgentWorker] Processing task {task.task_id} | Step: {task.step}")

        if task.step == "PLAN":
            return {
                "next_step": "EXECUTE",
                "result": ["search data", "analyze data", "summarize"]
            }
        
        if task.step == "EXECUTE":
            return {
                "next_step": "VALIDATE",
                "result": "Execution completed"
            }
        
        if task.step == "VALIDATE":
            return {
                "next_step": "END",
                "result": "Validated successfully"
            }
        
        raise ValueError(f"Unknown step: {task.step}")