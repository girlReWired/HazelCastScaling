
# Python Hazelcast Adaptive Scaling

This project demonstrates a simple version of how to scale a Hazelcast cluster in Python based on the size of a distributed map. The program adds new instances to the cluster when the load gets too high and removes instances when the load gets too low.

## How It Works

1. The program starts with one Hazelcast instance and a distributed map called `myMap`.
2. It continuously checks the size of the map as a representation of the "load."
3. If the map size exceeds 1000 entries, a new Hazelcast instance is started.
4. If the map size drops below 500 entries, an instance is terminated (while ensuring at least one instance is always running).

## Running the Program

1. Install the Hazelcast Python client with `pip install hazelcast-python-client`.
2. Run the script `hazelcast_scaling.py` in your terminal.
3. The output will show when instances are added and removed based on the map size.

## Example Output

```bash
First instance started...
Map size: 50
Load low, removing an instance...
Map size: 1100
Load too high, starting new instance...
```

## Configuration

- You can modify the `is_too_full` and `is_not_busy` methods in the `LoadMonitor` class to change the thresholds for scaling.
