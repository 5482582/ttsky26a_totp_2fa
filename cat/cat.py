from PIL import Image

WIDTH = 128
HEIGHT = 128
THRESHOLD = 150
INVERT = True

img = Image.open("cat.png")
img = img.resize((WIDTH, HEIGHT)).convert("L")  # grayscale

pixels = img.load()

mem_index = 0

for y in range(HEIGHT):
    for xbyte in range(WIDTH // 8):
        byte = 0

        for bit in range(8):
            x = xbyte * 8 + bit
            val = pixels[x, y]

            # threshold
            pixel = 1 if val < THRESHOLD else 0

            # optional invert
            if INVERT:
                pixel = 1 - pixel

            byte |= (pixel << bit)

        print(f"mem[{mem_index}] = 8'h{byte:02x};")
        mem_index += 1
