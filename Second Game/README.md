# While Loops

Perhaps you have already tried to make several harvest() calls in a row:

harvest()
harvest()
harvest()

This allows you to harvest several times in one program run. 
However, it would be nice to harvest more than three times, and writing the same code multiple times is bad practice. 
The solution is a loop. 
A loop allows you to run the same code multiple times.

The while loop takes a condition, which is a logical value that can only be in one of two states: True or False. 
Such a value is called a Boolean value.

The loop then executes the code inside the loop until the condition is False.
The while loop looks like this:

while condition:
	#loop body
	#loop body
	#...
	
Where you have to replace "condition" with a boolean value and #loop body with whatever you want to do in the loop.

There are two constant boolean values available. Constants are values that never change during the program.

To create a constant boolean value that is always True, you can simply write True. Write False as a constant boolean value that will always be False.
So you could either write


while False:
	do_a_flip()

or

while True:
	do_a_flip()

The first will never do a flip and the second will do flips forever (an infinite loop). 

Normally creating an infinite loop is a bad idea because it will freeze the program, but in this game there are delays between each iteration of the loop, so it will cause the drone to keep doing a flip until you manually stop it by pressing the execute button again.

Notice how the line after the colon is indented. Indentation like this is used to separate blocks of code.
Just press Tab to add indentation and Shift + Tab (or Backspace) to remove it.

The loop will repeat all indented statements after the colon.
Statements after the indented block will be executed after the loop has finished.


# If Branch

The execution speed has been doubled. The problem is that the drone now harvests faster than the grass can grow resulting in no harvest at all. To deal with this if branches and the can_harvest() function are now unlocked.

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()

can_harvest() returns True if the plant under the drone is fully grown and False otherwise.


# Move Drone

Your farm has grown! This space is not much use if you can't move the drone, so there is a new function move() that moves the drone. move() requires that you specify the direction in which you want the drone to move. There are four new constants for this: North, East, South, West

For example, move(North) will move the drone one square to the north.

If you move over the edge of the farm the drone will be moved to the other side of the farm.
The following example code will keep moving north and wrap back to the start when it reaches the edge of the farm:

while True:
	move(North)


# Plants

Grass is nice because it grows automatically. All other plants have to be planted with the plant() function. The only plant you can plant right now is a bush.
You can pass the type of plant you want to plant to the function like this:

plant(Entities.Bush)

This will plant a bush under the drone.

Call clear() to reset the farm to all grass and reset the drone position.


# For Loop

Your farm has expanded again! Now the tiles are no longer in a nice row, so you need to find a way to traverse a square grid.

With the while loop this is simply not possible (at least until you unlock senses).
It is time to introduce the for loop.

The for loop works just like the for loop in Python. (Called a foreach loop in some languages, not to be confused with the C-style for loop, which is a different thing). 
It must be given a sequence to iterate over:

for i in sequence:
	#do something with i
	
Currently the only way to get such a sequence is through the range() function. 
range(n) returns a sequence containing numbers from 0 to n(exclusive) in steps of 1.
range(start, end) returns a sequence containing numbers from start to end(exclusive) in steps of 1.
range(start, end, step_size) returns a sequence containing numbers from start to end(exclusive) in steps of step_size.

So what's mainly useful right now is being able to run some code exactly n times like this:

#do n flips
for i in range(n):
	do_a_flip()

The function get_world_size() is also available now. It returns the side length of your farm. This way you can write code that won't break with the next expand upgrade.

If you're stuck on trying to figure out how to move the drone around the farm click the spoiler for a hint.


# Senses

The drone can see now! 

The functions get_pos_x() and get_pos_y() return the current x and y position of the drone. At the start position they are both 0. The x position increases by 1 every tile towards East and the y position increases by 1 every tile towards North.

num_items(item) returns how many of an item you have.
For example num_items(Items.Hay) returns how much hay you have.

get_entity_type() and get_ground_type() return the type of entity or ground that is under the drone. Once you have unlocked Operators you can check if the drone is over a specific entity or ground:

Do a flip if you are over a bush:
if get_entity_type() == Entities.Bush:
	do_a_flip()

The None keyword is also unlocked now! None is a value that represents that there is no value.
For example, a function that has no return statement will actually return None.

get_entity_type() returns None if there is no entity under the drone.


