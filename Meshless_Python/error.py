def absolute_error(analytical, approximate):
    error = []
    for i in range(len(analytical)):
        error.append(abs(analytical[i] - approximate[i]))
    return error


def relative_error(analytical, approximate):
    relativeerror = []
    for i in range(len(analytical)):
        relativeerror.append((abs(analytical[i] - approximate[i])) / analytical[i])
    return relativeerror
