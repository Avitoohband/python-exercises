# this program calculate how much water are trapped between the columns
def cal_trapped_water(container):
    water_trapped = 0  # will store the amount of water are trapped
    for i in range(len(container)):
        left = i  # left pointer
        right = i  # right pointer
        left_height = container[i]  # the current height for the left side
        right_height = container[i]  # the current height for the left side
        while left >= 0:  # checks all columns to the left for the highest one
            left_height = max(left_height, container[left])
            left -= 1
        while right < len(container):  # checks all columns to the right for the highest one
            right_height = max(right_height, container[right])
            right += 1
        min_height = min(left_height, right_height)  # choosing the shortest columns between the two highest columns
        water_trapped += min_height - container[i]  # diff with the higher column and less the current height
    return water_trapped


water_container = [3, 0, 2, 0, 4]  # should return 7
print(cal_trapped_water(water_container))
