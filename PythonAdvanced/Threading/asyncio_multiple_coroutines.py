# How to execute multiple coroutines concurrently with asyncio
import asyncio
import time



# coroutine 1
async def print_num():
    num = 1

    while True:
        print (num)
        num += 1
        await asyncio.sleep(1) # asyncio.sleep always suspends current task, allowing other tasks to run

# coroutine 2
async def print_time_interval():
    start_time = time.time()

    while True:
        time_duration = int(time.time() - start_time)
        if(time_duration % 3 == 0):
            print('{} seconds have passed'.format(time_duration))
        await asyncio.sleep(1) # asyncio.sleep always suspends current task, allowing other tasks to run

async def main():
    # Tasks are used to schedule coroutines concurrently
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(print_time_interval())

    # task1 and task2 are executed concurrently (single core) using asyncio.gather
    # asyncio.gather() takes multiple awaitable objects as input and executes them concurrently
    await asyncio.gather( task1, task2 ) # main coroutine waits for completion of task1 and task2

asyncio.run(main())