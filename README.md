# What does this do?
This is a radicale plugin to give users access based on a propery RADICALE\:acl.
It is supposed to be a comma separated list of the patttern user\:rights, e.g.:
user1:rw, user2:r, user3:rw
There are to rights flags\:
- r: read
- w: write
To use this you will need a radicale web plugin which can set the RDAICALE\:acl property.

The following configuration is needed:

```
[rights]

type = radicale-rights-acl

```
