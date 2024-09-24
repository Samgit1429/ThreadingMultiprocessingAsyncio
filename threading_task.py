import threading
import time

def simulate_io_task(file_name, duration):
  """Simluates an I/O-boud task."""
  print(f'Starting I/O task for {file_name}')
  time.sleep(duration)
  print(f"Finished I/O task for {file_name}")

def run_io_tasks():
  """Run multiple I/O-bound tasks concurrently using threading."""
  threads = []
  file_names = [f"file_{i}.txt" for i in range(5)]

  #Simulate processing five files concurrently
  for i, file_name in enumerate(file_names):
    t = threading.Thread(target=simulate_io_task, args=(file_name, 2))
    threads.append(t)
    t.start()

  #Wait for all threads to finish
  for t in threads:
    t.join()
