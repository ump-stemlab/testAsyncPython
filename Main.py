import asyncio
import klibrary


try:
    asyncio.ensure_future(klibrary.testAsync())
    asyncio.ensure_future(klibrary.testAsync2())
    klibrary.loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    print("Closing loop")
    klibrary.loop.close()