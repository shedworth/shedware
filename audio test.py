import pyglet

sound = pyglet.media.load('Koan Sound - Mr Brown.wav', streaming=False)
sound.play()

print "Wahoo!"
