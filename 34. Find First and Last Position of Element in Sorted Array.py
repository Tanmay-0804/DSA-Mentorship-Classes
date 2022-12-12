class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_pos = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[l] == target:
                start_pos = l
                break

            if l == r:
                if nums[mid] == target:
                    start_pos = mid
                break

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                start_pos = mid
                r = mid - 1
            else:
                r = mid - 1

        end_pos = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[r] == target:
                end_pos = r
                break

            if l == r:
                if nums[mid] == target:
                    end_pos = mid
                break

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                end_pos = mid
                l = mid + 1
            else:
                r = mid - 1

        return start_pos, end_pos