# Operators

You've unlocked operators to be used within expressions. They work like in Python.

arithmetic operators: +, -, *, /, //, %, **
comparison operators: ==, !=, <=, >=, <, >
boolean operators: not, and, or

Note: All numbers in the game are floating point numbers. So all arithmetic operators are floating point operators.
// is defined to just floor the number after the division.

For assignment operators you need to unlock the "Variables" unlock.


## For Beginners

Operators allow you to perform operations on values.
The arithmetic operators +, -, *, /, //, %, ** are used to perform common mathematical operations on numbers.

+ and - are used for addition and subtraction.

2 + 3 evaluates to 5
3 - 2 evaluates to 1

* and / are used for multiplication and division.

2 * 3 evaluates to 6
5 / 2 evaluates to 2.5

% is the modulo operator, also known as the remainder operator. It essentially divides the two numbers and then returns the remainder. You can also think of it as repeatedly subtracting the right number from the left number until the remainder is less than the right number.

4 % 2 evaluates to 0
5 % 2 evaluates to 1
6 % 2 evaluates to 0
2 % 6 evaluates to 2
1.5 % 1 evaluates to 0.5

** is the power operator.

2**2 evaluates to 4
(-5)**3 evaluates to -125

The comparison operators ==, !=, <=, >=, <, > are used to compare values. The result is always either True or False

== and != are used to check of two values are "equal"(==) or "not equal"(!=). They can be used on all types of values.

2 == 2 evaluates to True
Entities.Bush != Entities.Bush evaluates to False
3 != 3 + 1 evaluates to True

<=, >=, <, > can only be used on numbers. They check if the left number is "smaller or equal"(<=), "bigger or equal"(>=), "smaller" (<) or "bigger" (>) than the right number.

1 <= 1 evaluates to True
2 >= 3 evaluates to False
-2 < -1 evaluates to True
6 > 6 evaluates to False

The logic operators (also called boolean operators) not, and, or are used to combine truth values.

not simply inverts the value:

not False evaluates to True
not True evaluates to False

and evaluates to True only if both values are True

True and True evaluates to True
True and False evaluates to False
False and False evaluates to False

or evaluates to True if at least one of the values is True

True or True evaluates to True
True or False evaluates to True
False or False evaluates to False


# Carrots

Before you can plant carrots with plant(Entities.Carrots), you have to do two new things. First, carrots can only grow on tilled soil. To till the soil, simply call till(). Calling till() again will change it back to Grounds.Turf.

The second new feature is that carrots need seeds to grow. You can buy carrot seeds with the new trade() function.
You have to pass an item type to trade() like this: trade(Items.Carrot_Seed)

If the item can be bought, then it will be bought with this.

You can see the cost of any item in its tooltip. The tooltip appears when you mouse over the item itself or the item name in the code.


# Watering

Plants grow faster when they are watered. Soil and turf have a water level ranging from 0 to 1.
The function get_water() returns the water level of the ground it is over.

The growth speed of a plant growing on tilled soil grows linearly from 1x speed at water level 0 to 5x speed at water level 1.

Soil dries up over time: The water loses 1% of it's current water every now and then. Keeping the water level high will consume much more water than keeping it low.

You can use water tanks to water your plants. You can purchase empty tanks with wood using trade(Items.Empty_Tank)

A tank can hold 0.25 water.

Tanks fill up automatically. The fill rate is 0.5% of the number of empty tanks per second. So if you have 100 empty tanks one of them will fill every 2 seconds.

Call use_item(Items.Water_Tank) over any ground to empty a tank and water the ground.


# Trees

Trees are a better way to get wood than bushes. They give 5 wood each. Like bushes, they can be planted on grass or soil.

Trees like to have some space and planting them right next to each other will slow down their growth. The growing time is doubled for each tree that is on a tile directly to the North, East, West or South of it. So if you plant trees on every tile, they will take 2*2*2*2 = 16 times longer to grow.


 The % operator can be useful here. Remember that the % operator returns the remainder of the division. Even numbers divided by 2 have a remainder of 0 and odd numbers divided by 2 have a remainder of 1.
So you can check if a number is even like this:

def is_even(n):
	return n % 2 == 0

This returns True if n is even and False if it isn't.


# Sunflowers

Sunflowers collect the power of the sun. You can harvest that power. 

