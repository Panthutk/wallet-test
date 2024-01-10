This repository contains tests for the Wallet Lab.
It is designed to be used as a Git [Submodule][submodules] added inside *your* lab1 repo.

What we want:  *add the submodule repo as a `tests` directory inside your working copy of lab1*. So (finally) your working code will look like this:

```
lab1-yourname/
    cash.py
    money.py
    wallet.py
    tests/
        test_cash.py
        test_wallet.py
```

## Instructions

The test code is at: <https://github.com/PROG2024/wallet-test>.

1. In your working copy of `lab1` (e.g. `lab1-yourname`) clone the test submodule into a subdir named `tests` (git creates the `tests` directory):
   ```
   git submodule  add  https://github.com/PROG2024/wallet-test  tests
   ```

2. Now you can run the unit tests in your `lab1` directory like this:
   ```
   python -m unittest tests/*.py
   ```
   If you are using a Windows terminal (sorry about that), replace `tests/*.py` with `tests\*.py`.

3. When you add a submodule, Git creates a file (in your working dir) named `.gitmodules` and "stages" it for the next commit. (`git status` shows this.) You can commit it to your own lab1 repo using:  
   ```
   git commit -m "add submodule for tests"
   ```
   - this adds the submodule to your repo, but does not add the submodule files into your repo -- which is good (we don't want a copy of the submodule files).


## Getting Updates to a Submodule

If the tests change, you can "pull" the changes the same way you "pull" changes from a remote git repository.

In a terminal window, change directory to `tests` and pull changes
```
  terminal> chdir tests         ('chdir' or 'cd' means change directory)
  terminal> git pull
```

[submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
