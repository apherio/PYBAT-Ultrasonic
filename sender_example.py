
from pybat.codec.ecc import OnebyteReedSolomonEcc, EmptyEcc
from pybat.communication import SoundWriter, SoundSender


def write(coder=EmptyEcc(), debug=False, target_str='', file_name='./out.wav'):
    print("Encoding...")
    writer = SoundWriter(debug=debug, coder=coder)
    writer.write_string_to_file(target_str, file_name)


def send(coder=EmptyEcc(), debug=False, target_str=''):
    print("Encoding...")
    sender = SoundSender(debug=debug, coder=coder)
    sender.send_string(target_str)


if __name__ == "__main__":
    # send string message with Reedsolomon
    send(coder=OnebyteReedSolomonEcc(), debug=True, target_str="")
    # write(coder=OnebyteReedSolomonEcc(), target_str="nn", file_name="out.wav")
