# -*- coding: utf-8 -*-
__author__ = 'yghou'
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).

You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""


class Solution(object):
    def __init__(self):
        self.result = set()

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(gas) != len(cost) or sum(gas) < sum(cost):
            return -1
        start = 0
        total_gas = 0
        for i in range(len(gas)):
            if total_gas < 0:
                total_gas = gas[i] - cost[i]
                start = i
            else:
                total_gas += (gas[i] - cost[i])

        return start

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        N = len(cost)
        for i in range(N):
            #self._can_complete_circuit_recur(i, i, 0, gas, cost, N, 'L')
            self._can_complete_circuit_recur(i, i, 0, gas, cost, N, 'R')

        if len(self.result) > 0:
            return list(self.result)[-1]
        else:
            return -1

    def _can_complete_circuit_recur(self, begin, pos, total_gas, gas, cost, N, direction):

        if begin == (N + pos-1) % N and total_gas + gas[pos] >= cost[(N + pos-1) % N] and direction == 'L':
            self.result.add(begin)
        elif begin == (N + pos + 1) % N and total_gas + gas[pos] >= cost[pos] and direction == 'R':
            self.result.add(begin)
        else:
            if total_gas + gas[pos] > cost[pos] and direction == 'R':
                total_gas += (gas[pos] - cost[pos])
                self._can_complete_circuit_recur(begin, (N + pos + 1) % N, total_gas, gas, cost, N, direction)
            # if total_gas + gas[pos] > cost[(N + pos-1) % N] and direction == 'L':
            #     total_gas += (gas[pos] - cost[(N + pos-1) % N])
            #     self._can_complete_circuit_recur(begin, (N + pos - 1) % N, total_gas, gas, cost, N, direction)
if __name__ == '__main__':
    print Solution().canCompleteCircuit([5], [4])
    print Solution().canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1])
    print Solution().canCompleteCircuit([1, 2], [2, 1])
    print Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])