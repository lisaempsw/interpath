# InterPath

InterPath is a Python-based utility designed to track and display detailed task information along with system usage statistics on Windows. This tool provides real-time insights into CPU, memory, and disk usage, as well as network statistics, helping users effectively manage their system resources.

## Features

- **CPU Usage**: Monitor the current CPU usage percentage.
- **Memory Usage**: Display the percentage of used memory.
- **Disk Usage**: Track disk space usage percentage.
- **Network Statistics**: View the total bytes sent and received over the network.
- **Task Information**: List all running processes with their CPU and memory usage.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure you have Python 3 installed on your system.
2. Install the `psutil` library using pip:

   ```bash
   pip install psutil
   ```

3. Download the `interpath.py` file from this repository.

## Usage

Run the script using Python:

```bash
python interpath.py
```

The script will display system usage statistics and running tasks every 5 seconds. To exit, simply close the terminal window or press `Ctrl + C`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

InterPath is a simple yet powerful tool for monitoring and managing system resources on Windows. Use it to gain valuable insights into your system's performance and resource allocation.