Planting them works exactly the same way as planting carrots, except you have to buy sunflower seeds instead of carrot seeds. 

However, when you harvest a sunflower, the power of all the sunflowers on the farm flows together into the harvested plant. 
Thus, harvesting a sunflower yields power equal to the square root of the number of sunflowers on the farm.
Only one of the sunflowers with the most petals can handle this.
If you harvest a sunflower that doesn't have the most petals of all the sunflowers on the farm the power will destroy all the sunflowers on the farm.

measure() returns the number of petals of the sunflower under the drone.

Several sunflowers can have the same number of petals so there can also be several sunflowers with the largest number of petals. In this case, it doesn't matter which one of them you harvest.

As long as you have power the drone will use it to run twice as fast. 
It consumes 1 power every 30 actions (like moves, harvests, plants...)
Executing other code statements can also use power but a lot less than drone actions.

In general, everything that is sped up by speed upgrades is also sped up by power.
Anything sped up by power also uses power proportional to the time it takes to execute it, ignoring speed upgrades.


# Variables

Variables are dynamically typed like in python and can be assigned like this:

Declare a variable named a and store the value 5 in it:
a = 5
Declare a variable named b and store the return value of can_harvest() in it:
b = can_harvest()

You can think of variables as named containers that can store a value. Just like functions you can name them whatever you want.

The = operator is used to declare a variable and store a value in it.

Do not confuse the = operator with the == operator. 
The == operator checks whether two values are equal and returns True or False.
The = operator assigns the value on the right to the name on the left.

After a variable has been assigned you can use it in the code to retrieve the value it contains

a = 5
for i in range(a):
	do_a_flip()

The above loop is executed 5 times because a is set to 5.
The i in the for loop is also a variable that is automatically assigned to by the for loop.

With variables you can do the same thing also with a while loop:

a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1

This does the same thing as the for loop above. We just have to increment i manually.
Note that to increment i, we set it to be its own value plus 1. Changing the value of a variable based on its previous value is something very common. 
It can be abbreviated using these operators: +=, -=, *=, /=, %=

i = i + 1 is the same as i += 1
a = a / 3 is the same as a /= 3


# Functions

You've already seen built-in functions like harvest().
Now you can also define your own functions.

Use the def keyword to define a new function:
def f():
	#function code

You can then call the function to execute the function code:
f()

This allows for easy code reuse.

You can also pass values to a function that specify what the function should do. 
For example the following code moves the drone 10 tiles North and 2 tiles West.

def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(10, North)
move_n_dir(2, West)

Use the return keyword to make a function return a value. 
For example the following function defines the exclusive or operation. The exclusive or is True if exactly one value is True and the other one is False:

def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()

Functions are values just like any other value, and the def statement just acts like an assignment statement, assigning the function to whatever name you give it.
This means you can do wild things like this:

def f():
	def d():
		do_a_flip()
	return d

f()()

Here f() calls the function f which defines and returns a new function d. The second () then executes the returned function and performs flip.
(You probably shouldn't do things like this because it's hard to read)

Unlike Python, functions defined in the global scope of any open file can be called by their name, even if the def statement has never been executed.


# Pumpkins

Pumpkins grow like carrots on tilled soil. They require pumpkin seeds to be planted, which cost one carrot each.

When all the pumpkins in a field are fully grown, they grow together to form a giant pumpkin. The yield of a giant pumpkin is the cubed side length of the pumpkin.

A 2x2 pumpkin yields 2*2*2 = 8 pumpkins instead of 4
A 3x3 pumpkin yields 3*3*3 = 27 pumpkins instead of 9
A 4x4 pumpkin yields 4*4*4 = 64 pumpkins instead of 16
...

It's a good idea to get the pumpkins as big as possible before harvesting. The problem is that about 1 in 5 pumpkins will die before they grow up. This means that even if you plant a pumpkin on every tile in a square, one of the pumpkins may die and prevent the mega pumpkin from growing. A pumpkin that dies will simply disappear so you can plant a new one.


# Lists

Lists are an easy way to store multiple values in a single variable.
You can create new lists like this:

list = [2, True, Items.Hay]

The list now contains the values 2, True and Items.Hay.
A list can also be empty:

empty_list = []

You can access an element of a list by its index. The index is 0 for the first element, 1 for the second element, 2 for the third...

