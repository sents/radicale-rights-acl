from radicale import rights
from radicale.pathutils import sanitize_path
from radicale.storage import load

from radicale.log import logger

name = "radicale-rights-grp"


class Rights(rights.BaseRights):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.Collection = load(configuration)

    def authorized(self, user, path):
        logger.debug(
            "User %r is trying to access path %r. Permissions: %r",
            user,
            path,
        )
        # everybody can access the root collection
        if path == "/":
            logger.debug("Accessing root path. Access granted.")
            return True
        user = user or ""
        sane_path = sanitize_path(path)
        sane_path = sane_path.lstrip("/")
        pathowner, subpath = sane_path.split("/", maxsplit=1)
        if user == pathowner:
            logger.debug("User %r is pathowner. Access granted.", user)
            return True
        collection = self.Collection(sane_path)
        acl_string = collection.get_meta("RADICALE:acl")
        if acl_string is not None:
            for acl in acl_string.strip(",").split(","):
                acl.strip()
                username, rw_string = acl.split(":")
                username, rw_string = username.strip(), rw_string.strip()
                if username == user:
                    logger.debug(
                        "User {} found in acl for path {}. Granted rights: {}.".format(
                            user, pathowner, rw_string,
                        )
                    )
                    return rw_string
        logger.debug(
            "User %r is not in access control list for %r.", user, pathowner
        )
        return ''
