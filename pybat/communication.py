from pybat.codec.decoder import Decoder
from pybat.codec.ecc import EmptyEcc
from pybat.codec.encoder import Encoder


class SoundSender:
    def __init__(self, debug=False, coder=EmptyEcc()):
        self.enc = Encoder(coder=coder)
        self.debug = debug

    def send_string(self, string_to_send):
        data = [ord(t) for t in string_to_send]
        self.send_byte_data(data)

    def send_byte_data(self, byte_data):
        if self.debug:
            print("Decimal: %s" % [int(d) for d in byte_data])
            print("Binary: %s" % [format(int(d), 'b') for d in byte_data])
        self.enc.encodeplay(byte_data)


class SoundWriter:
    def __init__(self, debug=False, coder=EmptyEcc()):
        self.enc = Encoder(coder=coder)
        self.debug = debug

    def write_string_to_file(self, string_to_send, filename):
        data = [ord(t) for t in string_to_send]
        self.write_byte_data_to_file(data, filename)

    def write_byte_data_to_file(self, byte_data, filename):
        if self.debug:
            print("Decimal: %s" % [int(d) for d in byte_data])
            print("Binary: %s" % [format(int(d), 'b') for d in byte_data])
            print("Write to: %s" % filename)
        self.enc.encode2wav(byte_data, filename)


class SoundReceiver:
    def __init__(self, debug=False, coder=EmptyEcc()):
        self.dec = Decoder(debug=debug, coder=coder)
        self.debug = debug

    def receive(self):
        return self.dec.listen()

    def receive_as_ascii(self):
        return SoundReceiver.convert_data_to_ascii_string(self.receive())

    @staticmethod
    def convert_data_to_ascii_string(target):
        return "".join([chr(int(format(int(d), 'b'), 2)) for d in target])
