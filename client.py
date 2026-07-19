import hashlib, time

class ClarkAiCoworkerClient:
    def assign_task(self, task: str, deliverable_format: str) -> dict:
        coworker_id = "clark-" + hashlib.md5(f"{task}{time.time()}".encode()).hexdigest()[:8]
        words = task.split()
        plan = [
            f"[UNDERSTAND] Analyze task scope: '{task[:60]}'",
            f"[RESEARCH] Gather relevant data from cloud environment",
            f"[EXECUTE] Process and apply logic across {len(words)} task dimensions",
            f"[FORMAT] Compile deliverable as {deliverable_format}",
            f"[DELIVER] Upload result and notify requester"
        ]
        duration = max(5, len(words) * 2)
        return {"plan": plan, "estimated_duration_min": duration, "coworker_id": coworker_id}
