# CS2 Lag Reducer

## Overview

CS2 Lag Reducer is a Python script designed to optimize system and network settings to improve performance and reduce lag for the CS2 game. It performs several actions including setting system power plans, adjusting network settings, cleaning temporary files, and setting the CS2 process to high priority.

## Features

- **Optimize System Settings**:
  - Set power plan to High Performance (Windows).
  - Disable unnecessary services (Windows).
  - Set CPU governor to performance mode (Linux).

- **Optimize Network Settings**:
  - Adjust TCP settings (Windows).
  - Adjust network settings using `sysctl` (Linux).

- **Clean Temporary Files**:
  - Deletes temporary files from common directories.

- **Set High Priority**:
  - Set CS2 process to high priority (Windows and Linux).

## Requirements

- Python 3.x
- Administrative or root privileges (for system and network optimizations)

## Installation

1. Clone the repository or download the script.

   ```sh
   git clone https://github.com/yourusername/cs2-lag-reducer.git
   cd cs2-lag-reducer
