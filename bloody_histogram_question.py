
def max_rectangle(a):
    heights = []
    distances = []

    max_rec = 0

    for i in range(len(a)):
        if len(heights) < 1 or a[i] > heights[-1]:
            heights.append(a[i])
            distances.append(i)
        else:
            max_rec = max(max_rec, heights[-1] * (i - distances[-1]))
            heights.pop()
            heights.append(a[i])

    while len(heights) > 0:
        max_rec = max(max_rec, heights[-1] * (len(a) - distances[-1]))
        heights.pop()
        distances.pop()

    return max_rec


a = [1,3,2,1,2]
print(max_rectangle(a))