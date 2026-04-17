import random
from PIL import Image

print("--- map area estimator ---")
filename = input("image name? : ")

try:
    img = Image.open(filename).convert('RGB')
except FileNotFoundError:
    print("error: couldn't find the image. put it in the same folder.")
    exit()

w, h = img.size
total_area = 42.0

try:
    samples = int(input("how many random darts? "))

    if samples <= 0:
        print("must be at least 1, using 100000")
        samples = 100000
    elif samples > 5000000:
        print("whoa, that's too many! capping at 5,000,000 so we don't crash.")
        samples = 5000000
        
except ValueError:
    samples = 100000
    print("bad input, using 100000")

print(f"\nthrowing {samples} darts...")

red_hits = 0

for _ in range(samples):
    x = random.randint(0, w - 1)
    y = random.randint(0, h - 1)
    
    r, g, b = img.getpixel((x, y))

    if r > 100 and g < 100 and b < 100:
        red_hits += 1

ratio = red_hits / samples
mined = ratio * total_area

print("\n--- results ---")
print(f"red hits: {red_hits}")
print(f"red %:    {ratio * 100:.1f}%")
print(f"mined area: {mined:.2f} sq miles")