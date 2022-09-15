from os import system
from time import sleep
from random import randint
import keyboard


class Snake():
    def __init__(self,xcord,ycord):
        self.position = [[xcord,ycord],[xcord,ycord-1]]
        self.direction = 'up'
    def snake_step(self):
        if len(self.position) == 2:
            if self.direction == 'up':
                self.position[0][1] -= 1
                self.position[-1][1] -= 1
            elif self.direction == 'down':
                self.position[0][1] += 1
                self.position[-1][1] += 1
            elif self.direction == 'left':
                self.position[0][0] -= 1
                self.position[-1][0] -= 1
            elif self.direction == 'right':
                self.position[0][0] += 1
                self.position[-1][0] += 1
        else:
            if self.direction == 'up':
                self.position[0][1] -= 1
            elif self.direction == 'down':
                self.position[0][1] += 1
            elif self.direction == 'left':
                self.position[0][0] -= 1
            elif self.direction == 'right':
                self.position[0][0] += 1
            if self.position[-1][1] == self.position[-2][1]:
                if self.position[-1][0] > self.position[-2][0]:
                    self.position[-1][0] -= 1
                else:
                    self.position[-1][0] += 1
            else:
                if self.position[-1][1] > self.position[-2][1]:
                    self.position[-1][1] -= 1
                else:
                    self.position[-1][1] += 1
            if self.position[-1] == self.position[-2]:
                self.position.pop(-2)
    def grow(self):
        if self.position[-2][0] == self.position[-1][0]:
            if self.position[-2][1] > self.position[-1][1]:
                self.position[-1][1] -= 1
            else:
                self.position[-1][1] += 1
        else:
            if self.position[-2][0] > self.position[-1][0]:
                self.position[-1][0] -= 1
            else:
                self.position[-1][0] += 1


    def round(self,direction):
        if self.direction != direction:
            a = [self.position[0][0],self.position[0][1]]
            self.position.insert(1, a)
            self.direction = direction


class World():
    def __init__(self,size):
        self.size = size
        self.fruit_position = [randint(0,self.size), randint(0,self.size)]
    def spawn_fruit(self):
        self.fruit_position = [randint(0,self.size), randint(0,self.size)]
    

class Game():
    def __init__(self):
        self.world = World(24)
        self.snake = Snake(12,12)
    def render(self):
        self.snake_points = []
        for i in range(1,len(self.snake.position)):
            if self.snake.position[i][0] == self.snake.position[i-1][0]:
                if self.snake.position[i][1] > self.snake.position[i-1][1]:
                    for x in range(self.snake.position[i-1][1],self.snake.position[i][1]+1):
                        self.snake_points.append([self.snake.position[i][0],x])
                else:
                    for x in range(self.snake.position[i][1],self.snake.position[i-1][1]+1):
                        self.snake_points.append([self.snake.position[i][0],x])
            else:
                if self.snake.position[i][0] > self.snake.position[i-1][0]:
                    for x in range(self.snake.position[i-1][0],self.snake.position[i][0]+1):
                        self.snake_points.append([x,self.snake.position[i][1]])
                else:
                    for x in range(self.snake.position[i][0],self.snake.position[i-1][0]+1):
                        self.snake_points.append([x,self.snake.position[i][1]])

        self.ui = '#' * (self.world.size+1) + '\n'
        for i in range(self.world.size):
            temp_str = ''
            for x in range(self.world.size-1):
                if [x,i] in self.snake_points:
                    temp_str += '$'
                elif [x,i] == self.world.fruit_position:
                    temp_str += '*'
                else:
                    temp_str += ' '
            self.ui += '#' + temp_str + '#' + '\n'
        self.ui += '#' * (self.world.size+1)
        print(self.ui)
        del self.snake_points

    def engine(self):
        while 1:
            if self.snake.position[0] == self.world.fruit_position:
                self.world.spawn_fruit()
                self.snake.grow()
            if (self.snake.position[0][0] < 0 or self.snake.position[0][0] > self.world.size) or (self.snake.position[0][1] < 0 or self.snake.position[0][1] > self.world.size):
                break
            self.snake.snake_step() 
            keyboard.add_hotkey('w', lambda: self.snake.round('up'))
            keyboard.add_hotkey('a', lambda: self.snake.round('left'))
            keyboard.add_hotkey('s', lambda: self.snake.round('down'))
            keyboard.add_hotkey('d', lambda: self.snake.round('right'))
            self.render()
            sleep(0.2)
            system('cls')
        print('Game Over...')

g = Game()
g.engine()