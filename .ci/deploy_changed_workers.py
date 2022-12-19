import os

print("Files changed:")
changed=os.environ.get("FILES_CHANGED")
print(type(changed))
print(changed)