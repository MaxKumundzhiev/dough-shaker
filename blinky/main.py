#################
# single Blinky #
#################
import time
import random

class SingleBlinky:
    def __init__(self) -> None:
        self.face = "(o.o)"
    
    def show_face(self, new_face, delay):
        self.face = new_face
        print('\r', self.face, end='\r')
        time.sleep(delay)
    
    def run(self):
        while True:
            self.show_face('(-.-)', 0.1)
            self.show_face('(o.o)', random.uniform(0.1, 1.5))

# blinky = SingleBlinky()
# blinky.run()

#####################################
# family of Blinkies with threading #
#####################################
import threading

def print_family(family):
    for blinky in family:
        print(blinky, end=' ')
    print(end='\r')

class FamilyBlinky:
    def __init__(self, family) -> None:
        self.face = '(o.o)'
        self.family = family

    def __str__(self) -> str:
        return self.face

    def show_face(self, new_face, delay):
        self.face = new_face
        print_family(self.family)
        time.sleep(delay)
    
    def run(self):
        while True:
            self.show_face('(-.-)', 0.1)
            self.show_face('(o.o)', random.uniform(0.1, 1.5))
    

family, family_size = [], range(10)
family.extend(FamilyBlinky(family) for _ in family_size)

# for blinky in family:
#     threading.Thread(target=blinky.run).start()

###################################
# family of Blinkies with asyncio #
###################################
import asyncio

def print_family(family):
    for blinky in family:
        print(blinky, end=' ')
    print(end='\r')

class AsyncFamilyBlinky:
    def __init__(self, family) -> None:
        self.face = '(o.o)'
        self.family = family
    
    def __str__(self) -> str:
        return self.face

    async def show_face(self, new_face, delay):
        self.face = new_face
        print_family(self.family)
        await asyncio.sleep(delay)
    
    async def run(self):
        while True:
            await self.show_face('(o.o)', 0.1)
            await self.show_face('(-.-)', random.uniform(0.1, 1.5))
    

family, family_size = [], range(10)
family.extend([AsyncFamilyBlinky(family) for _ in family_size])

async def run_all():
    tasks = []
    for blinky in family:
        tasks.append(asyncio.ensure_future(blinky.run()))
    
    for task in tasks:
        await task

asyncio.run(run_all())