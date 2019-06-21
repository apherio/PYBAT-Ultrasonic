from pybat.codec.ecc import OnebyteReedSolomonEcc, EmptyEcc
from pybat.communication import SoundReceiver


def launch_receiver(coder=EmptyEcc()):
    print("Listening...")
    receiver = SoundReceiver(debug=False, coder=coder)
    while True:
        data = receiver.receive()
        if len(data) > 0:
            data_string = receiver.convert_data_to_ascii_string(data)
            print("Decoded Decimal: %s" % [int(d) for d in data])
            print("Decoded Binary : %s" % [format(int(d), 'b') for d in data])
            print("Decoded String : %s" % data_string)


if __name__ == "__main__":
    # Launch a sound receiver with Reedsolomon
    launch_receiver(OnebyteReedSolomonEcc())
    # Launch a sound receiver without error correcting
    # launch_receiver()
