fail = False
watering = False
while True:
    hours = time.localtime(time.time() + offset)[3] * 60 * 60
    minutes = time.localtime(time.time() + offset)[4] * 60
    seconds = time.localtime(time.time() + offset)[5]
    realtime = hours + minutes + seconds

    if (soil.read() >= 0 and soil.read() <= 750):
        if relay.value() == 1:
            watering = False
            fail = False
            revert()
        else:
            pass
    elif (soil.read() > 750) and watering == False:
        if realtime >= 34680 and realtime <= 35400:
            if (stop.value() == 1 and fail == False):
                revert()
                fail = True
            elif (button_on.value() == 1 and fail == True):
                fail = False
                watering = False
            elif fail == False and watering == False:
                water()
                watering = True
            elif fail == True:
                pass
        elif realtime >= 35400 and (watering == True or fail == True):
            fail = False
            watering = False
            revert()
        else:
            pass
    if (button_on.value() == 1) and watering == False:
        water()
        watering = True
    elif (stop.value() == 1) and watering == True:
        revert()
        watering = False
