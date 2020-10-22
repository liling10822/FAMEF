Delegator.py — Subprocesses for Humans 2.0 =======================================

![image](https://img.shields.io/pypi/v/delegator.py.svg%0A%20:target:%20https://pypi.python.org/pypi/delegator.py)

![image](https://img.shields.io/pypi/l/delegator.py.svg%0A%20:target:%20https://pypi.python.org/pypi/delegator.py)

![image](https://img.shields.io/pypi/wheel/delegator.py.svg%0A%20:target:%20https://pypi.python.org/pypi/delegator.py)

![image](https://img.shields.io/pypi/pyversions/delegator.py.svg%0A%20:target:%20https://pypi.python.org/pypi/delegator.py)

![image](https://img.shields.io/badge/SayThanks.io-☼-1EAEDB.svg%0A%20:target:%20https://saythanks.io/to/kennethreitz)

**Delegator.py** is a simple library for dealing with subprocesses, inspired by both [envoy](https://github.com/kennethreitz/envoy) and [pexpect](http://pexpect.readthedocs.io) (in fact, it depends on it!).

This module features two main functions `delegator.run()` and `delegator.chain()`. One runs commands, blocking or non-blocking, and the other runs a chain of commands, separated by the standard unix pipe operator: `|`.

Basic Usage
===========

Basic run functionality:

``` {.sourceCode .pycon}
>>> c = delegator.run('ls')
>>> print c.out
README.rst   delegator.py

>>> c = delegator.run('long-running-process', block=False)
>>> c.pid
35199
>>> c.block()
>>> c.return_code
0
```

Commands can be passed in as lists as well (e.g. `['ls', '-lrt']`), for parameterization.

Basic chain functionality:

``` {.sourceCode .pycon}
# Can also be called with ([['fortune'], ['cowsay']]).
# or, delegator.run('fortune').pipe('cowsay')

>>> c = delegator.chain('fortune | cowsay')
>>> print c.out
  _______________________________________
 / Our swords shall play the orators for \
 | us.                                   |
 |                                       |
 \ -- Christopher Marlowe                /
  ---------------------------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
```

Expect functionality is built-in too, on non-blocking commands:

``` {.sourceCode .pycon}
>>> c.expect('Password:')
>>> c.send('PASSWORD')
>>> c.block()
```

Other functions:

``` {.sourceCode .pycon}
>>> c.kill()
>>> c.send('SIGTERM', signal=True)

# Only available when block=True, otherwise, use c.out.
>>> c.err
''

# Direct access to pipes.
>>> c.std_err
<open file '<fdopen>', mode 'rU' at 0x10a5351e0>

# Adjust environment variables for the command (existing will be overwritten).
>>> c = delegator.chain('env | grep NEWENV', env={'NEWENV': 'FOO_BAR'})
>>> c.out
NEWENV=FOO_BAR
```

Installation
============

    $ pip install delegator.py

✨🍰✨
