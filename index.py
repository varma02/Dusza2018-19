try: import os, re
except Exception: 
  print("Az egyik szükséges modul nincs rajta a gépeden!")
  exit()

# ↓ Végigmegy az összes almappán, és összegyűjti az alaprajzfájlokat ↓
file_pathes = []
for root, _, files in os.walk("./"):
  for file_name in files:
    if re.match(r"^alaprajz\d.txt$", file_name): file_pathes.append(root.replace("\\", "/")+"/"+file_name)

# ↓ Kiírja a talált fájlokat és a sorszámukat ↓
print("Talált fájlok:")
for index, file_path in enumerate(file_pathes):
  print(f"  {index} - {file_path}")

# ↓ Bekéri a felhasználótól a választott fájlt, aztán ellenőrzi, hogy jó-e ↓
while True:
  try: 
    chosen_file = file_pathes[int(input("Válassz egy fájlt (írd be a sorszámát): "))]
    break
  except ValueError: print("Nem számot adtál meg! Próbáld újra.")
  except IndexError: print("Túl nagy vagy túl nagy számot adtál meg! Próbáld újra.")

# ↓ Beolvassa a választott fájlt és kinyeri belőle a szükséges adatokat ↓
with open(chosen_file, "r") as file:
  lines = file.readlines()
  height, width = lines[0].strip().split(" ")
  height = int(height); width = int(width)
  grid = [[int(x) for x in y.strip()] for y in lines[1:]]

# ↓ PATHFINDING ↓
for y in range(height):
  for x in range(width):
    if grid[y][x]: print("U", end="")
    else: print(".", end="")
  print()