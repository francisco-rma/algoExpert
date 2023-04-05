def mergeOverlappingIntervals(intervals):

    final_intervals_dict = {}
    final_intervals = []

    original_size = len(intervals)
    final_intervals_dict[original_size] = intervals.pop(0)

    i = len(intervals)

    while i > 0:
        interval = intervals.pop(0)
        i = len(intervals)

        merged = False

        for key, value in final_intervals_dict.items():

            final_max = value[len(value) - 1]
            final_min = value[0]

            overlaps: bool = (final_min <= interval[0] and interval[0] <= final_max) or (

                final_min <= interval[len(interval) - 1] and interval[len(interval) - 1] <= final_max) or (

                interval[len(interval) - 1] > final_max and interval[0] < final_min)

            if overlaps:
                if interval[0] < final_min:
                    final_min = interval[0]

                if interval[len(interval) - 1] > final_max:
                    final_max = interval[len(interval) - 1]

                final_interval = [final_min, final_max]
                final_intervals_dict[key] = final_interval

                merged = True
                break

        if merged:
            continue

        else:
            final_intervals_dict[i] = interval

    for key, value in final_intervals_dict.items():
        final_intervals.append(value)

    return final_intervals
