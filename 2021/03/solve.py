
from typing import List


BIT_LENGTH = 12

sample_size = 0
bit_count = [0 for _ in range(BIT_LENGTH)]

lines = [
    line.rstrip("\n") for line in open("input.txt")
]

for line in lines:
    sample_size += 1
    for k, bit in enumerate(line):
        bit_count[k] += bit == "1"

most_common_bit = ["1" if bc > sample_size/2 else "0" for bc in bit_count]

gamma_rate = int("".join(most_common_bit), 2)

epsilon_rate = int(
    "".join(
        str(1 - int(bit)) for bit in most_common_bit
    ),
    2
)

print(gamma_rate * epsilon_rate)


def bit_criteria(oxygen: List[str], bit_index: int, most_common: bool) -> str:
    if len(oxygen) == 1 or bit_index > BIT_LENGTH:
        return oxygen[0]
    else:
        current_most_common_bit = "1" if [value[bit_index] for value in oxygen].count(
            "1") >= len(oxygen)/2 else "0"
        return bit_criteria(
            [
                value for value in oxygen
                if (value[bit_index] == current_most_common_bit) == most_common
            ],
            bit_index + 1,
            most_common
        )


oxygen_generator_values = lines[:]
co2_scrubber_values = lines[:]

oxygen_generator_rating = int(bit_criteria(
    oxygen_generator_values, 0, True), 2)

co2_scrubber_rating = int(bit_criteria(co2_scrubber_values, 0, False), 2)

print(oxygen_generator_rating * co2_scrubber_rating)
