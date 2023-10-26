git add .
git commit -m "**Title**:  FLOYD WARSHALL
**Description**:  DEEP LEARNING OF FLOYD WARSHALL ALGORITH WITH EXAMPLES AND PROBLEM STATEMENTS

## Overview
Floyd Warshall is also known as **Multisource Shortest Path** .
It not helps you to find /work on positive cycle but also on Negative cycle as well.

**Real life Applications**

1. Robotics:- Robots are used to navigate through an environment, Floyd Warshall can be used to plan the shortest paths between different points/different areas.

2. Transportation Networks:  This can help in urban planning, traffic optimization, and efficient routing for emergency services
like ambulance, fire brigade etc.

3. Infrastructure Maintenance Planning: This helps in planning cost-effective maintenance schedules, reducing downtime.

**Time Complexity**
O(V^3), where V is the number of vertices in the graph. 
--Floyd Warshall algorithm performs well on small to moderately-sized graphs with a relatively low number of vertices.
--The cubic time complexity makes the algorithm less efficient for large graphs, particularly those with a high number of 
vertices.
**Space Complexity**
 O(V^2), where V is the number of vertices in the graph.
--Floyd Warshall performs well on graphs with a moderate number of vertices, where the cubic time complexity and square space complexity are manageable.
--It may not be suitable in scenarios where the available memory resources are limited or strictly constrained."
**LEETCODE PROBLEMS **

[605. Can Place Flowers] (https://leetcode.com/problems/can-place-flowers/)
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

- 1 <= flowerbed.length <= 2 * 104
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length

--**Explanation**
This problem is about planting flowers in a flowerbed without violating the rule that no two flowers can be planted adjacent to each other. You're given a flowerbed represented as an array where 0 represents an empty plot and 1 represents a plot with a flower already planted. You need to determine if it's possible to plant 'n' new flowers in the flowerbed without violating the rule. Here's a step-by-step explanation:

-  You have a flowerbed, which is essentially an array of 0s and 1s. For example: [1,0,0,0,1]. 
- You want to plant 'n' new flowers in this flowerbed. 
- The rule is that you cannot plant two flowers adjacent to each other, meaning you cannot have two 1s (flowers) next to each other in the array. 

Now, you need to check if it's possible to plant 'n' new flowers in the flowerbed without breaking this rule. Here's how you can approach this problem:

-  Loop through the flowerbed array.
-  Whenever you find an empty plot (0), check if the previous plot and the next plot are also empty (0).
-  If they are both empty, you can plant a flower in the current plot (set it to 1) and decrease 'n' by 1, indicating that you've planted a flower.
-  Continue this process until you've either planted all 'n' flowers or reached the end of the flowerbed. 
- If at the end 'n' is zero, you can plant 'n' flowers without breaking the rule, so return true. Otherwise, return false.

**Code**
public boolean canPlaceFlowers(int[] flowerbed, int n) {
    int count = 0;
    int i = 0;
    
    while (i < flowerbed.length) {
        if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
            flowerbed[i] = 1;  
            count++;
        }
        i++;
    }
    
    return count >= n;
}
**Time Complexity** O(n)
**Space Complexity** O(1)
