"""Generate the code reference pages."""


import mkdocs_gen_files
from pathlib import Path

nav = mkdocs_gen_files.Nav()


packages_to_track = ["package_a", "package_b"]


def build_doc_tree(package: str):
    """Build the documentation tree for a package."""
    for path in sorted(Path(package).rglob("*.py")):
        # we look for the module files
        module_path = path.relative_to(".").with_suffix("")
        # we convert their path to a md file path with the same tree structure
        doc_path = path.relative_to(".").with_suffix(".md")
        # we generate an abs path
        full_doc_path = Path("reference", doc_path)

        parts = tuple(module_path.parts)

        if parts[0] == "__init__":
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")

        elif parts[-1] == "__init__":
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")
            parts = parts[:-1]

        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            # Add the file to MkDocs pages, without actually writing it in the docs folder.
            identifier = ".".join(parts)
            print(
                ":::", identifier, file=fd
            )  # we print the module identifier in the file
        mkdocs_gen_files.set_edit_path(full_doc_path, path)


for package in packages_to_track:
    build_doc_tree(package)


# Finally we write the nav file
navigation_filepath = Path("reference", "navigation.md")
with mkdocs_gen_files.open(navigation_filepath, "w") as nav_file:
    # Add the file to MkDocs pages, without actually writing it in the docs folder.
    nav_file.writelines(nav.build_literate_nav())
