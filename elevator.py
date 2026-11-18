import sys

def run_elevator():
    state = "IdleFloor1"
    
    for line in sys.stdin:
        event = line.strip()
        if not event:
            continue
        
        if state == "IdleFloor1":
            if event in ["CAR_FLOOR1", "FLOOR1_UP"]:
                print("OPEN_DOOR")
                state = "IdleFloor1"
            elif event in ["CAR_FLOOR2", "FLOOR2_UP", "FLOOR2_DOWN"]:
                print("CLOSE_DOOR")
                print("MOVE_UP_SLOW")
                state = "MovingUpSlow"
            elif event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MovingUpFast"
                
        elif state == "IdleFloor2":
            if event in ["CAR_FLOOR2", "FLOOR2_UP", "FLOOR2_DOWN"]:
                print("OPEN_DOOR")
                state = "IdleFloor2"
            elif event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("CLOSE_DOOR")
                print("MOVE_UP_SLOW")
                state = "MovingUpSlow"
            elif event in ["CAR_FLOOR1", "FLOOR1_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_SLOW")
                state = "MovingDownSlow"
                
        elif state == "IdleFloor3":
            if event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("OPEN_DOOR")
                state = "IdleFloor3"
            elif event in ["CAR_FLOOR2", "FLOOR2_DOWN", "FLOOR2_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_SLOW")
                state = "MovingDownSlow"
            elif event in ["CAR_FLOOR1", "FLOOR1_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MovingDownFast"
                
        elif state == "MovingUpFast":
            if event == "BETWEEN_2_3":
                print("MOVE_UP_SLOW")
                state = "MovingUpSlow"
            elif event == "AT_FLOOR3":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor3"
                
        elif state == "MovingUpSlow":
            if event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"
            elif event == "AT_FLOOR3":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor3"
                
        elif state == "MovingDownFast":
            if event == "BETWEEN_1_2":
                print("MOVE_DOWN_SLOW")
                state = "MovingDownSlow"
            elif event == "AT_FLOOR1":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor1"
                
        elif state == "MovingDownSlow":
            if event == "AT_FLOOR1":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor1"
            elif event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"

if __name__ == "__main__":
    run_elevator()
