from client import ClarkAiCoworkerClient
client = ClarkAiCoworkerClient()
result = client.assign_task(
    task="Research top 10 AI agent frameworks in 2026 and summarize competitive advantages",
    deliverable_format="Markdown Report"
)
print(f"Coworker: {result['coworker_id']} | ETA: {result['estimated_duration_min']} mins")
for step in result["plan"]:
    print(f"  {step}")