plants carrots
list = [Entities.Tree, Entities.Carrots, Entities.Pumpkin]
plant(list[1])

You can iterate over a list using a for loop. The following example sums the all elements in the list.

list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number
sum is now 18

The following list methods allow you to add and remove elements:

list.append(elem) adds an element to the end of the list:

list = [2, 6, 12]
list.append(7)
list is now [2, 6, 12, 7]

list.remove(elem) removes the first occurrence of an element from a list:

list = [1, 2, 4, 2]
list.remove(2)
list is now [1, 4, 2]

list.insert(index, elem) inserts an element at the given index:

list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)
list is now [Entities.Tree, Items.Wood, Items.Hay]

list.pop(index) removes the element at the specified index.
If no index is specified, the last item is removed.

list = [3, 5, 8, 25]
list.pop()
list is now [3, 5, 8]
list.pop(1)
list is now [3, 8]

The len() function returns the length of the list.
list = [3, 2, 1]
x = len(list)
x is now 3

Lists have reference semantics. This means that assigning a list to a variable assigns the same list object to that variable, rather than making a copy of the list.
If two variables reference the same list, changes to the list will be seen by both.

a = [1,2]
b = a
b.pop()
a and b are now both [1]


# Dictionaries

Dictionaries are a datastructure that allows you to map keys to values in the same way that a real dictionary maps words to their definitions and you can look them up very quickly.

A dictionary can be created like this:
rotation = {North:East, East:South, South:West, West:North}

The expression before the colon is the key and the expression after the colon is the value to which the key maps.
The above dictionary maps directions to the direction to their right.

Accessing the value mapped to a key is similar to accessing an element in a list:
value = dict[key]

Example:
orientation = rotation[South]
This sets orientation to West.

You can add a new key-value pair to a dictionary like this:
dict[key] = value
This will map the key to the value.

Keys are unique, so adding a key that already exists in the dictionary will overwrite the previous value.

Use dict.pop(key) to remove a key-value pair from dict.

key in dict evaluates to True if key is a key in the dict and False otherwise.
So you can use if key in dict: to check if dict contains the key.

Putting a dictionary in a for loop allows you to iterate through all keys:
for key in dict:
	value = dict[key]

There are no guarantees about the order in which the keys are iterated.


Sets are like dictionaries, but without values. You just have a set of keys.

They are created like dictionaries, but without values.
set = {North, East, West}

Use set.add(elem) to add a new element to the set.

Use set.remove(elem) to remove an element from a set.

Use if elem in set: to check if the set contains an element.

Use for elem in set: to iterate all elements in the set.

Just like dictionaries, sets are unordered, so there are no guarantees about the order in which the elements are iterated.

Also, elements in sets are unique, so adding an element that is already in the set will not change the set.


# Costs

Any cost can be represented as a dictionary that maps items to numbers.

The get_cost() function returns such a dictionary. It returns the price to buy an item using the trade() function, the seed required to plant a plant, or the cost of an unlock.

get_cost(Items.Pumpkin_Seed)
returns {Items.Carrot:1}

get_cost(Entities.Pumpkin)
returns {Items.Pumpkin_Seed:1}

get_cost(Unlocks.Loops)
returns {Items.Hay:5}

For upgrades that are already at the max level the get_cost() will return None.

It can be used like this:
cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]


# Fertilizer

At some point, waiting for the plants to grow is just not efficient enough anymore. 
Fertilizer can make plants grow much faster. use_item(Items.Fertilizer) will instantly grow the plant under the drone by 2 seconds.
Fertilizer can be bought with trade(Items.Fertilizer).

Using fertilizer dries up the ground. The water speed buff will still apply while the fertilizer is being used, but after that, the water level on the ground will be reduced to 0.


# Mazes

If you use fertilizer on a full-grown bush, it will grow into a maze of hedges with a 10% probability. For some reason the drone can't fly over the hedges, even though they don't look that high.

There is a treasure hidden somewhere in the hedge. Use harvest() on the treasure to receive gold equal to the area of the maze. (For example, a 5x5 maze will yield 25 gold.)

If you use harvest() anywhere else the maze will simply disappear.

get_entity_type() is equal to Entities.Treasure if the drone is over the treasure and Entities.Hedge everywhere else in the maze.

