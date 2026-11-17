import asyncio

async def loop_a():
    while True:
        print("hello 1")
        await asyncio.sleep(1)

async def loop_b():
    while True:
        print("hello 2")
        await asyncio.sleep(2)

async def main():
    task_a = asyncio.create_task(loop_a())
    task_b = asyncio.create_task(loop_b())

    await asyncio.sleep(10)
    task_a.cancel()
    await task_b

asyncio.run(main())