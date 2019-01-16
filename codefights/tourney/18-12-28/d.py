def easyAssignmentProblem(skills):
    print(skills[0][0] + skills[1][1] > skills[0][1] + skills[1][0])
    return





skills= [[1,3],
 [2,3]]

# Expected Output:
#
# [2, 1]

print(easyAssignmentProblem(skills))
#
# int[] easyAssignmentProblem(int[][] skills) {
#     return skills[0][0] + skills[1][1] > skills[0][1] + skills[1][0] ?
#     new int[] {1, 2} : new int[] {2, 1};
# }



