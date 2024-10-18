import os

def enter_and_save_metadata(file_name):
    print("Please enter the metadata for your experiment. Type 'back' to go back to the previous field.")

    # Metadata fields and whether they are required (True for required, False for optional)
    fields = [
        ("Experiment basename", True),
        ("organoid_line", True),
        ("tcell_line", True),
        ("exp_nr", True),
        ("well", True),
        ("date", True),
        ("dead_dye_channel", True),
        ("organoid_distance_channel", True),
        ("tcell_contact_threshold", True),
        ("tcell_dead_dye_threshold", True),
        ("(optional) tcell_stats_folder", False),
        ("organoid_contact_threshold", True),
        ("organoid_dead_dye_threshold", True),
        ("(optional) organoid_stats_folder", False),
        ("tumor_name", True),
        ("Object_distance (TRUE/FALSE)", True),
    ]

    metadata = {}
    index = 0

    while index < len(fields):
        field_name, is_required = fields[index]
        value = input(f"Enter {field_name}: ")

        if value.lower() == "back" and index > 0:
            index -= 1  # Go back to the previous field
            continue

        # Check if input is valid (non-empty for required fields)
        if value.strip() or not is_required:  # If optional, allow empty
            metadata[field_name] = value
            index += 1
        else:
            print(f"{field_name} is required. Please enter a value.")

    # Check if the file exists. If not, create it with a header row
    file_exists = os.path.exists(file_name)
    with open(file_name, "a") as f:
        if not file_exists:
            # Write the header row (field names)
            header = "\t".join([field[0] for field in fields])
            f.write(header + "\n")

        # Prepare the metadata as tab-separated values
        metadata_values = [metadata.get(field[0], "") for field in fields]
        f.write("\t".join(metadata_values) + "\n")

    print(f"Metadata has been saved to {file_name}")


# To use the function:
def main():
    filename = input("File name to store metadata: ")
    enter_and_save_metadata(filename + ".tsv")
main()
