def find_shortest_path(graph, start, end):
    # Basis: jika start dan end sama, maka jaraknya 0
    if start == end:
        return 0
    # Jika tidak, cari jarak terpendek dari titik awal ke titik tujuan
    else:
        # Inisialisasi jarak terpendek ke infinity
        shortest_path = float('inf')
        # Loop melalui setiap node yang terhubung dengan start
        for neighbor, path_length in graph[start].items():
            # Jika jarak tersebut lebih pendek dari jarak terpendek yang sudah ditemukan
            if path_length < shortest_path:
                # Cari rute terpendek dari node tersebut ke titik tujuan
                recursive_path = find_shortest_path(graph, neighbor, end)
                # Jika rute tersebut ditemukan dan jarak rute tersebut lebih pendek dari jarak terpendek yang sudah ditemukan
                if recursive_path is not None and recursive_path + path_length < shortest_path:
                    # Update jarak terpendek
                    shortest_path = recursive_path + path_length
        # Jika jarak terpendek tidak berubah dari nilai awal, artinya tidak ada jalur yang ditemukan
        if shortest_path == float('inf'):
            return None
        # Kembalikan jarak terpendek yang ditemukan
        return shortest_path
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 3},
    'D': {}
}
start = 'A'
end = 'D'
shortest_path = find_shortest_path(graph, start, end)
print(f"Jarak terpendek dari {start} ke {end} adalah {shortest_path}")


