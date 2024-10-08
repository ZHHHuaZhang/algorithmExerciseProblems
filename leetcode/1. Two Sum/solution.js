/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (target === nums[j] + nums[i]) {
        return [i, j];
      }
    }
  }
  return [];
};

console.log(twoSum([2, 7, 11, 15], 9));
// node solution.js