# pip install "python-socketio[client]"

import socketio
import json

sio = socketio.Client(ssl_verify=False)


@sio.event
def connect():
    ## USE THIS LIST TO FILTER AND RECEIVE ONLY INSTRUMENTS YOU NEED. LEAVE EMPTY TO RECEIVE ALL
    # if you want to subscribe only specific instruments, emit instruments. To receive all instruments, comment the lines below.
    instruments = ['EURUSD', 'USDJPY', 'BTCUSD', 'ETH']
    sio.emit('instruments', instruments);

    # Use the 'trial' as key to establish a 2-minute streaming connection with real-time data.
    # After the 2-minute test, the server will drop the connection and block the IP for an Hour.
    sio.emit('key', 'trial')


@sio.event
def rates(rates):
    try:
        # f = open("../data_set2.txt", "a+t", encoding="utf-8")
        instr = json.loads(rates)
        with open("data_set_2024.txt", "a+") as f:
            print(instr, file=f)
        # f.write(instr)
        # print(instr)

    except:
        print(rates)
    finally:
        f.close()


@sio.event
def disconnect():
    print('disconnected from server')


def writer_file():
    pass


sio.connect('https://wss.live-rates.com/', transports=['websocket'])

sio.wait()
