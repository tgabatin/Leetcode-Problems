"""
A gene string can be represented by an 8-character long string, with choices 'A', 'C',
'G', and 'T'. 

Suppose we need to investigate a mutation from a gene string startGene to a gene string
endGene where one mutation is defined as one single character changed in the gene string. 

* For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be
in bank to make it a valid gene string. 

Given the two gene strings startGene and endGene and the gene bank bank, return the
minimum number of mutations needed to mutate from startGene to endGene. If there is no
such mutation, return -1. 

Note that the starting point is assumed to be valid, so it might not be included in
the bank. 
"""

"""
Time Complexity: O(nm^2)
Space Complexity: O(nm^2)
"""

from collections import deque
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        
        queue = deque([startGene, 0])
        visited = set([startGene])

        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for c in ['A', 'C', 'G', 'T']:
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations+1))
        
        return -1
        