Mazes do not contain any loops unless you reuse the maze (see below how to reuse a maze). So there is no way for the drone to end up in the same position again without going back.

You can check if there is a wall by trying to move through it. 
move() returns True if it succeeded and False otherwise.

If you have no idea how to get to the treasure, take a look at Hint 1. It shows you how to approach a problem like this.


For an extra challenge you can also reuse the maze by using fertilizer on the treasure. 
This has a 10% probability of increasing the treasure by one full maze and moving it to a random position in the maze.
Using measure() on a treasure returns the position it will go to next as a tuple (x_position, y_position).

For example, while above the treasure, the following code gives you the position where the treasure will be after you fertilize it:
next_x, next_y = measure()

Each time the treasure is relocated a random wall may be removed from the maze. So reused mazes can contain loops.

Note that loops in the maze make it much more difficult so if you are a beginner you may not want to reuse mazes. Reusing mazes doesn't give you more gold than spawning a new maze. It's only worth it if the extra information and the shortcuts help you solve the maze faster.

The same maze can be solved a maximum of 300 times. This corresponds to 299 relocations. After that, fertilizing the treasure won't have any effect anymore.


# Polyculture

Grass, bushes, trees, and carrots yield ten times more when they have the right plant companion. Companion preference is different for each individual plant and cannot be predicted. Fortunately, the companion preference of the plant under the drone can be measured using get_companion(). It returns a list where the first element is the type of plant it wants as its companion and the second and third elements are the x and y coordinates of the position where it wants its companion.

For example if you plant a bush and then call get_companion() it will return something like [Entities.Carrots, 3, 5]. This means that this bush would like to have carrots at the position (3,5). So if you plant carrots at (3,5) and then harvest the bush, it will yield ten times more wood. The growth stage of the carrot doesn't matter.

A plant's companion preference can be either Entities.Grass, Entities.Bush, Entities.Tree or Entities.Carrots. Each plant chooses this randomly, but it will always choose a different plant than itself. The position can also be any position within 3 moves of the plant except the position of the plant itself.

If there is no plant under the drone that has a companion preference get_companion() will return None.


# Multi Trade

Buying items one by one takes a lot of time. You can now specify the number of items you want to trade in a second argument.

For example, if you want to buy 5 carrot seeds, you can write
trade(Items.Carrot_Seed, 5)
If you can't afford that many, this will simply do nothing instead of buying less.


# Auto Unlocks

To fully automate the game, you can use the unlock() function to automatically unlock features.
For example, you can use unlock(Unlocks.Speed) and unlock(Unlocks.Expand) to unlock the speed and expansion features.

To determine the cost of an unlock, simply use the get_cost() function as you would for a plant or item.
Example:
get_cost(Unlocks.Loops)
returns {Items.Hay:5}

If you want to find out how many of a particular unlock you have, use the num_unlocked(unlock) function.

For example, num_unlocked(Unlocks.Speed) will return the number of speed upgrades you have.

num_unlocked(Unlocks.Senses) will return 1 if senses are unlocked and 0 if they are not.

You can also use num_unlocked() on Items, Entities or Grounds. This will return 1 if it's unlocked otherwise 0.

Be careful num_unlocked(Unlocks.Carrots) will return the number of times it was unlocked/upgraded.
num_unlocked(Items.Carrots) will only return 0 or 1. (Same for other plants)


# Cactus

Cacti can be grown on soil from cactus seeds.

They have an odd sense of community.

When you harvest a cactus all cacti on the field are harvested.
The number of cactus items dropped per cactus is equal to the world size as returned by get_world_size().

A cactus only drops cactus items when harvested if it's in sorted order. 
A cactus is considered to be in sorted order if there is a smaller or equal cactus to the South and to the West and a larger or equal cactus to the North and to the East.
Essentially the cacti must be sorted in increasing x and y directions for them to drop anything.

If a cactus is at the edge of the field, only the existing neighboring fields need to be correct for it to be sorted.

The size of a cactus can be measured with measure(). 
It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.

You can swap a cactus with its neighbor in any direction using the swap() command.
swap(direction) swaps the object under the drone with the object one tile in the direction of the drone.


# Dinosaurs

Dinosaurs are ancient, majestic creatures that can be farmed for ancient bones.

