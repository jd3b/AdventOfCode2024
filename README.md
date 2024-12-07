# Day 1: Historian Hysteria

## Problem Overview

The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! The last anyone heard, he was visiting locations historically significant to the North Pole. A group of Senior Historians has asked you to accompany them as they check the locations the Chief Historian was most likely to visit.

Each location is identified by a unique number called the **location ID**. You need to reconcile two lists of location IDs, created by two groups of Historians, and measure how far apart the locations are or calculate how often numbers from one list appear in the other. 

### Part One: Total Distance

The two lists are different, and you need to determine how far apart the numbers are. To do this:

1. Sort both lists in ascending order.
2. Pair up the smallest number from each list, then the second smallest, and so on.
3. For each pair, calculate the absolute difference between the two numbers.
4. Sum all the differences to find the total distance.

For example:

#### Example Input:


#### Steps:
1. Sort both lists:
   - Left list: `1, 2, 3, 3, 3, 4`
   - Right list: `3, 3, 3, 4, 5, 9`
   
2. Pair the numbers in ascending order:
   - `(1, 3)`, distance = `|1 - 3| = 2`
   - `(2, 3)`, distance = `|2 - 3| = 1`
   - `(3, 3)`, distance = `|3 - 3| = 0`
   - `(3, 4)`, distance = `|3 - 4| = 1`
   - `(3, 5)`, distance = `|3 - 5| = 2`
   - `(4, 9)`, distance = `|4 - 9| = 5`
   
3. Sum all the distances:
   - `2 + 1 + 0 + 1 + 2 + 5 = 11`

#### Answer: The total distance is `11`.

### Part Two: Similarity Score

In this part, you're asked to find the **similarity score** by checking how often each number in the left list appears in the right list. For each number in the left list:

1. Count how many times the number appears in the right list.
2. Multiply the number by its count in the right list.
3. Sum all of these values to get the similarity score.

For the same example input:

#### Example Input:


#### Steps:
1. For `3` in the left list, it appears 3 times in the right list: `3 * 3 = 9`
2. For `4` in the left list, it appears 1 time in the right list: `4 * 1 = 4`
3. For `2` in the left list, it does not appear in the right list: `2 * 0 = 0`
4. For `1` in the left list, it does not appear in the right list: `1 * 0 = 0`
5. For `3` in the left list again, it appears 3 times in the right list: `3 * 3 = 9`
6. For `3` in the left list once more, it appears 3 times in the right list: `3 * 3 = 9`

#### Sum the values:
- `9 + 4 + 0 + 0 + 9 + 9 = 31`

#### Answer: The similarity score is `31`.



