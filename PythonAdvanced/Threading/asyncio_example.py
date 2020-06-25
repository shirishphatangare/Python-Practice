# Concurrency Vs Parallelism
# asyncio helps to write concurrent, asynchronous and cooperative code in sequential style

# Concurrency - Executing multiple tasks simultaneously on a single CPU core - Tasks start, run and complete in overlapping time periods
# Parallelism - Executing multiple tasks simultaneously on multiple CPU cores - Tasks actually run simultaneosuly without context switching using multiple CPU cores

# Preemptive multitasking Vs Cooperative multitasking

# Preemptive multitasking - Scheduler interrupts tasks at regular intervals - involves frequent and inconvenient context-switching
# Cooperative multitasking - Tasks yield to the Scheduler at their convenience - yield keyword in python

# asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, DB connection libraries, distributed task queues etc.
from collections import deque
from types import coroutine
import asyncio

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# A coroutine is a function which co-executes with other coroutines simultaneously. A coroutine can pause and resume its execution.
async def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        await asyncio.sleep(1) # asyncio.sleep always suspends current task, allowing other tasks to run
        print(f'Hello {friend}')

#friend_upper() # Error - RuntimeWarning: coroutine 'friend_upper' was never awaited

# Post Python 3.7
asyncio.run(friend_upper()) # success with asyncio

# Pre Python 3.7 An alternative to asyncio.run - Event loop
# loop = asyncio.get_event_loop()
# loop.run_until_complete(friend_upper())
# loop.close()