from services.orchestrator.orchestrator import Orchestrator
from services.agent_runtime.models import AgentTask

task = AgentTask(
    task_id="task-1",
    step="PLAN",
    goal="Analyze sales data"
)

orchestrator = Orchestrator()
orchestrator.run(task)