To get dinosaurs you have to trade eggs and use them with use_item(Items.Egg).

Dinosaurs like to move. From time to time, the dinosaur will swap with a random neighbor.
This swap works just like calling swap(direction) manually except that it happens randomly from time to time.

Dinosaurs can be harvested for bones using the harvest() command.
There are 4 different types of dinosaurs. 
Harvesting a Dinosaur will also harvest all adjacent Dinosaurs of the same type, so an entire connected group of Dinosaurs will be harvested at once.

The type of a dinosaur can be measured with measure(). This will return a unique number for each type of dinosaur.

You can also pass a direction into measure to measure an entity next to the drone.
measure(North) for example will measure the entity to the north of the drone.

The number of bones you get depends on the size of the group of dinosaurs you harvest. Harvesting groups up to 4 will drop bones equal to the square of the group size. Groups of size 4 or larger drop bones equal to 4 times the group size.

Thus, the number of bones per Dinosaur increases with group size up to size 4, and then remains constant.
For optimal efficiency, you always want to harvest groups of size 4 or larger.

Groups also wrap around the side of the farm. So a Dinosaur on the edge of the farm is considered adjacent to a Dinosaur on the other side of the farm.


# Available Functions

harvest()
Harvests the entity under the drone. 
If you harvest an entity that can't be harvested, it will be destroyed.

returns True if an entity was removed, False otherwise.

takes the time of 200 operations to execute if an entity was removed, 1 operation otherwise.

example usage:
harvest()

-------------------------------------------------------------------------------

can_harvest()
Used to find out if plants are fully grown.

returns True if there is an entity under the drone that is ready to be harvested, False otherwise.

takes the time of 1 operation to execute.

example usage:
if can_harvest():
    harvest()

-------------------------------------------------------------------------------

swap(direction)
Swaps the entity under the drone with the entity next to the drone in the specified direction.
Doesn't work on all entities.
Also works if one (or both) of the entities are None.

returns None

takes the time of 200 operations to execute.

example usage:
swap(North)

-------------------------------------------------------------------------------

range()
Generates a sequence of numbers.

overloads:
range(end) returns a sequence of numbers from 0(inclusive) to end(exclusive).
range(start,end) returns a sequence of numbers from start(inclusive) to end(exclusive).
range(start,end,step) returns a sequence of numbers from start(inclusive) to end(exclusive) in steps of size step

takes the time of 1 operation to execute.

example usage:
for i in range(10):
    print(i)

for i in range(2,6):
    print(i)

for i in range(10, 0, -1):
    print(i)

-------------------------------------------------------------------------------

plant(entity) 
Plants the specified entity under the drone if it can be planted.
Otherwise it just does nothing.

returns True if it succeeded, False otherwise.

takes the time of 200 operations to execute if it succeeded, 1 operation otherwise.

example usage:
plant(Entities.Bush)

-------------------------------------------------------------------------------

move(direction)
Moves the drone into the specified direction by one tile.
If the drone moves over the edge of the farm it wraps back to the other side of the farm.

East   =  right
West   =  left
North  =  up
South  =  down

returns True if the drone has moved, False otherwise.

takes the time of 200 operations to execute if the drone has moved, 1 operation otherwise.

example usage:
move(North)

-------------------------------------------------------------------------------

till() 
Tills the ground under the drone into Grounds.Soil. If it's already soil it will change the ground back to Grounds.Turf.

returns None

takes the time of 200 operations to execute.

example usage:
till()

-------------------------------------------------------------------------------

get_pos_x() 
Gets the current x position of the drone.
The x position starts at 0 in the West and increases in the East direction.

returns a number representing the current x coordinate of the drone.

takes the time of 1 operation to execute.

example usage:
x, y = get_pos_x(), get_pos_y()

-------------------------------------------------------------------------------

get_pos_y() 
Gets the current y position of the drone.
The y position starts at 0 in the South and increases in the North direction.

returns a number representing the current y coordinate of the drone.

takes the time of 1 operation to execute.

example usage:
x, y = get_pos_x(), get_pos_y()

-------------------------------------------------------------------------------

get_world_size() 
Get the current size of the farm.

returns the side length of the grid in the north to south direction.

takes the time of 1 operation to execute.

example usage:
for i in range(get_world_size()):
    move(North)

-------------------------------------------------------------------------------

