import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.sid = -1  # String ID

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        n = len(source)
        
        # 1. Map all unique strings to IDs
        unique_strs = list(set(original) | set(changed))
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        # 2. Floyd-Warshall for shortest transformation paths
        dist = [[float('inf')] * m for _ in range(m)]
        for i in range(m): dist[i][i] = 0
        
        for u, v, c in zip(original, changed, cost):
            u_id, v_id = str_to_id[u], str_to_id[v]
            dist[u_id][v_id] = min(dist[u_id][v_id], c)
            
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # 3. Build a Trie for fast substring matching
        root = TrieNode()
        for s, s_id in str_to_id.items():
            curr = root
            for char in s:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.sid = s_id
            
        # 4. DP with Trie traversal
        # dp[i] is the min cost to convert prefix of length i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Pre-calculate unique lengths to limit search space
        valid_lengths = sorted(list(set(len(s) for s in unique_strs)))
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            
            # Case 1: source[i] already matches target[i]
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case 2: Try converting substrings starting at index i
            # We traverse the trie for both source and target simultaneously
            curr_s = root
            curr_t = root
            for j in range(i, n):
                char_s = source[j]
                char_t = target[j]
                
                if char_s not in curr_s.children or char_t not in curr_t.children:
                    break
                    
                curr_s = curr_s.children[char_s]
                curr_t = curr_t.children[char_t]
                
                # If both substrings are "known" strings in our dictionary
                if curr_s.sid != -1 and curr_t.sid != -1:
                    c = dist[curr_s.sid][curr_t.sid]
                    if c != float('inf'):
                        dp[j+1] = min(dp[j+1], dp[i] + c)
                        
        return dp[n] if dp[n] != float('inf') else -1