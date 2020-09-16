import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

thrust = 100
boost_used = False
checkpoints = []
record_lap = True
longer_segment_calculated = False
index_to_boost_to = None

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if not record_lap and not boost_used and not longer_segment_calculated:
        longest_distance = None
        for idx, checkpoint in enumerate(checkpoints):
            x = 0
            y = 0
            if idx < (len(checkpoints) - 1):
                x = math.fabs(checkpoint["x"] - checkpoints[idx + 1]["x"])
                y = math.fabs(checkpoint["y"] - checkpoints[idx + 1]["y"])
            else:
                x = math.fabs(checkpoint["x"] - checkpoints[0]["x"])
                y = math.fabs(checkpoint["y"] - checkpoints[0]["y"])
            dist = math.sqrt(x**2 + y**2)
            if not longest_distance or dist > longest_distance:
                longest_distance = dist
                if idx < (len(checkpoints) - 1):
                    index_to_boost_to = idx + 1
                else:
                    index_to_boost_to = 0
        longer_segment_calculated = True

    if record_lap:
        if len(checkpoints) == 0:
            checkpoints.append({"x": next_checkpoint_x, "y": next_checkpoint_y})
        elif checkpoints[len(checkpoints) - 1]["x"] != next_checkpoint_x or \
                checkpoints[len(checkpoints) - 1]["y"] != next_checkpoint_y:
            if next_checkpoint_x == checkpoints[0]["x"] \
                    and next_checkpoint_y == checkpoints[0]["y"]:
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
        if next_checkpoint_dist < 2000:
            thrust = (next_checkpoint_dist - 600) // 14
        else:
            thrust = 100

    if not record_lap and \
            not boost_used and \
            math.fabs(next_checkpoint_angle) < 10 and \
            next_checkpoint_x == checkpoints[index_to_boost_to]["x"] and \
            next_checkpoint_y == checkpoints[index_to_boost_to]["y"] and \
            next_checkpoint_dist > 5000:
        thrust = "BOOST"
        boost_used = True

    print("record_lap: " + str(record_lap), file=sys.stderr, flush=True)
    for checkpoint in checkpoints:
        print(checkpoint, file=sys.stderr, flush=True)
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100) or "BOOST"
    # i.e.: "x y thrust"
    print(f"{next_checkpoint_x} {next_checkpoint_y} {thrust}")
