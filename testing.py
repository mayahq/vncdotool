from vncdotool import api
import asyncio
import os

# To connect to a VNC server through a repeater, add the repeater_id parameter
# The value for repeater_id should be the ID of the target server on the repeater
server_url = os.getenv('SERVER_URL')
repeater_id = os.getenv('REPEATER_ID')

async def main():
    client = api.connect(server_url, repeater_id=repeater_id)
    print("Client connected.")
    print("Waiting for handshake.")
    client.wait_for_handshake()
    print("Handshake complete.")
    client.captureScreen('screenshot.png')
    print("Captured.")

# client.disconnect()
if __name__ == "__main__":
    asyncio.run(main())