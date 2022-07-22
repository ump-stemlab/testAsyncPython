import asyncio

async def testAsync():
    while True:
        print ("Test 1 repeat 2 seconds")
        await asyncio.sleep(2)

async def testAsync2():
    while True:
        print ("Test 2 repeat 1 seconds")
        await asyncio.sleep(1)

loop= asyncio.get_event_loop()
#Test commit
