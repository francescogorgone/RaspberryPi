import asyncio #server per gestire chiamate asincrone
import telegram

async def main():
    bot = telegram.Bot("your_API_token")
    async with bot:
        print(await bot.get_me())

if __name__ == '__main__':
    asyncio.run(main())
  
