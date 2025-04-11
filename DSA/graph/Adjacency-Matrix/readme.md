
# 📊 Adjacency Matrix Graph Implementation
A simple and clean Python implementation of a **Graph using an Adjacency Matrix**. This is for representing an **undirected** and **simple** graph (i.e., no self-loops or multiple edges).

## 📌 Project Structure

This file defines a `Graph` class with the following methods:
- `__init__` to initialize the adjacency matrix
- `add_edge()` to add an edge between two vertices
- `remove_edge()` to remove an edge
- `has_edge()` to check the existence of an edge
- `print_adj_matrix()` to display the adjacency matrix

---

## 🧠 Visual Guide

Here’s a visual explanation of the implementation and how the adjacency matrix works:

![image](https://github.com/user-attachments/assets/c370017a-20b9-49be-afa8-8098c3111226)

---

## 🛠️ How to Use

1. Clone or copy the code file.
2. Run the Python script containing the `Graph` class.
3. Try adding/removing edges and printing the matrix.

```python
# Example usage:
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.print_adj_matrix()
