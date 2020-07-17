============================
Using Empty Repo Boilerplate
============================

.. image:: https://readthedocs.com/projects/revdb-cookiecutter-empty/badge/?version=latest&token=e0c37051abfda101ab4d452a12a594e73e53f8da60a96464fe37bb33730e1165
    :target: https://revdb-cookiecutter-empty.readthedocs-hosted.com/en/latest/?badge=latest
    :alt: Documentation Status

Sometimes you need to create empty repo in GitHub.
Whether it's a new kind of project or maybe just a storage
for artifacts. This cookiecutter will create a repo with 
bare essentials.

The cookiecutter primarily used with the 
`Terraform github module <https://github.com/revenants-cie/terraform-github/tree/master/modules/github-repo>`_.
When the ``repo_kind`` is ``empty``, this cookiecutter will be used.

.. code-block:: terraform

    module "empty-repo" {
      source        = "./modules/github-repo/"
      name          = "empty-repo"
      description   = "General purpose repo"
      private       = true
      organization  = var.github_organization
      owner_team_id = github_team.committers.id
      admin_team_id = github_team.admins.id
      ssh_key_path  = abspath(".env/id_rsa")
      repo_kind     = "empty"
    }
