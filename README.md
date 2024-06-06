# MICHI

NFDI4Chem metadata schema

## Website

[https://NFDI4Chem.github.io/MICHI](https://NFDI4Chem.github.io/MICHI)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [michi](src/michi)
    * [schema](src/michi/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/michi/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
