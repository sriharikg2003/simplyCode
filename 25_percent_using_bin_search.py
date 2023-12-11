class Solution(object):

    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def lb(heights,ele):

            l = 0
            r = len(heights)-1
            ans = -1
            while(l<=r):
                mid = l + int((r-l)/2)
                if heights[mid]>=ele:
                    ans = mid
                    r = mid-1
                else:
                    l = mid +1
            return ans


        def ub(heights,ele):

            l = 0
            r = len(heights)-1
            ans = -1
            while(l<=r):
                mid = l + int((r-l)/2)
                if heights[mid]<=ele:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans


        n = len(arr)
        first =int( n / 4)
        second = int(n / 2)
        third = int(3 * n / 4)

        def isValid(ele):
            l = lb(arr,ele)
            r = ub(arr,ele)
            if r-l + 1> int(n/4):
                return True
            return False

        if isValid(arr[first]):
            return arr[first]
        elif isValid(arr[second]):
            return arr[second]
        elif isValid(arr[third]):
            return arr[third]
        else :
            return -1
