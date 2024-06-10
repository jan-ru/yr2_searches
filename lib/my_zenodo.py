# https://astrodata.nyc/posts/2021-04-23-zenodo-sphinx/
import pathlib
import warnings

zenodo_path = pathlib.Path("../ris_files/ZENODO.rst")
if not zenodo_path.exists():
    import textwrap

    try:
        import requests

        headers = {"accept": "application/x-bibtex"}
        # response = requests.get('https://zenodo.org/api/records/4159870',
        response = requests.get(
            "https://zenodo.org/api/records/1044157", headers=headers
        )
        response.encoding = "utf-8"
        zenodo_record = textwrap.indent(response.text, " " * 4)
    except Exception as e:
        warnings.warn("Failed to retrieve Zenodo record for Gala: " f"{str(e)}")
        zenodo_record = (
            "`Retrieve the Zenodo record here " "<https://zenodo.org/record/1044157>`_"
        )

    with open(zenodo_path, "w") as f:
        f.write(zenodo_record)

# 10.5281/zenodo.1044157
