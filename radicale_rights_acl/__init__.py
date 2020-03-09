from radicale import rights
from radicale.storage import sanitize_path
from radicale.storage import load

name = "radicale-rights-grp"


class Rights(rights.BaseRights):
    def __init__(self, configuration, logger):
        super().__init__(configuration, logger)
        self.Collection = load(configuration, logger)

    def authorized(self, user, path, permissions):
        self.logger.debug(
            "User %r is trying to access path %r. Permissions: %r",
            user,
            path,
            permissions,
        )
        # everybody can access the root collection
        if path == "/":
            self.logger.debug("Accessing root path. Access granted.")
            return True
        user = user or ""
        sane_path = sanitize_path(path)
        sane_path = sane_path.lstrip("/")
        pathowner, subpath = sane_path.split("/", maxsplit=1)
        if user == pathowner:
            self.logger.debug("User %r is pathowner. Access granted.", user)
            return True
        collection = self.Collection(sane_path)
        acl_string = collection.get_meta("RADICALE:acl")
        if acl_string is not None:
            for acl in acl_string.strip(",").split(","):
                acl.strip()
                username, rw_string = acl.split(":")
                username, rw_string = username.strip(), rw_string.strip()
                if username == user and set(permissions).issubset(rw_string):
                    self.logger.debug(
                        "User's {} rights {} matches required rights {}. Access granted.".format(
                            user, rw_string, permissions
                        )
                    )
                    return True
        self.logger.debug(
            "Access to path %r is not granted to user %r.", pathowner, user
        )
        return False
