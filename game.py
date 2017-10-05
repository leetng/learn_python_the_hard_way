#!/usr/bin/env python
# coding=utf-8
"""
a game using class, and implemented only
map/engin/scene/death/central_corridor

"""
from sys import exit
class Scene(object):

    def enter(self):
        print("not implemented yet.")

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n ---------------")
            next_scene_name = current_scene.enter() # enter() in each scene return a new scene_name.
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    def enter(self):
        print("you're dead")
        exit(1)

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class CentralCorridor():

    def enter(self):
        answer = input("come back again or go die?")

        if answer == "come back again":
            return 'central_corridor'

        elif answer == "go die":
            return "death"

        else:
            print("ok, I don't know what to do:*, what about come back?")
            return 'central_corridor'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weaponArmory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
