import os

print("Files changed:")
all_changes=os.environ.get("FILES_CHANGED")
print(type(all_changes))
print(all_changes)

worker_changes = [x.removeprefix("workers/") for x in all_changes.split() if x.startswith("workers/")]
print(worker_changes)
