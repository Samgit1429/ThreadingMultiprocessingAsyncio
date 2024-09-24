import asyncio

async def async_write_to_file(filename, data, duration):
    """Simulates writing data to a file asynchronously."""
    await asyncio.sleep(duration)  # Simulate async delay
    with open(filename, "w") as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Finished writing to {filename}")

async def run_async_tasks(primes):
    """Write prime numbers to multiple files asynchronously."""
    tasks = []
    chunk_size = len(primes) // 5
    for i in range(5):
        chunk = primes[i*chunk_size:(i+1)*chunk_size]
        tasks.append(async_write_to_file(f"primes_{i}.txt", chunk, 2))
    
    await asyncio.gather(*tasks)
