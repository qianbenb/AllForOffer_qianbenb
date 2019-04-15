class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        s = '0'
        if N == 0:
            return 0
        if K % 2 == 0:
            if self.kthGrammar(N-1,K/2) == 0:
                return 1
            else:
                return 0
        if K % 2 == 1:
            if self.kthGrammar(N-1,(K + 1)/2) == 0:
                return 0
            else:
                return 1