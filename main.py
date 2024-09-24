import multiprocessing_task
import threading_task
import async_task
import generate_numbers
import asyncio
import multiprocessing
import time #impot time module to track execution time

def main():
    # Step 1: Generate numbers file
    start_time = time.time() #Start time tracking
    print("Generating numbers.txt file...")
    generate_numbers.generate_numbers_file("numbers.txt", 10000, 5, 15)
    print(f"Numbers saved to numbers.txt in {time.time() - start_time:.2f} seconds\n")
    
    # Step 2: Read numbers from file
    start_time = time.time() #Reset start time for this step
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    print(f"Numbers loaded in {time.time() - start_time:.2f} seconds \n")

    # Step 3: Run multiprocessing task to find primes
    start_time = time.time()
    print("Running multiprocessing task...")
    primes = multiprocessing_task.find_primes_in_range(numbers, chunk_size=len(numbers)//multiprocessing.cpu_count())
    print(f"Prime numbers found: {len(primes)}")
    print(f"Multiprocessing task completed in {time.time() - start_time:.2f} seconds\n")

    # Step 4: Run threading task to simulate I/O
    start_time = time.time()
    print("Running threading I/O tasks...")
    threading_task.run_io_tasks()
    print(f"Threading I/O tasks completed in {time.time() - start_time:.2f} seconds\n")

    # Step 5: Run async tasks to write prime numbers to files
    start_time = time.time()
    print("Running async I/O tasks...")
    asyncio.run(async_task.run_async_tasks(primes))
    print(f"Asyn I/O tasks completed in {time.time() - start_time:.2f} seconds\n")

if __name__ == "__main__":
    overall_start_time = time.time() #Track the overall runtime
    main()
    print(f"Total program runtime: {time.time() - overall_start_time:.2f} seconds")
