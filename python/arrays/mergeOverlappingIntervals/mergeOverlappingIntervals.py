def mergeOverlappingIntervals(intervals):

    final_intervals = []

    def merge(intervalArray):
        i = len(intervalArray)
        if i == 0:
            mergeCount = 0
            return
        final_intervals_dict = {}
        original_size = len(intervalArray)
        final_intervals_dict[original_size] = intervalArray.pop(0)
        mergeCount = 0

        while i > 0:
            if len(intervalArray) == 0:
                break

            interval = intervalArray.pop(0)
            i = len(intervalArray)

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
                mergeCount += 1
                continue

            else:
                final_intervals_dict[i] = interval

        for key, value in final_intervals_dict.items():
            final_intervals.append(value)
        return mergeCount

    mergeCount = 1
    merge(intervals)

    while mergeCount != 0:
        mergeCount = merge(final_intervals)

    return final_intervals
