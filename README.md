# WGUPS Routing Tool
## Overview
This project implements an optimized package delivery system using a **Greedy Algorithm (Nearest Neighbor Algorithm)** for route optimization and a **Hash Table** for efficient data storage and retrieval. The system is designed to minimize travel time and mileage while ensuring fast lookups for package data.

## Features
- **Nearest Neighbor Algorithm** for route optimization
- **Hash Table** implementation for quick package lookups
- **Manual Truck Loading** with plans for automated constraints-based allocation
- **Modular Programming** for scalability and easy updates
- **Performance Considerations** with insights on improving efficiency using **Dijkstra's Algorithm**

## Technologies Used
- **Programming Language:** Python 3.12
- **IDE:** PyCharm 2024.3.1.1
- **Hardware:** Intel i7-12700K, 64GB RAM, 1TB SSD
- **Operating System:** Windows 11



## Usage
1. **Initialize Trucks:** Loads packages and sets their initial status.
2. **Optimize Delivery Route:** Uses Nearest Neighbor Algorithm to find the most efficient delivery path.
3. **Deliver Packages:** Updates package statuses and records delivery times.
4. **Return to Hub:** Computes total travel distance and time.
5. **User Interface:** Allows querying package statuses and details.

## Performance Analysis
- **Time Complexity:** O(n²) due to nested nearest neighbor searches.
- **Space Complexity:** O(n²) primarily from the distance matrix.
- **Future Optimization:** Implementing Dijkstra’s Algorithm for better efficiency.

## Strengths & Weaknesses
### Strengths:
- Fast package lookups using Hash Table (O(1)).
- Simple and adaptable implementation.
- Modular design for easy updates.

### Weaknesses:
- Performance depends on the hash function; poor distribution can degrade performance.
- Nearest Neighbor Algorithm does not guarantee global route optimization.

## Future Enhancements
- **Automated Truck Loading:** Implement a smart decision-making system for package allocation.
- **Graph Representation:** Optimize route planning using a graph-based approach.
- **Alternative Algorithms:** Explore **Dijkstra’s Algorithm** and **Bellman-Ford Algorithm** for improved efficiency.

