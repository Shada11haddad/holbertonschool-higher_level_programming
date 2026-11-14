#!/usr/bin/python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Write one output_X.txt file per attendee, filling the template."""
    if not isinstance(template, str):
        print("Error: Invalid input type for template: expected str, "
              "got {}.".format(type(template).__name__))
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid input type for attendees: expected a list "
              "of dictionaries, got {}.".format(type(attendees).__name__))
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        try:
            with open("output_{}.txt".format(index), "w") as file:
                file.write(content)
        except OSError as e:
            print("Error writing output_{}.txt: {}".format(index, e))
