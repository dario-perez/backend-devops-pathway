# Linux Navigation & Permissions Cheat Sheet

## Key Concepts
| Term | Definition | Example |
| :-- | :-- | :-- |
| **Working Directory** | The current folder where your terminal session is operating. | `pwd` |
| **Permissions** | Rules that govern who can read, write, or execute a file. | `chmod +x script.sh` |
| **Pipes** | Directing the output of one command as the input to another using `\|`. | `ps aux \| grep python` |

## Commands/Code Snippets
```bash
# Print current working directory
pwd

# List all files including hidden ones with detailed attributes
ls -la

# Change directory
cd /path/to/directory

# Grant execution permissions to a script
chmod +x script.sh

# View process list
ps aux
```
## Common Errors & Fixes
| Error | Cause | Fix |
| :-- | :-- | :-- |
| `Permission denied` | The user lacks execution or read rights for the target file or directory. | Use `chmod +x <file>` or check file ownership with `ls -l`. |
| `No such file or directory` | Typo in the path or the directory does not exist in the current scope. | Verify path spelling using `pwd` and `ls`. |

## Resources
- [Linux Journey](https://linuxjourney.com/)

- [The Linux Command Line Book](https://linuxcommand.org/tlcl.sh)