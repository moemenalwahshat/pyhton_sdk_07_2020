



def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the lst is already sorted, and you can terminate
        if already_sorted:
            break

    return lst