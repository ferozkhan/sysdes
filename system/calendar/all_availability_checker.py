

""" complexity: run time => O(nlogn) | space => O(n) """
def get_all_availability_slots(booked_time_slots):
    # sort by start time
    booked_time_slots = sorted(booked_time_slots, key=lambda slot: slot[0])

    #initialize
    avail_slots = [booked_time_slots[0]]
    for current_start, current_end in booked_time_slots[1:]:
        last_start, last_end = avail_slots[-1]

        # if the current meeting overlap with last meeting, then use the
        # later end time of the two
        if current_start <= last_end:
            avail_slots[-1] = (last_start, max(last_end, current_end))
        else:
            avail_slots.append((current_start, current_end))
    return avail_slots


# test
assert list(get_all_availability_slots([(1, 3), (2, 4)])) == [(1, 4)]
assert list(get_all_availability_slots([(1, 2), (2, 3)])) == [(1, 3)]
assert list(get_all_availability_slots([(1, 5), (2, 3)])) == [(1, 5)]
assert list(get_all_availability_slots([(5, 8), (1, 4), (6, 8)])) == [(1, 4), (5, 8)]
