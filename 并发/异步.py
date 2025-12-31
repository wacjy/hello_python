import asyncio
from threading import current_thread

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    await future


async def f1(future):
    await asyncio.sleep(3)
    future.set_result('')


