# It's possible to start with an empty dictionary
# and then add stuff like below
alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Add value to dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Edit values in dictionary
alien_0['color'] = 'red'
print("\n")
print(alien_0)

del alien_0['points']
print("\n")
print(alien_0)
print("\n\n")

###
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x position: " + str(alien_1['x_position']))

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print("Current alien x position is: " + str(alien_1['x_position']))

# A list of dictionaries

aliens = [alien_0, alien_1]
for alien in aliens:
    print(alien)
