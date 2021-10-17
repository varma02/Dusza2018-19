try: import os, re
except Exception: 
  print("Az egyik szükséges modul nincs rajta a gépeden!")
  exit()

# ↓ Végigmegy az összes almappán, és összegyűjti az alaprajzfájlokat ↓
file_pathes = []
for root, _, files in os.walk("./"):
  for file_name in files:
    if re.match(r"^alaprajz(\d|\d\d)\.txt$", file_name): file_pathes.append(root.replace("\\", "/")+"/"+file_name)

# ↓ Ellenőrzi, hogy talált e fájlokat ↓
if not file_pathes:
  print("Nem talált helyes fájlt a program.")
  exit()

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
  except IndexError: print("Túl nagy vagy túl kicsi számot adtál meg! Próbáld újra.")

class Pathfinding:
  def __init__(self, file_path:str):
    with open(file_path, "r") as file:
      lines = file.readlines()
      self.height, self.width = lines[0].strip().split(" ")
      self.height = int(self.height); self.width = int(self.width)
      self.grid = [[int(x) for x in y.strip()] for y in lines[1:]]
      self.complete_grid = [["F"]]
  
  def get_obj(self, y:int, x:int):
    try: return self.complete_grid[y][x]
    except IndexError: 
      try: 
        if self.grid[y][x]: return "U"
        else: return "."
      except IndexError:
        return "."

  def make_grid(self, printing:bool=True, range_reverse:bool=False):
    for y in range(0 if not range_reverse else self.height-1, self.height if not range_reverse else 0, 1 if not range_reverse else -1):
      for x in range(0 if not range_reverse else self.width-1, self.width if not range_reverse else 0, 1 if not range_reverse else -1):
        if self.grid[y][x] and \
        (self.get_obj(y-1, x) == "F" or \
        self.get_obj(y+1, x) == "F" or \
        self.get_obj(y, x-1) == "F" or \
        self.get_obj(y, x+1) == "F"):
          if printing: print("F", end="")
          self.complete_grid[y].append("F")

        elif self.grid[y][x] and \
        self.get_obj(y-1, x) == "." and \
        self.get_obj(y+1, x) == "." and \
        self.get_obj(y, x-1) == "." and \
        self.get_obj(y, x+1) == ".":
          if printing: print("S", end="")
          self.complete_grid[y].append("S")

        elif self.grid[y][x] and \
        (self.get_obj(y-1, x) in ["A", "U"] or \
        self.get_obj(y+1, x) in ["A", "U"]) and \
        (self.get_obj(y, x+1) in ["A", "U"] or \
        self.get_obj(y, x-1) in ["A", "U"]) and \
        (self.get_obj(y+1, x+1) in ["A", "U"] or \
        self.get_obj(y-1, x-1) in ["A", "U"] or \
        self.get_obj(y+1, x-1) in ["A", "U"] or \
        self.get_obj(y-1, x+1) in ["A", "U"]):
          if printing: print("A", end="")
          self.complete_grid[y].append("A")

        elif self.grid[y][x]: 
          if printing: print("K", end="")
          self.complete_grid[y].append("K")

        else: 
          if printing: print(".", end="")
          self.complete_grid[y].append(".")
      self.complete_grid.append([])
      if printing: print()
    return self.complete_grid

xd = Pathfinding(chosen_file)
xd.make_grid(False)
xd.make_grid(False)
xd.make_grid()

#FFFFFFFFFFF
#F.....F...F
#F.KK..F.K.F
#F.K...F.K.F
#F.K...F.K.F
#F.K.S.F.K.F
#F.....F.K.F
#FFF...F...F
#F.....F...F
#F.AA..F...F
#F.AA..F...F
#F.AA..F...F
#F.....F...F
#FFFFFFFFFFF

