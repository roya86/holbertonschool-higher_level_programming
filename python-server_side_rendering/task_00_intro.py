#!/usr/bin/python3
"""
task_00_intro.py

Generate personalized invitation files from a template string and a list of
attendee dictionaries.

Output files:
  output_1.txt, output_2.txt, ...
"""

import os


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and attendee data.

    Args:
        template (str): Template text containing placeholders:
                        {name}, {event_title}, {event_date}, {event_location}
        attendees (list[dict]): List of dictionaries with attendee data.

    Behavior:
      - If template is empty -> print:
          "Template is empty, no output files generated."
        and return (no files created)
      - If attendees is empty -> print:
          "No data provided, no output files generated."
        and return (no files created)
      - If invalid input types -> print an error and return
      - Missing/None values -> replaced with "N/A"
      - Files named output_X.txt (X starts at 1)
      - If a file already exists, it will be overwritten (checked with exists)
    """
    # ---------- Type checks ----------
    if not isinstance(template, str):
        print(f"Invalid input type: template must be str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type: attendees must be list, got {type(attendees).__name__}.")
        return

    # Ensure it's a list of dictionaries
    if not all(isinstance(item, dict) for item in attendees):
        bad_types = [type(item).__name__ for item in attendees if not isinstance(item, dict)]
        print(
            "Invalid input type: attendees must be a list of dictionaries, "
            f"found non-dict types: {bad_types}."
        )
        return

    # ---------- Empty input checks ----------
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------- Generate files ----------
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, person in enumerate(attendees, start=1):
        try:
            invitation = template

            # Replace each placeholder; missing/None -> "N/A"
            for key in placeholders:
                value = person.get(key, "N/A")
                if value is None:
                    value = "N/A"
                invitation = invitation.replace("{" + key + "}", str(value))

            filename = f"output_{idx}.txt"

            # Check existence as requested (still overwriting afterward)
            _ = os.path.exists(filename)

            with open(filename, "w", encoding="utf-8") as f:
                f.write(invitation)

        except (OSError, IOError) as e:
            print(f"Error writing file {filename}: {e}")
        except Exception as e:
            print(f"Unexpected error processing attendee #{idx}: {e}")