get_entity_type() 
Find out what kind of entity is under the drone.

returns None if the tile is empty, otherwise returns the type of the entity under the drone.

takes the time of 1 operation to execute.

example usage:
if get_entity_type() == Entities.Grass:
    harvest()

-------------------------------------------------------------------------------

get_ground_type() 
Find out what kind of ground is under the drone.

returns the type of the ground under the drone.

takes the time of 1 operation to execute.

example usage:
if get_ground_type() != Grounds.Soil:
    till()

-------------------------------------------------------------------------------

get_time() 
Get the current game time.

returns the time in seconds since the start of the game.

takes the time of 1 operation to execute.

example usage:
start = get_time()

do_something()

time_passed = get_time() - start

-------------------------------------------------------------------------------

get_op_count()
Used to measure the number of operations performed.

returns the number of operations performed since the start of execution.

takes the time of 1 operation to execute.

example usage:
do_something()

print(get_op_count())

-------------------------------------------------------------------------------

trade(item) 
Tries to buy the specified item.
If the item cannot be bought or you don't have the required resources it simply does nothing.

overloads:
trade(item): Buy the item once.
trade(item, n): If Unlocks.Multi_Trade is unlocked, this will buy the item n times immediately. If you can't afford all n items, it won't buy any at all. If Unlocks.Multi_Trade is not unlocked, it throws an error.

returns True if it was able to buy the items, False otherwise.

takes the time of 200 operations to execute if it succeeded, 1 operation otherwise.

example usage:
if num_unlocked(Unlocks.Multi_Trade) > 0:
    trade(Items.Carrot_Seed, 10)
else:
    for i in range(10):
        trade(Items.Carrot_Seed)

-------------------------------------------------------------------------------

use_item(item) 
Attempts to use the specified item. Can only be used with some items including Items.Water_Tank, Items.Fertilizer and Items.Egg.

returns True if an item was used, False otherwise.

takes the time of 200 operations to execute if it succeeded, 1 operation otherwise.

example usage:
use_item(Items.Fertilizer)

-------------------------------------------------------------------------------

get_water() 
Get the current water level under the drone.

returns the water level under the drone as a number between 0 and 1.

takes the time of 1 operation to execute.

example usage:
if get_water() < 0.5:
    use_item(Items.Water_Tank)

-------------------------------------------------------------------------------

do_a_flip() 
Makes the drone do a flip! This action is not affected by speed upgrades.

returns None

takes 1s to execute.

example usage:
while True:
    do_a_flip()

-------------------------------------------------------------------------------

print(something) 
Prints something into the air above the drone using smoke. This action is not affected by speed upgrades.
Multiple values can be printed at once.

returns None

takes 1s to execute.

example usage:
print("ground:", get_ground_type())

-------------------------------------------------------------------------------

quick_print()
Prints a value just like print() but it doesn't stop to write it into the air so it can only be found on the output page.

returns None

takes the time of 1 operations to execute.

example usage:
quick_print("hi mom")

-------------------------------------------------------------------------------

len(collection) 
Get the number of elements in a list, set, dict or tuple.

returns the length of the collection.

takes the time of 1 operation to execute.

example usage:
for i in range(len(list)):
    list[i] += 1

-------------------------------------------------------------------------------

num_items(item) 
Find out how much of item you currently have.

returns the number of item currently in your inventory.

takes the time of 1 operation to execute.

example usage:
if num_items(Items.Fertilizer) == 0:
    trade(Items.Fertilizer)

-------------------------------------------------------------------------------

get_cost(thing) 
Gets the cost of a thing

If thing is an item get the cost of buying it when using trade(item).
If thing is an entity get the seed needed to plant it.
If thing is an unlock get the cost of unlocking it.

returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
returns None when used on an upgradeable unlock that is already at the max level.

takes the time of 1 operation to execute.

example usage:
cost = get_cost(Unlocks.Carrots)
for item in cost:
    if num_items(item) < cost[item]:
        print("not enough items to unlock carrots")

-------------------------------------------------------------------------------

clear() 
Removes everything from the farm, and moves the drone back to position (0,0).

returns None

takes the time of 200 operations to execute.

example usage:
clear()

-------------------------------------------------------------------------------

get_companion() 
Get the companion preference of the plant under the drone.

