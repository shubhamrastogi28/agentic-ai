

class MemoryStore:
    def __init__(self):
        self.store = {}

    def save(self, task_id: str, data):
        self.store[task_id] = data

    def load(self, task_id: str):
        return self.store.get(task_id)