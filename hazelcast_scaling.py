
import hazelcast
import time

# This class monitors the load, which is the number of entries in the map
class LoadMonitor:
    def __init__(self, client):
        self.client = client
        self.map = client.get_map("myMap").blocking()

    # Check if the map is too full (load is high)
    def is_too_full(self):
        size = self.map.size()
        print(f"Map size: {size}")
        return size > 1000  # Threshold to add more instances

    # Check if the map has few entries (load is low)
    def is_not_busy(self):
        size = self.map.size()
        return size < 500  # Threshold to remove instances


# This is the main function to scale Hazelcast instances based on load
def main():
    # List to keep track of Hazelcast clients (simulating instances)
    instances = []

    # Start the first Hazelcast client instance
    first_client = hazelcast.HazelcastClient()
    instances.append(first_client)
    print("First instance started...")

    # Create the LoadMonitor to check the map size (load)
    monitor = LoadMonitor(first_client)

    # Simulate adaptive scaling
    while True:
        if monitor.is_too_full():
            print("Load too high, starting new instance...")
            new_client = hazelcast.HazelcastClient()  # Start a new instance (simulated)
            instances.append(new_client)
        elif monitor.is_not_busy() and len(instances) > 1:
            print("Load low, removing an instance...")
            to_shutdown = instances.pop()  # Remove the last instance
            to_shutdown.shutdown()

        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
