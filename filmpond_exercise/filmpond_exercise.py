class FilmpondChallenge:
    def foo(self):
        return 'bar'
    
    def get_continents(self, connections, continents):
    	visited_land_position = []

    	for land_position in connections.keys():
	    if not land_position in visited_land_position:
	        continent_land_positions = []

                self.get_continent(connections, land_position, continent_land_positions)
		continents.append(continent_land_positions)
		visited_land_position = visited_land_position + continent_land_positions

    def get_continent(self, connections, pos, continents):
        if pos not in continents:
	    continents.append(pos)
	    for new_pos in connections[pos]:
	        self.get_continent(connections, new_pos, continents)

    def get_all_connections(self, map, res): 
        for i,row in enumerate(map):
            for x,pos in enumerate(row):
		if pos == '+':
	            self.get_connections(map, (i,x), res)
    
    def get_connections(self, map, position, res):
        row = position[0]
	column = position[1]

	connections = []
	num_columns = len(map[0])
	num_rows = len(map)

	if (row -1 >= 0) and (column -1 >= 0):
	    connections.append((row - 1, column - 1))

        if (row -1 >= 0):
	    connections.append((row - 1, column))

	if (row -1 >= 0) and (column + 1 < num_columns):
	    connections.append((row - 1, column + 1))

	if (column + 1 < num_columns):
	    connections.append((row, column + 1))

	if (row + 1 < num_rows) and (column + 1 < num_columns):
	    connections.append((row + 1, column + 1))

	if (row + 1 < num_rows):
	    connections.append((row + 1, column))
	 
	if (row + 1 < num_rows) and (column - 1 >= 0):
	    connections.append((row + 1, column - 1))
	
	if (column - 1 >= 0):
	    connections.append((row, column - 1))

	res[position] = [pos for pos in connections if map[pos[0]][pos[1]] == '+']

	# print res[position]

	# res[position] = connections

