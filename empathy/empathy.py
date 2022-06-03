import matplotlib.pyplot as plt
img = plt.imread("emp.png")
fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5)

xmax=80
x = range(xmax)
ax.imshow(img, extent=[0,xmax,0,25])

height = 20
width=3

values = [
    ("Hay", 15, height+2),
    ("Mumble", 17, height),
    ("Derp", 33, height),
    ("Camille", 35, height+2),
    ("Rouse", 49, height+2),
    ("Stew", 52, height),
    ("Colleen", 55, height),
    ("Ariana", 70, height-2),
    ("Rob (ari)", 76, height),
    ("Audrey", 76, height+2)
]

last=-1
lastwidth=width
for name, val, nameheight in values:

    if val == last:
        lastwidth=lastwidth-1
    else:
        lastwidth=width

    xval = [val,val]
    yval = [0,nameheight]
    plt.text(val, nameheight, name)
    ax.plot(xval,yval, label=name,linewidth=lastwidth )
    last = val

plt.savefig("emp.pdf")
