import os

def extract_jpegs(filename):
    with open(filename, 'rb') as f:
        data = f.read()

    start = b'\xff\xd8' 
    end = b'\xff\xd9'   
    i = 0
    pos = 0

    while True:
        start_idx = data.find(start, pos)
        end_idx = data.find(end, start_idx)

        if start_idx == -1 or end_idx == -1:
            break

        jpeg = data[start_idx:end_idx+2]
        with open(f'image_{i:05d}.jpg', 'wb') as img:
            img.write(jpeg)
        i += 1
        pos = end_idx + 2

    print(f"Extracted {i} JPEG images.")

extract_jpegs('stream.raw')
