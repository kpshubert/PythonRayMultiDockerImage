"""Simple Ray test: run many short tasks and show which container ran each one."""

import socket
import time
from collections import Counter

import ray

# When run as a job on the cluster, "auto" attaches to the running head node.
ray.init(address="auto")


@ray.remote
def where_am_i(i):
    time.sleep(2)  # simulate work so tasks overlap and spread across nodes
    return socket.gethostname()


alive = [n for n in ray.nodes() if n["Alive"]]
print(f"Nodes alive in cluster: {len(alive)}")

NUM_TASKS = 24
start = time.time()
results = ray.get([where_am_i.remote(i) for i in range(NUM_TASKS)])
elapsed = time.time() - start

print(f"{NUM_TASKS} tasks finished in {elapsed:.1f}s")
for host, count in sorted(Counter(results).items()):
    print(f"  {host}: {count} tasks")
