# What does this do?
This is a Radicale 3 plugin to give users access based on a CalDav property RADICALE\:acl.
It is supposed to be a comma separated list of the pattern user\:[rights](https://radicale.org/3.0.html#documentation/authentication-and-rights), e.g.:<br>
`user1:rw, user2:r, user3:rw`<br>
To use this you will need a radicale web plugin which can set the RADICALE\:acl property.<br>
For example: <https://github.com/sents/radicale-web-groups> <br>

The following configuration is needed:

```
[rights]

type = radicale-rights-acl

```
