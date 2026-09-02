class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_chars = [i for i in range(26) if cnt[i] % 2 == 1]
        if n % 2 == 0:
            if odd_chars:
                return ""
            mid_char = -1
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = odd_chars[0]

        half = n // 2
        half_cnt = [cnt[i] // 2 for i in range(26)]
        T = target

        def build_full(h_list):
            h = ''.join(chr(97 + c) for c in h_list)
            mid = '' if mid_char == -1 else chr(97 + mid_char)
            return h + mid + h[::-1]

        # greedily match T[0:half] using half_cnt
        working = half_cnt[:]
        matched_len = 0
        for i in range(half):
            c = ord(T[i]) - 97
            if working[c] > 0:
                working[c] -= 1
                matched_len += 1
            else:
                break

        if matched_len == half:
            h_list = [ord(ch) - 97 for ch in T[:half]]
            candidate = build_full(h_list)
            if candidate > T:
                return candidate
            start_j = half - 1
        else:
            start_j = matched_len

        # prefix character counts of T[0:j] for j = 0..matched_len
        prefix_counts = [[0] * 26]
        run = [0] * 26
        for i in range(matched_len):
            run = run[:]
            run[ord(T[i]) - 97] += 1
            prefix_counts.append(run)

        for j in range(start_j, -1, -1):
            pc = prefix_counts[j]
            remaining = [half_cnt[c] - pc[c] for c in range(26)]
            tc = ord(T[j]) - 97
            found_c = -1
            for c in range(tc + 1, 26):
                if remaining[c] > 0:
                    found_c = c
                    break
            if found_c != -1:
                remaining[found_c] -= 1
                h_list = [ord(T[k]) - 97 for k in range(j)]
                h_list.append(found_c)
                for c in range(26):
                    h_list.extend([c] * remaining[c])
                return build_full(h_list)

        return ""