def maxArea(height):
        l = 0
        r = len(height)-1
        area = 0

        while l<r:
            area = max(area, (r-l)*min(height[r], height[l]))
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return area