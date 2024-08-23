# LevelDB Merge Tool

This Python script merges two LevelDB databases into a target database, printing out differences when they exist. It was designed to handle cases where data from multiple databases need to be consolidated into a single database.

## Features

- Merges two LevelDB databases (A and B) into a target database (C).
- Prints differences when the values for the same key in A/B and C differ.
- Updates the target database (C) with values from A and B.

## Requirements

- Python 3.x
- `plyvel` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repo_name.git
    cd your_repo_name
    ```

2. Install the required dependencies:

    ```bash
    pip install plyvel
    ```

## Usage

To merge two LevelDB databases into a target database:

```bash
python merge_leveldb.py /path/to/db_a /path/to/db_b /path/to/db_c
```

## Arguments
`/path/to/db_a`: Path to the first LevelDB database (A).

`/path/to/db_b`: Path to the second LevelDB database (B).

`/path/to/db_c`: Path to the target LevelDB database (C).

## Example
```bash 
python merge_leveldb.py /home/user/leveldb_a /home/user/leveldb_b /home/user/leveldb_c
```


This command merges the data from leveldb_a and leveldb_b into leveldb_c, printing any differences encountered during the merge process.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or want to contribute to this project.

## License
This project is licensed under the MIT License.