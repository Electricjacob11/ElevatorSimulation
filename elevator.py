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
                print("MOVE_UP_FAST")
                state = "MovingUpToFloor2"
            elif event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MovingUpToFloor3"
                
        elif state == "IdleFloor2":
            if event in ["CAR_FLOOR2", "FLOOR2_UP", "FLOOR2_DOWN"]:
                print("OPEN_DOOR")
                state = "IdleFloor2"
            elif event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("CLOSE_DOOR")
                print("MOVE_UP_FAST")
                state = "MovingUpToFloor3"
            elif event in ["CAR_FLOOR1", "FLOOR1_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MovingDownToFloor1"
                
        elif state == "IdleFloor3":
            if event in ["CAR_FLOOR3", "FLOOR3_DOWN"]:
                print("OPEN_DOOR")
                state = "IdleFloor3"
            elif event in ["CAR_FLOOR2", "FLOOR2_DOWN", "FLOOR2_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MovingDownToFloor2"
            elif event in ["CAR_FLOOR1", "FLOOR1_UP"]:
                print("CLOSE_DOOR")
                print("MOVE_DOWN_FAST")
                state = "MovingDownToFloor1"
                
        elif state == "MovingUpToFloor2":
            if event == "BETWEEN_1_2":
                print("MOVE_UP_SLOW")
                state = "MovingUpSlowToFloor2"
            elif event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"
                
        elif state == "MovingUpSlowToFloor2":
            if event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"
                
        elif state == "MovingUpToFloor3":
            if event == "BETWEEN_2_3":
                print("MOVE_UP_SLOW")
                state = "MovingUpSlowToFloor3"
            elif event == "AT_FLOOR3":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor3"
                
        elif state == "MovingUpSlowToFloor3":
            if event == "AT_FLOOR3":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor3"
                
        elif state == "MovingDownToFloor1":
            if event == "BETWEEN_1_2":
                print("MOVE_DOWN_SLOW")
                state = "MovingDownSlowToFloor1"
            elif event == "AT_FLOOR1":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor1"
                
        elif state == "MovingDownSlowToFloor1":
            if event == "AT_FLOOR1":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor1"
                
        elif state == "MovingDownToFloor2":
            if event == "BETWEEN_2_3":
                print("MOVE_DOWN_SLOW")
                state = "MovingDownSlowToFloor2"
            elif event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"
                
        elif state == "MovingDownSlowToFloor2":
            if event == "AT_FLOOR2":
                print("STOP")
                print("OPEN_DOOR")
                state = "IdleFloor2"

if __name__ == "__main__":
    run_elevator()