returns a list of the form [companion_type, companion_x_position, companion_y_position]

takes the time of 1 operation to execute.

example usage:
companion = get_companion()
if companion != None:
	print(companion)

-------------------------------------------------------------------------------

unlock(unlock) 
Has exactly the same effect as clicking the button corresponding to unlock in the research tree.

returns True if the unlock was successful, False otherwise.

takes the time of 200 operations to execute if it succeeded, 1 operation otherwise.

example usage:
unlock(Unlocks.Carrots)

-------------------------------------------------------------------------------

num_unlocked(thing)
Used to check if an unlock, entity, ground or item is already unlocked.

returns 1 plus the number of times thing has been upgraded if thing is upgradable. Otherwise returns 1 if thing is unlocked, 0 otherwise.

takes the time of 1 operation to execute.

example usage:
if num_unlocked(Unlocks.Multi_Trade) > 0:
    trade(Items.Carrot_Seed, 10)
else:
    for i in range(10):
        trade(Items.Carrot_Seed)

-------------------------------------------------------------------------------

measure() 
Can measure some values on some entities. The effect of this depends on the entity.

overloads:
measure() measures the entity under the drone.
measure(direction) measures the neighboring entity in the direction of the drone.

returns the number of petals of a sunflower.
returns the next position for a treasure.
returns the size of a cactus.
returns the number corresponding to the type of a dinosaur.
returns None for all other entities.

takes the time of 1 operation to execute.

example usage:
num_petals = measure()

-------------------------------------------------------------------------------

min(a,b)
Gets the minimum of a sequence of elements or several passed arguments.
Can be used on numbers and strings.

overloads:
min(a,b,c): Returns the minimum of the passed arguments.
min(sequence): Returns the minimum of all values in a sequence.

execution time depends on the input.

example usage:
min([3,6,34,16])

-------------------------------------------------------------------------------

max(a,b)
Gets the maximum of a sequence of elements or several passed arguments.
Can be used on numbers and strings.

overloads:
max(a,b,c): Returns the maximum of the passed arguments.
max(sequence): Returns the maximum of all values in a sequence.

takes the time of #comparisons operations to execute.

example usage:
max([3,6,34,16])

-------------------------------------------------------------------------------

abs(number)
Computes the absolute value of a number.

returns number if number is positive, -number otherwise.

takes the time of #comparisons operations to execute.

example usage:
abs(-69)

-------------------------------------------------------------------------------

random()
Samples a random number between 0 (inclusive) and 1 (exclusive).

returns the random number.

takes the time of 1 operations to execute.

example usage:
def random_elem(list):
	index = random() * len(list) // 1
	return list[index]

-------------------------------------------------------------------------------

list()
Creates a new list.

overloads:
list(collection): Creates a list with the elements of an existing list, set, dict or tuple.

returns a list.

takes the time of 1 + len(collection) operations to execute.

example usage:
new_list = list((1,2,3))

-------------------------------------------------------------------------------

set()
Creates a new set.

overloads:
set(collection): Creates a set with the elements of an existing list, set, dict or tuple.

returns a set.

takes the time of 1 + len(collection) operations to execute.

example usage:
new_set = set((1,2,3))

-------------------------------------------------------------------------------

dict()
Creates a new empty dictionary.

returns an empty dictionary.

takes the time of 1 operation to execute.

example usage:
new_dict = dict()

-------------------------------------------------------------------------------

set_execution_speed(speed)
Limits the speed at which the program is executed to better see what's happening.

A speed of 1 is the speed the drone has without any speed upgrades.
A speed of 10 makes the code execute 10 times faster and corresponds to the speed of the drone after 9 speed upgrades.
A speed of 0.5 makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

If speed is faster than the execution can currently go it will just go at max speed.

If speed is 0 or negative, the speed is changed back to max speed.
The effect will also stop when the execution stops.

returns None

takes the time of 200 operations to execute.

example usage:
set_execution_speed(1)

-------------------------------------------------------------------------------

set_farm_size(size)
Limits the size of the farm to better see what's happening.
Also clears the farm.
Sets the farm to a size x size grid.
The smallest size possible is 3.
A size smaller than 3 will change the grid back to its full size.
The effect will also stop when the execution stops.

returns None

takes the time of 200 operations to execute.

example usage:
set_farm_size(5)