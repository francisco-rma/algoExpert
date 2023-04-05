def mergeOverlappingIntervals(intervals):
    final_intervals = []

    final_intervals.append(intervals.pop(0))

    process_count = 1
    i = len(intervals)

    while process_count > 0 and i > 0:
        process_count = 0

        if len(intervals) == 0:
            for index, value in enumerate(final_intervals):
                intervals.append(value)

        i = len(intervals)
        interval = intervals.pop(0)

        merged = False

        for index, value in enumerate(final_intervals):

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

                if final_interval not in final_intervals:
                    final_intervals[index] = final_interval
                    process_count += 1
                    merged = True

                    break

        if merged:
            continue

        elif interval not in final_intervals:
            final_intervals.append(interval)
            process_count += 1

    return final_intervals
