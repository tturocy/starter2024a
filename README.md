# Template repository for oTree experiment project

This is a template repository that sets up a project using oTree (https://otree.org).

Aside from saving a few steps in setting up the repository itself (via GitHub's templating feature),
this pre-populates your project with some useful infrastructural files:

* Sets up a `requirements.txt` file including oTree (5.10.4) as well as numpy, scipy, and pandas,
  which are often useful to have in programming an experiment.
  To replicate, do these steps:
  * `pip install otree numpy scipy pandas`
  * `pip freeze > requirements.txt`
* Adds a `runtime.txt`, so the project is ready for deployment to Heroku.
* Runs `otree startproject` and includes the basic files generated.
* Some improvements to the `.gitignore` file.
