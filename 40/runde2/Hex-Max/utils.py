

def calcOutsideMoves(a, s, open_a, open_s):
    if open_a == open_s:
        return 0, 0, open_a, open_s, a, s
    elif open_a > open_s:
        used_open = "a"
    else:
        used_open = "s"
    # ^^ used open ^^
    if used_open == "a":
        if open_a > s:
            outside_s = s
            s = 0
        else:
            outside_s = open_a
            s -= open_a

        # return: outside a, outside s, open a, open s, a, s
        return 0, outside_s, open_a, open_s, a, s
    else:
        if open_s > a:
            outside_a = a
            a = 0
        else:
            outside_a = open_s
            a -= open_s

        return outside_a, 0, open_a, open_s, a, s


def enoughMovesLeft(open_a, open_s, a, s, shifts):
    if open_a > open_s:
        if open_a > s:
            min_moves = open_a + a
        else:
            min_moves = s + a
    else:
        if open_s > a:
            min_moves = open_s + s
        else:
            min_moves = a + s
    return int(min_moves) < int(shifts)


def generateChanges(hex_from, hex_to):
    segment_changes = []
    for i in range(7):
        if hex_from.getSegment(i + 1) == 0:
            if hex_to.getSegment(i + 1) == 0:
                segment_changes.append(0)
            else:
                segment_changes.append(2)
        else:
            if hex_to.getSegment(i + 1) == 0:  # from 1 to 0
                segment_changes.append(3)
            else:
                segment_changes.append(1)
    return segment_changes


def moveOutside(outside, num_outside, hex, changes, cur_hex, a, s):
    used_shifts = 0
    if outside == "a":
        for i in range(num_outside):
            for j in hex:
                for k in range(7):
                    cur_seg = j.getSegment(k + 1)
                    if cur_seg == 3:
                        for l in range(7):
                            if changes.getSegment(l + 1) == 2:
                                changes.setSegment(l + 1, 1)
                                cur_hex.setSegment(l + 1, 1)
                                a -= 1
                                break
                        j.setSegment(k + 1, 0)
                        hexOutput(hex)
                        used_shifts += 1
    else:
        for i in range(num_outside):
            for j in hex:
                for k in range(7):
                    cur_seg = j.getSegment(k + 1)
                    if cur_seg == 2:
                        for l in range(7):
                            if changes.getSegment(l + 1) == 3:
                                changes.setSegment(l + 1, 0)
                                cur_hex.setSegment(l + 1, 0)
                                a -= 1
                                break
                        j.setSegment(k + 1, 1)
                        hexOutput(hex)
                        used_shifts += 1

    return used_shifts, changes, cur_hex, a, s


def moveInside(digit, changes, a, s):
    shifts = 0
    if a == s:
        for i in range(a):
            idx_a = None
            idx_s = None
            for i in range(7):
                if changes.getSegment(i + 1) == 2:
                    idx_a = i
                    break
            for i in range(7):
                if changes.getSegment(i + 1) == 3:
                    idx_s = i
                    break
            changes.setSegment(idx_a + 1, 1)
            changes.setSegment(idx_s + 1, 0)
            digit.setSegment(idx_a + 1, 1)
            digit.setSegment(idx_s + 1, 0)
            shifts += 1
        return shifts
    elif a > s:
        for i in range(s):
            idx_a = None
            idx_s = None
            for i in range(7):
                if changes.getSegment(i + 1) == 2:
                    idx_a = i
                    break
            for i in range(7):
                if changes.getSegment(i + 1) == 3:
                    idx_s = i
                    break
            changes.setSegment(idx_a + 1, 1)
            changes.setSegment(idx_s + 1, 0)
            digit.setSegment(idx_a + 1, 1)
            digit.setSegment(idx_s + 1, 0)
            shifts += 1
            a -= 1
            s -= 1
    else:
        for i in range(a):
            idx_a = None
            idx_s = None
            for i in range(7):
                if changes.getSegment(i + 1) == 2:
                    idx_a = i
                    break
            for i in range(7):
                if changes.getSegment(i + 1) == 3:
                    idx_s = i
                    break
            changes.setSegment(idx_a + 1, 1)
            changes.setSegment(idx_s + 1, 0)
            digit.setSegment(idx_a + 1, 1)
            digit.setSegment(idx_s + 1, 0)
            shifts += 1
            a -= 1
            s -= 1
    return shifts, a, s, changes, digit


def hexOutput(hex):
    pass
