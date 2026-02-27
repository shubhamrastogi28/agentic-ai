from services.agent_runtime.worker import AgentWorker
from services.agent_runtime.models import AgentTask
from services.memory.memory import MemoryStore

class Orchestrator:
    def __init__(self):
        self.worker = AgentWorker()
        self.memory = MemoryStore()

    def run(self, task: AgentTask):
        while task.step != "END":
            result = self.worker.process(task)

            # Save progress externally
            self.memory.save(task.task_id, result)

            task.step = result["next_step"]
        
        print(f"[Orchestrator] Task {task.task_id} completed")
        