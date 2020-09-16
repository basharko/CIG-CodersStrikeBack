import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

thrust = 100
boost_used = False
checkpoints = []
record_lap = True

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    if record_lap:
        if len(checkpoints) == 0:
            checkpoints.append({"x": next_checkpoint_x, "y": next_checkpoint_y})
        elif checkpoints[len(checkpoints) - 1]["x"] != next_checkpoint_x or checkpoints[len(checkpoints) - 1]["y"] != next_checkpoint_y:
            if next_checkpoint_x == checkpoints[0]["x"] and next_checkpoint_y == checkpoints[0]["y"]:
                record_lap = False
            else:
                checkpoints.append({"x": next_checkpoint_x, "y": next_checkpoint_y})
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    elif next_checkpoint_angle > 30 or next_checkpoint_angle < -30:
        thrust = int(100 - ((math.fabs(next_checkpoint_angle) - 30) * 100 // 60))
    else:
        if next_checkpoint_dist > 5000 and not boost_used and next_checkpoint_angle < 10 and next_checkpoint_angle > -10:
            thrust = "BOOST"
            boost_used = True
        else:
            thrust = 100

    print("record_lap: " + str(record_lap), file=sys.stderr, flush=True)
    for checkpoint in checkpoints:
        print(checkpoint, file=sys.stderr, flush=True)
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
