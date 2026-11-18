import sys

def run_elevator():
    state = "IdleFloor1"
    current_floor = 1
    destination = None
    stops = {1: False, 2: False, 3: False}

    def determine_next_destination():
        nonlocal destination
        if current_floor == 1:
            if stops[2] or stops[3]:
                destination = 3 if (stops[3] and not stops[2]) else 2
                if stops[3] and stops[2]:
                    destination = 3
            else:
                destination = None
        elif current_floor == 3:
            if stops[2] or stops[1]:
                destination = 1 if (stops[1] and not stops[2]) else 2
                if stops[1] and stops[2]:
                    destination = 1
            else:
                destination = None
        elif current_floor == 2:
            if stops[3]:
                destination = 3
            elif stops[1]:
                destination = 1
            else:
                destination = None

    for line in sys.stdin:
        event = line.strip()
        if not event:
            continue

        if event in ["CAR_FLOOR1", "FLOOR1_UP"]:
            stops[1] = True
        elif event in ["CAR_FLOOR2", "FLOOR2_UP", "FLOOR2_DOWN"]:
            stops[2] = True
        elif event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
            stops[3] = True

        if state == "IdleFloor1":
            if stops[1] and not stops[2] and not stops[3]:
                print("OPEN_DOOR")
                stops[1] = False
            else:
                determine_next_destination()
                if destination:
                    print("CLOSE_DOOR")
                    print("MOVE_UP_FAST")
                    state = f"MovingUpToFloor{destination}"

        elif state == "IdleFloor2":
            if stops[2] and not stops[1] and not stops[3]:
                print("OPEN_DOOR")
                stops[2] = False
            else:
                determine_next_destination()
                if destination == 3:
                    print("CLOSE_DOOR")
                    print("MOVE_UP_FAST")
                    state = "MovingUpToFloor3"
                elif destination == 1:
                    print("CLOSE_DOOR")
                    print("MOVE_DOWN_FAST")
                    state = "MovingDownToFloor1"

        elif state == "IdleFloor3":
            if stops[3] and not stops[1] and not stops[2]:
                print("OPEN_DOOR")
                stops[3] = False
            else:
                determine_next_destination()
                if destination:
                    print("CLOSE_DOOR")
                    print("MOVE_DOWN_FAST")
                    state = f"MovingDownToFloor{destination}"

        elif state in ["MovingUpToFloor2", "MovingUpToFloor3"]:
            target_f = 2 if "2" in state else 3
            if event == "BETWEEN_1_2" and target_f == 2:
                print("MOVE_UP_SLOW")
            elif event == "BETWEEN_2_3" and target_f == 3:
                print("MOVE_UP_SLOW")
            elif event == f"AT_FLOOR{target_f}":
                print("STOP")
                print("OPEN_DOOR")
                current_floor = target_f
                stops[target_f] = False
                
                determine_next_destination()
                if destination and destination > current_floor:
                    print("CLOSE_DOOR")
                    print("MOVE_UP_FAST")
                    state = f"MovingUpToFloor{destination}"
                elif destination and destination < current_floor:
                    print("CLOSE_DOOR")
                    print("MOVE_DOWN_FAST")
                    state = f"MovingDownToFloor{destination}"
                else:
                    state = f"IdleFloor{current_floor}"

        elif state in ["MovingDownToFloor1", "MovingDownToFloor2"]:
            target_f = 1 if "1" in state else 2
            if event == "BETWEEN_2_3" and target_f == 2:
                print("MOVE_DOWN_SLOW")
            elif event == "BETWEEN_1_2" and target_f == 1:
                print("MOVE_DOWN_SLOW")
            elif event == f"AT_FLOOR{target_f}":
                print("STOP")
                print("OPEN_DOOR")
                current_floor = target_f
                stops[target_f] = False

                determine_next_destination()
                if destination and destination > current_floor:
                    print("CLOSE_DOOR")
                    print("MOVE_UP_FAST")
                    state = f"MovingUpToFloor{destination}"
                elif destination and destination < current_floor:
                    print("CLOSE_DOOR")
                    print("MOVE_DOWN_FAST")
                    state = f"MovingDownToFloor{destination}"
                else:
                    state = f"IdleFloor{current_floor}"

if __name__ == "__main__":
    run_elevator()
