set_farm_size(3)

# Weltgröße abrufen
world_size = get_world_size()

# Feld leeren
clear()

# Kakteen pflanzen
for a in range(world_size):
    for b in range(world_size):
        make_ground(Grounds.Soil)
        plant(Entities.Cactus)
        move(East)
    move(South)
    for c in range(world_size):
        move(West)

# Kakteen mit Bubble-Sort sortieren
for a in range(world_size * world_size):
    for b in range(world_size):
        for c in range(world_size - 1):
            # Aktuellen Kaktus messen
            current_size = measure()
            
            # Zum Kaktus im Osten bewegen
            move(East)
            
            # Wenn der aktuelle Kaktus größer als der nächste ist, tauschen
            if current_size > measure():
                swap(West)
            
            # Zurück zum aktuellen Kaktus bewegen
            move(West)
        
        # Zur nächsten Reihe bewegen
        move(South)
    
    # Zurück zum Anfang des Feldes bewegen
    for d in range(world_size):
        move(North)

# Kakteen ernten
for a in range(world_size):
    for b in range(world_size):
        harvest()
        move(East)
    move(South)
    for c in range(world_size):
        move(West)