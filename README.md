# xcom-pygame

## Game Menu
- New Game
- Load Game
- Options
- Exit
## Squad Select
Three windows. Each lets you customize or randomize the soldiers you play.
## Game Phase
Square Grid. Rotated if possible.  
Premade or generated (procedurally) levels.  
Soldiers spawn in designated position.  
Alien are picked at random and spawned in appointed location.  

Every character and enemy have speed which allows us to create an Action Queue.

Characters can: shoot, throw a granade, special skill (depending on which class the soldier is), move

Moving towards a terrain element grants you resistance.

Enemies can: shoot, special shoot (can be customizable depending on which type of enemy it is), move


# Classes 

## Enitities
### Soldier
- Name
- HP
- Speed (when it's going to act)
- DMG (base damage from shooting)
- Class
- Nationality (Italian, Polish, French)
- Personality (Timid, Brave, Resilient)
- Equipment

Depending on a Class (Scout, Sniper, Technician) Soldier will have different abilities.  
Scout - Sword Strike  
Sniper - No range on shooting  
Technician - Healing bot  

### Alien
- HP
- Speed (when it's going to act)
- DMG (base damage from shooting)
- Type
- Personality

### Terrain
- Type (Tree, Bush, Rocks, Car, Barrel)
- Coverage (1, 0.5)

## Functionalities
### Action Queue
`from collections import deque`