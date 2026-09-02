from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start = None
        litter = []
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    start = (i, j)
                elif c == 'L':
                    litter.append((i, j))

        k = len(litter)
        if k == 0:
            return 0

        litter_index = {pos: idx for idx, pos in enumerate(litter)}
        full_mask = (1 << k) - 1

        sr, sc = start
        start_mask = 0
        if (sr, sc) in litter_index:
            start_mask |= 1 << litter_index[(sr, sc)]

        # key = (r, c, mask) -> best (max) energy seen so far at this node
        best_energy = {(sr, sc, start_mask): energy}
        queue = deque([(sr, sc, start_mask, energy, 0)])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, mask, e, dist = queue.popleft()

            if mask == full_mask:
                return dist

            if e == 0:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask
                    if (nr, nc) in litter_index:
                        nmask |= 1 << litter_index[(nr, nc)]

                    key = (nr, nc, nmask)
                    if best_energy.get(key, -1) < ne:
                        best_energy[key] = ne
                        queue.append((nr, nc, nmask, ne, dist + 1))

        return -1