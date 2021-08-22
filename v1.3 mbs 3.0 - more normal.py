from PIL import Image
import colorsys, math
rateOfColorChange = 9
#f(z) = z^2 + c
#c = j + ii
isJulia = "y"
isJulia = input("Generate a Julia Set? (y/n)")
if isJulia == "y":
    isJulia = True
    cj = - 0.6567134268537076
    ci = 0.45713301603206424
    cj = float(input("What is your real 'c' value"))
    oj = cj
    ci = float(input("What is your imaginary 'c' value"))
    oi = ci
    #Ratio *10 has to be an int
    ratio = 2
else:
    cj = 0
    oj = 0
    ci = 0
    oi = 0
    isJulia = False
    ratio = 1.5

sizeX = 100000
sizeX = int(input("How many pixels do you want (wide)"))
skips = 1
maxI = 125
zoomNo = 0.17
hue = 0
color = 0
size = int(sizeX / (ratio))

#For progress Line
factorTest = size
factorChar = 1
center = 0

cosOfAngle = math.cos(45)
sinOfAngle = math.sin(60)

pixelsDone = []

print("initialisation")
for i in range(0, sizeX):
    pixelsDone.append([])
    for j in range(0, size):
        pixelsDone[i].append(False)
print("start")

while factorTest >= 1:
    factorTest /= 10
    factorChar += 1
    factorMax = factorChar
if factorChar % 2 == 0:
 center = int(factorChar * 0.5)
else:
 center = int(factorChar * 0.5 + .5)
zoomNo *= size * 2

im = Image.new("RGB", (sizeX, size), (255, 255, 255))
pixel = im.load()

for i in range(0, size, skips):
  for j in range(0, sizeX, skips):

      if isJulia is False:
          ci = (i - 0.5 * size) / (zoomNo)
          cj = (j - 0.5 * sizeX) / (zoomNo)
          # print(cj, ci)
          zi = 0
          zj = 0


      else:
          zi = (i - 0.5 * size) / (zoomNo)
          zj = (j - 0.5 * sizeX) / (zoomNo)



      for b in range(0, maxI):
          yout = zi * zj * 2 + ci
          xout = zj * zj - zi * zi + cj
          if yout * yout + xout * xout > 4:
              break
          if isJulia is False:
              zi = yout
              zj = xout
          else:
              zi = yout
              zj = xout
      for height in range(int((- size * 0.001) * b * 1.5), 0):
          px = (cosOfAngle * (i - j) + 0.5 * sizeX)
          py = (height) + sinOfAngle * (j + i) + size
          if isJulia is True:
              py += 0.25 * size
              px += 0.25 * sizeX


          px = int(px + 0.5)
          py = int(py + 0.5)

          if pixelsDone[px][py] == False:
              pixelsDone[px][py] = True


              if b > 1:
                  if b >= (maxI) - 1:
                      pixel[px, py] = (0, 0, 0)
                  else:
                      hue = (b * rateOfColorChange)/360
                      color = colorsys.hsv_to_rgb(hue, 1, 1)
                      r = int(255 * (color[0]))
                      g = int(255 * (color[1]))
                      blue = int(255 * (color[2]))
                      pixel[px, py] = (r, g, blue)
          else:
              break
  factorChar = 0
  factorTest = (i + 1)
  while factorTest >= 1:
      factorTest /= 10
      factorChar += 1
  for p in range(0, factorMax - factorChar):
      print(" ", end="")
  print(str(i + 1), end= "")
  print(" /", str(size) + " | " + str(int(((i + 1) * 1000) / (size)) / 10) + "%", end="\r")
print("Compiling Image")
name = ("set " + str(oj) + " + " + str(oi) + "i" + ".png")

im.save(name)
input("Finished")

