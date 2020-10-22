def contains(pres, rsp_list):
    x = 0
    while x < 52:
        if pres in rsp_list[x]:
            return 1
        x += 1
