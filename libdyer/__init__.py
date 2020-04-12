


import pkg_resources

def report_version(args):
    """Reports the current version of the library"""

    title = args.script_name
    byline = args.script_byline

    version = pkg_resources.get_distribution("libdyer").version

    if args.verbose:
        contents = [
            f"{title} - {byline}",
            "Kenneth P. J. Dyer <kenneth@avoceteditors.com>",
            "Avocet Editorial Consulting",
            f"Version: {version}"
        ]
        line = "\n  ".join(contents)
    else:
        line = f"{title} - version {version}"

    print(line)
