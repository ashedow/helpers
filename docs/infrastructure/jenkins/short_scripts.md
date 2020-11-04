Get branchlist 

```Groovy
try {
  def branches = ("git ls-remote -h git@github.com:acc_name/repo_name.git").execute()

  return branches.text.readLines()
    .collect { it.split()[1].replaceAll('refs/heads/', '')  }
    .unique()
} catch (Exception e) {
    return "There was a problem fetching the artifacts"
}
```