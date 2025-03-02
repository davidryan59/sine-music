from functions.helpers import get_output_filename


def template_script():
    fname = template_script.__name__
    filename = get_output_filename(fname)
    print(f"{fname}: started with {filename=}")

    # Implement script here

    print(f"{fname}: finished")
