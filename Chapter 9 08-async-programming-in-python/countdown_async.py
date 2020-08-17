import asyncio


async def countdown(name, delay):
    counter = 5

    while counter:
        await asyncio.sleep(delay)  # number of seconds
        print(f'{name} is counting down: {counter}...')
        counter -= 1

    print(f'{name} finished counting down')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(countdown('Coroutine Alice', 1)),
        loop.create_task(countdown('Coroutine Bob', 2))
    ]

    loop.run_until_complete(asyncio.wait(tasks))
