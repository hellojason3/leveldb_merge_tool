import plyvel
import argparse

def merge_db_into_c(db_path_source, db_path_target):
    db_source = plyvel.DB(db_path_source, create_if_missing=False)
    db_target = plyvel.DB(db_path_target, create_if_missing=True)

    for key, value_source in db_source:
        value_target = db_target.get(key)

        if value_target is None:
            db_target.put(key, value_source)
        elif value_source != value_target:
            # If there is a difference, print the difference
            key_str = key.decode('utf-8', 'ignore')
            value_source_str = value_source.decode('utf-8', 'ignore')
            value_target_str = value_target.decode('utf-8', 'ignore')
            print(f"Key: {key_str}")
            print(f"  Source (A or B): {value_source_str}")
            print(f"  Target (C): {value_target_str}")

            # Update the value in the target database
            db_target.put(key, value_source)

    # Close the databases
    db_source.close()
    db_target.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge LevelDB databases.")
    parser.add_argument("db_path_a", help="Path to the first LevelDB database (A).")
    parser.add_argument("db_path_b", help="Path to the second LevelDB database (B).")
    parser.add_argument("db_path_c", help="Path to the target LevelDB database (C).")

    args = parser.parse_args()

    # Merge database A into C
    print("Merging A into C:")
    merge_db_into_c(args.db_path_a, args.db_path_c)

    # Merge database B into C
    print("\nMerging B into C:")
    merge_db_into_c(args.db_path_b, args.db_path_c)
