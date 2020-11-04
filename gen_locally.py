from build_radio_list import generate_gadio_list


if __name__ == '__main__':
    with open('./live_streams.sii', 'wb') as f:
        f.write(generate_gadio_list().encode('utf-8'))
    