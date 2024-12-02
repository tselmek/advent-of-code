
lines = [line.rstrip("\n") for line in open("input.txt")]
lines = [list(map(int, line.split("   "))) for line in lines]

left_list = [line[0] for line in lines]
right_list = [line[1] for line in lines]

def compute_total_distance(left_list, right_list):
  
  ordered_left = sorted(left_list)
  ordered_right = sorted(right_list)

  return sum(abs(ordered_left[i] - ordered_right[i]) for i in range(len(ordered_left)))


def compute_similarity_score(left_list, right_list):

  return sum(l * right_list.count(l) for l in left_list)

print(compute_total_distance(left_list, right_list))

print(compute_similarity_score(left_list, right_list))