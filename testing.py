from vncdotool import api
import asyncio

# To connect to a VNC server through a repeater, add the repeater_id parameter
# The value for repeater_id should be the ID of the target server on the repeater

async def main():
    client = api.connect('65.0.170.114:1', repeater_id='1111')
    print("Client connected.")
    print("Sleeping.")
    await asyncio.sleep(20)

    print("Slept.")
    client.captureScreen('screenshot.png')
    print("Captured.")

# client.disconnect()
if __name__ == "__main__":
    asyncio.run(main())