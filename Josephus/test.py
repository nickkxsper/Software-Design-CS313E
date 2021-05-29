def schedule(TAs, sections):
    return helper(TAs, sections, 0)



def helper(TAs, sections, index):

    if len(TAs) == index:
        return True

    elif len(TAs) > index:
        available_times = len(TAs[index])
        for i in range(available_times):
            time_to_TA = TAs[index][i]

            for j in range(sections):
                if time_to_TA == sections[j][0] and sections[j][1] == None:
                    sections[i][1] = TAs[index][0]

                    if helper(TAs, sections, index +1):
                        return True

                    else:
                        sections[j][1] = None

        return False


if __name__ == '__main__': schedule(TAs, sections)

