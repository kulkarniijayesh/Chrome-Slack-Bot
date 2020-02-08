import asyncio
import websockets
import json

async def connect():
    uri = "ws://127.0.0.1:9222/devtools/browser/839d03fa-718d-472c-9ad9-cda4d5c842ed"
    async with websockets.connect(uri, ping_interval=None) as websocket:
        await websocket.send(json.dumps({"method":"Target.getBrowserContexts","params":{},"id":1}))
        #ws = await websockets.connect(uri)
        response = await websocket.recv()
        await websocket.send(json.dumps({"method":"Target.setDiscoverTargets","params":{"discover":True},"id":2}))
#        await websocket.send(json.dumps({"method":"Target.createTarget","params":{"url":"about:blank"},"id":3}))
        await websocket.send(json.dumps({"sessionId":"9EF0826FDFEB8BA36FAC0A9D210DE19E","method":"Page.getFrameTree","params":{},"id":3}))

#        for i in range(15):
#            response = await websocket.recv()
#            print('response from server: ', {response})

        await websocket.send(json.dumps({"sessionId":"9EF0826FDFEB8BA36FAC0A9D210DE19E","method":"Page.navigate","params":{"url":"https://www.youtube.com/watch?v=g-C8QJH-NWI","frameId":"45B441361C15E9C18F38D1EA7B26E060"},"id":4}))
        await websocket.send(json.dumps({"sessionId":"9EF0826FDFEB8BA36FAC0A9D210DE19E","method":"Input.dispatchKeyEvent","params":{"type":"keyDown","modifiers":0,"windowsVirtualKeyCode":32,"code":"Space","key":" ","text":" ","unmodifiedText":" ","autoRepeat":False,"location":0,"isKeypad":False},"id":5}))
        response = await websocket.recv()
        print('response from server: ', {response})

asyncio.get_event_loop().run_until_complete(connect())
