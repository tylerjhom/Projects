from collections import defaultdict
import heapq as heap
from itertools import permutations

class Graph:
    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.edges = []
        self.building_indices = {}  # Mapping from building names to indices

    #Connects buildings with vertices
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])
        if u not in self.building_indices:
            self.building_indices[u] = len(self.building_indices)
        if v not in self.building_indices:
            self.building_indices[v] = len(self.building_indices)

    #Determines the shortest path between two vertices
    def dijkstra(self, start, end):
        graph = defaultdict(list)

        for u, v, w in self.edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        parent_map = {building: None for building in graph}
        distance = {building: float('inf') for building in graph}
        distance[start] = 0

        pq = [(0, start)]

        #itterate through all neighbors to find shortest distance
        while pq:
            current_distance, current_node = heap.heappop(pq)

            # skip if visited
            if current_node in visited:
                continue
            
            # add current node to visited set
            visited.add(current_node)

            # update new time with weight
            for neighbor, weight in graph[current_node]:
                new_distance = distance[current_node] + weight

                # updates the map with the most efficient route
                if new_distance < distance[neighbor]:
                    parent_map[neighbor] = current_node
                    distance[neighbor] = new_distance
                    heap.heappush(pq, (new_distance, neighbor))

        return parent_map, distance


def main():
  # create the Graph object
    UT_Campus = Graph(36)

    #Fills out map with buildings on UT campus
    UT_Campus.add_edge("GSB", "Waggener", 2)
    UT_Campus.add_edge("GSB", "UTC", 1)
    UT_Campus.add_edge("GSB", "Greg", 1)
    UT_Campus.add_edge("GSB", "PCL", 1)
    UT_Campus.add_edge("UTC", "PCL", 1)
    UT_Campus.add_edge("Blanton", "PCL", 4)
    UT_Campus.add_edge("Blanton", "Jester", 3)
    UT_Campus.add_edge("Blanton", "Clark", 3)
    UT_Campus.add_edge("GSB", "Mezes", 2)
    UT_Campus.add_edge("Greg", "Jester", 2)
    UT_Campus.add_edge("Greg", "DKR", 7)
    UT_Campus.add_edge("DKR", "LBJ", 8)
    UT_Campus.add_edge("Jester", "Clark", 2)
    UT_Campus.add_edge("Clark", "DKR", 5)
    UT_Campus.add_edge("Mezes", "Parlin", 3)
    UT_Campus.add_edge("Mezes", "Harry Ransom Center", 3)
    UT_Campus.add_edge("Parlin", "Harry Ransom Center", 3)
    UT_Campus.add_edge("Parlin", "UT Tower", 5)
    UT_Campus.add_edge("Union", "UT Tower", 4)
    UT_Campus.add_edge("Biological Sciences Greenhouses", "UT Tower", 4)
    UT_Campus.add_edge("Biological Sciences Greenhouses", "Union", 3)
    UT_Campus.add_edge("UT Tower", "College of Natural Science", 1)
    UT_Campus.add_edge("Waggener", "SAC", 1)
    UT_Campus.add_edge("Waggener", "College of Natural Science", 3)
    UT_Campus.add_edge("SAC", "RLP", 1)
    UT_Campus.add_edge("College of Natural Science", "UT Tower", 3)
    UT_Campus.add_edge("College of Natural Science", "Welch Hall", 2)
    UT_Campus.add_edge("College of Natural Science", "Painter", 2)
    UT_Campus.add_edge("Painter", "GEA", 2)
    UT_Campus.add_edge("GEA", "Burdine", 3)
    UT_Campus.add_edge("Burdine", "PMA", 4)
    UT_Campus.add_edge("PMA", "EER", 2)
    UT_Campus.add_edge("PMA", "ETC", 2)
    UT_Campus.add_edge("PMA", "ASE", 4)
    UT_Campus.add_edge("ETC", "EER", 2)
    UT_Campus.add_edge("ETC", "ASE", 3)
    UT_Campus.add_edge("ASE", "Kinsolving", 7)
    UT_Campus.add_edge("Kinsolving", "Moody", 1)
    UT_Campus.add_edge("Speech Center", "Moody", 1)
    UT_Campus.add_edge("Speech Center", "FAC", 4)
    UT_Campus.add_edge("FAC", "Architecture", 2)
    UT_Campus.add_edge("FAC", "Union", 1)
    UT_Campus.add_edge("Architecture", "Union", 1)
    UT_Campus.add_edge("Architecture", "Parlin", 1)
    UT_Campus.add_edge("Architecture", "UT Tower", 2)
    UT_Campus.add_edge("EER", "San Jacinto Garage", 7)
    UT_Campus.add_edge("ETC", "San Jacinto Garage", 6)
    UT_Campus.add_edge("San Jacinto Garage", "School of Law", 5)
    UT_Campus.add_edge("School of Law", "LBJ", 7)
    UT_Campus.add_edge("School of Law", "Music", 2)
    UT_Campus.add_edge("Music", "LBJ", 7)
    
    print()
    print("Welcome to your 40-Acres Walktime Calculator!")
    while True:
        while True:
            try:
                num_locations = int(input("How many locations would you like to stop by today (Enter 0 if done): "))
                print()
                if num_locations >= 0:
                    break
                else:
                    print("Please enter number of buildings you wish to visit")
                    print()
            except ValueError:
                print("Please enter number of buildings you wish to visit")
                print()
        if num_locations == 0:
            print()
            print("Have a good day!")
            return
        total_distance = float('inf')
        total_path = []

        print("Buildings to choose from:")
        building_list = [
    "Aerospace Engineering Building (ASE)", "Graduate School of Business (GSB)", "Waggener",
    "Gregory Gymnasium (Greg)", "Mezes", "Jester West Residence Hall (Jester)",
    "Darrell K Royal Texas Memorial Stadium (DKR)", "LBJ Presidential Library (LBJ)",
    "Caven Clark Field (Clark)", "Parlin Hall (Parlin)", "Harry Ransom Center", "UT Tower",
    "Union", "Biological Sciences Greenhouses", "College of Natural Science",
    "Student Activity Center (SAC)", "Robert L. Patton Building (RLP)", "Welch Hall",
    "Painter Hall (Painter)", "Mary E. Gearing Hall (GEA)", "Burdine Hall (Burdine)",
    "Physics Math Astronomy Building (PMA)", "Engineering Education and Research Center (EER)",
    "Engineering Teaching Center (ETC)", "Kinsolving Residence Hall (Kinsolving)",
    "Moody College of Communication (Moody)", "University of Texas Speech Center (Speech Center)",
    "Flawn Academic Center (FAC)", "School of Architecture (Architecture)",
    "The University of Texas at Austin School of Law", "San Jacinto Garage",
    "Butler School of Music - University of Texas at Austin"
        ]
        sorted_building_list = sorted(building_list)
        sorted_buildings_str = ', '.join(sorted_building_list)
        print(sorted_buildings_str)
        print()

        # Input the starting building
        start_building = input("Enter the starting building: ")
        while start_building not in UT_Campus.building_indices:
            print("Invalid building name. Please enter valid building name.")
            print()
            start_building = input("Enter the starting building: ")
            print()

        # Input the list of buildings to visit
        not_visited = []
        for _ in range(num_locations):
            building = input("Enter a building to visit: ")
            while building not in UT_Campus.building_indices:
                print("Invalid building name. Please enter valid building name.")
                print()
                building = input("Enter the starting building: ")
                print()
            not_visited.append(building)
            
        else:
        # Calculate the optimal path
            for permuted_buildings in permutations(not_visited):
                current_building = permuted_buildings[0]
                remaining_buildings = permuted_buildings[1:]

                # Calculate the distance from the starting building to the first destination
                first_parent, first_distance = UT_Campus.dijkstra(start_building, current_building)
                first_distance = first_distance[current_building]

                # Calculate the optimal path for the remaining buildings
                remaining_path = [current_building]
                remaining_distance = 0

                for next_building in remaining_buildings:
                    shortest_path_parent, shortest_path_distances = UT_Campus.dijkstra(current_building, next_building)
                    path = []
                    current_node = next_building

                    while current_node:
                        path.append(current_node)
                        current_node = shortest_path_parent[current_node]

                    path.reverse()
                    remaining_path.extend(path[1:])
                    remaining_distance += shortest_path_distances[next_building]

                    current_building = next_building

                # Update the total path if the current permutation has a shorter total distance
                if first_distance + remaining_distance < total_distance:
                    total_distance = first_distance + remaining_distance
                    total_path = [start_building] + remaining_path

        print(f"Optimal path: {total_path}")
        print(f"Total travel time: {total_distance} min")
        print()

if __name__ == "__main__":
    main()
