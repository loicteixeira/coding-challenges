# Advent of Code 2016 - Day 3: Squares With Three Sides

Source: http://adventofcode.com/2016/day/3

## Part 1

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... `5 10 25`? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side.

In your puzzle input, **how many** of the listed triangles are **possible**?

### Examples

- The triangle `541 588 421` is valid, because `541 + 588 > 421`, `588 + 421 > 541` and `421 + 541 > 588`. 
- The "triangle" `5 10 25` is impossible, because `5 + 10` is not larger than `25`.
