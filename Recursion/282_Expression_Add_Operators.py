def addOperators(nums, target):
    result = []

    # TC = O(4^N) SC = O(n)
    # index, curr_exp, curr_eval, prev_num
    def backtrack(index, curr_exp, curr_eval, prev_num):
        if index == len(nums) and curr_eval == target:
            result.append(curr_exp)
            return

        for i in range(index, len(nums)):
            temp = int(nums[index : i + 1])
            if index == 0:
                backtrack(i + 1, nums[index : i + 1], temp, temp)
            else:
                backtrack(
                    i + 1, curr_exp + "+" + nums[index : i + 1], curr_eval + temp, temp
                )
                backtrack(
                    i + 1, curr_exp + "-" + nums[index : i + 1], curr_eval - temp, -temp
                )
                backtrack(
                    i + 1,
                    curr_exp + "*" + nums[index:i],
                    curr_eval - prev_num + prev_num * temp,
                    prev_num * temp,
                )

            if nums[index] == "0":
                break

    backtrack(0, "", 0, None)
    return result


nums = "105"
target = 6
print(addOperators(nums, target))
