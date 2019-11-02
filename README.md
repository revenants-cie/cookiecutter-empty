# Empty Repo Boilerplate

Sometimes you need to create empty repo in GitHub. 
Whether it's a new kind of project or maybe just a storage
for artifacts. This cookiecutter will create a repo with 
bare essentials.

The cookiecutter primarily used with the 
[Terraform github module](https://github.com/revenants-cie/terraform-github/tree/master/modules/github-repo).
 When the `repo_kind` is `empty`, this cookiecutter will be used.
 
```hcl
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
```

