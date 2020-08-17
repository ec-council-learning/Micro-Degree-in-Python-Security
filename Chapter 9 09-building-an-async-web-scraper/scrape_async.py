import aiofiles
import aiohttp
import asyncio
import os


URLS = [
    'http://httpstat.us/200',
    'http://httpstat.us/200?sleep=2000',
    'http://httpstat.us/404',
    'http://httpstat.us/500?sleep=3000',
    'http://httpstat.us/524'
]


async def download_html(session, url):
    async with session.get(url, ssl=False) as res:
        filename = f'output/{os.path.basename(url).replace("?", "")}.html'

        async with aiofiles.open(filename, 'wb') as f:
            while True:
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

        return await res.release()

async def download_all(session):
    await asyncio.gather(*[asyncio.create_task(download_html(session, url))
                           for url in URLS])

async def main():
    async with aiohttp.ClientSession() as session:
        await download_all(session)


if  __name__ == '__main__':
    asyncio.run(main())
