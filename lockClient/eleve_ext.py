import socket
import logging

logging.error('This is not an error FROM EXT')

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

# Enable port reusage so we will be able to run multiple clients and servers on single (host, port). 
# Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
# For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
# So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
# Thanks to @stevenreddie
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

# Enable broadcasting mode
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client.bind(("", 37020))
client.setblocking(False)

# create pygame window
import pygame
import time

pygame.init()
#WIDTH=1366; HEIGHT=768
WIDTH=800; HEIGHT=600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.NOFRAME)
pygame.display.set_caption('Katso')
pygame.mouse.set_visible(False)
running = True

screen.fill((0,0,0))
pygame.display.flip()

passunlock = "unlockscreen"
passtemp = "000000000000"

while running:
	try:
		data, addr = client.recvfrom(1024)
		print("received message: %s"%data)

		if data.decode() == "unlock":
			print("Quit")
			running = False

	except:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				try:
					passtemp = passtemp[1:]+chr(event.key)
					print(passtemp)
					if passtemp == passunlock:
						running = False
				except:
					print("strange key")

pygame.display.quit()
pygame.quit()
exit()
