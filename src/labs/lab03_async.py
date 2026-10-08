import asyncio
import time


async def fake_call(i: int) -> int:
    await asyncio.sleep(1)
    return i


async def main() -> None:
    start = time.perf_counter()
    print(await asyncio.gather(*(fake_call(i) for i in range(3))))
    print(f"{time.perf_counter() - start:.1f}s")


asyncio.run(main())
