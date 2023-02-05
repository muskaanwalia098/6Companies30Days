from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sl, ans = SortedList(), 0
        mp = {x: i for i, x in enumerate(nums1)}
        for i, y in enumerate(nums2):
            y = mp[y]
            left = sl.bisect_left(y)
            ans += (left * ((len(nums2) - y -1) - (len(sl) - left)))
            sl.add(y)
        return ans

           

        # # index of a(from A) in B
        # A, B = nums1, nums2
        # pos = [0] * len(A)
        # for i, b in enumerate(B):
        #     pos[b] = i
        # # Build pre_a[i]: no. of elements on a[i]'s left in both A and B.
        # # pos_in_b: sorted indexes (in B) of all the visited elements in A.
        # pos_in_b, pre_a = SortedList([pos[A[0]]]), [0]
        # for a in A[1:]:
        #     pos_in_b.add(pos[a])
        #     pre_a.append(pos_in_b.bisect_left(pos[a]))
        # # Build suf_a[i]: no of elementson a[i]'s right in both A and B.
        # pos_in_b, suf_a = SortedList([pos[A[-1]]]), [0]
        # for a in reversed(A[:len(A)-1]):
        #     idx = pos_in_b.bisect(pos[a])
        #     suf_a.append(len(pos_in_b) - idx)
        #     pos_in_b.add(pos[a])
        # suf_a.reverse()
        # # Sum up all the unique triplets centered on A[i]
        # ans = 0
        # for i, j in zip(pre_a, suf_a):
        #     ans += i * j
        # return ans
