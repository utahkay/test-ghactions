import os
import subprocess
from collections import defaultdict


def detect_workers_changed(all_changes):
    worker_changes = [x[len("workers/"):] for x in all_changes.split() if x.startswith("workers/")]
    print(worker_changes)
    w = {}
    for change in worker_changes:
        i = change.find('/')
        if i != -1:
            w[change[:i]] = True
    return w.keys()


def build_docker_image(worker):
    base_dir = "/Users/kayjohansen/code/utahkay/test-ghactions/workers"
    worker_dir = os.path.join(base_dir, worker)
    run_shell_command("ls -l", worker_dir)


def run_shell_command(cmd, working_dir=None):
    print(cmd)
    process = subprocess.Popen(cmd, cwd=working_dir, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()[0].decode("utf-8")
    print(output)
    return process.returncode, output


if __name__ == "__main__":
    print("Files changed:")
    all_changes=os.environ.get("FILES_CHANGED")
    print(all_changes)
    workers = detect_workers_changed(all_changes)
    for worker in workers:
        build_docker_image(worker)
