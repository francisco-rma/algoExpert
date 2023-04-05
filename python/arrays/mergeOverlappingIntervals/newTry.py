def mergeOverlappingIntervals(intervals):

    def merge(intervals):
        process_count = 0
        final_intervals = []

        final_intervals.append(intervals.pop(0))

        i = len(intervals)

        while i > 0:
            interval = intervals.pop(0)
            i = len(intervals)

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
                        process_count += 1

                    final_intervals[index] = final_interval

                    merged = True
                    break

            if merged:
                continue

            elif interval not in intervals:
                final_intervals.append(interval)
                process_count += 1

        return final_intervals, process_count

    process_count = len(intervals) - 1

    while process_count > len(intervals) - 1:
        intervals, process_count = merge(intervals)

    return intervals
