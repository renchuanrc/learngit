import asyncio
import time

ts = None

@asyncio.coroutine
def main():
    global ts
    yield from sub()
    newts = time.time()
    print(newts - ts)

@asyncio.coroutine
def sub():
    global ts
    ts = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
