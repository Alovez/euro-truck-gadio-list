import os
import ctypes
from build_radio_list import generate_gadio_list
from ctypes.wintypes import MAX_PATH


def get_live_stream_file_path():
    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        return os.path.join(buf.value, 'Euro Truck Simulator 2', 'live_streams.sii')


if __name__ == '__main__':
    with open(get_live_stream_file_path(), 'wb') as f:
        # f.write(generate_gadio_list().encode('utf-8'))
        print(generate_gadio_list())
    